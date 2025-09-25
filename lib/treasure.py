from typing import Dict, Optional
from flask import session, request

# ====================== CHRIS (NORTH) ======================
CHRIS_TREASURE: Dict[str, str] = {
}

# ====================== TRAVIS (EAST) ======================
TRAVIS_TREASURE: Dict[str, str] = {
    "E-018": "rat_infestation_ribbon",
}

# ====================== CHARLIE (SOUTH) ====================
CHARLIE_TREASURE: Dict[str, str] = {
}

# ====================== TREY (WEST) ========================
TREY_TREASURE: Dict[str, str] = {
}


def all_treasure():
    merged: Dict[str, str] = {}
    for d in (CHRIS_TREASURE, TRAVIS_TREASURE, CHARLIE_TREASURE, TREY_TREASURE):
        merged.update(d)
    return merged


def get_item_for(scene_id: str):
    scene_id = str(scene_id).strip()
    return all_treasure().get(scene_id)


def _ensure_player_vars():
    p = session.get('player', {})
    vars_obj = p.get('vars')
    return vars_obj


def current_scene_id():
    endpoint = request.endpoint
    if not endpoint or not endpoint.startswith('scene_'):
        return None
    view_args = request.view_args or {}
    scene_id = str(view_args.get('scene_id') or '').strip()
    return scene_id or None

def grant_treasure_for_current(*, value: object = True):
    scene_id = current_scene_id()
    item_key = get_item_for(scene_id)
    if not item_key:
        return None
    vars_obj = _ensure_player_vars()
    if vars_obj.get(item_key) == value:
        return item_key
    vars_obj[item_key] = value
    p = session.get('player', {})
    p['vars'] = vars_obj
    session['player'] = p
    return item_key
