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
