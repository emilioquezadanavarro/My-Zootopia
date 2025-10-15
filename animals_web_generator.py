import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

# Load the list of animal dictionaries
animals_data = load_data('animals_data.json')

# Loop through each animal in the list
for animal in animals_data:
    # Print the name (always exists)
    print(f"Name: {animal['name']}")

    # Check for 'diet' inside 'characteristics' before printing
    if 'diet' in animal['characteristics']:
        print(f"Diet: {animal['characteristics']['diet']}")

    # Check for 'location' inside 'animal' before printing
    # Also checks if the list is not empty.
    if 'locations' in animal:
        if animal['locations']:
            print(f"Location: {animal['locations'][0]}")

    # Check for 'type' inside 'characteristics' before printing
    if 'type' in animal['characteristics']:
        print(f"Type: {animal['characteristics']['type']}")

    # Print a blank line for separation
    print()