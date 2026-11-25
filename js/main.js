/* =====================================================================
   We Brand U — interacción y movimiento (vanilla JS, sin dependencias)
   ===================================================================== */
(() => {
  'use strict';

  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => Array.from(c.querySelectorAll(s));

  const reduceMQ = matchMedia('(prefers-reduced-motion: reduce)');
  const hoverMQ = matchMedia('(hover: hover) and (pointer: fine)');
  const reduced = () => reduceMQ.matches;
  const canHover = () => hoverMQ.matches;   // en mobile/touch los estados van por tap

  /* Reinicia la animación de una ilustración (clase .play en el <svg>) */
  function play(svg) {
    if (!svg) return;
    svg.classList.remove('play');
    void svg.getBoundingClientRect();        // fuerza reflow para reiniciar
    svg.classList.add('play');
  }

  /* Dispara `fn` UNA sola vez cuando `el` entra en vista */
  function onceInView(el, fn, threshold = 0.35) {
    if (!('IntersectionObserver' in window)) { fn(); return; }
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) { io.unobserve(e.target); fn(); }
      });
    }, { threshold });
    io.observe(el);
  }

  /* Pequeño candado para que el hover no encadene cambios mientras algo
     se está moviendo debajo del cursor. */
  function makeLock(ms) {
    let until = 0;
    return {
      set: () => { until = performance.now() + (reduced() ? 0 : ms); },
      on: () => performance.now() < until,
    };
  }

  /* -------------------------------------------------------------------
     Imágenes / placeholders (config en js/imagenes.js)
     ------------------------------------------------------------------- */
  const IMAGES = window.WBU_IMAGES || {};
  $$('[data-slot]').forEach((slot) => {
    const name = slot.dataset.slot;
    const cfg = IMAGES[name];
    if (!cfg) return;
    // hero-bg sin imagen: se ve el fondo dibujado en SVG, sin placeholder
    if (name === 'hero-bg' && !cfg.src) return;
    if (!slot.classList.contains('slot--cover')) slot.style.aspectRatio = `${cfg.w} / ${cfg.h}`;
    if (cfg.src) {
      const img = new Image();
      img.src = /^(https?:)?\/\//.test(cfg.src) ? cfg.src : (window.WBU_BASE || '') + cfg.src;
      img.alt = cfg.alt || '';
      img.width = cfg.w;
      img.height = cfg.h;
      img.decoding = 'async';
      if (name !== 'hero-bg') img.loading = 'lazy';
      slot.appendChild(img);
    } else {
      const ph = document.createElement('div');
      ph.className = 'ph';
      ph.innerHTML = `<b>${name}</b>${cfg.w} × ${cfg.h}`;
      slot.appendChild(ph);
    }
  });

  /* -------------------------------------------------------------------
     Navegación en dos niveles
     · .rail     menú principal (páginas). La página activa la marca build.mjs.
     · .subrail  menú de secciones: se arma con los bloques de <main> que
                 tienen data-label + data-icon. El brillo sigue a la vista.
     En mobile: barra inferior + "Menu" con páginas y secciones.
     ------------------------------------------------------------------- */
  const docEl0 = document.documentElement;
  const rail = $('.rail');
  const subrail = $('.subrail');
  // El home (landing) tiene un solo menú: el principal, con todas las páginas.
  // El menú de secciones existe solo en las páginas internas.
  const sectionViews = document.body.hasAttribute('data-paged') ? [] : $$('main > [data-label]');
  const slug = (s) => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  const used = new Set($$('[id]').map((el) => el.id));
  sectionViews.forEach((v) => {                         // cada sección necesita un id para su ancla
    if (v.id) return;
    let id = slug(v.dataset.label) || 'section';
    while (used.has(id)) id += '-2';
    used.add(id);
    v.id = id;
  });
  const sectionLink = (v, extra) => `<a href="#${v.id}" class="rail-link" data-target="${v.id}" aria-label="${v.dataset.label}">`
    + `<svg viewBox="0 0 24 24" class="rail-ico" aria-hidden="true"><use href="#${v.dataset.icon}"/></svg>${extra}</a>`;

  const placeGlow = () => {
    const a = subrail && $('.rail-link.is-active', subrail);
    if (a) subrail.style.setProperty('--gy', `${a.offsetTop + a.offsetHeight / 2}px`);
  };
  // la sección visible se marca en el menú de secciones (y en el "Menu" mobile)
  function setRail(id) {
    const hits = $$(`.rail-link[data-target="${id}"]`);
    if (!hits.length) return;                           // p. ej. el footer: queda la última
    $$('.rail-link[data-target]').forEach((a) => {
      const on = a.dataset.target === id;
      a.classList.toggle('is-active', on);
      if (on) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current');
    });
    placeGlow();
  }
  let subrailReady = false;
  function showSubrail(on) {
    if (!subrailReady) return;
    docEl0.classList.toggle('has-subrail', on);
    subrail.classList.toggle('is-in', on);
  }

  if (subrail && sectionViews.length >= 2) {
    subrail.insertAdjacentHTML('beforeend', sectionViews.map((v) => sectionLink(v, `<span class="rail-tip">${v.dataset.label}</span>`)).join(''));
    subrail.hidden = false;
    // el principal se compacta y el de secciones entra deslizándose
    requestAnimationFrame(() => requestAnimationFrame(() => {
      subrailReady = true;
      showSubrail(true);
    }));
    setRail(sectionViews[0].id);
    addEventListener('resize', placeGlow);
    // sin modo vistas (mobile): la sección activa se detecta al scrollear
    if ('IntersectionObserver' in window) {
      const io = new IntersectionObserver((entries) => {
        entries.forEach((e) => { if (e.isIntersecting && !docEl0.classList.contains('paged')) setRail(e.target.id); });
      }, { rootMargin: '-45% 0px -45% 0px' });
      sectionViews.forEach((s) => io.observe(s));
    }
  }

  if (rail) {
    // al elegir una página, su ícono queda seleccionado (fondo sólido) mientras carga
    $$('.rail > .rail-link').forEach((a) => a.addEventListener('click', () => {
      $$('.rail > .rail-link').forEach((b) => b.classList.toggle('is-active', b === a));
    }));

    const more = $('.rail-more', rail);
    const sheet = $('.rail-sheet', rail);
    if (sectionViews.length >= 2) {                     // "Menu" mobile: también las secciones
      sheet.insertAdjacentHTML('beforeend', '<p class="rail-sheet-head">On this page</p><div class="rail-sheet-grid">'
        + sectionViews.map((v) => sectionLink(v, `<span class="rail-sheet-label">${v.dataset.label}</span>`)).join('') + '</div>');
    }
    const setSheet = (open) => {
      sheet.hidden = !open;
      more.setAttribute('aria-expanded', String(open));
    };
    more.addEventListener('click', () => setSheet(sheet.hidden));
    sheet.addEventListener('click', (e) => { if (e.target.closest('a')) setSheet(false); });
    document.addEventListener('click', (e) => { if (!sheet.hidden && !rail.contains(e.target)) setSheet(false); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !sheet.hidden) { setSheet(false); more.focus(); } });
  }

  /* -------------------------------------------------------------------
     2 · Servicios — estados brand / tech / growth
     ------------------------------------------------------------------- */
  const svcRow = $('.svc-row');
  if (svcRow) {
    const cards = $$('.svc', svcRow);
    const lock = makeLock(700);
    let current = null;

    const setSvc = (key) => {
      if (key === current) return;
      current = key;
      svcRow.dataset.active = key || 'none';
      cards.forEach((c) => {
        const on = c.dataset.key === key;
        c.classList.toggle('is-active', on);
        c.setAttribute('aria-expanded', String(on));
        if (on && key !== 'brand') play($('.ill', c));   // tech: nodos · growth: curva
      });
      lock.set();
    };

    cards.forEach((card) => {
      const key = card.dataset.key;
      // hover (solo dispositivos con puntero fino): mousemove, no mouseenter,
      // así una tarjeta que se desliza bajo el cursor quieto no se activa sola
      card.addEventListener('mousemove', () => {
        if (canHover() && !lock.on()) setSvc(key);
      });
      card.addEventListener('click', (e) => {
        // en el home (data-links="false") el click expande, como en la 1ª versión
        const isLink = card.tagName === 'A' && svcRow.dataset.links === 'true';
        if (card.tagName === 'A' && !isLink) e.preventDefault();
        if (canHover()) { if (!isLink) setSvc(key); return; }
        if (isLink && current === key) return;         // segundo tap: navega
        if (isLink) e.preventDefault();
        setSvc(current === key ? null : key);          // tap
      });
      card.addEventListener('focus', () => { if (card.matches(':focus-visible')) setSvc(key); });
    });
    svcRow.addEventListener('mouseleave', () => { if (canHover()) setSvc(null); });

    // al entrar en vista: se trazan los dibujos del estado inicial
    onceInView(svcRow, () => {
      play($('.ill-tech', svcRow));
      play($('.ill-growth', svcRow));
    });

    // Hub /servicios: al entrar, las tarjetas se expanden solas una por una
    // (demostración) hasta que la persona las toca.
    if (svcRow.dataset.links === 'true' && !reduced()) {
      const demo = ['brand', 'tech', 'growth', null];
      const timers = demo.map((k, n) => setTimeout(() => setSvc(k), 900 + n * 1700));
      const stop = () => timers.forEach(clearTimeout);
      svcRow.addEventListener('pointerdown', stop, { once: true });
      svcRow.addEventListener('mousemove', stop, { once: true });
      svcRow.addEventListener('focusin', stop, { once: true });
    }
  }

  /* -------------------------------------------------------------------
     3 · Why work with Us? — rueda de 3 estados sobre el arco
     Orden cíclico: arriba = anterior, centro = activo, abajo = siguiente.
     ------------------------------------------------------------------- */
  const why = $('.slab--why');
  if (why) {
    const ORDER = ['custom', 'fast', 'free'];
    const items = $$('.why-item', why);
    const byKey = Object.fromEntries(items.map((el) => [el.dataset.key, el]));
    const lock = makeLock(850);
    let state = 'base';

    const rolesFor = (idx) => ({
      [ORDER[(idx + 2) % 3]]: 'top',
      [ORDER[idx]]: 'mid',
      [ORDER[(idx + 1) % 3]]: 'bot',
    });

    // mueve los ítems a sus roles; el que da la vuelta (arriba↔abajo)
    // se desvanece, salta y reaparece en vez de cruzar por el medio
    function applyRoles(roles, animate) {
      Object.entries(roles).forEach(([key, role]) => {
        const el = byKey[key];
        const prev = el.dataset.role;
        const wraps = animate && prev && ((prev === 'top' && role === 'bot') || (prev === 'bot' && role === 'top'));
        if (!wraps) { el.dataset.role = role; return; }
        el.classList.add('is-wrapping');
        setTimeout(() => {
          el.classList.add('no-anim');
          el.dataset.role = role;
          void el.offsetWidth;
          el.classList.remove('no-anim');
          el.classList.remove('is-wrapping');
        }, 260);
      });
    }

    function setWhy(key) {
      const next = key || 'base';
      if (next === state) return;
      state = next;
      applyRoles(rolesFor(ORDER.indexOf(key || 'fast')), !reduced());
      why.dataset.state = next;
      items.forEach((el) => el.setAttribute('aria-pressed', String(el.dataset.key === key)));
      if (key) play($(`[data-panel="${key}"] .ill`, why));
      lock.set();
    }

    applyRoles(rolesFor(1), false);   // estado base

    items.forEach((el) => {
      const key = el.dataset.key;
      el.addEventListener('mousemove', () => {
        if (canHover() && !lock.on()) setWhy(key);
      });
      el.addEventListener('click', () => {
        if (canHover()) setWhy(key);
        else setWhy(state === key ? null : key);       // tap
      });
      el.addEventListener('focus', () => { if (el.matches(':focus-visible')) setWhy(key); });
    });
    why.addEventListener('mouseleave', () => { if (canHover()) setWhy(null); });
  }

  /* -------------------------------------------------------------------
     5 · Testimonios — carrusel (centro enfocado, laterales atenuados)
     ------------------------------------------------------------------- */
  const track = $('.tst-track');
  if (track) {
    const cards = $$('.tst', track);
    const n = cards.length;
    let cur = 0;
    let timer = null;
    let visible = false;
    let hovering = false;

    function layout(animate) {
      cards.forEach((card, i) => {
        const role = i === cur ? 'center' : i === (cur + 1) % n ? 'right' : 'left';
        const prev = card.dataset.role;
        const center = role === 'center';
        card.setAttribute('aria-hidden', String(!center));
        card.tabIndex = center ? -1 : 0;
        const wraps = animate && prev && ((prev === 'left' && role === 'right') || (prev === 'right' && role === 'left'));
        if (!wraps) { card.dataset.role = role; return; }
        card.classList.add('is-wrapping');
        setTimeout(() => {
          card.classList.add('no-anim');
          card.dataset.role = role;
          void card.offsetWidth;
          card.classList.remove('no-anim', 'is-wrapping');
        }, 300);
      });
    }

    const go = (i) => { cur = (i + n) % n; layout(!reduced()); restart(); };
    const next = () => go(cur + 1);
    const prev = () => go(cur - 1);

    cards.forEach((card, i) => {
      card.addEventListener('click', () => { if (i !== cur) go(i); });
      card.addEventListener('keydown', (e) => {
        if ((e.key === 'Enter' || e.key === ' ') && i !== cur) { e.preventDefault(); go(i); }
      });
    });
    track.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight') next();
      if (e.key === 'ArrowLeft') prev();
    });

    // swipe en touch
    let x0 = null;
    track.addEventListener('pointerdown', (e) => { if (e.pointerType !== 'mouse') x0 = e.clientX; });
    track.addEventListener('pointerup', (e) => {
      if (x0 === null) return;
      const dx = e.clientX - x0;
      x0 = null;
      if (Math.abs(dx) > 40) (dx < 0 ? next : prev)();
    });

    // avance automático: solo en vista, sin hover y sin reduced-motion
    function restart() {
      clearInterval(timer);
      if (visible && !hovering && !reduced()) timer = setInterval(next, 7000);
    }
    track.addEventListener('mouseenter', () => { hovering = true; restart(); });
    track.addEventListener('mouseleave', () => { hovering = false; restart(); });
    track.addEventListener('focusin', () => { hovering = true; restart(); });
    track.addEventListener('focusout', () => { hovering = false; restart(); });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(([e]) => { visible = e.isIntersecting; restart(); }, { threshold: 0.4 }).observe(track);
    }

    layout(false);
  }

  /* -------------------------------------------------------------------
     Navegación por vistas (escritorio, TODAS las páginas). La página NO
     scrollea: el <main> se desplaza con una transición propia.
     Cada hijo de <main> es una vista. Un gesto de rueda/trackpad = un paso.
     Si una vista es más alta que la pantalla (precios, un artículo), se
     recorre en pasos de una pantalla, sin saltearse contenido.
     También teclado, swipe, rail y anclas. En mobile (≤ 760px) el scroll
     es el normal.
     ------------------------------------------------------------------- */
  const deskMQ = matchMedia('(min-width: 761px)');
  const docEl = document.documentElement;
  const mainEl = $('main');
  const views = mainEl ? [...mainEl.children] : [];
  const DURATION = 1000;                 // ms, igual que la transición del CSS (--dur-page)
  const STEP = 0.85;                     // dentro de una vista alta: avanza 85% de pantalla
  let paged = false;
  let stops = [0];
  let at = 0;                            // índice en stops
  let pageLock = false;
  let lastInput = 0;

  views.forEach((v) => { if (!v.hasAttribute('tabindex')) v.setAttribute('tabindex', '-1'); });
  const indexOf = (id) => views.findIndex((v) => v.id === id);
  const maxY = () => Math.max(0, mainEl.offsetHeight - innerHeight);

  // posiciones de parada: el comienzo de cada vista y, si es alta, pasos intermedios
  function computeStops() {
    const H = innerHeight;
    const max = maxY();
    const list = [];
    views.forEach((v) => {
      const top = v.offsetTop;
      const h = v.offsetHeight;
      // apenas más alta que la pantalla: una sola parada, centrada (solo se recorta aire)
      if (h > H + 2 && h - H < H * 0.3) { list.push(top + (h - H) / 2); return; }
      list.push(top);
      if (h > H + 2) {
        for (let y = top + H * STEP; y < top + h - H; y += H * STEP) list.push(y);
        list.push(top + h - H);
      }
    });
    stops = [...new Set(list.map((y) => Math.round(Math.max(0, Math.min(max, y)))))]
      .sort((a, b) => a - b)
      .filter((y, i, arr) => i === 0 || y - arr[i - 1] > 4);
  }
  const currentY = () => stops[at] || 0;
  const stopForY = (y) => {                            // la última parada que no pasa de y
    let best = 0;
    stops.forEach((s, i) => { if (s <= y + 1) best = i; });
    return best;
  };
  const viewAt = (y) => views.find((v) => v.offsetTop <= y + innerHeight / 2 && y + innerHeight / 2 < v.offsetTop + v.offsetHeight);

  function applyPage() {
    const y = currentY();
    mainEl.style.setProperty('--page-y', y);
    const v = viewAt(y);
    if (v && v.id) setRail(v.id);
  }
  // se libera cuando terminó la transición y el gesto dejó de mandar eventos
  // (el trackpad sigue emitiendo por inercia: así un gesto no salta dos pasos)
  function releaseLock() {
    if (performance.now() - lastInput < 220) setTimeout(releaseLock, 120);
    else pageLock = false;
  }
  function goToY(y) {
    computeStops();                                    // el contenido puede haber cambiado (FAQ, formulario)
    const i = stopForY(Math.min(y, maxY()));
    if (i === at && Math.abs(stops[i] - (parseFloat(mainEl.style.getPropertyValue('--page-y')) || 0)) < 2) return;
    at = i;
    pageLock = true;
    applyPage();
    setTimeout(releaseLock, reduced() ? 60 : DURATION);
  }
  function step(dir) {
    const from = currentY();
    computeStops();
    at = stopForY(from);
    const i = Math.max(0, Math.min(stops.length - 1, at + dir));
    if (i === at) return;
    goToY(stops[i]);
  }
  const goToView = (i) => { if (i >= 0) goToY(views[i].offsetTop); };

  function setPaged(on) {
    if (on === paged) return;
    if (on) {
      const y = scrollY;
      paged = true;
      docEl.classList.add('paged');
      window.scrollTo(0, 0);
      computeStops();
      at = stopForY(y);
      applyPage();
    } else {
      const y = currentY();
      paged = false;
      docEl.classList.remove('paged');
      mainEl.style.removeProperty('--page-y');
      window.scrollTo(0, y);
    }
  }

  // rueda / trackpad
  window.addEventListener('wheel', (e) => {
    if (!paged || e.ctrlKey) return;                     // ctrl + rueda = zoom
    const ta = e.target.closest && e.target.closest('textarea');
    if (ta && ta.scrollHeight > ta.clientHeight) return; // dejar scrollear el mensaje
    e.preventDefault();
    lastInput = performance.now();
    if (pageLock || Math.abs(e.deltaY) < 4) return;
    step(e.deltaY > 0 ? 1 : -1);
  }, { passive: false });

  // teclado
  window.addEventListener('keydown', (e) => {
    if (!paged || e.altKey || e.ctrlKey || e.metaKey) return;
    if (e.target.closest && e.target.closest('input, textarea, select, [contenteditable]')) return;
    const keys = {
      ArrowDown: 1, PageDown: 1, ArrowUp: -1, PageUp: -1,
      ' ': e.shiftKey ? -1 : 1, Home: -999, End: 999,
    };
    if (!(e.key in keys)) return;
    if (e.key === ' ' && e.target.closest && e.target.closest('button, a')) return;
    e.preventDefault();
    if (pageLock) return;
    if (Math.abs(keys[e.key]) > 1) goToY(keys[e.key] > 0 ? maxY() : 0);
    else step(keys[e.key]);
  });

  // swipe (pantallas táctiles grandes)
  let touchY = null;
  window.addEventListener('touchstart', (e) => { if (paged) touchY = e.touches[0].clientY; }, { passive: true });
  window.addEventListener('touchmove', (e) => { if (paged) e.preventDefault(); }, { passive: false });
  window.addEventListener('touchend', (e) => {
    if (!paged || touchY === null) return;
    const dy = touchY - e.changedTouches[0].clientY;
    touchY = null;
    if (Math.abs(dy) > 50 && !pageLock) step(dy > 0 ? 1 : -1);
  });

  // rail, CTAs y cualquier ancla interna (#contacto, etc.)
  document.addEventListener('click', (e) => {
    const a = e.target.closest && e.target.closest('a[href^="#"]');
    if (!a) return;
    const i = indexOf(a.getAttribute('href').slice(1));
    if (i < 0) return;
    e.preventDefault();
    if (paged) goToView(i);
    else views[i].scrollIntoView({ behavior: reduced() ? 'auto' : 'smooth', block: 'start' });
    views[i].focus({ preventScroll: true });   // Tab sigue dentro de la vista elegida
  });

  // tabular a un elemento fuera de la pantalla lleva hasta él
  document.addEventListener('focusin', (e) => {
    if (!paged || !mainEl.contains(e.target) || views.includes(e.target)) return;
    const r = e.target.getBoundingClientRect();
    if (r.top >= 0 && r.bottom <= innerHeight) return;
    goToY(currentY() + r.top - innerHeight * 0.3);
  });
  // el navegador no debe scrollear por su cuenta en modo vistas
  window.addEventListener('scroll', () => { if (paged && scrollY !== 0) window.scrollTo(0, 0); });

  // inicio (respeta un #ancla en la URL)
  setPaged(deskMQ.matches);
  if (paged && location.hash) {
    const i = indexOf(location.hash.slice(1));
    if (i > 0) { computeStops(); at = stopForY(views[i].offsetTop); applyPage(); }
  }
  deskMQ.addEventListener('change', (e) => setPaged(e.matches));
  addEventListener('resize', () => {
    if (!paged) return;
    const y = currentY();
    computeStops();
    at = stopForY(y);
    applyPage();
  });

  /* -------------------------------------------------------------------
     Ilustraciones de servicio fuera del home (hero de cada servicio):
     mismo código; se expanden y animan una vez al entrar en vista.
     ------------------------------------------------------------------- */
  $$('[data-play-on-view]').forEach((stage) => {
    onceInView(stage, () => {
      stage.classList.add('is-active');
      play($('.ill', stage));
    });
  });

  /* Timeline: el arco se dibuja y los hitos se encienden al entrar en vista.
     Después recorre los pasos solo (como el carrusel del home); el que
     tocás o señalás queda activo. */
  $$('.timeline').forEach((tl) => {
    const cards = $$('.timeline-steps > .card', tl);
    const nodes = $$('.timeline-node', tl);
    let i = -1;
    let timer = null;
    let hold = false;
    const set = (k) => {
      i = k;
      cards.forEach((c, n) => c.classList.toggle('is-on', n === k));
      nodes.forEach((c, n) => c.classList.toggle('is-on', n === k));
    };
    const loop = () => {
      clearInterval(timer);
      if (!reduced()) timer = setInterval(() => { if (!hold) set((i + 1) % cards.length); }, 3200);
    };
    cards.forEach((c, n) => {
      c.addEventListener('mouseenter', () => { hold = true; set(n); });
      c.addEventListener('mouseleave', () => { hold = false; });
      c.addEventListener('click', () => set(n));
    });
    onceInView(tl, () => {
      tl.classList.add('play');
      setTimeout(() => { set(0); loop(); }, reduced() ? 0 : 1800);
    }, 0.3);
  });

  /* Contadores: los números de la trayectoria suben al entrar en vista */
  $$('[data-count]').forEach((el) => {
    const to = parseFloat(el.dataset.count);
    const dec = parseInt(el.dataset.decimals || '0', 10);
    const suf = el.dataset.suffix || '';
    onceInView(el, () => {
      if (reduced()) return;
      const t0 = performance.now();
      const D = 1800;                                     // --dur-long
      const tick = (now) => {
        const p = Math.min(1, (now - t0) / D);
        const e = 1 - Math.pow(1 - p, 3);                  // salida suave
        el.textContent = (to * e).toFixed(dec) + suf;
        if (p < 1) requestAnimationFrame(tick);
      };
      el.textContent = (0).toFixed(dec) + suf;
      requestAnimationFrame(tick);
    }, 0.5);
  });

  /* Carrera del programa: las barras corren al entrar en vista */
  $$('[data-race]').forEach((r) => onceInView(r, () => r.classList.add('play'), 0.35));

  /* Entregables: la tarjeta señalada se expande (como en el home) */
  $$('[data-expand]').forEach((row) => {
    const cards = $$('.expand-card', row);
    const lock = makeLock(500);
    const set = (c) => { cards.forEach((x) => x.classList.toggle('is-on', x === c)); lock.set(); };
    set(cards[0]);
    cards.forEach((c) => {
      c.addEventListener('mousemove', () => { if (canHover() && !lock.on() && !c.classList.contains('is-on')) set(c); });
      c.addEventListener('click', () => set(c));
      c.addEventListener('focus', () => set(c));
    });
  });

  /* Selector de dos estados */
  $$('[data-switch]').forEach((sw) => {
    const btns = $$('button', sw);
    const panels = $$('.switch-panel', sw.nextElementSibling);
    btns.forEach((b, n) => b.addEventListener('click', () => {
      btns.forEach((x, m) => { x.classList.toggle('is-on', m === n); x.setAttribute('aria-selected', String(m === n)); });
      panels.forEach((p, m) => p.classList.toggle('is-on', m === n));
    }));
  });

  /* Out of the Box · Shout to win: mantener apretado = gritar.
     El nivel sube mientras apretás y baja al soltar. Pasar la marca gana. */
  $$('[data-shout]').forEach((box) => {
    const bars = $('[data-shout-bars]', box);
    const btn = $('[data-shout-btn]', box);
    const title = $('[data-shout-title]', box);
    const N = 28;
    const MARK = 0.85;
    bars.innerHTML = Array.from({ length: N }, () => '<i></i>').join('');
    const els = $$('i', bars);
    let level = 0;
    let down = false;
    let won = false;
    let raf = null;
    let last = 0;
    const draw = (t) => {
      els.forEach((el, k) => {
        const x = (k + 0.5) / N;
        // forma de onda: más alta al centro, con vibración mientras "gritás"
        const shape = 0.55 + 0.45 * Math.sin(Math.PI * x);
        const jitter = down ? 0.12 * Math.sin(t / 70 + k * 1.7) : 0;
        const h = Math.max(0.04, Math.min(1, level * shape + jitter * level));
        el.style.setProperty('--h', `${(h * 100).toFixed(1)}%`);
        el.classList.toggle('is-on', h > 0.06);
      });
    };
    const frame = (t) => {
      const dt = last ? Math.min(0.05, (t - last) / 1000) : 0.016;
      last = t;
      level += down ? dt * 0.42 : -dt * 0.9;
      level = Math.max(0, Math.min(1, level));
      if (!won && level >= MARK) {
        won = true;
        box.classList.add('is-won');
        title.textContent = 'You win.';
        btn.textContent = 'Again';
      }
      draw(t);
      if (down || level > 0) raf = requestAnimationFrame(frame);
      else { raf = null; last = 0; }
    };
    const start = (e) => {
      if (e) e.preventDefault();
      if (won && !down) {                                 // "Again": reinicia
        won = false; box.classList.remove('is-won');
        title.textContent = 'Try it.'; btn.textContent = 'Hold to shout';
      }
      down = true; btn.classList.add('is-down');
      if (!raf) raf = requestAnimationFrame(frame);
    };
    const stop = () => { down = false; btn.classList.remove('is-down'); };
    btn.addEventListener('pointerdown', start);
    addEventListener('pointerup', stop);
    btn.addEventListener('pointerleave', stop);
    btn.addEventListener('keydown', (e) => { if ((e.key === ' ' || e.key === 'Enter') && !e.repeat) start(e); });
    btn.addEventListener('keyup', (e) => { if (e.key === ' ' || e.key === 'Enter') stop(); });
    draw(0);
  });

  /* -------------------------------------------------------------------
     Preguntas frecuentes (acordeón)
     ------------------------------------------------------------------- */
  $$('.faq-item').forEach((item) => {
    const q = $('.faq-q', item);
    q.addEventListener('click', () => {
      const open = !item.classList.contains('is-open');
      item.classList.toggle('is-open', open);
      q.setAttribute('aria-expanded', String(open));
    });
  });

  /* -------------------------------------------------------------------
     Evaluación gratuita: formulario multipaso (/contacto)
     Una pregunta por pantalla; valida antes de avanzar.
     ------------------------------------------------------------------- */
  const wizard = $('.wizard');
  if (wizard) {
    const steps = $$('.wizard-step', wizard);
    const bar = $('.progress > span', wizard);
    const count = $('[data-step-count]', wizard);
    const err = $('.wizard-error', wizard);
    const back = $('[data-back]', wizard);
    const next = $('[data-next]', wizard);
    const done = $('.wizard-done', wizard.parentElement);
    let i = 0;

    const show = (n) => {
      i = n;
      steps.forEach((s, k) => { s.hidden = k !== i; });
      bar.style.setProperty('--p', (i + 1) / steps.length);
      count.textContent = `${i + 1} / ${steps.length}`;
      back.hidden = i === 0;
      next.textContent = i === steps.length - 1 ? next.dataset.last : next.dataset.label;
      err.textContent = '';
      const first = $('input, textarea', steps[i]);
      if (first && wizard.dataset.started) first.focus({ preventScroll: true });
    };
    const valid = () => {
      const s = steps[i];
      if (s.dataset.need === 'one' && !$('input:checked', s)) return s.dataset.error;
      for (const input of $$('input[required]', s)) {
        const bad = !input.value.trim() || (input.type === 'email' && !/^\S+@\S+\.\S+$/.test(input.value));
        input.classList.toggle('is-invalid', bad);
        if (bad) { input.focus(); return s.dataset.error; }
      }
      return '';
    };
    back.addEventListener('click', () => { wizard.dataset.started = '1'; show(i - 1); });
    wizard.addEventListener('submit', (e) => {
      e.preventDefault();
      wizard.dataset.started = '1';
      const msg = valid();
      if (msg) { err.textContent = msg; return; }
      if (i < steps.length - 1) { show(i + 1); return; }
      const fd = new FormData(wizard);
      const data = Object.fromEntries(fd);
      data.need = fd.getAll('need');
      // TODO: conectar el envío (endpoint / servicio de formularios) — pendiente de definir.
      wizard.dispatchEvent(new CustomEvent('wbu:submit', { detail: data, bubbles: true }));
      wizard.hidden = true;
      if (done) done.hidden = false;
    });
    wizard.addEventListener('input', (e) => e.target.classList && e.target.classList.remove('is-invalid'));
    // ?need=out-of-the-box (CTA de Out of the Box) llega con esa opción ya elegida
    const pre = new URLSearchParams(location.search).get('need');
    if (pre) {
      const box = $$('input[name="need"]', wizard).find((el) => el.value === pre);
      if (box) box.checked = true;
    }
    show(0);
  }

  /* -------------------------------------------------------------------
     6 · Formulario
     ------------------------------------------------------------------- */
  const form = $('.form');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      let ok = true;
      $$('input[required]', form).forEach((input) => {
        const bad = !input.value.trim() || (input.type === 'email' && !/^\S+@\S+\.\S+$/.test(input.value));
        input.classList.toggle('is-invalid', bad);
        if (bad && ok) { input.focus(); ok = false; }
      });
      if (!ok) return;
      const data = Object.fromEntries(new FormData(form));
      data.help = new FormData(form).getAll('help');
      // TODO: conectar el envío (endpoint / servicio de formularios) — pendiente de definir.
      form.dispatchEvent(new CustomEvent('wbu:submit', { detail: data, bubbles: true }));
    });
    form.addEventListener('input', (e) => e.target.classList.remove('is-invalid'));
  }
})();
