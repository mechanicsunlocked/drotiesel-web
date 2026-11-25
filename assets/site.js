// Light/dark switch, stored in the browser. Without a stored choice the system setting applies.
(function () {
  var root = document.documentElement, btn = document.getElementById('theme');
  function current() {
    var t = root.getAttribute('data-theme');
    if (t) return t;
    return window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }
  function label() { if (btn) btn.textContent = current() === 'dark' ? 'Light' : 'Dark'; }
  if (btn) btn.addEventListener('click', function () {
    var next = current() === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('theme', next); } catch (e) {}
    label();
  });
  label();
  var y = document.getElementById('y'); if (y) y.textContent = new Date().getFullYear();
})();

// Truing-stand scene: the wheel turns with the scroll position, the dial reads the radial runout.
// The reading depends only on the scroll position: -15 .. +15 hundredths, one cycle per wheel turn.
(function () {
  var wheel = document.getElementById('rw-wheel'), needle = document.getElementById('rw-needle'),
      out = document.getElementById('rw-value');
  if (!wheel || !needle) return;
  var cx = needle.getAttribute('data-cx'), cy = needle.getAttribute('data-cy');
  var PX_PER_TURN = 1600;                       // scroll distance for one wheel turn
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  function draw(scroll) {
    var turn = scroll / PX_PER_TURN;            // wheel turns
    var deg = turn * 360;
    var reading = 15 * Math.sin(turn * 2 * Math.PI);          // hundredths of a mm
    wheel.setAttribute('transform', 'rotate(' + deg.toFixed(2) + ')');
    needle.setAttribute('transform', 'rotate(' + (reading * 3.6).toFixed(2) + ' ' + cx + ' ' + cy + ')');
    if (out) { var mm = reading / 100; out.textContent = (mm >= 0 ? '+' : '−') + Math.abs(mm).toFixed(2) + ' mm'; }
  }
  if (reduce) { draw(PX_PER_TURN * 0.11); return; }
  var queued = false;
  function onScroll() {
    if (queued) return; queued = true;
    requestAnimationFrame(function () { queued = false; draw(window.scrollY || window.pageYOffset || 0); });
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  draw(window.scrollY || 0);
})();
