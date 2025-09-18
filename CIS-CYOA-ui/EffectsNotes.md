# Effects Bundle: Sound + Screen Shake (Flask + plain JS/CSS)

## What this gives you
- Play a sound on any button or scene load.
- Screen shake the whole page (or a specific container).
- No frameworks. Works with Flask/Jinja templates.

---

## 1) HTML (put in your base template)
Add these **once** in `templates/base.html` (or whatever your layout is).

```html
<!-- SOUND: preload common effects (add/remove as needed) -->
<audio id="sfx-sword"   src="{{ url_for('static', filename='sounds/sword.mp3') }}"></audio>
<audio id="sfx-bow"     src="{{ url_for('static', filename='sounds/bow.mp3') }}"></audio>
<audio id="sfx-hit"     src="{{ url_for('static', filename='sounds/hit.mp3') }}"></audio>
<audio id="sfx-ambient" src="{{ url_for('static', filename='sounds/ambient.mp3') }}"></audio>

<!-- OPTIONAL: auto-play ambient on scene load -->
{% if play_ambient %}
<script>
  window.addEventListener("load", () => {
    const a = document.getElementById("sfx-ambient");
    if (a) { a.currentTime = 0; a.play().catch(()=>{}); } // ignore autoplay blockers
  });
</script>
{% endif %}
///////////////Usage in any template button/link:
<!-- Click to play a sword sound -->
<button class="btn sfx" data-sfx="sword">Draw Sword</button>

<!-- Click to play a bow sound AND shake -->
<button class="btn sfx shake-on-click" data-sfx="bow">Loose Arrow</button>

<!-- Just shake (no sound) -->
<button class="btn shake-on-click">Take Hit</button>
///////////////////////////////2) CSS (add to your existing CSS file, e.g. static/style.css or your theme)
/* Screen shake animation */
@keyframes shake {
  0%   { transform: translate(1px, 1px) rotate(0deg); }
  10%  { transform: translate(-1px, -2px) rotate(-1deg); }
  20%  { transform: translate(-3px, 0) rotate(1deg); }
  30%  { transform: translate(3px, 2px) rotate(0deg); }
  40%  { transform: translate(1px, -1px) rotate(1deg); }
  50%  { transform: translate(-1px, 2px) rotate(-1deg); }
  60%  { transform: translate(-3px, 1px) rotate(0deg); }
  70%  { transform: translate(3px, 1px) rotate(-1deg); }
  80%  { transform: translate(-1px, -1px) rotate(1deg); }
  90%  { transform: translate(1px, 2px) rotate(0deg); }
  100% { transform: translate(0, 0) rotate(0); }
}

.shake {
  animation: shake 0.5s;
  animation-iteration-count: 1;
}

/* Optional: reduce motion respect */
@media (prefers-reduced-motion: reduce) {
  .shake { animation: none; }
}
/////////////3) JavaScript- NOT JAVA!!  (put at the bottom of base.html, before </body>)3) JavaScript (put at the bottom of base.html, before </body>)
<script>
// ---- SOUND ----
function playSfx(name) {
  const el = document.getElementById("sfx-" + name);
  if (!el) return;
  try {
    el.currentTime = 0;
    el.play();
  } catch (_) { /* ignore autoplay/security blocks */ }
}

// Delegate clicks for any element with class "sfx"
document.addEventListener("click", (e) => {
  const target = e.target.closest(".sfx");
  if (target) {
    const which = target.getAttribute("data-sfx");
    if (which) playSfx(which);
  }
});

// ---- SCREEN SHAKE ----
// Shake the whole page (body) or pass a specific element.
function triggerShake(el = document.body, ms = 500) {
  if (!el) return;
  el.classList.add("shake");
  setTimeout(() => el.classList.remove("shake"), ms);
}

// Any element with "shake-on-click" will shake body on click
document.addEventListener("click", (e) => {
  const target = e.target.closest(".shake-on-click");
  if (target) triggerShake(document.body, 500);
});

// Example hooks you can call from your scene JS or inline:
//   triggerShake();                 // shake whole screen
//   playSfx("hit");                 // play "hit" sound
//   playSfx("sword");               // play "sword" sound
</script>
//////////////////////4) Flask tips (optional)//////////////////////////////////////////////////////////////

Put audio files in: static/sounds/ (e.g., sword.mp3, bow.mp3, hit.mp3, ambient.mp3).

To auto-play ambient on a specific scene, render with: return render_template("scene.html", play_ambient=True).

Buttons only need class="sfx" and data-sfx="NAME" to play a sound, and shake-on-click to add shake.

////////////////////////5) Quick sanity checklist ( good luck with that )///////////////////////////////////////////

Files exist at /static/sounds/*.mp3 and paths match.

CSS loaded (your base template links the CSS).

Script block is after the elements or at the end of body.

Browser may block auto-play; user click will always play.