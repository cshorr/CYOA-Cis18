## Observer Pattern with Blinker (Python / Flask style)

**Concept:** One subject (game state) notifies many observers (UI, logs, etc.) when it changes. This is the classic "one-to-many" relationship.

```python
from blinker import Namespace
## Blinker is already included in flask , travis if your wondering 

# Subject (signal namespace)
game_signals = Namespace()
weapon_changed = game_signals.signal("weapon_changed")

# Observers (things that react)
def update_combat_label(sender, weapon, **extra):
    print(f"[UI] Combat button now says: Draw your {weapon}")

def log_weapon_choice(sender, weapon, **extra):
    print(f"[LOG] Player chose {weapon}")

# Subscribe observers to the signal
weapon_changed.connect(update_combat_label)
weapon_changed.connect(log_weapon_choice)

# Fire the event (subject notifies observers)
def choose_weapon(weapon):
    weapon_changed.send("game_state", weapon=weapon)

# Example usage
choose_weapon("sword")
# → [UI] Combat button now says: Draw your sword
# → [LOG] Player chose sword
