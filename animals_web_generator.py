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

# Start with an empty string before the loop
animals_info_string = ""

for animal in animals_data:
    # --- Start building the HTML for one animal ---

    # 1. Add the opening <li> tag (the "bread" of our sandwich)
    animals_info_string += '<li class="cards__item">'

    # 2. Add the title, wrapped in its own <div>
    animals_info_string += f'<div class="card__title">{animal["name"]}</div>'

    # 3. Add the opening <p> tag to group the details
    animals_info_string += '<p class="card__text">'

    # 4. Add each detail, now with a <strong> tag around the label
    if 'diet' in animal['characteristics']:
        diet = animal['characteristics']['diet']
        animals_info_string += f'<strong>Diet:</strong> {diet}<br/>'

    if 'locations' in animal and animal['locations']:
        location = animal['locations'][0]
        animals_info_string += f'<strong>Location:</strong> {location}<br/>'

    if 'type' in animal['characteristics']:
        type_ = animal['characteristics']['type']
        animals_info_string += f'<strong>Type:</strong> {type_}<br/>'

    # 5. Add the closing </p> tag
    animals_info_string += '</p>'

    # 6. Add the closing </li> tag to finish this animal's card
    animals_info_string += '</li>'

# 3. Replace the placeholder in the template with our generated string
final_html_content = template_content.replace('__REPLACE_ANIMALS_INFO__', animals_info_string)

# 4. Write the final content to a new HTML file
with open('animals.html', 'w') as file:
    file.write(final_html_content)

print("Successfully created!")