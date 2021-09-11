from pathlib import Path
from PIL import ImageFont

COMPONENT_DIR = Path(__file__).parent
ROOT_DIR = COMPONENT_DIR.parent
ASSETS_DIR = COMPONENT_DIR.parent / 'assets'
OUTPUT_DIR = COMPONENT_DIR / 'output'
MOVES_OUTPUT_DIR = OUTPUT_DIR / 'moves'
CARD_FRONTS_OUTPUT_DIR = OUTPUT_DIR / 'card_fronts'
CARD_BACKS_OUTPUT_DIR = OUTPUT_DIR / 'card_backs'
DECKS_OUTPUT_DIR = OUTPUT_DIR / 'decks'
CARD_OBJECT_TEMPLATE = ASSETS_DIR / 'card_object_template.json'
DECK_OBJECT_TEMPLATE = ASSETS_DIR / 'deck_object_template.json'

ART_FORM_URL = 'https://www.serebii.net/pokemon/art'

ORIENTAL_64 = ImageFont.truetype(str(ASSETS_DIR / 'la_oriental.otf'), size=64)
ORIENTAL_80 = ImageFont.truetype(str(ASSETS_DIR / 'la_oriental.otf'), size=80)
ORIENTAL_96 = ImageFont.truetype(str(ASSETS_DIR / 'la_oriental.otf'), size=96)
ORIENTAL_160 = ImageFont.truetype(str(ASSETS_DIR / 'la_oriental.otf'), size=160)
BARLOW_96 = ImageFont.truetype(str(ASSETS_DIR / 'barlow.ttf'), size=96)
BARLOW_80 = ImageFont.truetype(str(ASSETS_DIR / 'barlow.ttf'), size=80)
BARLOW_64 = ImageFont.truetype(str(ASSETS_DIR / 'barlow.ttf'), size=64)
BARLOW_56 = ImageFont.truetype(str(ASSETS_DIR / 'barlow.ttf'), size=56)
BARLOW_48 = ImageFont.truetype(str(ASSETS_DIR / 'barlow.ttf'), size=48)

DARK_COLOUR = (37, 37, 50)
WHITE_COLOUR = (255, 255, 255)
PURPLE_COLOUR = (250, 0, 200)

STANDARD_CARD_BACK_CLOUD_URL = 'http://cloud-3.steamusercontent.com/ugc/1717542408497689638/14AF78B5203C3A9A3851A45D7BA0DACA3B19473D/'
PERFECT_WORLD_ORDER_CARD_BACK_CLOUD_URL = 'http://cloud-3.steamusercontent.com/ugc/1695025250441629233/2C1456E366D0C8B7C49CF659542814A3AD55D92B/'
DECK_FACE_CLOUD_URLS = [
    'http://cloud-3.steamusercontent.com/ugc/1691651067504980915/45E267964DE7D8DB00B34B4B53234E92D91DA03E/',
    'http://cloud-3.steamusercontent.com/ugc/1691651067504981092/7C1A9F9CB7152F7BFD9E3FAB557D69C04D3B8132/',
    'http://cloud-3.steamusercontent.com/ugc/1691651067504981277/2DB8637439EEF7B40A9D10B0DA966711B77A0057/',
    'http://cloud-3.steamusercontent.com/ugc/1691651067504981435/8D4F885DF3D4B4402CF3C9EF02AFAAD64F34A174/'
]

# Type Chart

NORMAL = 'normal'
FIRE = 'fire'
WATER = 'water'
ELECTRIC = 'electric'
GRASS = 'grass'
ICE = 'ice'
FIGHTING = 'fighting'
POISON = 'poison'
GROUND = 'ground'
FLYING = 'flying'
PSYCHIC = 'psychic'
BUG = 'bug'
ROCK = 'rock'
GHOST = 'ghost'
DRAGON = 'dragon'
DARK = 'dark'
STEEL = 'steel'
FAIRY = 'fairy'

IMMUNE = 'immune'
RESIST = 'resist'
WEAK = 'weak'

TYPE_CHART = {
    NORMAL: {IMMUNE: [GHOST], RESIST: [ROCK, STEEL], WEAK: []},
    FIRE: {IMMUNE: [], RESIST: [FIRE, WATER, ROCK, DRAGON], WEAK: [GRASS, ICE, BUG, STEEL]},
    WATER: {IMMUNE: [], RESIST: [WATER, GRASS, DRAGON], WEAK: [FIRE, GROUND, ROCK]},
    ELECTRIC: {IMMUNE: [GROUND], RESIST: [ELECTRIC, GRASS, DRAGON], WEAK: [WATER, FLYING]},
    GRASS: {IMMUNE: [], RESIST: [FIRE, GRASS, POISON, FLYING, BUG, DRAGON, STEEL], WEAK: [WATER, GROUND, ROCK]},
    ICE: {IMMUNE: [], RESIST: [FIRE, WATER, ICE, STEEL], WEAK: [GRASS, GROUND, FLYING, DRAGON]},
    FIGHTING: {IMMUNE: [GHOST], RESIST: [POISON, FLYING, PSYCHIC, BUG, FAIRY], WEAK: [NORMAL, ICE, ROCK, DARK, STEEL]},
    POISON: {IMMUNE: [STEEL], RESIST: [POISON, GROUND, ROCK, GHOST], WEAK: [GRASS, FAIRY]},
    GROUND: {IMMUNE: [FLYING], RESIST: [GRASS, BUG], WEAK: [FIRE, ELECTRIC, POISON, ROCK, STEEL]},
    FLYING: {IMMUNE: [], RESIST: [ELECTRIC, ROCK, STEEL], WEAK: [GRASS, FIGHTING, BUG]},
    PSYCHIC: {IMMUNE: [DARK], RESIST: [PSYCHIC, STEEL], WEAK: [FIGHTING, POISON]},
    BUG: {IMMUNE: [], RESIST: [FIRE, FIGHTING, POISON, FLYING, GHOST, STEEL, FAIRY], WEAK: [GRASS, PSYCHIC, DARK]},
    ROCK: {IMMUNE: [], RESIST: [FIGHTING, GROUND, STEEL], WEAK: [FIRE, ICE, FLYING, BUG]},
    GHOST: {IMMUNE: [NORMAL], RESIST: [DARK], WEAK: [PSYCHIC, GHOST]},
    DRAGON: {IMMUNE: [FAIRY], RESIST: [STEEL], WEAK: [DRAGON]},
    DARK: {IMMUNE: [], RESIST: [FIGHTING, DARK, FAIRY], WEAK: [PSYCHIC, GHOST]},
    STEEL: {IMMUNE: [], RESIST: [FIRE, WATER, GRASS, STEEL], WEAK: [ICE, ROCK, FAIRY]},
    FAIRY: {IMMUNE: [], RESIST: [FIRE, POISON, STEEL], WEAK: [FIGHTING, DRAGON, DARK]}
}

EFFECTIVENESS_COLOURS = {IMMUNE: (250, 150, 150), RESIST: (250, 200, 150), WEAK: (150, 200, 150)}
