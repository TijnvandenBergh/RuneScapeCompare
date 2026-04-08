from app.models.player import Player


class TestPlayer:
    def test_parse_string_data(self, sample_data):
        player = Player("TestUser", sample_data)
        assert player.username == "TestUser"
        assert len(player.skills) == 24

    def test_parse_bytes_data(self, sample_data):
        player = Player("TestUser", sample_data.encode("utf-8"))
        assert player.username == "TestUser"
        assert len(player.skills) == 24

    def test_total_level(self, sample_data):
        player = Player("TestUser", sample_data)
        assert player.total_level == 1500

    def test_total_experience(self, sample_data):
        player = Player("TestUser", sample_data)
        assert player.total_experience == 50000000

    def test_skill_data_structure(self, sample_data):
        player = Player("TestUser", sample_data)
        attack = player.skills["Attack"]
        assert attack["rank"] == 100000
        assert attack["level"] == 75
        assert attack["experience"] == 1300000

    def test_combat_skills(self, sample_data):
        player = Player("TestUser", sample_data)
        combat = player.combat_skills
        expected = {
            "Attack",
            "Strength",
            "Defence",
            "Hitpoints",
            "Ranged",
            "Prayer",
            "Magic",
        }
        assert set(combat.keys()) == expected

    def test_non_combat_skills(self, sample_data):
        player = Player("TestUser", sample_data)
        non_combat = player.non_combat_skills
        assert "Attack" not in non_combat
        assert "Overall" not in non_combat
        assert "Cooking" in non_combat
        assert "Mining" in non_combat

    def test_total_level_missing_overall(self):
        player = Player("Test", "")
        assert player.total_level == 0

    def test_total_experience_missing_overall(self):
        player = Player("Test", "")
        assert player.total_experience == 0

    def test_partial_data(self):
        data = "1000,500,10000\n2000,50,5000\n"
        player = Player("Partial", data)
        assert player.total_level == 500
        assert "Overall" in player.skills
        assert "Attack" in player.skills
        assert len(player.skills) == 2

    def test_malformed_line_skipped(self):
        data = "1000,500,10000\nbaddata\n2000,50,5000\n"
        player = Player("Test", data)
        assert "Overall" in player.skills
        assert len(player.skills) == 2

    def test_all_skills_parsed(self, sample_data):
        player = Player("TestUser", sample_data)
        assert player.skills["Construction"]["level"] == 15
        assert player.skills["Hunter"]["level"] == 20
