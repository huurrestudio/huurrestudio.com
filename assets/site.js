// The header's Games menu is a <details> element, so it works without
// JavaScript. This only adds the finishing touches: it closes when you
// click elsewhere, press Escape, or pick a link.
document.addEventListener('click', e => {
  document.querySelectorAll('details.menu[open]').forEach(m => { if (!m.contains(e.target)) m.open = false; });
});
document.addEventListener('keydown', e => {
  if (e.key !== 'Escape') return;
  document.querySelectorAll('details.menu[open]').forEach(m => { m.open = false; m.querySelector('summary').focus(); });
});
