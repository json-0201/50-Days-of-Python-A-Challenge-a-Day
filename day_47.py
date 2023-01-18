# Save a JSON
import json

def save_json(d: dict):
    """Saves JSON from input dictinoary."""

    with open("day_47.json", "w") as file:
        json.dump(d, file, indent=4)

names = {
    "name": "Carol",
    "sex": "female",
    "age": 55,
}
save_json(names)


def read_json(file: json):
    """Reads JSON file."""

    with open(file, "r") as file:
        data = json.load(file)
    print(data)

read_json("day_47.json")
