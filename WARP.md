# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

Project overview
- Stack: Python + Flask (templates/Jinja2, static assets)
- Entry point: app.py
- Data-driven CYOA (Choose Your Own Adventure) game; scenes are stored as JSON and rendered via a shared scene template with themed styling per author/path.

Common commands (Windows PowerShell)
- Create and activate virtualenv, install dependencies
```pwsh path=null start=null
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

- Run the development server (auto-reload on Python code changes)
```pwsh path=null start=null
python app.py
```

Notes
- There is no configured linter or test suite in this repo. Do not assume commands for linting or tests exist.
- Scene JSON is loaded at process start. Editing JSON files will not hot-reload; restart the server to pick up changes.

High-level architecture
- Routing
  - GET / renders the Crossroads (templates/home.html) with the "crossroads" theme and links to each author’s story.
  - Each author has a start route that redirects to a canonical first scene ID:
    - /chris -> N-001, /travis -> E-001, /charlie -> S-001, /trey -> W-001.
  - Dynamic scene routes per author map to a single scene renderer:
    - /chris/<scene_id>, /travis/<scene_id>, /charlie/<scene_id>, /trey/<scene_id>.
  - Special endpoints: /death and /the_end render shared end screens.
  - Optional Oracle path mirrors the same pattern: /oracle and /oracle/<scene_id>.

- Data loading (on import)
  - app.py defines one JSON file per path under static/data/:
    - scenes_chris.json, scenes_travis.json, scenes_charlie.json, scenes_trey.json, scenes_oracle.json (optional).
  - Each file is loaded into an in-memory dict keyed by scene_id. Missing files are tolerated (loaded as empty dicts); unknown scene IDs 404.
  - Expected JSON schema (summarized from README):
    - scene_id, title, where_when, text, choices[] (each: label, next_id), exit_line.
    - scene_id conventions: N/S/E/W prefixes for Chris/Charlie/Travis/Trey; keep IDs unique within each author.

- Rendering and navigation
  - All scenes use templates/scene.html which:
    - Displays title, where_when, text (with newlines converted via replace_all_newlines filter).
    - Renders choices as buttons. Choice handling:
      - next_id == "END" -> links to /the_end (Finish)
      - next_id == "DIE" -> links to /death with optional death_text
      - Otherwise routes back to the author’s dynamic scene endpoint with the next_id
    - Renders an optional exit_line and a link back to the Crossroads.

- Theming
  - templates/base.html includes a stylesheet based on a theme value provided by the route.
  - Themes are CSS files under static/themes/: chris.css, travis.css, charlie.css, trey.css, crossroads.css (and oracle.css if Oracle is enabled).
  - Each route sets an appropriate theme string when rendering.

Repository essentials
- app.py: Flask app, routes, JSON loaders, Jinja filter replace_all_newlines.
- templates/: Jinja templates (base.html, home.html, scene.html, death.html, TheEnd.html).
- static/themes/: CSS per theme.
- static/data/: Expected location for scenes_*.json files referenced by app.py (may not be present until authors add their stories).
- requirements.txt: Flask dependency.

How this relates to README.md
- The README defines the scene JSON schema and author workflow. Ensure JSON files conform to that schema and are saved under static/data/ with the expected filenames so the loaders in app.py can find them.

Troubleshooting
- 404 on a scene: The corresponding scenes_*.json likely doesn’t include that scene_id, or the JSON file is missing; confirm the file exists under static/data/ and restart the dev server.
- Missing styles: Ensure the theme CSS exists under static/themes/ and matches the theme name set by the route.
