import random
from collections import Counter
from color_collection import collect_colors, count_colors
from color_data import dress_data
from database_repository import save_to_db


def mean_color(colours: list) -> list:
    frequencies = count_colors(colours)

    mean_frequency = len(colours) / len(frequencies)
    mean_frequency = round(mean_frequency)

    mean_colors = []

    for colour, frequency in frequencies.items():
        if frequency == mean_frequency:
            mean_colors.append(colour)

    return mean_colors


def most_worn_color(frequencies: Counter) -> tuple:
    most_worn = frequencies.most_common(1)
    return most_worn[0]


def median_color(colours: list) -> str:
    sorted_colours = sorted(colours)
    colour_ind = len(sorted_colours) // 2
    return sorted_colours[colour_ind]


def variance_of_colours(frequencies: Counter):
    values = list(frequencies.values())

    mean_frequency = sum(values) / len(values)

    return (
        sum((frequency - mean_frequency) ** 2 for frequency in values)
        / len(values)
    )


def possibility_of_choosing_red(colours: list):
    frequencies = count_colors(colours)
    red_count = frequencies.get("RED", 0)

    total_count = len(colours)

    return f"The percentage possibility of selecting colour red is {red_count / total_count * 100}%"


def recursive_search(numbers, target, index=0):
    if index >= len(numbers):
        return -1
    if numbers[index] == target:
        return index
    return recursive_search(numbers, target, index + 1)


def generate_binary_number():
    binary_number = "".join(
        random.choice("01") for _ in range(4)
    )
    decimal_number = int(binary_number, 2)

    print("Binary number:", binary_number)
    print("Decimal number:", decimal_number)

    return binary_number, decimal_number


def sum_first_50_fibonacci():
    first = 0
    second = 1
    total = 0
    for _ in range(50):
        total += first
        first, second = second, first + second

    return total


print("Sum of the first 50 Fibonacci numbers:",
      sum_first_50_fibonacci())

colours = collect_colors(dress_data)

frequencies = count_colors(colours)

mean_colour_of_shirt = mean_color(colours)
most_colour = most_worn_color(frequencies)
median_colour = median_color(colours)
variance = variance_of_colours(frequencies)
red = possibility_of_choosing_red(colours)

print(f"The mean colour of shirt is {mean_colour_of_shirt}")
print(f"The most colour of shirt worn is {most_colour}")
print(f"The median colour is {median_colour}")
print(f"The variance of colour is {variance}")
print(red)
save_to_db(frequencies)


numbers = [10, 25, 30, 45, 50]
target = int(input("Enter a number to search for: "))
result = recursive_search(numbers, target)
if result == -1:
    print("Number not found.")
else:
    print("Number found at index:", result)
generate_binary_number()

print("Sum of the first 50 Fibonacci numbers:",
      sum_first_50_fibonacci())
