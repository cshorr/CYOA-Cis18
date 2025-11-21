

window.shake = function (intensity = 8, duration = 300, target = ".panel") {
  const el = document.querySelector(target);
  if (!el) return;
  el.style.setProperty("--shake-intensity", intensity + "px");
  el.style.setProperty("--shake-duration", duration + "ms");
  el.classList.remove("shake");
  void el.offsetWidth; // reflow to restart animation
  el.classList.add("shake");
  setTimeout(() => el.classList.remove("shake"), duration);
};
