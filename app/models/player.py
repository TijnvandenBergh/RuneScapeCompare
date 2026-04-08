SKILLS = [
    "Overall",
    "Attack",
    "Defence",
    "Strength",
    "Hitpoints",
    "Ranged",
    "Prayer",
    "Magic",
    "Cooking",
    "Woodcutting",
    "Fletching",
    "Fishing",
    "Firemaking",
    "Crafting",
    "Smithing",
    "Mining",
    "Herblore",
    "Agility",
    "Thieving",
    "Slayer",
    "Farming",
    "Runecraft",
    "Hunter",
    "Construction",
]


class Player:
    """Represents an OSRS player with their hiscores data."""

    def __init__(self, username, data):
        self.username = username
        self.skills = {}
        self._parse_data(data)

    def _parse_data(self, data):
        """Parse the CSV hiscores data into structured skill information.

        Each line is: rank,level,experience
        """
        if isinstance(data, bytes):
            data = data.decode("utf-8")

        lines = data.strip().split("\n")
        for i, line in enumerate(lines):
            if i >= len(SKILLS):
                break
            parts = line.split(",")
            if len(parts) >= 3:
                self.skills[SKILLS[i]] = {
                    "rank": int(parts[0]),
                    "level": int(parts[1]),
                    "experience": int(parts[2]),
                }

    @property
    def total_level(self):
        """Get the player's total level."""
        overall = self.skills.get("Overall")
        if overall:
            return overall["level"]
        return 0

    @property
    def total_experience(self):
        """Get the player's total experience."""
        overall = self.skills.get("Overall")
        if overall:
            return overall["experience"]
        return 0

    @property
    def combat_skills(self):
        """Get combat-related skills."""
        combat_names = [
            "Attack",
            "Strength",
            "Defence",
            "Hitpoints",
            "Ranged",
            "Prayer",
            "Magic",
        ]
        return {k: v for k, v in self.skills.items() if k in combat_names}

    @property
    def non_combat_skills(self):
        """Get non-combat skills."""
        combat_names = [
            "Overall",
            "Attack",
            "Strength",
            "Defence",
            "Hitpoints",
            "Ranged",
            "Prayer",
            "Magic",
        ]
        return {k: v for k, v in self.skills.items() if k not in combat_names}
