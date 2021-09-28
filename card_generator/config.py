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

CARD_FRONTS_DECK_CLOUD_URLS = [
    'http://cloud-3.steamusercontent.com/ugc/1688276347683853835/A2715D65AC6A99EF6803BF95BEF3C50CA0173FF2/',
    'http://cloud-3.steamusercontent.com/ugc/1688276347683854094/CF1D5250454EE056A00C95E61E4C85BFD24397BB/',
    'http://cloud-3.steamusercontent.com/ugc/1688276347683854431/3CCB9BCCFA4F5556D6B1E8FB327695EE619DC6F2/',
    'http://cloud-3.steamusercontent.com/ugc/1688276347683854629/7E8719802FC75261E701241F38FC4D1FE3A3F3FB/'
]
CARD_BACKS_DECK_CLOUD_URLS = [
    'http://cloud-3.steamusercontent.com/ugc/1688276347683853710/BF1D113B67D60D3C3AD0E0E2D8C38E103EEEDE4C/',
    'http://cloud-3.steamusercontent.com/ugc/1688276347683853999/D673BAB4A539CE0FB87BCDD7C63A9B5AB94CA2EA/',
    'http://cloud-3.steamusercontent.com/ugc/1688276347683854296/F9F166003C441378DB03B6892FEB0F387A8EC77C/',
    'http://cloud-3.steamusercontent.com/ugc/1688276347683854537/BC77EA0F2BC5CEDD42DAE7E3193A05B5046ED63B/'
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
REGULAR = 'regular'
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
# TYPE_COLOURS = {
#     NORMAL: {144 / 255, 153 / 255, 161 / 255},
#     FIRE: {255 / 255, 156 / 255, 84 / 255},
#     WATER: {77 / 255, 144 / 255, 213 / 255},
#     ELECTRIC: {243 / 255, 210 / 255, 59 / 255},
#     GRASS: {99 / 255, 187 / 255, 91 / 255},
#     ICE: {116 / 255, 206 / 255, 192 / 255},
#     FIGHTING: {206 / 255, 64 / 255, 105 / 255},
#     POISON: {171 / 255, 106 / 255, 200 / 255},
#     GROUND: {217 / 255, 119 / 255, 70 / 255},
#     FLYING: {143 / 255, 168 / 255, 221 / 255},
#     PSYCHIC: {249 / 255, 113 / 255, 118 / 255},
#     BUG: {144 / 255, 193 / 255, 44 / 255},
#     ROCK: {199 / 255, 183 / 255, 139 / 255},
#     GHOST: {82 / 255, 105 / 255, 172 / 255},
#     DRAGON: {10 / 255, 109 / 255, 196 / 255},
#     DARK: {90 / 255, 83 / 255, 102 / 255},
#     STEEL: {90 / 255, 142 / 255, 161 / 255},
#     FAIRY: {236 / 255, 143 / 255, 230 / 255}
# }

EFFECTIVENESS_COLOURS = {IMMUNE: (250, 150, 150), RESIST: (250, 200, 150), WEAK: (150, 200, 150)}
