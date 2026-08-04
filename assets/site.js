/* ============================================================
   HARDT — interaction layer

   Vanilla, no dependencies, ~4KB. Everything degrades: with JS off
   the page is fully readable, the nav is reachable, and every
   accordion panel is open.

   Motion is deliberately restrained. The brand is "quiet confidence" —
   things settle into place, nothing bounces or slides in from off
   screen. Every animation is skipped under prefers-reduced-motion.
   ============================================================ */
(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- reveal on scroll -------------------------------
     Elements start slightly low and transparent, then settle.
     If IntersectionObserver is missing or motion is reduced we
     just mark everything visible immediately.               */
  var reveals = document.querySelectorAll('[data-reveal]');
  if (reduced || !('IntersectionObserver' in window)) {
    reveals.forEach(function (el) { el.classList.add('is-in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target;
        // stagger siblings so a grid resolves left-to-right
        var delay = parseInt(el.getAttribute('data-reveal-delay') || '0', 10);
        setTimeout(function () { el.classList.add('is-in'); }, delay);
        io.unobserve(el);
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.08 });
    reveals.forEach(function (el) { io.observe(el); });
  }

  /* ---------- mobile navigation ------------------------------
     The desktop nav is hidden under 940px, so without this there
     is no way to reach any page on a phone.                  */
  var burger = document.querySelector('[data-nav-toggle]');
  var drawer = document.getElementById('mobile-nav');
  if (burger && drawer) {
    var lastFocus = null;

    var setOpen = function (open) {
      burger.setAttribute('aria-expanded', String(open));
      drawer.hidden = !open;
      document.documentElement.classList.toggle('nav-open', open);
      if (open) {
        lastFocus = document.activeElement;
        var first = drawer.querySelector('a, button');
        if (first) first.focus();
      } else if (lastFocus) {
        lastFocus.focus();
      }
    };

    burger.addEventListener('click', function () {
      setOpen(burger.getAttribute('aria-expanded') !== 'true');
    });

    drawer.addEventListener('click', function (e) {
      if (e.target.closest('a')) setOpen(false);
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && burger.getAttribute('aria-expanded') === 'true') setOpen(false);
    });

    // keep focus inside the drawer while it's open
    drawer.addEventListener('keydown', function (e) {
      if (e.key !== 'Tab') return;
      var f = drawer.querySelectorAll('a[href], button:not([disabled])');
      if (!f.length) return;
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });

    window.addEventListener('resize', function () {
      if (window.innerWidth > 940 && burger.getAttribute('aria-expanded') === 'true') setOpen(false);
    });
  }

  /* ---------- accordions (FAQ) -------------------------------
     Markup is a plain button + region. With JS off every panel is
     already open, so the content is always indexable and readable. */
  document.querySelectorAll('[data-accordion]').forEach(function (root) {
    root.querySelectorAll('.acc__q').forEach(function (btn, i) {
      var panel = btn.nextElementSibling;
      if (!panel) return;
      var open = i === 0;                       // first one starts open
      btn.setAttribute('aria-expanded', String(open));
      panel.hidden = !open;
      btn.addEventListener('click', function () {
        var isOpen = btn.getAttribute('aria-expanded') === 'true';
        btn.setAttribute('aria-expanded', String(!isOpen));
        panel.hidden = isOpen;
      });
    });
  });

  /* ---------- before / after slider --------------------------
     Pointer + keyboard. The "after" image is clipped by a inset
     that follows the handle.                                  */
  document.querySelectorAll('[data-compare]').forEach(function (el) {
    var handle = el.querySelector('.ba__handle');
    var top = el.querySelector('.ba__after');
    if (!handle || !top) return;

    var set = function (pct) {
      pct = Math.max(0, Math.min(100, pct));
      el.style.setProperty('--pos', pct + '%');
      handle.setAttribute('aria-valuenow', Math.round(pct));
    };
    set(50);

    var fromEvent = function (e) {
      var r = el.getBoundingClientRect();
      var x = (e.touches ? e.touches[0].clientX : e.clientX) - r.left;
      set((x / r.width) * 100);
    };

    var dragging = false;
    var start = function (e) { dragging = true; fromEvent(e); e.preventDefault(); };
    var move  = function (e) { if (dragging) fromEvent(e); };
    var end   = function () { dragging = false; };

    el.addEventListener('mousedown', start);
    el.addEventListener('touchstart', start, { passive: false });
    window.addEventListener('mousemove', move);
    window.addEventListener('touchmove', move, { passive: true });
    window.addEventListener('mouseup', end);
    window.addEventListener('touchend', end);

    handle.addEventListener('keydown', function (e) {
      var cur = parseFloat(el.style.getPropertyValue('--pos')) || 50;
      var step = e.shiftKey ? 10 : 3;
      if (e.key === 'ArrowLeft')  { set(cur - step); e.preventDefault(); }
      if (e.key === 'ArrowRight') { set(cur + step); e.preventDefault(); }
      if (e.key === 'Home')       { set(0);  e.preventDefault(); }
      if (e.key === 'End')        { set(100); e.preventDefault(); }
    });
  });

  /* ---------- header state -----------------------------------
     Header gains a shadow once you've left the top, and the sticky
     mobile call bar appears only after the hero has scrolled away
     so it never covers the primary CTA.                       */
  var head = document.querySelector('.site-head');
  var bar = document.querySelector('[data-callbar]');
  var hero = document.querySelector('[data-hero]');

  var onScroll = function () {
    var y = window.pageYOffset;
    if (head) head.classList.toggle('is-stuck', y > 12);
    if (bar) {
      var past = hero ? y > hero.offsetHeight * 0.75 : y > 600;
      bar.classList.toggle('is-up', past);
    }
  };
  var ticking = false;
  window.addEventListener('scroll', function () {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(function () { onScroll(); ticking = false; });
  }, { passive: true });
  onScroll();

  /* ---------- form: honest inline validation -----------------
     No red-alarm styling until the field has actually been left
     in a bad state. Nobody needs to be shouted at here.       */
  document.querySelectorAll('form[data-validate]').forEach(function (form) {
    form.querySelectorAll('input, select, textarea').forEach(function (f) {
      f.addEventListener('blur', function () {
        if (f.value.trim()) f.classList.remove('is-bad');
        else if (f.required) f.classList.add('is-bad');
      });
      f.addEventListener('input', function () { f.classList.remove('is-bad'); });
    });
  });
})();
