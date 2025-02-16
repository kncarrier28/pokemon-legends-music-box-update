from io import BytesIO

import pandas as pd
import requests
from PIL import Image, ImageDraw
from tqdm import tqdm

from config import *
from utils import xy, read_cube, get_img


# Utils

def get_types(stats):
    return [type_ for type_ in (stats.type_1, stats.type_2) if not pd.isnull(type_)]


def get_moves(stats):
    return [move for move in (stats.move_1, stats.move_2, stats.move_3, stats.move_4) if not pd.isnull(move)]


# Functions

def compose_base(stats):
    card_base = 'standard' if stats.encounter_tier not in ('grunt', 'commander', 'boss', 'ultra_burst') else 'team_galactic'
    base_img = Image.open(ASSETS_DIR / 'card_bases' / f'{card_base}.png').convert('RGBA').resize(xy(16, 28))

    try:
        climate_img = Image.open(ASSETS_DIR / 'climates' / f'{stats.climate.lower()}.png')
    except (FileNotFoundError, AttributeError):
        climate_img = Image.open(ASSETS_DIR / 'climates' / f'unknown.png')

    climate_img = climate_img.convert('RGBA').resize(xy(15.5, 27.5))
    base_img.paste(climate_img, xy(0.25, 0.25), climate_img)

    try:
        biome_img = Image.open(ASSETS_DIR / 'biomes' / f'{stats.biome.lower()}.png')
        biome_img = biome_img.convert('RGBA').resize(xy(15.5, 27.5))
        base_img.alpha_composite(biome_img, xy(0.25, 0.25))
    except (FileNotFoundError, AttributeError):
        pass

    return base_img


def add_frame(img):
    frame_img = Image.open(ASSETS_DIR / 'frame_base.png').convert('RGBA').resize(xy(15.5, 19.25))
    img.paste(frame_img, xy(0.25, 0.25), frame_img)


def add_creator_emblem(img):
    creator_emblem_img = Image.open(ASSETS_DIR / 'creator_emblem.png').convert('RGBA').resize(xy(1, 1))
    img.paste(creator_emblem_img, xy(14.75, 15.75), creator_emblem_img)


