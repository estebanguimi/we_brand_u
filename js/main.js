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
      img.src = cfg.src;
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
     Rail: sección activa + resplandor
     ------------------------------------------------------------------- */
  const rail = $('.rail');
  const links = $$('.rail-link');
  function setRail(id) {
    links.forEach((a) => {
      const on = a.dataset.target === id;
      a.classList.toggle('is-active', on);
      if (on) {
        a.setAttribute('aria-current', 'true');
        rail.style.setProperty('--gy', `${a.offsetTop + a.offsetHeight / 2}px`);
      } else {
        a.removeAttribute('aria-current');
      }
    });
  }
  setRail('hero');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => { if (e.isIntersecting) setRail(e.target.id); });
    }, { rootMargin: '-45% 0px -45% 0px' });
    $$('[data-section]').forEach((s) => io.observe(s));
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
      card.addEventListener('click', () => {
        if (canHover()) setSvc(key);
        else setSvc(current === key ? null : key);     // tap
      });
      card.addEventListener('focus', () => { if (card.matches(':focus-visible')) setSvc(key); });
    });
    svcRow.addEventListener('mouseleave', () => { if (canHover()) setSvc(null); });

    // al entrar en vista: se trazan los dibujos del estado inicial
    onceInView(svcRow, () => {
      play($('.ill-tech', svcRow));
      play($('.ill-growth', svcRow));
    });
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
