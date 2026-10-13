from typing import Any
from collections import Counter
import color_data


def collect_colors(data: dict) -> list:
    colours = []
    for colour_list in data.values():
        colours.extend(colour_list)
    return colours


def count_colors(colours: list) -> Any:
    return Counter(colours)


colours = collect_colors(color_data.dress_data)

frequencies = count_colors(colours)






# print(frequencies)
# print("Total entries:", len(colours))
# print("Mean Frequency:", mean_frequency)
# print("\nColour frequencies:")

# for colour, frequency in sorted(frequencies.items()):
#     print(f"{colour}: {frequency}")
