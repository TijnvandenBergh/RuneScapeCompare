import pytest

from app import create_app

SAMPLE_HISCORES_DATA = (
    "45000,1500,50000000\n"  # Overall
    "100000,75,1300000\n"  # Attack
    "110000,70,750000\n"  # Defence
    "90000,80,2000000\n"  # Strength
    "95000,75,1200000\n"  # Hitpoints
    "120000,65,500000\n"  # Ranged
    "200000,50,110000\n"  # Prayer
    "130000,60,300000\n"  # Magic
    "80000,70,750000\n"  # Cooking
    "85000,65,450000\n"  # Woodcutting
    "150000,55,170000\n"  # Fletching
    "90000,60,280000\n"  # Fishing
    "70000,55,170000\n"  # Firemaking
    "160000,50,110000\n"  # Crafting
    "170000,50,110000\n"  # Smithing
    "100000,60,280000\n"  # Mining
    "200000,40,40000\n"  # Herblore
    "180000,45,65000\n"  # Agility
    "190000,40,40000\n"  # Thieving
    "210000,35,25000\n"  # Slayer
    "220000,30,14000\n"  # Farming
    "230000,25,8000\n"  # Runecraft
    "240000,20,5000\n"  # Hunter
    "250000,15,2500\n"  # Construction
)


@pytest.fixture
def app():
    """Create application for testing."""
    app = create_app("testing")
    return app


@pytest.fixture
def client(app):
    """Create a test client."""
    return app.test_client()


@pytest.fixture
def sample_data():
    """Provide sample hiscores data."""
    return SAMPLE_HISCORES_DATA
