import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

# ---- Main Script ----

# Load the list of animal dictionaries
animals_data = load_data('animals_data.json')

# 1 - Read html template file
with open('animals_template.html', 'r') as file:
    template_content = file.read()

# 2. Generate a single string containing all animal info
animals_info_string = ""
for animal in animals_data:
    animals_info_string += f"Name: {animal['name']}\n"

    if 'diet' in animal['characteristics']:
        animals_info_string += f"Diet: {animal['characteristics']['diet']}\n"

    if 'locations' in animal and animal['locations']:
        animals_info_string += f"Location: {animal['locations'][0]}\n"

    if 'type' in animal['characteristics']:
        animals_info_string += f"Type: {animal['characteristics']['type']}\n"

    animals_info_string += "\n"  # Add a space after each animal

# 3. Replace the placeholder in the template with our generated string
final_html_content = template_content.replace('__REPLACE_ANIMALS_INFO__', animals_info_string)

# 4. Write the final content to a new HTML file
with open('animals.html', 'w') as file:
    file.write(final_html_content)

print("Successfully created animals.html!")