def add_types_and_moves(img, stats):
    types = get_types(stats)
    for i, type_ in enumerate(types):
        type_img = get_img(ASSETS_DIR / 'types' / f'{type_}.png', xy(2.5, 2.5))
        img.paste(type_img, xy(0.5 + i * 2.5, 0.5), type_img)

    if pd.isnull(stats.trainer):
        moves = get_moves(stats)
        for i, move in enumerate(moves):
            size = 1.25
            move_img = get_img(ASSETS_DIR / 'types' / f'{move}.png', xy(size, size))
            img.paste(move_img, xy(3.25 - (len(moves) / 2 * size) + (i % 2 * size), 16.75 + i // 2 * size), move_img)


def get_variant(stats):
    variant = ''
    if stats.pokedex_number in (422, 423) and stats.description == 'East Ocean Form':
        variant = '-e'
    elif stats.pokedex_number == 412:
        variant = '-p'
    elif stats.pokedex_number == 421:
        variant = '-s'
    return variant


def get_size(stats):
    min_size = 7
    max_size = 11
    if not pd.isnull(stats.trainer):
        max_size = 10
    return max(min(stats.total // 2 + 3, max_size), min_size)


def converted_pokedex_number(stats):
    if isinstance(stats.pokedex_number, int):
        return f'{stats.pokedex_number:03}'
    else:
        return stats.pokedex_number


def get_pokemon_art(stats):
    variant = get_variant(stats)
    pokemon_art_size = get_size(stats)
    try:
        pokemon_art_img = get_img(ASSETS_DIR / 'pokemon' / f'{converted_pokedex_number(stats)}{variant}.png',
                                  xy(pokemon_art_size, pokemon_art_size))
    except (FileNotFoundError, AttributeError):
        response = requests.get(f'{ART_FORM_URL}/{converted_pokedex_number(stats)}{variant}.png')
        pokemon_art_img = get_img(BytesIO(response.content), xy(pokemon_art_size, pokemon_art_size))
        pokemon_art_img.save(ASSETS_DIR / 'pokemon' / f'{converted_pokedex_number(stats)}{variant}.png')
    return pokemon_art_img


def add_pokemon_art(img, stats):
    pokemon_art_img = get_pokemon_art(stats)
    img.paste(pokemon_art_img, xy((16 - pokemon_art_img.width / 64) / 2, (20 - pokemon_art_img.height / 64) / 2),
              pokemon_art_img)


def add_bases(img, stats):
    if pd.isnull(stats.trainer):
        if not stats.uncapturable:
            held_item_base_img = Image.open(ASSETS_DIR / 'held_item_base.png').convert('RGBA').resize(xy(3.5, 3.5))
            img.paste(held_item_base_img, xy(1.75, 12.75), held_item_base_img)
        else:
            uncapturable_base_img = Image.open(ASSETS_DIR / 'uncapturable_base.png').convert('RGBA').resize(xy(3.5, 3.5))
            img.paste(uncapturable_base_img, xy(1.75, 12.75), uncapturable_base_img)

        if stats.encounter_tier in ('ultra_beast', 'ultra_burst'):
            prism_armour_base_img = get_img(ASSETS_DIR / 'prism_armour_base.png', xy(3.5, 4))
            img.paste(prism_armour_base_img, xy(10.75, 12.5), prism_armour_base_img)
        else:
            map_base_img = get_img(ASSETS_DIR / 'map_base.png', xy(3.5, 3.5))
            img.paste(map_base_img, xy(10.75, 12.75), map_base_img)

    health_base_img = Image.open(ASSETS_DIR / 'health_base.png').convert('RGBA').resize(xy(3.5, 2))
    img.paste(health_base_img, xy(11.75, 7.75), health_base_img)
    initiative_base_img = Image.open(ASSETS_DIR / 'initiative_base.png').convert('RGBA').resize(xy(3.5, 2))
    img.paste(initiative_base_img, xy(11.75, 10.25), initiative_base_img)


def add_trainer(img, stats):
    if pd.isnull(stats.trainer):
        return

    trainer_img = get_img(ASSETS_DIR / 'trainers' / f'{stats.trainer}.png', xy(5, 9.5))
    img.paste(trainer_img, xy(0, 6.75), trainer_img)

    rank_img = get_img(ASSETS_DIR / 'trainer_icons' / f'rank_{stats.encounter_tier}.png', xy(2.5, 2.5))
    img.paste(rank_img, xy(0.75, 16.75), rank_img)

    party_order_img = get_img(ASSETS_DIR / 'trainer_icons' / f'trainer.png', xy(2, 2))
    img.paste(party_order_img, xy(13, 17), party_order_img)


def add_encounter_icon(img, stats):
    if stats.encounter_tier in ('grunt', 'commander', 'boss'):
        icon_img = get_img(ASSETS_DIR / 'encounter_icons' / 'galactic.png', xy(2, 2))
    elif 'elder' in stats.encounter_tier:
        icon_img = get_img(ASSETS_DIR / 'encounter_icons' / 'noble.png', xy(2, 2))
    else:
        icon_img = get_img(ASSETS_DIR / 'encounter_icons' / f'{stats.encounter_tier}.png', xy(2, 2))
    img.paste(icon_img, xy(7, 17), icon_img)


def add_location(img, stats):
    if not pd.isnull(stats.trainer):
        return

    if stats.encounter_tier == 'legendary':
        location_icon_img = get_img(ASSETS_DIR / 'map_icons' / f'unknown.png', xy(3, 3))
    elif stats.encounter_tier == 'noble':
        village_name = stats.description.split(' ')[1].lower()
        location_icon_img = get_img(ASSETS_DIR / 'map_icons' / f'noble_{village_name}.png', xy(3, 3))
    elif stats.encounter_tier in ('ultra_beast', 'ultra_burst'):
        location_icon_img = None
    else:
        try:
            location_icon_img = get_img(ASSETS_DIR / 'map_icons' / f'{stats.climate.lower()}_{stats.biome.lower()}.png',
                                        xy(3, 3))
        except (FileNotFoundError, AttributeError):
            location_icon_img = get_img(ASSETS_DIR / 'map_icons' / f'unknown.png', xy(3, 3))

    if location_icon_img:
        img.paste(location_icon_img, xy(11, 13), location_icon_img)


def add_evolution_cost(img, stats):
    if not pd.isnull(stats.trainer):
        return

    if not pd.isnull(stats.evolve_into):
        d = ImageDraw.Draw(img)
        evolution_icon_img = get_img(ASSETS_DIR / 'evolution_icon.png', xy(2.5, 2.5))
        img.paste(evolution_icon_img, xy(12.75, 16.75), evolution_icon_img)
        d.text(xy(14, 18), str(int(stats.evolve_cost)), fill=WHITE_COLOUR, font=ORIENTAL_96, anchor='mm')
    else:
        evolution_icon_img = get_img(ASSETS_DIR / 'evolution_final_icon.png', xy(2.5, 2.5))
        img.paste(evolution_icon_img, xy(12.75, 16.75), evolution_icon_img)


def get_stats_font_size(stats_value):
    if stats_value < 10:
        return ORIENTAL_96
    if stats_value < 20:
        return ORIENTAL_80
    return ORIENTAL_64


def add_text(img, stats):
    d = ImageDraw.Draw(img)
    types = get_types(stats)

    # Pokémon Name
    d.text(xy(1 + len(types) * 2.5, 1.75 - (0.5 if not pd.isnull(stats.description) else 0)), stats.pokedex_name,
           fill=DARK_COLOUR, font=BARLOW_96 if pd.isnull(stats.description) else BARLOW_80, anchor='lm')

    # Pokémon Description
    if not pd.isnull(stats.description):
        d.text(xy(1 + len(types) * 2.5, 2.5), stats.description, fill=DARK_COLOUR, font=BARLOW_48, anchor='lm')

    # Pokémon Stats
    d.text(xy(12.75, 8.75), str(stats.health), fill=DARK_COLOUR, font=get_stats_font_size(stats.health), anchor='mm')
    d.text(xy(12.75, 11.25), str(stats.initiative), fill=DARK_COLOUR, font=get_stats_font_size(stats.initiative),
           anchor='mm')


def add_move(img, stats):
    move_img = get_img(MOVES_OUTPUT_DIR / f'{stats.move_name}.png', xy(14.5, 7.5))
    img.paste(move_img, xy(0.75, 19.75), move_img)


def run(overwrite=False):
    print('Generating card fronts:')
    CARD_FRONTS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = read_cube()
    for i, stats in tqdm(df.iterrows(), total=df.shape[0]):
        output_path = CARD_FRONTS_OUTPUT_DIR / f'{i}_{stats.pokedex_name.lower()}.png'
        if output_path.is_file() and not overwrite:
            continue

        base_img = compose_base(stats)
        img = Image.new('RGBA', xy(16, 28))
        add_frame(img)
        add_creator_emblem(img)
        add_pokemon_art(img, stats)
        add_trainer(img, stats)
        add_bases(img, stats)
        add_types_and_moves(img, stats)
        add_location(img, stats)
        add_text(img, stats)
        add_move(img, stats)
        add_encounter_icon(img, stats)
        add_evolution_cost(img, stats)

        base_img.paste(img, xy(0, 0), img)
        base_img.save(output_path)


if __name__ == '__main__':
    run(overwrite=True)
