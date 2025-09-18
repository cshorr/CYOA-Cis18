from flask import Flask, render_template, url_for, redirect, abort, request
import json
from pathlib import Path

app = Flask(__name__)

# --- Base paths ---
BASE_DIR = Path(__file__).parent.resolve()

# ========= CHRIS (NORTH) =========
SCENES_FILE_CHRIS = BASE_DIR / "static" / "data" / "scenes_chris.json"

def _load_chris():
    with SCENES_FILE_CHRIS.open(encoding="utf-8") as f:
        raw = json.load(f)
    return {str(s["scene_id"]).strip(): s for s in raw}

try:
    CHRIS = _load_chris()
except FileNotFoundError:
    CHRIS = {}

def get_chris(scene_id: str) -> dict:
    key = str(scene_id).strip()
    try:
        return CHRIS[key]
    except KeyError:
        abort(404, f"Scene {key} not found")


# ========= TRAVIS (EAST) =========
SCENES_FILE_TRAVIS = BASE_DIR / "static" / "data" / "scenes_travis.json"

def _load_travis():
    with SCENES_FILE_TRAVIS.open(encoding="utf-8") as f:
        raw = json.load(f)
    return {str(s["scene_id"]).strip(): s for s in raw}

try:
    TRAVIS = _load_travis()
except FileNotFoundError:
    TRAVIS = {}

def get_travis(scene_id: str) -> dict:
    key = str(scene_id).strip()
    try:
        return TRAVIS[key]
    except KeyError:
        abort(404, f"Scene {key} not found")


# ========= CHARLIE (SOUTH) =========
SCENES_FILE_CHARLIE = BASE_DIR / "static" / "data" / "scenes_charlie.json"

def _load_charlie():
    with SCENES_FILE_CHARLIE.open(encoding="utf-8") as f:
        raw = json.load(f)
    return {str(s["scene_id"]).strip(): s for s in raw}

try:
    CHARLIE = _load_charlie()
except FileNotFoundError:
    CHARLIE = {}

def get_charlie(scene_id: str) -> dict:
    key = str(scene_id).strip()
    try:
        return CHARLIE[key]
    except KeyError:
        abort(404, f"Scene {key} not found")


# ========= TREY (WEST) =========
SCENES_FILE_TREY = BASE_DIR / "static" / "data" / "scenes_trey.json"

def _load_trey():
    with SCENES_FILE_TREY.open(encoding="utf-8") as f:
        raw = json.load(f)
    return {str(s["scene_id"]).strip(): s for s in raw}

try:
    TREY = _load_trey()
except FileNotFoundError:
    TREY = {}

def get_trey(scene_id: str) -> dict:
    key = str(scene_id).strip()
    try:
        return TREY[key]
    except KeyError:
        abort(404, f"Scene {key} not found")


# --- Crossroads ---
@app.get("/")
def home():
    return render_template("home.html", title="The Crossroads", theme="crossroads")

# Keep compass routes, but drive them into each owner’s story
@app.get("/north")
def north_path():
    return redirect(url_for("chris_start"))

@app.get("/east")
def east_path():
    return redirect(url_for("travis_start"))

@app.get("/south")
def south_path():
    return redirect(url_for("charlie_start"))

@app.get("/west")
def west_path():
    return redirect(url_for("trey_start"))


# --- Chris dynamic routes ---
@app.get("/chris")
def chris_start():
    return redirect(url_for("scene_chris", scene_id="N-001"))

@app.get("/chris/<scene_id>")
def scene_chris(scene_id):
    scene = get_chris(scene_id)
    return render_template("scene.html", scene=scene, title=scene.get("title"), theme="chris")


# --- Travis dynamic routes ---
@app.get("/travis")
def travis_start():
    return redirect(url_for("scene_travis", scene_id="E-001"))

@app.get("/travis/<scene_id>")
def scene_travis(scene_id):
    scene = get_travis(scene_id)
    return render_template("scene.html", scene=scene, title=scene.get("title"), theme="travis")


# --- Charlie dynamic routes ---
@app.get("/charlie")
def charlie_start():
    return redirect(url_for("scene_charlie", scene_id="S-001"))

@app.get("/charlie/<scene_id>")
def scene_charlie(scene_id):
    scene = get_charlie(scene_id)
    return render_template("scene.html", scene=scene, title=scene.get("title"), theme="charlie")


# --- Trey dynamic routes ---
@app.get("/trey")
def trey_start():
    return redirect(url_for("scene_trey", scene_id="W-001"))

@app.get("/trey/<scene_id>")
def scene_trey(scene_id):
    scene = get_trey(scene_id)
    return render_template("scene.html", scene=scene, title=scene.get("title"), theme="trey")


# --- Shared death page (defaults to Chris theme if none given) ---
@app.get("/death")
def death():
    msg = request.args.get("msg") or "You slip at the last moment and fall to your death. That is the end of your story."
    theme = request.args.get("theme") or "chris"
    return render_template("death.html", title="You Died", msg=msg, theme=theme)

@app.template_filter('replace_all_newlines')
def replace_all_newlines(s: str):
    from markupsafe import Markup

    return Markup(s.replace('\n', '<br>'))

# --- Main entry ---
if __name__ == "__main__":
    app.run(debug=True)
