import argparse
import json
import os
import sys

import numpy as np
from PIL import Image, ImageDraw

# Ranges for amount of non-transparent pixels in a bezel
# This pigeonholes these into certain types of frames, which can
# then be removed. It works for most 4:3 (vertical) and 3:4 CRT games.
vertical_game_opaque_pixels_min = 1100000
vertical_game_opaque_pixels_max = 1250000

tv_game_opaque_pixels_min = 500000
tv_game_opaque_pixels_max = 610000

tv_game_double_wide_narrow_pixels_min = 1230000
tv_game_double_wide_narrow_pixels_max = 1240000

tv_game_double_wide_pixels_min = 670000
tv_game_double_wide_pixels_max = 700000

transparent = (0, 0, 0, 0)

known_abnormals = ("aburner2.png")

known_aspects = {"rougien.png":"3:4"}

viewports = {
    "4:3": [486, 0, 1434, 1080],
    "3:4": [224,0, 1696, 1080],
    "3:4x2":None,
    "3:8":None,
    "abnormal":None,
}


def check_aspect_ratio(img: Image):
    opaque_pixel_count = count_opaque(img)
    if vertical_game_opaque_pixels_min < opaque_pixel_count < vertical_game_opaque_pixels_max:
        return "4:3"
    if tv_game_opaque_pixels_min < opaque_pixel_count < tv_game_opaque_pixels_max:
        return "3:4"
    if tv_game_double_wide_narrow_pixels_min < opaque_pixel_count < tv_game_double_wide_narrow_pixels_max:
        return "3:4x2"
    if tv_game_double_wide_pixels_min < opaque_pixel_count < tv_game_double_wide_pixels_max:
        return "3:8"
    else:
        return "abnormal"

def count_opaque(img: Image):
    alpha_channel = img.getchannel('A')
    opaque_pixel_count = alpha_channel.histogram()[255]
    return opaque_pixel_count

def draw_transparent_rectangle(coords: list, img: Image, full_path: str):
    imgdraw = ImageDraw.Draw(img)
    img.paste(transparent, coords)
    img.save(full_path)


def remove_bezel_from_folder(folder_path: str):
    for file_name in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file_name)
        if file_name in known_aspects:
            aspect = known_aspects[file_name]
        else:
            if os.path.isfile(full_path) and full_path.endswith(".png"):
                img = Image.open(full_path).convert("RGBA")
                aspect = check_aspect_ratio(img)
        if aspect == "abnormal" and file_name not in known_abnormals:
            pixels = count_opaque(img)
            raise(Exception(f"{file_name} is abnormal: {pixels}"))
        if viewports[aspect]:
            coords = viewports[aspect]
            draw_transparent_rectangle(coords, img, full_path)

folder_paths = ["naomi", "fbneo", "mame", "atomiswave","neogeo"]
for folder_path in folder_paths:
    remove_bezel_from_folder(folder_path)