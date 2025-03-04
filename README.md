# Cooking AI Agent
Welcome to the Cooking AI Agent, a Python-based interactive cooking assistant designed to guide you through preparing delicious savory dishes and desserts! This script offers a collection of 100 recipes—50 savory dishes and 50 desserts—complete with ingredients and step-by-step instructions, narrated aloud using text-to-speech functionality.

### Overview
- The Cooking AI Agent provides a user-friendly interface to:
- Browse a list of 100 recipes, split into savory dishes (1-50) and desserts (51-100).
- Select a recipe by number.
- Display and hear the recipe’s introduction, ingredients, and cooking steps narrated via text-to-speech.
- The project uses the pyttsx3 library for text-to-speech functionality, making it an engaging tool for cooks who enjoy auditory instructions.

### Features
- 100 Recipes: 50 savory dishes (e.g., Spicy Chickpea Tacos, Thai Green Curry) and 50 desserts (e.g., Chocolate Lava Cake, Peach Cobbler).
- Text-to-Speech: Instructions are printed to the console and spoken aloud.
- Error Handling: Gracefully handles invalid inputs with friendly messages.
- Customizable: Easily extensible by adding more recipes to the recipes list.

## Prerequisites
- To run this project, you’ll need:
- Python 3.x installed on your system.
- The pyttsx3 library for text-to-speech functionality.

## Setup
- Clone or Download the Project:
- Save the cooking_assistant.py file to your desired directory (e.g., C:\Users\melis\OneDrive\Masaüstü\Cooking AI Agent).
### Install Dependencies:
- Open a terminal or command prompt.
- Install the required library using pip:
- pip install pyttsx3
- Verify Installation:
- Ensure Python and pyttsx3 are installed correctly by running:
- python -c "import pyttsx3; print('pyttsx3 is installed')"

## Usage
- Run the Script:
- Navigate to the directory containing cooking_assistant.py in your terminal:
- cd C:\Users\yourname\OneDrive\Desktop\Cooking AI Agent
- Execute the script:
- python cooking_assistant.py
- Interact with the Program:
- The script will display a welcome message and list all 100 recipes:
- Savory Dishes (1-50)
- Desserts (51-100)
- Enter a number between 1 and 100 to select a recipe.
- The script will print and narrate the recipe’s introduction, ingredients, and steps.

## Example Output:
- Welcome to your Cooking Buddy! Pick a recipe:
- Savory Dishes (1-50):
- Spicy Chickpea Tacos
- Nachos ...
- French Onion Soup
- Desserts (51-100):
- Chocolate Lava Cake
- Mango Sticky Rice ...
- Vanilla Cupcakes
- Enter the number of your recipe (1-100): 99
- Starting with Peach Cobbler...
- A warm and comforting dessert perfect for summer. Here’s what you’ll need:
- 3 cups sliced peaches
- 1 cup granulated sugar ...
- 1 cup biscuit or cobbler topping mix
- Let’s get cooking:
- Step 1: Preheat oven to 375°F (190°C). ...
- Step 7: Bake until the topping is golden brown.
- All done! Enjoy your meal!

### Error Handling:
- If you enter an invalid number (e.g., outside 1-100), it will say:
"- Oops, that’s not a valid choice! Try a number between 1 and 100."
- If you enter text instead of a number, it will say:
- "Hey, enter a number, not words! Try again."

### Project Structure
- cooking_assistant.py: The main script containing:
- A list of 100 recipes (recipes).
- A read_recipe function for displaying and narrating recipes.
- A main program loop for user interaction.
- Adding New Recipes
- To add a new recipe:
- Open cooking_assistant.py in a text editor.
- Locate the recipes list.
- Place it in the appropriate section (savory: 1-50, dessert: 51-100) and adjust numbering if needed.

## Notes
- Text-to-Speech: Ensure your system’s audio is enabled for the narration to work.
- Recipe Count: The output shows 50 savory and 50 desserts, but adjust the main program if you add more recipes beyond 100.
- Customization: Modify the speech rate (engine.setProperty('rate', 150)) or volume (engine.setProperty('volume', 0.9)) in the script to suit your preferences.

### Troubleshooting
- No Sound: Check your system’s audio settings or ensure pyttsx3 is installed correctly.
- Syntax Errors: Verify all recipe dictionaries are properly formatted with closing brackets (}, ]).
- File Not Found: Ensure you’re in the correct directory when running the script.

## License
- [MIT License]

