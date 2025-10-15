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
    # 1. Add the OPENING <li> tag for this animal
    animals_info_string += '<li class="cards__item">'

    # 2. Add the animal details, now ending with <br/>
    animals_info_string += f"Name: {animal['name']}<br/>"

    if 'diet' in animal['characteristics']:
        animals_info_string += f"Diet: {animal['characteristics']['diet']}<br/>"

    if 'locations' in animal and animal['locations']:
        animals_info_string += f"Location: {animal['locations'][0]}<br/>"

    if 'type' in animal['characteristics']:
        animals_info_string += f"Type: {animal['characteristics']['type']}<br/>"

    # 3. Add the CLOSING </li> tag to finish this animal's card
    animals_info_string += '</li>'

# 3. Replace the placeholder in the template with our generated string
final_html_content = template_content.replace('__REPLACE_ANIMALS_INFO__', animals_info_string)

# 4. Write the final content to a new HTML file
with open('animals.html', 'w') as file:
    file.write(final_html_content)

print("Successfully created!")