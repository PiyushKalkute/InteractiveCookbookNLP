# InteractiveCookbookNLP

Our project is a recipe parser configured to recognize various ingredients, tools and
cooking methods used in a given recipe. To achieve that, we developed a framework to
ensure seamless transformations on the recipe along multiple utilitarian dimensions like
to and from vegan, scaling the amount to half or double, changing to a favorite style of
cuisine, making it healthier, etc. by using our system’s internal representation for
ingredients, cooking methods, and tools.

### Interface

The project comprised of 3 python files, each providing an API for a specific purpose:
*   **_reci_scraper.py_** - scrapes the website to retrieve contents of the recipe
*   **_reci_parser.py_** - parses the scraped content to get structured info.
*   **_recipe_interface.py_** ​- main file that provides a readable UI for easy access

Along with that, we have 2 additional files to allow the seamless transformations, so that
you can have your desired recipe before you could say​ _‘Bon Appetit.’_
*   **_collectionDB.json_** - ​ useful mappings for transformation and extraction.
*   **_README.md_** - ​  this ‘readme’ file contains all the information you need

### Executing files:

- On opening the directory, create a virtual environment:
    >>​ **_py -m venv env_** ​ **(On windows)**
    **>>** ​ **_python3 -m venv env_** ​ **(On macOS and Linux)**
- Then activate the environment:
    >>​ **_.\env\Scripts\activate_** ​ **(On windows)**
    **>>source env/bin/activate (On macOS and Linux)**
- Run ​ **_pip install -r requirements.txt_** ​ ​to get all the necessary packages imported
    onto your system (environment).
- To run the Cookbook API, clone the repo to your local directory, navigate to the
    /code directory in the terminal and run the following command:
       _>>_ ​ **_python3 recipe_interface.py_**


## “What’s on the Menu?” (or ​ recipe, ​ we should say)

The very first step in cooking is getting the ingredients. Although for us, it involved
parsing the text scraped using the RecipeFetcher API (reci_scraper.py), which we
obtained from any valid input URL from ​https://www.allrecipes.com/​.
This helped us segregate the information present on the website into categories and
subcategories such as:
#### ● Ingredients

○ _Ingredient Name:_ ​ main parts of the recipe; changes with the transformation

○ _Quantity:_ ​ numbers and fractions, converted to decimals for easier conversion

○ _Measurement:_ ​ ​keeping track of measurements was pivotal to scale amount
 * Part of grocery - whole, quarter, half, full
 * Measuring Unit - ounces, pound, lts, gm, gal
 * Utensil measure- teaspoons(tsp), cups, tablespoon (TBsp)

○ _Preparation:_ sliced, chopped, dried, shredded, etc

#### ● Tools
Essential utensils in the cooking process like pan, bowl, oven, pot, skillet, dish.

#### ● Cooking Methods

○ Primary- Major cooking methods common across a variety of cuisines
which determine the overall health value, nutrition and taste.
    Eg: Bake, boil, steam, fry (deep/shallow), etc.

○ *Secondary-* Cooking practices which don't overall determine the composition
of a cuisine, but is essential to make the dish the way it is.
    Eg: Preheat, sprinkle, mix, melt, heat, drain, grease, etc.

#### ● Recipe Directions
○ Step-by-step detailed description of the cooking process, including the
preparation, primary and secondary procedures as seen on the website.

## Transform and Make!

Once you know what the recipe involves, what its main ingredients are, and what tools
you should have handy, you can play around with the numerous transformation that we
provided to convert the recipe into the favorite that kindles your appetite, as well as go
well with any and all dietary restrictions/preferences you may have. These include
transforming your recipe to:


#### For the health-conscious (and the heavy gainers):

1. Healthy
2. Non-Healthy

#### For scaling down to a meal (or scaling up to a feast):

3. Half
4. Double

#### For those who can’t eat meat (and those that can’t live without it):

5. Vegetarian
6. Non-Vegetarian

#### For the love of Indian food (who doesn’t?):

7. Indian


## Highlights

#### Cascading Transforms
  -> Each transformation is incremental on the previous one, i.e. retaining all
the changes from any prior change that you made (including ingredients)
  -> Convert from ​ any Recipe --> Vegetarian --> Healthy --> Double ​, and all
the possible combinations that you want to try.

#### Detailed Step-by-step description
  -> Numbered steps for convenience and future conversational interfaces.
  -> Once transformed, ingredients and steps are printed in a concise manner.

#### Transformation Log
  -> Helps keep track of transformation from one recipe to another.

#### Easy-on-the-eye
  -> Detailed description, changelog and a clean interface provides a
convenient cooking experience.
