from typing import Dict, Any, Optional


class ShakeConfig:
    """Simple value object for a screen shake preset."""

    def __init__(self, name: str, intensity_px: int, duration_ms: int) -> None:
        self.name = name
        self.intensity_px = int(intensity_px)
        self.duration_ms = int(duration_ms)

    def to_dict(self) -> Dict[str, int]:
        """Turn into a plain dict for Jinja / JS."""
        return {
            "name": self.name,
            "intensity_px": self.intensity_px,
            "duration_ms": self.duration_ms,
        }


# Preset levels students can use in JSON: "light", "medium", "heavy", "quake"
PRESETS: Dict[str, ShakeConfig] = {
    "light": ShakeConfig("light", 4, 150),
    "medium": ShakeConfig("medium", 8, 300),
    "heavy": ShakeConfig("heavy", 12, 450),
    "quake": ShakeConfig("quake", 16, 700),
}


def resolve(raw_value: Any) -> Optional[Dict[str, int]]:
    """
    Turn whatever is in scene['shake'] into a concrete config dict
    or None if nothing / invalid.
    Accepted values:
      - None / missing -> None
      - "light" / "medium" / "heavy" / "quake"
      - {"intensity_px": 10, "duration_ms": 500}
    """
    if not raw_value:
        return None

    # Custom dict from JSON
    if isinstance(raw_value, dict):
        try:
            intensity = int(raw_value.get("intensity_px", 8))
            duration = int(raw_value.get("duration_ms", 300))
        except (TypeError, ValueError):
            return None

        return {
            "intensity_px": intensity,
            "duration_ms": duration,
        }

    # Preset name as string
    if isinstance(raw_value, str):
        preset = PRESETS.get(raw_value.lower())
        if not preset:
            return None
        return preset.to_dict()

    # Anything else, ignore
    return None


def apply_to_scene(scene: Dict[str, Any]) -> Dict[str, Any]:
    """
    Safe helper to call from app.py.
    Reads scene['shake'] and replaces it with a concrete config dict
    that the template can use, or None.
    """
    cfg = resolve(scene.get("shake"))
    scene = dict(scene)  # copy so we do not mutate shared data
    scene["shake"] = cfg
    return scene
