
# CYOA-18 — Tutorial Notes

## Intro Scene Example: "The Crossroads"

**Scene ID:** MENU  
**Title:** The Crossroads  
**Where/When:** Foggy clearing, morning

**What happens here?**  
You wake up in a foggy clearing, your head aching. “How did I get here?” you ask aloud. As the fog begins to lift, you realize you don’t remember where — or who — you are. A rustling comes from the trees, heavy and close. You need to move! Which way will you go?

**Choices**
- **Choice A (North – Chris):** You push into the northern hills. → Next Scene: `N-001`
- **Choice B (East – Travis):** You follow the rising sun toward the trade roads. → Next Scene: `E-001`
- **Choice C (South – Charlie):** You head for the marshy ground. → Next Scene: `S-001`
- **Choice D (West – Trey):** You turn into the deep forest. → Next Scene: `W-001`

**Exit line:**  
*The crossroads fades behind you as your chosen path unfolds.*

---

## Scene Form (Blank Template)

**Author Name:** _________________________  
**Direction/ID:** N / E / S / W
- Example: Trey → W-001, W-002, W-003.
- Chris → N-###
- Travis → E-###
- Charlie → S-###

**Scene ID:** ________  
**Title:** __________________________  
**Where/When:** __________________________  
*(Example: stormy night, forest clearing, dawn at the docks.)*

**What happens here?**  
2–5 sentences describing the scene. Add atmosphere, a little tension, or a problem to solve.

---

### Choices (Write at least 2)

**Choice A:** ________________________________
- **Outcome:** __________________________
- **Next Scene ID:** ____________________

**Choice B:** ________________________________
- **Outcome:** __________________________
- **Next Scene ID:** ____________________

**Choice C (optional):** _______________________
- **Outcome:** __________________________
- **Next Scene ID:** ____________________

**Exit line:**  
*(One sentence to close the scene and push the player to click a button.)*  
Examples:
- “The door creaks open, and something stirs in the dark.”
- “Your stomach growls — the forest is quiet, too quiet.”

---

## Numbering Rule of Thumb

- **Parent = number, children = letters.**
- Every scene gets a number (e.g. `N-001`).
- Each choice inside creates a child scene:
    - Choice A → `N-001A`
    - Choice B → `N-001B`
    - Choice C → `N-001C`
- If a child scene also branches, just keep adding letters:
    - From `N-001B`:
        - Choice A → `N-001BA`
        - Choice B → `N-001BB`

This keeps paths clear and avoids overlap.

---

✅ That’s all you need to get writing. No forks, no Git jargon,  Just scenes, choices, IDs, and exit lines.

///////////////////////////////4. Example (Ready to Steal)//////////////////////////////////////////////////
   {
   "scene_id": "S-001",
   "title": "Swamp Path",
   "where_when": "Southern marsh, dusk",
   "text": "You step into the marsh. The mud grips your boots and the air hums with insects.",
   "choices": [
   {
   "label": "Follow the fireflies",
   "next_id": "S-002"
   },
   {
   "label": "Push deeper into the reeds",
   "next_id": "S-003"
   }
   ],
   "exit_line": "The marsh closes in as your path narrows."