import pyttsx3

# Set up the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

# List of 100 recipes (50 savory, 50 desserts)
recipes = [
    # Savory Dishes (50)
    {"name": "Spicy Chickpea Tacos", "intro": "Hey taco fan! Time for Spicy Chickpea Tacos!",
     "ingredients": ["1 can (15 oz) chickpeas (drained and rinsed)", "2 tbsp olive oil", "1 tsp chili powder", "1 tsp ground cumin", "1/2 tsp smoked paprika", "1/4 tsp garlic powder", "1/4 tsp onion powder", "Salt and pepper to taste", "4 soft tortillas (corn or flour)", "1 cup shredded lettuce", "1 medium tomato (diced)", "1 avocado (sliced)", "1/4 cup salsa", "Optional: 1/2 cup shredded cheddar or vegan cheese", "2 tbsp fresh cilantro (chopped)", "1 lime (cut into wedges)"],
     "steps": [
         "Preheat your oven to 200°C if you want warm tortillas—let’s get ready!",
         "Heat the olive oil in a large skillet over medium heat until it’s nice and hot.",
         "Add the drained chickpeas and stir to coat them in the oil—give ‘em a good toss!",
         "Sprinkle in the chili powder, cumin, paprika, garlic powder, onion powder, salt, and pepper—mix it well!",
         "Cook the chickpeas for 7-10 minutes, stirring occasionally, until they’re crispy on the outside.",
         "While they cook, wrap the tortillas in foil and pop them in the oven for 5 minutes to warm up.",
         "Take the tortillas out, lay them flat on a plate, and spoon the spicy chickpeas evenly onto each one.",
         "Top with shredded lettuce, diced tomato, avocado slices, and a dollop of salsa—load it up!",
         "If you’re using cheese, sprinkle it over the top now—melty goodness!",
         "Garnish with fresh cilantro, squeeze a lime wedge over each taco, fold ‘em up, and enjoy—taco time!"
     ]},
    {"name": "Nachos", "intro": "Let's make some mouthwatering Nachos!",
     "ingredients": ["1 bag tortilla chips", "1 can (15 oz) black beans, rinsed and drained", "1 cup shredded cheddar cheese", "1/2 cup salsa", "1/4 cup sour cream", "1 avocado, diced", "1 jalapeño, sliced (optional)", "Cilantro, chopped (for garnish)"],
     "steps": [
         "Preheat oven to 350°F (175°C).",
         "Spread tortilla chips on a baking sheet.",
         "Sprinkle black beans and cheddar cheese over the chips.",
         "Bake for 5-7 minutes, or until cheese is melted and bubbly.",
         "Top with salsa, sour cream, avocado, and jalapeño slices (if using).",
         "Garnish with cilantro and serve immediately!"
     ]},
    {"name": "Japanese Veggie Curry", "intro": "Anime chef alert! Let’s make Japanese Veggie Curry!",
     "ingredients": ["2 tbsp vegetable oil", "1 large onion (chopped)", "2 medium carrots (peeled and sliced)", "2 medium potatoes (peeled and cubed)", "1 tbsp Japanese curry powder", "1 tsp soy sauce", "1/2 tsp garlic paste", "1/2 tsp ginger paste", "3 cups vegetable broth", "1 cup frozen peas", "1 cup green beans (trimmed)", "Optional: 200g firm tofu (cubed)", "2 cups cooked rice (white or brown)", "1 tbsp chopped green onions", "Salt and pepper to taste"],
     "steps": [
         "Heat the vegetable oil in a large pot over medium heat—get it shimmering!",
         "Add the chopped onion and sauté for 4-5 minutes until soft and golden—stir often!",
         "Stir in the garlic and ginger pastes, cooking for 30 seconds until fragrant—smells amazing!",
         "Toss in the carrots, potatoes, and green beans, stirring to coat them in the onion mix.",
         "Sprinkle the curry powder over everything and stir for 1 minute to toast the spices—wake ‘em up!",
         "Pour in the vegetable broth and soy sauce, stirring to combine—bring it to a gentle boil.",
         "Lower the heat, cover the pot, and simmer for 20-25 minutes until the veggies are tender—test with a fork!",
         "Add the frozen peas and tofu (if using), cooking for another 5 minutes to heat through.",
         "Season with salt and pepper to taste—give it a final stir and check the flavor!",
         "Serve over warm rice, sprinkle with green onions, and dig in—curry night, Japanese style!"
     ]},
    {"name": "Pasta Primavera", "intro": "Pasta party! Let’s whip up Pasta Primavera!",
     "ingredients": ["200g spaghetti or penne", "2 tbsp olive oil", "1 small zucchini (sliced)", "1 yellow bell pepper (chopped)", "1 cup broccoli florets", "1 cup asparagus (trimmed and chopped)", "2 garlic cloves (minced)", "1 cup cherry tomatoes (halved)", "1 tsp dried basil", "1/2 tsp dried oregano", "1/4 tsp red pepper flakes", "Salt and pepper to taste", "1/4 cup vegetable broth", "Optional: 1/4 cup grated parmesan or nutritional yeast", "2 tbsp fresh parsley (chopped)", "1 lemon (zested)"],
     "steps": [
         "Fill a large pot with water, add a generous pinch of salt, and bring it to a rolling boil.",
         "Add the pasta and cook according to the package until al dente—about 8-10 minutes—then drain.",
         "While the pasta cooks, heat olive oil in a large skillet over medium heat—let it get nice and hot!",
         "Add the minced garlic and sauté for 30 seconds until fragrant—don’t let it burn!",
         "Toss in the zucchini, bell pepper, broccoli, and asparagus—stir-fry for 5-7 minutes until crisp-tender.",
         "Add the cherry tomatoes, basil, oregano, red pepper flakes, salt, and pepper—mix it all up!",
         "Pour in the veggie broth and simmer for 2-3 minutes—let the flavors meld together!",
         "Add the drained pasta to the skillet, tossing everything to coat the noodles in the veggie goodness.",
         "Sprinkle with parmesan or nutritional yeast, fresh parsley, and lemon zest—give it a final toss!",
         "Serve hot in big bowls—pasta perfection achieved!"
     ]},
    {"name": "Moroccan Lentil Stew", "intro": "Spice it up! Moroccan Lentil Stew time!",
     "ingredients": ["1 cup dried red lentils (rinsed)", "2 tbsp olive oil", "1 large onion (chopped)", "2 garlic cloves (minced)", "1 tsp ground cumin", "1 tsp ground cinnamon", "1/2 tsp ground turmeric", "1/2 tsp smoked paprika", "1/2 tsp ground ginger", "1 can (14 oz) diced tomatoes", "3 cups vegetable broth", "1 carrot (sliced)", "1 zucchini (chopped)", "1/4 cup raisins", "1/4 cup chopped dried apricots", "Salt and pepper to taste", "2 tbsp fresh cilantro (chopped)"],
     "steps": [
         "Heat the olive oil in a large pot over medium heat—let it warm up nicely!",
         "Add the chopped onion and sauté for 4-5 minutes until soft and golden—keep stirring!",
         "Toss in the minced garlic and cook for 30 seconds—smell that goodness!",
         "Sprinkle in the cumin, cinnamon, turmeric, paprika, and ginger—stir for 1 minute to toast the spices.",
         "Add the rinsed lentils, diced tomatoes, and vegetable broth—give it a big stir to mix everything.",
         "Toss in the carrot, zucchini, raisins, and apricots—bring it to a gentle simmer.",
         "Cover and cook for 25-30 minutes, stirring occasionally, until the lentils are soft and creamy.",
         "Season with salt and pepper to taste—adjust it to your liking!",
         "Let it sit off the heat for 5 minutes to meld the flavors—then sprinkle with cilantro.",
         "Serve hot with some bread or couscous—Moroccan cozy vibes incoming!"
     ]},
    {"name": "Indian Paneer Tikka", "intro": "Bollywood vibes! Let’s grill Paneer Tikka!",
     "ingredients": ["200g paneer or firm tofu (cubed)", "1/2 cup plain yogurt or vegan yogurt", "1 tbsp ginger-garlic paste", "1 tsp turmeric", "1 tsp garam masala", "1 tsp ground cumin", "1 tsp chili powder", "1/2 tsp coriander powder", "1 tbsp lemon juice", "1 red bell pepper (cubed)", "1 green bell pepper (cubed)", "1 large onion (cubed)", "2 tbsp vegetable oil", "Salt to taste", "1 tbsp fresh cilantro (chopped)", "Skewers (soaked if wooden)"],
     "steps": [
         "In a large bowl, whisk together the yogurt, ginger-garlic paste, turmeric, garam masala, cumin, chili powder, coriander, lemon juice, and salt—smooth marinade time!",
         "Add the paneer or tofu cubes to the bowl, tossing gently to coat—let it soak up the spices!",
         "Cover and marinate in the fridge for at least 30 minutes—overnight if you’re feeling extra!",
         "Chop the bell peppers and onion into bite-sized chunks—colorful skewers ahead!",
         "Preheat your grill or oven to 200°C—get it hot for that perfect char!",
         "Thread the marinated paneer/tofu, peppers, and onion onto skewers—alternate for a pretty pattern!",
         "Brush the skewers with vegetable oil to keep them juicy—don’t skip this step!",
         "Grill or bake for 15-20 minutes, turning halfway, until the edges are golden and slightly charred.",
         "Carefully remove from skewers onto a plate, sprinkle with cilantro, and serve with naan—Bollywood feast ready!"
     ]},
    {"name": "Thai Green Curry", "intro": "Spicy vibes! Time for Thai Green Curry!",
     "ingredients": ["2 tbsp vegetable oil", "3 tbsp green curry paste", "1 can (14 oz) coconut milk", "1 cup vegetable broth", "1 red bell pepper (sliced)", "1 zucchini (sliced)", "1 cup snap peas", "1 cup bamboo shoots (drained)", "1 tbsp fish sauce or soy sauce (for vegan)", "1 tbsp brown sugar", "1 tsp lime zest", "200g firm tofu or chicken (cubed)", "1 cup fresh basil leaves", "2 cups cooked jasmine rice", "1 lime (cut into wedges)", "1 tbsp chopped Thai chili (optional)"],
     "steps": [
         "Heat the vegetable oil in a large pot over medium heat—let it shimmer!",
         "Add the green curry paste and stir for 1-2 minutes until fragrant—spicy vibes incoming!",
         "Pour in the coconut milk and veggie broth, stirring to dissolve the paste—smooth it out!",
         "Stir in the fish sauce or soy sauce, brown sugar, and lime zest—taste the Thai magic!",
         "Add the bell pepper, zucchini, snap peas, and bamboo shoots—let them swim in the curry!",
         "Bring to a simmer and cook for 10-12 minutes until the veggies are tender—don’t overdo it!",
         "Toss in the tofu or chicken cubes, cooking for 5-7 minutes until heated through—gentle stir!",
         "Turn off the heat, stir in the basil leaves and optional chili—they’ll wilt beautifully!",
         "Serve over jasmine rice, squeeze a lime wedge on top, and enjoy—Thai spice perfection!"
     ]},
    {"name": "Greek Spanakopita", "intro": "Mediterranean magic! Let’s make Spanakopita!",
     "ingredients": ["200g fresh spinach (chopped)", "100g feta cheese or vegan feta (crumbled)", "1/2 cup ricotta or vegan cream cheese", "1 pack (16 oz) phyllo dough (thawed)", "3 tbsp olive oil", "1 small onion (finely chopped)", "2 garlic cloves (minced)", "1 tsp dried dill", "1/2 tsp nutmeg", "1/2 tsp lemon zest", "Salt and pepper to taste", "1 egg or 1 flax egg (1 tbsp flax + 3 tbsp water)", "1 tbsp sesame seeds (optional)", "1 tbsp melted butter or oil (for brushing)"],
     "steps": [
         "Preheat your oven to 180°C and grease a baking dish—let’s get flaky!",
         "If using a flax egg, mix 1 tbsp ground flaxseed with 3 tbsp water and let it sit for 5 minutes.",
         "Heat 1 tbsp olive oil in a skillet over medium heat, sauté the onion for 3-4 minutes until soft.",
         "Add the garlic and cook for 30 seconds—smells Mediterranean already!",
         "Toss in the spinach and cook for 2-3 minutes until wilted—stir it down and drain excess water!",
         "In a bowl, mix the spinach, feta, ricotta, dill, nutmeg, lemon zest, salt, pepper, and egg/flax egg—blend it well!",
         "Lay a phyllo sheet in the dish, brush with olive oil or butter, and repeat with 6-8 layers—build that base!",
         "Spread the spinach mix evenly over the phyllo, then top with another 6-8 oiled layers—tuck the edges neatly!",
         "Sprinkle sesame seeds on top, bake for 25-30 minutes until golden and crispy—watch it rise!",
         "Cool for 5 minutes, slice into squares, and serve—Greek deliciousness awaits!"
     ]},
    {"name": "Mexican Black Bean Soup", "intro": "Soup’s on! Let’s cook Mexican Black Bean Soup!",
     "ingredients": ["2 cans (15 oz each) black beans (drained and rinsed)", "2 tbsp olive oil", "1 large onion (chopped)", "2 garlic cloves (minced)", "1 red bell pepper (chopped)", "1 jalapeño (seeded and diced)", "1 tsp ground cumin", "1 tsp chili powder", "1/2 tsp smoked paprika", "1/2 tsp oregano", "3 cups vegetable broth", "1 can (14 oz) diced tomatoes", "1 cup corn kernels (frozen or fresh)", "Salt and pepper to taste", "1 avocado (diced)", "2 tbsp fresh cilantro (chopped)", "1 lime (cut into wedges)"],
     "steps": [
         "Heat the olive oil in a large pot over medium heat—let it get nice and warm!",
         "Add the chopped onion and sauté for 4-5 minutes until soft and golden—stir often!",
         "Toss in the garlic, bell pepper, and jalapeño, cooking for 2-3 minutes—spicy aromas incoming!",
         "Sprinkle in the cumin, chili powder, paprika, and oregano—stir for 1 minute to toast the spices!",
         "Add the black beans, veggie broth, and diced tomatoes—give it a big stir to combine everything.",
         "Bring to a simmer, then lower the heat and cook for 20-25 minutes—let those flavors meld!",
         "Blend half the soup with an immersion blender for creaminess—or keep it chunky if you prefer!",
         "Stir in the corn and cook for 5 more minutes—taste and adjust salt and pepper as needed!",
         "Ladle into bowls, top with diced avocado and cilantro, squeeze a lime wedge over it, and serve—fiesta in a bowl!"
     ]},
    {"name": "Korean Bibimbap", "intro": "K-pop kitchen! Time for Bibimbap!",
     "ingredients": ["2 cups cooked short-grain rice", "2 tbsp sesame oil", "1 carrot (julienned)", "1 zucchini (julienned)", "1 cup spinach (fresh)", "1 cup bean sprouts (fresh)", "1/2 cup shiitake mushrooms (sliced)", "1 tbsp soy sauce", "1 tsp garlic (minced)", "1 tsp sugar", "1 egg or 100g tofu (cubed)", "2 tbsp gochujang (Korean red paste)", "1 tsp sesame seeds (toasted)", "1 green onion (chopped)", "Salt and pepper to taste", "1 tbsp vegetable oil"],
     "steps": [
         "Cook the rice ahead of time—keep it warm and fluffy in a pot or rice cooker!",
         "Heat 1 tbsp sesame oil in a skillet over medium heat—let it get nice and hot!",
         "Add the julienned carrots and sauté for 2-3 minutes until crisp-tender—season with a pinch of salt!",
         "Move carrots to a plate, then sauté the zucchini in the same skillet for 2 minutes—add salt and pepper!",
         "In a small pot, blanch the spinach in boiling water for 1 minute, drain, and season with 1 tsp sesame oil and salt—set aside!",
         "Blanch the bean sprouts for 1 minute, drain, and mix with 1 tsp soy sauce and sugar—set aside too!",
         "Sauté the mushrooms with garlic and remaining soy sauce in the skillet for 3-4 minutes—keep ‘em juicy!",
         "If using an egg, fry it sunny-side up in 1 tbsp vegetable oil; if using tofu, sauté until golden—your protein pick!",
         "In a large bowl, scoop the warm rice, arrange the veggies and tofu/egg in sections on top—make it colorful!",
         "Add a dollop of gochujang, sprinkle with sesame seeds and green onion, mix it up, and enjoy—K-pop feast!"
     ]},
    {"name": "French Ratatouille", "intro": "Oui oui! Let’s make Ratatouille!",
     "ingredients": ["1 medium eggplant (cubed)", "1 zucchini (sliced)", "1 yellow squash (sliced)", "1 red bell pepper (chopped)", "1 yellow bell pepper (chopped)", "1 can (14 oz) diced tomatoes", "2 tbsp olive oil", "1 large onion (chopped)", "2 garlic cloves (minced)", "1 tsp dried thyme", "1 tsp dried basil", "1/2 tsp dried rosemary", "Salt and pepper to taste", "1 tbsp fresh parsley (chopped)", "1 tbsp balsamic vinegar", "1 tbsp tomato paste"],
     "steps": [
         "Heat 1 tbsp olive oil in a large skillet over medium heat—let it shimmer!",
         "Add the chopped onion and sauté for 4-5 minutes until soft and golden—stir often!",
         "Toss in the garlic and cook for 30 seconds—smells like France already!",
         "Add the eggplant cubes and cook for 5-7 minutes until they start to soften—give ‘em room!",
         "Stir in the zucchini, yellow squash, and bell peppers—cook for 5 more minutes, stirring occasionally.",
         "Add the diced tomatoes, tomato paste, thyme, basil, rosemary, salt, and pepper—mix it all together!",
         "Lower the heat, cover, and simmer for 25-30 minutes until the veggies are tender—check with a fork!",
         "Stir in the balsamic vinegar for a tangy kick—taste and adjust seasoning if needed!",
         "Drizzle with the remaining olive oil, sprinkle with parsley, and serve with crusty bread—très délicieux!"
     ]},
    {"name": "Ethiopian Misir Wat", "intro": "Spicy vibes! Time for Misir Wat!",
     "ingredients": ["1 cup dried red lentils (rinsed)", "2 tbsp olive oil", "1 large onion (finely chopped)", "2 garlic cloves (minced)", "1 tbsp berbere spice blend", "1 tsp ground cumin", "1/2 tsp ground coriander", "1/2 tsp paprika", "1 can (14 oz) diced tomatoes", "3 cups vegetable broth", "1 carrot (diced)", "1 potato (cubed)", "Salt and pepper to taste", "2 tbsp fresh parsley (chopped)", "Injera or flatbread (for serving)"],
     "steps": [
         "Heat the olive oil in a large pot over medium heat—let it get nice and warm!",
         "Add the chopped onion and sauté for 5-6 minutes until soft and golden—stir often!",
         "Toss in the minced garlic and cook for 30 seconds—smells spicy already!",
         "Sprinkle in the berbere, cumin, coriander, and paprika—stir for 1 minute to toast the spices!",
         "Add the rinsed lentils, diced tomatoes, and veggie broth—give it a big stir to combine.",
         "Toss in the carrot and potato cubes—bring it to a gentle simmer.",
         "Cover and cook for 25-30 minutes, stirring occasionally, until the lentils and veggies are soft.",
         "Season with salt and pepper to taste—adjust the heat with more berbere if you dare!",
         "Let it sit for 5 minutes off the heat, sprinkle with parsley, and serve with injera—Ethiopian spice win!"
     ]},
    {"name": "Vietnamese Pho", "intro": "Soup goals! Let’s slurp some Pho!",
     "ingredients": ["200g rice noodles", "2 tbsp vegetable oil", "1 large onion (halved)", "1-inch ginger (sliced)", "4 cups vegetable broth", "1 cinnamon stick", "2 star anise", "1 tsp coriander seeds", "1 tbsp soy sauce", "1 tsp hoisin sauce", "1 cup bean sprouts", "1 cup fresh basil leaves", "1 lime (cut into wedges)", "1 jalapeño (sliced)", "2 green onions (chopped)", "Salt to taste"],
     "steps": [
         "Heat a dry skillet over medium heat and char the onion halves and ginger slices for 5 minutes—get that smoky flavor!",
         "In a large pot, heat the vegetable oil over medium, then add the charred onion and ginger.",
         "Pour in the veggie broth and add the cinnamon stick, star anise, and coriander seeds—bring to a boil!",
         "Lower the heat and simmer for 20-25 minutes to infuse the broth—smells like Hanoi!",
         "Strain out the spices and solids, then stir in the soy sauce and hoisin sauce—season with salt to taste.",
         "Cook the rice noodles in boiling water for 5-7 minutes until soft—drain and set aside!",
         "Divide the noodles into bowls, ladle the hot broth over them—watch it steam!",
         "Top with bean sprouts, basil, jalapeño, and green onions—squeeze a lime wedge over each bowl.",
         "Serve hot and slurp it up—pho-nomenal!"
     ]},
    {"name": "Brazilian Feijoada", "intro": "Party time! Let’s cook Feijoada!",
     "ingredients": ["2 cans (15 oz each) black beans (drained)", "2 tbsp olive oil", "1 large onion (chopped)", "3 garlic cloves (minced)", "1 green bell pepper (chopped)", "1 tsp ground cumin", "1 tsp smoked paprika", "1 bay leaf", "3 cups vegetable broth", "1 cup diced tomatoes", "Optional: 200g vegan sausage or tofu (sliced)", "1 orange (zested and juiced)", "Salt and pepper to taste", "2 tbsp fresh parsley (chopped)", "2 cups cooked rice"],
     "steps": [
         "Heat the olive oil in a large pot over medium heat—let it get nice and warm!",
         "Add the chopped onion and sauté for 4-5 minutes until soft and golden—stir often!",
         "Toss in the garlic and bell pepper, cooking for 2-3 minutes—smells festive!",
         "Sprinkle in the cumin and paprika, stirring for 1 minute to toast the spices—wake ‘em up!",
         "Add the black beans, veggie broth, diced tomatoes, and bay leaf—give it a big stir!",
         "If using sausage or tofu, add it now—bring the pot to a simmer.",
         "Cover and cook for 20-25 minutes, stirring occasionally—let the flavors party together!",
         "Stir in the orange zest and juice—taste and adjust salt and pepper as needed!",
         "Remove the bay leaf, sprinkle with parsley, and serve over rice—Brazilian vibes on!"
     ]},
    {"name": "Spanish Paella", "intro": "Hola! Let’s make a veggie Paella!",
     "ingredients": ["1 cup Arborio rice", "2 tbsp olive oil", "1 large onion (chopped)", "2 garlic cloves (minced)", "1 red bell pepper (sliced)", "1 yellow bell pepper (sliced)", "1 cup green peas (frozen or fresh)", "1 cup artichoke hearts (drained)", "1 tsp smoked paprika", "1/2 tsp saffron threads", "3 cups vegetable broth", "1 can (14 oz) diced tomatoes", "Salt and pepper to taste", "1 tbsp fresh parsley (chopped)", "1 lemon (cut into wedges)"],
     "steps": [
         "Heat the olive oil in a large paella pan or skillet over medium heat—let it shimmer!",
         "Add the chopped onion and sauté for 4-5 minutes until soft and golden—stir often!",
         "Toss in the garlic and bell peppers, cooking for 3-4 minutes—colorful vibes!",
         "Sprinkle in the smoked paprika and saffron—stir for 1 minute to release the aromas!",
         "Add the Arborio rice and stir to coat in the oil—toast it for 2 minutes!",
         "Pour in the veggie broth and diced tomatoes—bring it to a simmer without stirring too much!",
         "Add the peas and artichoke hearts, season with salt and pepper—let it cook for 20-25 minutes until the rice is tender.",
         "Check for a crispy bottom (socarrat)—don’t stir now, let it form!",
         "Sprinkle with parsley, serve with lemon wedges, and enjoy—Spanish fiesta time!"
     ]},
    {"name": "Chinese Stir-Fry", "intro": "Wok it out! Time for Stir-Fry!",
     "ingredients": ["2 tbsp vegetable oil", "1 cup broccoli florets", "1 red bell pepper (sliced)", "1 carrot (sliced)", "1 cup snap peas", "1 cup mushrooms (sliced)", "200g firm tofu or chicken (cubed)", "2 garlic cloves (minced)", "1 tbsp ginger (minced)", "3 tbsp soy sauce", "1 tbsp oyster sauce or hoisin (for vegan)", "1 tsp sesame oil", "1 tsp cornstarch (mixed with 2 tbsp water)", "1 green onion (chopped)", "2 cups cooked rice"],
     "steps": [
         "Heat 1 tbsp vegetable oil in a wok or large skillet over high heat—get it smoking hot!",
         "Add the tofu or chicken cubes and stir-fry for 4-5 minutes until golden—set aside!",
         "Add the remaining oil, then toss in the garlic and ginger—stir for 30 seconds until fragrant!",
         "Add the broccoli, bell pepper, carrot, snap peas, and mushrooms—stir-fry for 5-7 minutes until crisp-tender!",
         "Return the tofu/chicken to the wok—give it a quick toss to mix!",
         "Pour in the soy sauce, oyster/hoisin sauce, and sesame oil—stir to coat everything!",
         "Add the cornstarch slurry and stir for 1-2 minutes until the sauce thickens—shiny and glossy!",
         "Sprinkle with green onion, serve over warm rice, and dig in—wok star status achieved!"
     ]},
    {"name": "Lebanese Falafel", "intro": "Crispy vibes! Let’s fry Falafel!",
     "ingredients": ["1 can (15 oz) chickpeas (drained) or 1 cup dried chickpeas (soaked overnight)", "1 small onion (chopped)", "2 garlic cloves (minced)", "1 cup fresh parsley (chopped)", "1 tsp ground cumin", "1 tsp ground coriander", "1/2 tsp baking powder", "1/4 tsp cayenne pepper", "Salt and pepper to taste", "2 tbsp all-purpose flour", "Vegetable oil for frying", "4 pita breads", "1 cup tahini sauce", "1 cup shredded lettuce", "1 tomato (sliced)"],
     "steps": [
         "If using dried chickpeas, soak them overnight, then drain—canned ones just need draining!",
         "In a food processor, pulse the chickpeas, onion, garlic, and parsley until coarse—don’t puree it!",
         "Add the cumin, coriander, baking powder, cayenne, salt, pepper, and flour—pulse to combine!",
         "Scoop out the mixture and shape into small balls or patties—about 2 tbsp each!",
         "Heat 2 inches of vegetable oil in a deep skillet over medium-high heat—get it to 175°C!",
         "Fry the falafel in batches for 3-4 minutes per side until golden and crispy—don’t crowd ‘em!",
         "Drain on paper towels to remove excess oil—keep ‘em crunchy!",
         "Warm the pita breads in the oven at 180°C for 2-3 minutes—soft and ready!",
         "Stuff the pitas with falafel, lettuce, tomato, and a drizzle of tahini sauce—Lebanese delight!"
     ]},
    {"name": "Italian Risotto", "intro": "Creamy dreams! Let’s cook Risotto!",
     "ingredients": ["1 cup Arborio rice", "2 tbsp olive oil", "1 small onion (finely chopped)", "2 garlic cloves (minced)", "1/2 cup dry white wine (optional)", "4 cups vegetable broth (warmed)", "1 cup mushrooms (sliced)", "1 tsp dried thyme", "1/2 tsp salt", "1/4 tsp black pepper", "1/4 cup grated parmesan or nutritional yeast", "1 tbsp butter or vegan butter", "2 tbsp fresh parsley (chopped)", "1 lemon (zested)"],
     "steps": [
         "Heat the veggie broth in a pot and keep it warm on low—ready for action!",
         "In a large skillet, heat the olive oil over medium heat—let it shimmer!",
         "Add the chopped onion and sauté for 3-4 minutes until soft and translucent—stir often!",
         "Toss in the garlic and mushrooms, cooking for 2-3 minutes until the mushrooms soften—smells earthy!",
         "Add the Arborio rice and stir for 1-2 minutes to toast it—coat it in oil!",
         "If using wine, pour it in and stir until it’s mostly absorbed—adds that Italian flair!",
         "Ladle in 1 cup of warm broth, stirring constantly until absorbed—keep it creamy!",
         "Continue adding broth, 1/2 cup at a time, stirring for 20-25 minutes until the rice is tender—patience pays off!",
         "Stir in the thyme, salt, pepper, parmesan or yeast, butter, parsley, and lemon zest—mix it silky!",
         "Serve hot in bowls—Italian comfort in every bite!"
     ]},
    {"name": "Turkish Menemen", "intro": "Breakfast vibes! Time for Menemen!",
     "ingredients": ["2 tbsp olive oil", "1 green bell pepper (finely chopped)", "1 red bell pepper (finely chopped)", "3 medium tomatoes (peeled and diced)", "1 small onion (finely chopped)", "3 large eggs", "1 tsp paprika", "1/2 tsp red pepper flakes", "1/2 tsp dried oregano", "Salt and pepper to taste", "1 tbsp fresh parsley (chopped)", "1/4 tsp cumin", "Optional: 1/4 cup feta cheese (crumbled)", "Bread for serving"],
     "steps": [
         "Heat the olive oil in a large skillet over medium heat—let it get nice and warm!",
         "Add the chopped onion and sauté for 3-4 minutes until soft and golden—stir often!",
         "Toss in the green and red bell peppers, cooking for 5-6 minutes until softened—keep ‘em moving!",
         "Add the diced tomatoes, paprika, red pepper flakes, oregano, cumin, salt, and pepper—mix it well!",
         "Simmer the mixture for 8-10 minutes, stirring occasionally, until it thickens into a sauce—smells amazing!",
         "Crack the eggs into a bowl, whisk lightly, then pour them into the skillet—let them sit for a sec!",
         "Gently stir the eggs into the veggies for 2-3 minutes until just set—keep it soft and creamy!",
         "Sprinkle with parsley and feta if using—give it a final stir!",
         "Serve hot with crusty bread for dipping—Turkish breakfast goals!"
     ]},
    {"name": "Peruvian Lomo Saltado", "intro": "Fusion fun! Let’s make Lomo Saltado!",
     "ingredients": ["2 tbsp vegetable oil", "1 large potato (cut into fries)", "1 red bell pepper (sliced)", "1 yellow bell pepper (sliced)", "1 large onion (sliced)", "200g firm tofu or beef (sliced)", "2 garlic cloves (minced)", "2 tbsp soy sauce", "1 tbsp red wine vinegar", "1 tsp ground cumin", "1/2 tsp paprika", "Salt and pepper to taste", "2 cups cooked rice", "1 tbsp fresh cilantro (chopped)", "1 tomato (sliced)"],
     "steps": [
         "Heat 1 tbsp oil in a large skillet over medium-high heat—get it hot for fries!",
         "Add the potato fries and cook for 5-7 minutes until golden and crispy—set aside on paper towels!",
         "Add the remaining oil to the skillet, then toss in the garlic and tofu/beef—stir-fry for 3-4 minutes until browned!",
         "Add the bell peppers and onion, cooking for 3-4 minutes until crisp-tender—keep ‘em colorful!",
         "Stir in the soy sauce, vinegar, cumin, paprika, salt, and pepper—coat everything well!",
         "Return the fries to the skillet, tossing to mix with the veggies and sauce—fusion vibes!",
         "Cook for 2 more minutes to heat through—taste and adjust seasoning if needed!",
         "Serve over warm rice, top with tomato slices and cilantro—Peruvian perfection!"
     ]},
    {"name": "Hungarian Goulash", "intro": "Hearty vibes! Time for Goulash!",
     "ingredients": ["2 tbsp olive oil", "1 large onion (chopped)", "2 garlic cloves (minced)", "1 red bell pepper (chopped)", "1 tbsp paprika", "1 tsp caraway seeds", "1/2 tsp smoked paprika", "1 can (14 oz) diced tomatoes", "3 cups vegetable broth", "2 medium potatoes (cubed)", "1 carrot (sliced)", "1 cup mushrooms (sliced)", "Salt and pepper to taste", "2 tbsp fresh parsley (chopped)", "Sour cream or vegan sour cream (optional)"],
     "steps": [
         "Heat the olive oil in a large pot over medium heat—let it warm up!",
         "Add the chopped onion and sauté for 4-5 minutes until soft and golden—stir often!",
         "Toss in the garlic and bell pepper, cooking for 2-3 minutes—smells hearty already!",
         "Sprinkle in the paprika, caraway seeds, and smoked paprika—stir for 1 minute to toast!",
         "Add the diced tomatoes, veggie broth, potatoes, carrot, and mushrooms—give it a big stir!",
         "Bring to a simmer, cover, and cook for 25-30 minutes until the veggies are tender—check ‘em!",
         "Season with salt and pepper to taste—adjust the spice if you like it bold!",
         "Let it sit for 5 minutes off the heat—sprinkle with parsley!",
         "Serve hot with a dollop of sour cream if using—Hungarian comfort in a bowl!"
     ]},
    {"name": "Turkish Manti", "intro": "Dumpling delight! Let’s make Manti!",
     "ingredients": ["2 cups all-purpose flour", "1 large egg or 1/4 cup water (for vegan)", "1/2 tsp salt", "1/2 cup water (for dough)", "200g ground lamb or lentils", "1 small onion (finely chopped)", "1 tsp paprika", "1/2 tsp black pepper", "Salt to taste", "2 tbsp butter or vegan butter", "1 cup plain yogurt or vegan yogurt", "1 garlic clove (minced)", "1 tsp red pepper flakes", "1 tbsp fresh parsley (chopped)"],
     "steps": [
         "In a bowl, mix the flour, egg or 1/4 cup water, salt, and 1/2 cup water—knead into a smooth dough!",
         "Cover the dough and let it rest for 30 minutes—give it some chill time!",
         "In another bowl, mix the lamb or lentils, onion, paprika, black pepper, and salt—your filling’s ready!",
         "Roll out the dough on a floured surface until thin—about 1-2 mm thick!",
         "Cut into 2-inch squares, place a small spoonful of filling in each, and fold into tiny dumplings—pinch the edges!",
         "Bring a large pot of salted water to a boil—drop the manti in carefully!",
         "Cook for 10-12 minutes until they float—drain and set aside!",
         "Melt the butter in a skillet, stir in red pepper flakes—drizzle over the manti!",
         "Mix the yogurt with minced garlic, spoon over the manti, sprinkle with parsley, and serve—Turkish heaven!"
     ]},
    {"name": "Adana Kebab", "intro": "Spicy skewers! Time for Adana Kebab!",
     "ingredients": ["200g ground lamb or firm tofu (crumbled)", "1 small onion (finely chopped)", "2 garlic cloves (minced)", "1 tsp chili powder", "1 tsp ground cumin", "1 tsp sumac", "1/2 tsp paprika", "1/2 tsp black pepper", "Salt to taste", "2 tbsp fresh parsley (chopped)", "1 tbsp olive oil", "4 skewers (soaked if wooden)", "1 cup flatbread", "1 tomato (sliced)", "1/4 cup pickled peppers"],
     "steps": [
         "In a large bowl, mix the lamb or tofu, onion, garlic, chili powder, cumin, sumac, paprika, pepper, salt, and parsley—get it sticky!",
         "Knead the mixture for 5 minutes until well combined—shape it around skewers into long kebabs!",
         "Brush the kebabs with olive oil—keeps ‘em juicy!",
         "Preheat your grill or oven to 200°C—get it hot for charring!",
         "Grill the kebabs for 10-12 minutes, turning halfway, until browned and cooked through—smells spicy!",
         "Warm the flatbread in the oven for 2-3 minutes—soft and ready!",
         "Slide the kebabs off the skewers onto a plate—serve with flatbread, tomato slices, and pickled peppers!",
         "Dig in—Adana spice party on!"
     ]},
    {"name": "Doner Kebab", "intro": "Street food vibes! Let’s make Doner Kebab!",
     "ingredients": ["200g chicken breast or seitan (thinly sliced)", "1/2 cup plain yogurt or vegan yogurt", "1 tbsp olive oil", "1 tsp ground cumin", "1 tsp paprika", "1/2 tsp garlic powder", "1/2 tsp onion powder", "1/2 tsp black pepper", "Salt to taste", "4 pita breads", "1 cup shredded lettuce", "1 tomato (sliced)", "1/4 red onion (thinly sliced)", "1/4 cup tahini sauce or vegan mayo", "1 tbsp fresh parsley (chopped)"],
     "steps": [
         "In a bowl, mix the yogurt, olive oil, cumin, paprika, garlic powder, onion powder, pepper, and salt—smooth marinade!",
         "Add the chicken or seitan slices, toss to coat, and marinate in the fridge for at least 1 hour—longer is better!",
         "Preheat your grill or oven to 200°C—get it ready for some sizzle!",
         "Thread the marinated slices onto skewers or spread on a baking sheet—keep it even!",
         "Grill or bake for 15-20 minutes, turning halfway, until golden and cooked—juicy vibes!",
         "Warm the pita breads in the oven for 2-3 minutes—soft and pliable!",
         "Slice the chicken or seitan thinly off the skewers—stack it high!",
         "Stuff the pitas with the slices, lettuce, tomato, onion, and a drizzle of tahini or mayo—sprinkle with parsley!",
         "Roll it up and enjoy—street food dreams!"
     ]},
    {"name": "Lahmacun", "intro": "Turkish pizza! Time for Lahmacun!",
     "ingredients": ["2 cups all-purpose flour", "1 tsp yeast", "1/2 tsp salt", "3/4 cup warm water", "200g ground lamb or mushrooms (chopped)", "1 small onion (finely chopped)", "1 tomato (finely chopped)", "1 tbsp tomato paste", "1 tsp paprika", "1/2 tsp cumin", "1/2 tsp red pepper flakes", "Salt and pepper to taste", "1 tbsp olive oil", "1 cup fresh parsley (chopped)", "1 lemon (cut into wedges)"],
     "steps": [
         "In a bowl, mix flour, yeast, salt, and warm water—knead into a smooth dough for 5 minutes!",
         "Cover and let the dough rise for 1 hour until doubled—cozy dough time!",
         "In another bowl, mix the lamb or mushrooms, onion, tomato, tomato paste, paprika, cumin, red pepper flakes, salt, and pepper—spicy topping ready!",
         "Preheat your oven to 220°C—get it super hot!",
         "Divide the dough into 4 balls, roll each into a thin circle—think pizza size!",
         "Spread the topping evenly over each dough circle—press it in lightly!",
         "Bake on a lined sheet for 10-12 minutes until the edges are crispy—watch that golden glow!",
         "Drizzle with olive oil, sprinkle with parsley, squeeze lemon over it, roll up, and eat—Turkish pizza win!"
     ]},
    {"name": "Yaprak Sarma", "intro": "Wrapped goodies! Let’s make Yaprak Sarma!",
     "ingredients": ["20 grape leaves (jarred or fresh)", "1 cup short-grain rice", "2 tbsp olive oil", "1 small onion (finely chopped)", "1 tbsp pine nuts", "1 tbsp currants", "1 tsp ground cinnamon", "1 tsp dried mint", "1/2 tsp allspice", "Salt and pepper to taste", "1 cup vegetable broth", "1 lemon (juiced)", "1 tbsp fresh dill (chopped)", "1 cup plain yogurt or vegan yogurt (for serving)"],
     "steps": [
         "If using fresh grape leaves, blanch in boiling water for 1 minute, then drain—jarred ones are ready to go!",
         "Heat 1 tbsp olive oil in a skillet over medium heat—sauté the onion for 3-4 minutes until soft!",
         "Add the pine nuts and currants, cooking for 2 minutes—smells nutty and sweet!",
         "Stir in the rice, cinnamon, mint, allspice, salt, and pepper—cook for 1 minute to coat!",
         "Add 1/2 cup water, cover, and simmer for 5 minutes until the rice is half-cooked—let it cool slightly!",
         "Lay a grape leaf flat, shiny side down, spoon 1 tbsp filling near the stem, fold sides, and roll tightly—repeat!",
         "Arrange the rolls in a pot, seam-side down, drizzle with remaining oil, lemon juice, and broth—cozy ‘em up!",
         "Cover and simmer on low for 30-35 minutes until the rice is tender—check one to be sure!",
         "Let cool slightly, sprinkle with dill, and serve with yogurt—Turkish delight in every bite!"
     ]},
    {"name": "Jamaican Jerk Tofu", "intro": "Island spice! Time for Jerk Tofu!",
     "ingredients": ["200g firm tofu (pressed and cubed)", "2 tbsp olive oil", "1 tbsp jerk seasoning", "1 tsp ground allspice", "1/2 tsp cinnamon", "1/2 tsp nutmeg", "1 tbsp soy sauce", "1 tbsp lime juice", "1 small onion (chopped)", "1 red bell pepper (chopped)", "1 garlic clove (minced)", "1 cup cooked rice", "1 tbsp fresh thyme (chopped)", "1 green onion (chopped)", "Salt to taste"],
     "steps": [
         "Press the tofu for 20 minutes to remove excess water—cube it up!",
         "In a bowl, mix jerk seasoning, allspice, cinnamon, nutmeg, soy sauce, lime juice, and 1 tbsp oil—spicy marinade time!",
         "Add the tofu cubes and toss to coat—let it marinate for 30 minutes if you’ve got time!",
         "Heat the remaining oil in a skillet over medium heat—let it get hot!",
         "Add the onion, bell pepper, and garlic—sauté for 3-4 minutes until soft!",
         "Toss in the marinated tofu and cook for 5-7 minutes until golden and crispy—flip ‘em gently!",
         "Season with salt and fresh thyme—give it a final stir!",
         "Serve over warm rice, sprinkle with green onion—Jamaican island vibes ready!"
     ]},
    {"name": "Polish Pierogi", "intro": "Dumpling love! Let’s make Pierogi!",
     "ingredients": ["2 cups all-purpose flour", "1 large egg or 1/4 cup water (for vegan)", "1/2 tsp salt", "1/2 cup water", "1 cup mashed potatoes", "1/2 cup grated cheddar or vegan cheese", "1 small onion (finely chopped)", "2 tbsp butter or vegan butter", "1 tsp black pepper", "Salt to taste", "1 tbsp olive oil", "1/4 cup sour cream or vegan sour cream", "1 tbsp fresh chives (chopped)"],
     "steps": [
         "In a bowl, mix flour, egg or 1/4 cup water, salt, and 1/2 cup water—knead into a smooth dough!",
         "Cover and let the dough rest for 30 minutes—give it a break!",
         "In a skillet, heat 1 tbsp butter and sauté the onion for 3-4 minutes until golden—set aside!",
         "Mix the mashed potatoes, cheese, half the onions, pepper, and salt—your filling’s ready!",
         "Roll out the dough on a floured surface until thin—cut into 3-inch circles!",
         "Spoon 1 tbsp filling onto each circle, fold over, and pinch the edges to seal—dumpling magic!",
         "Boil a pot of salted water, drop in the pierogi, and cook for 4-5 minutes until they float—drain ‘em!",
         "Heat the remaining butter and oil in the skillet, fry the pierogi for 2-3 minutes per side until golden—crisp it up!",
         "Serve with sour cream, remaining onions, and chives—Polish comfort on a plate!"
     ]},
    {"name": "Indian Chana Masala", "intro": "Curry night! Time for Chana Masala!",
     "ingredients": ["2 cans (15 oz each) chickpeas (drained)", "2 tbsp vegetable oil", "1 large onion (finely chopped)", "2 garlic cloves (minced)", "1 tbsp ginger (minced)", "1 tsp ground cumin", "1 tsp garam masala", "1 tsp turmeric", "1 tsp chili powder", "1 can (14 oz) diced tomatoes", "1 cup vegetable broth", "1 tsp coriander powder", "Salt and pepper to taste", "2 tbsp fresh cilantro (chopped)", "1 lemon (cut into wedges)", "2 cups cooked rice or naan"],
     "steps": [
         "Heat the vegetable oil in a large pot over medium heat—let it shimmer!",
         "Add the chopped onion and sauté for 4-5 minutes until golden—stir often!",
         "Toss in the garlic and ginger, cooking for 1 minute—smells like India!",
         "Sprinkle in the cumin, garam masala, turmeric, chili powder, and coriander—stir for 1 minute to toast!",
         "Add the diced tomatoes and veggie broth—give it a big stir to combine!",
         "Toss in the chickpeas, bring to a simmer, and cook for 20-25 minutes—let the flavors meld!",
         "Mash a few chickpeas with a spoon to thicken the sauce—creamy texture time!",
         "Season with salt and pepper—taste and adjust the spice level!",
         "Sprinkle with cilantro, serve with rice or naan, and squeeze lemon over it—curry bliss!"
     ]},
    {"name": "South African Bobotie", "intro": "Sweet and savory! Let’s make Bobotie!",
     "ingredients": ["200g ground beef or lentils", "2 tbsp olive oil", "1 large onion (chopped)", "2 garlic cloves (minced)", "1 tbsp curry powder", "1 tsp turmeric", "1/2 tsp cinnamon", "1 slice bread (soaked in 1/4 cup milk or plant milk)", "1/4 cup raisins", "1 tbsp apricot jam", "1 can (14 oz) diced tomatoes", "1 large egg or 1 flax egg (1 tbsp flax + 3 tbsp water)", "Salt and pepper to taste", "2 bay leaves", "1 tbsp fresh parsley (chopped)"],
     "steps": [
         "Preheat your oven to 180°C—let’s get baking!",
         "Heat the olive oil in a skillet over medium heat—add the onion and sauté for 4-5 minutes until soft!",
         "Toss in the garlic and cook for 30 seconds—smells fragrant!",
         "Add the beef or lentils, curry powder, turmeric, and cinnamon—cook for 5-7 minutes until browned!",
         "Squeeze the soaked bread and crumble it into the skillet—stir in the raisins and jam!",
         "Add the diced tomatoes, season with salt and pepper—simmer for 10 minutes!",
         "Transfer the mixture to a baking dish, remove the bay leaves—smooth it out!",
         "Whisk the egg or flax egg with a splash of milk, pour over the top—custard layer time!",
         "Bake for 25-30 minutes until golden—sprinkle with parsley and serve—South African vibes!"
     ]},
    {"name": "Russian Borscht", "intro": "Beet it! Time for Borscht!",
     "ingredients": ["2 medium beets (peeled and grated)", "2 tbsp olive oil", "1 large onion (chopped)", "2 garlic cloves (minced)", "1 carrot (grated)", "1 potato (cubed)", "1 cup cabbage (shredded)", "1 can (14 oz) diced tomatoes", "4 cups vegetable broth", "1 tbsp red wine vinegar", "1 tsp dill (dried or fresh)", "Salt and pepper to taste", "1 tbsp sugar", "1/4 cup sour cream or vegan sour cream", "1 tbsp fresh dill (chopped)"],
     "steps": [
         "Heat the olive oil in a large pot over medium heat—let it warm up!",
         "Add the chopped onion and sauté for 4-5 minutes until soft—stir often!",
         "Toss in the garlic and grated beets—cook for 5-7 minutes until they soften!",
         "Add the carrot, potato, and cabbage—stir to mix with the beets!",
         "Pour in the diced tomatoes and veggie broth—bring it to a simmer!",
         "Stir in the vinegar, dill, sugar, salt, and pepper—cover and cook for 25-30 minutes until tender!",
         "Taste and adjust seasoning—more vinegar for tang if you like!",
         "Ladle into bowls, top with a dollop of sour cream and fresh dill—Russian warmth served!"
     ]},
    {"name": "Malaysian Laksa", "intro": "Soup spice! Let’s make Laksa!",
     "ingredients": ["200g rice noodles", "2 tbsp vegetable oil", "1 large onion (chopped)", "2 garlic cloves (minced)", "1 tbsp ginger (minced)", "2 tbsp laksa paste", "1 can (14 oz) coconut milk", "3 cups vegetable broth", "1 red bell pepper (sliced)", "1 cup bean sprouts", "200g firm tofu (cubed)", "1 tsp fish sauce or soy sauce (vegan)", "1 tbsp lime juice", "1 cup fresh cilantro (chopped)", "1 chili (sliced)"],
     "steps": [
         "Cook the rice noodles in boiling water for 5-7 minutes until soft—drain and set aside!",
         "Heat the vegetable oil in a large pot over medium heat—let it shimmer!",
         "Add the onion, garlic, and ginger—sauté for 3-4 minutes until fragrant!",
         "Stir in the laksa paste and cook for 1-2 minutes—spicy aroma time!",
         "Pour in the coconut milk and veggie broth—stir to combine smoothly!",
         "Add the bell pepper and tofu, bring to a simmer—cook for 10-12 minutes!",
         "Stir in the fish sauce or soy sauce and lime juice—taste and adjust!",
         "Divide the noodles into bowls, ladle the hot laksa over them—top with bean sprouts, cilantro, and chili!",
         "Serve hot—Malaysian spice heaven!"
     ]},
    {"name": "Cuban Black Beans", "intro": "Tropical vibes! Time for Cuban Black Beans!",
     "ingredients": ["2 cans (15 oz each) black beans (drained)", "2 tbsp olive oil", "1 large onion (chopped)", "2 garlic cloves (minced)", "1 green bell pepper (chopped)", "1 tsp ground cumin", "1 tsp oregano", "1/2 tsp smoked paprika", "1 bay leaf", "2 cups vegetable broth", "1 tbsp red wine vinegar", "1 tsp sugar", "Salt and pepper to taste", "2 cups cooked rice", "1 tbsp fresh cilantro (chopped)"],
     "steps": [
         "Heat the olive oil in a large pot over medium heat—let it warm up!",
         "Add the onion and bell pepper—sauté for 4-5 minutes until soft!",
         "Toss in the garlic and cook for 30 seconds—smells tropical!",
         "Sprinkle in the cumin, oregano, and paprika—stir for 1 minute to toast!",
         "Add the black beans, veggie broth, bay leaf, vinegar, and sugar—mix it up!",
         "Bring to a simmer, cover, and cook for 20-25 minutes—let it thicken!",
         "Remove the bay leaf, season with salt and pepper—taste and tweak!",
         "Serve over warm rice, sprinkle with cilantro—Cuban comfort ready!"
     ]},
    {"name": "Swedish Meatballs", "intro": "Cozy up! Let’s make veggie Swedish Meatballs!",
     "ingredients": ["200g lentils or ground beef", "1/2 cup breadcrumbs", "1 large egg or 1 flax egg (1 tbsp flax + 3 tbsp water)", "1 small onion (finely chopped)", "1 tsp allspice", "1/2 tsp nutmeg", "Salt and pepper to taste", "2 tbsp olive oil", "2 cups vegetable broth", "1 tbsp soy sauce", "1/4 cup cream or vegan cream", "1 tbsp flour", "1 tbsp butter or vegan butter", "1 tbsp fresh parsley (chopped)", "2 cups mashed potatoes"],
     "steps": [
         "If using a flax egg, mix 1 tbsp flax with 3 tbsp water and let sit for 5 minutes!",
         "In a bowl, mix lentils or beef, breadcrumbs, egg/flax egg, onion, allspice, nutmeg, salt, and pepper—combine well!",
         "Shape into small meatballs—about 1-inch each!",
         "Heat olive oil in a skillet over medium heat—fry the meatballs for 5-7 minutes until browned all over!",
         "Remove meatballs and set aside—keep the skillet hot!",
         "Melt butter in the skillet, stir in flour to make a roux—cook for 1 minute!",
         "Slowly whisk in veggie broth, soy sauce, and cream—simmer until thickened, about 5 minutes!",
         "Return meatballs to the sauce, cook for 5-7 minutes—coat ‘em well!",
         "Serve over mashed potatoes, sprinkle with parsley—Swedish cozy time!"
     ]},
    {"name": "Egyptian Koshari", "intro": "Street eats! Time for Koshari!",
     "ingredients": ["1 cup lentils (rinsed)", "1 cup rice", "1 cup elbow pasta", "2 tbsp olive oil", "1 large onion (sliced)", "2 garlic cloves (minced)", "1 can (14 oz) diced tomatoes", "1 tsp ground cumin", "1 tsp coriander", "1/2 tsp chili powder", "Salt and pepper to taste", "1 cup crispy fried onions", "1/4 cup hot sauce (optional)", "1 tbsp fresh parsley (chopped)"],
     "steps": [
         "Cook the lentils in boiling water for 20-25 minutes until tender—drain and set aside!",
         "Cook the rice in a pot with 2 cups water until fluffy—about 15 minutes—set aside!",
         "Boil the pasta in salted water for 8-10 minutes until al dente—drain and set aside!",
         "Heat 1 tbsp olive oil in a skillet, sauté the sliced onion until golden and crispy—set aside for topping!",
         "In the same skillet, heat remaining oil, add garlic—cook for 30 seconds!",
         "Stir in diced tomatoes, cumin, coriander, chili powder, salt, and pepper—simmer for 10 minutes!",
         "Layer the lentils, rice, and pasta in bowls—spoon the tomato sauce over top!",
         "Top with crispy onions, a drizzle of hot sauce if using, and parsley—Egyptian street food vibes!"
     ]},
    {"name": "Filipino Adobo", "intro": "Tangy vibes! Let’s make Adobo!",
     "ingredients": ["200g firm tofu or chicken (cubed)", "2 tbsp vegetable oil", "1 large onion (sliced)", "3 garlic cloves (minced)", "1/4 cup soy sauce", "1/4 cup white vinegar", "1 tbsp brown sugar", "1 tsp black peppercorns", "2 bay leaves", "1 cup vegetable broth", "1 medium potato (cubed)", "1 carrot (sliced)", "Salt to taste", "1 tbsp fresh green onions (chopped)", "2 cups cooked rice"],
     "steps": [
         "Heat the vegetable oil in a large pot over medium heat—let it get hot!",
         "Add the onion and garlic—sauté for 3-4 minutes until fragrant!",
         "Toss in the tofu or chicken cubes—cook for 5-7 minutes until browned!",
         "Pour in the soy sauce, vinegar, brown sugar, peppercorns, and bay leaves—don’t stir yet!",
         "Add the veggie broth, potato, and carrot—now give it a big stir!",
         "Bring to a simmer, cover, and cook for 20-25 minutes until tender—smells tangy!",
         "Remove the bay leaves, taste and add salt if needed—adjust that flavor!",
         "Serve over warm rice, sprinkle with green onions—Filipino comfort on!"
     ]},
    {"name": "Mongolian Stir-Fry", "intro": "Quick and bold! Time for Mongolian Stir-Fry!",
     "ingredients": ["200g firm tofu or beef (sliced)", "2 tbsp vegetable oil", "1 large onion (sliced)", "1 red bell pepper (sliced)", "1 cup broccoli florets", "2 garlic cloves (minced)", "1 tbsp ginger (minced)", "1/4 cup soy sauce", "1 tbsp hoisin sauce", "1 tsp sesame oil", "1 tsp cornstarch (mixed with 2 tbsp water)", "1 green onion (chopped)", "2 cups cooked rice", "1 tsp sesame seeds (toasted)", "Salt and pepper to taste"],
     "steps": [
         "Heat 1 tbsp vegetable oil in a wok or large skillet over high heat—get it smoking hot!",
         "Add the tofu or beef slices and stir-fry for 4-5 minutes until golden—remove and set aside!",
         "Add the remaining oil to the wok, then toss in the garlic and ginger—stir-fry for 30 seconds until fragrant!",
         "Add the onion, bell pepper, and broccoli—stir-fry for 5-7 minutes until crisp-tender!",
         "Return the tofu or beef to the wok—give it a quick toss to mix everything!",
         "Pour in the soy sauce, hoisin sauce, and sesame oil—stir to coat all the goodies!",
         "Add the cornstarch slurry and stir for 1-2 minutes until the sauce thickens—shiny and bold!",
         "Season with salt and pepper to taste—give it one last stir!",
         "Serve hot over cooked rice, sprinkle with green onion and sesame seeds—Mongolian flavor blast!"
     ]},
    {"name": "Algerian Chakchouka", "intro": "Egg-citing! Let’s make Chakchouka!",
     "ingredients": ["2 tbsp olive oil", "1 large onion (chopped)", "1 red bell pepper (chopped)", "1 green bell pepper (chopped)", "2 garlic cloves (minced)", "1 tsp ground cumin", "1 tsp paprika", "1/2 tsp chili powder", "1 can (14 oz) diced tomatoes", "1 tbsp tomato paste", "Salt and pepper to taste", "4 large eggs or 200g crumbled tofu", "1 tbsp fresh parsley (chopped)", "1 tbsp fresh cilantro (chopped)", "Flatbread for serving"],
     "steps": [
         "Heat the olive oil in a large skillet over medium heat—let it shimmer!",
         "Add the chopped onion and sauté for 4-5 minutes until soft and golden—stir often!",
         "Toss in the red and green bell peppers—cook for 5-6 minutes until they soften!",
         "Stir in the garlic, cumin, paprika, and chili powder—cook for 1 minute to toast the spices!",
         "Add the diced tomatoes and tomato paste—mix well and bring to a simmer!",
         "Cook for 10-12 minutes until the sauce thickens—season with salt and pepper to taste!",
         "If using eggs, make 4 wells in the sauce and crack an egg into each; if using tofu, sprinkle it evenly over the top—cover and cook for 5-7 minutes until set!",
         "Sprinkle with parsley and cilantro—give it a vibrant finish!",
         "Serve hot with flatbread for dipping—Algerian breakfast magic!"
     ]},
    {"name": "Sri Lankan Dhal Curry", "intro": "Lentil love! Time for Dhal Curry!",
     "ingredients": ["1 cup red lentils (rinsed)", "2 tbsp coconut oil", "1 large onion (chopped)", "2 garlic cloves (minced)", "1 tbsp ginger (minced)", "1 tsp ground cumin", "1 tsp ground turmeric", "1/2 tsp mustard seeds", "1 can (14 oz) coconut milk", "2 cups vegetable broth", "1 cinnamon stick", "1 tsp chili powder", "Salt and pepper to taste", "1 tbsp fresh curry leaves (optional)", "2 cups cooked rice", "1 tbsp fresh cilantro (chopped)"],
     "steps": [
         "Rinse the red lentils under cold water until the water runs clear—set aside!",
         "Heat the coconut oil in a large pot over medium heat—let it melt and shimmer!",
         "Add the mustard seeds and cook until they start to pop—about 1 minute!",
         "Toss in the chopped onion and sauté for 4-5 minutes until golden—stir often!",
         "Stir in the garlic and ginger—cook for 1 minute until fragrant!",
         "Sprinkle in the cumin, turmeric, and chili powder—stir for 1 minute to toast the spices!",
         "Add the lentils, coconut milk, veggie broth, cinnamon stick, and curry leaves if using—bring to a simmer!",
         "Cover and cook for 20-25 minutes, stirring occasionally, until the lentils are soft and creamy—check the texture!",
         "Season with salt and pepper—remove the cinnamon stick and adjust the spice level if needed!",
         "Serve over warm rice, sprinkle with cilantro—Sri Lankan comfort in every bite!"
     ]},
    {"name": "Grilled Chicken Shawarma", "intro": "Middle Eastern delight! Time for Grilled Chicken Shawarma!",
     "ingredients": ["2 lbs boneless chicken thighs", "1/4 cup olive oil", "3 cloves garlic (minced)", "1 tsp ground cumin", "1 tsp paprika", "1/2 tsp turmeric", "1/2 tsp cinnamon", "Salt and pepper to taste", "Juice of 1 lemon", "Pita bread", "1/2 cup yogurt sauce"],
     "steps": [
         "In a bowl, mix olive oil, garlic, cumin, paprika, turmeric, cinnamon, salt, pepper, and lemon juice.",
         "Coat the chicken thighs in the marinade and refrigerate for at least 1 hour.",
         "Preheat grill to medium-high heat and grill chicken for 5-7 minutes per side until cooked through.",
         "Slice the chicken and serve in pita bread with yogurt sauce.",
         "Enjoy your homemade shawarma!"
     ]},
    {"name": "Thai Basil Stir-Fry", "intro": "Quick and delicious! Let's make Thai Basil Stir-Fry!",
     "ingredients": ["1 lb ground chicken or tofu", "2 tbsp vegetable oil", "4 cloves garlic (minced)", "2 red chilies (sliced)", "1/4 cup soy sauce", "1 tbsp fish sauce (optional)", "1 tbsp oyster sauce", "1 tbsp sugar", "1 cup fresh basil leaves", "1 cup cooked rice"],
     "steps": [
         "Heat oil in a pan over high heat, add garlic and chilies, and sauté for 30 seconds.",
         "Add ground chicken or tofu and cook until browned.",
         "Stir in soy sauce, fish sauce, oyster sauce, and sugar. Mix well.",
         "Add fresh basil leaves and stir until wilted.",
         "Serve over hot rice and enjoy!"
     ]},
     {"name": "Mexican Chili con Carne", "intro": "Spicy and hearty! Let's cook Mexican Chili con Carne!",
     "ingredients": ["1 lb ground beef", "1 tbsp olive oil", "1 onion (chopped)", "2 cloves garlic (minced)", "1 can (14 oz) diced tomatoes", "1 can (14 oz) kidney beans", "1 tbsp chili powder", "1 tsp cumin", "1/2 tsp paprika", "Salt and pepper to taste", "1 cup beef broth"],
     "steps": [
         "Heat oil in a pot and sauté onion and garlic until soft.",
         "Add ground beef and cook until browned.",
         "Stir in tomatoes, kidney beans, chili powder, cumin, paprika, salt, and pepper.",
         "Pour in beef broth and let simmer for 30 minutes.",
         "Serve hot with rice or cornbread!"
     ]},
     {"name": "Italian Bruschetta", "intro": "Fresh and delicious! Let's make Italian Bruschetta!",
     "ingredients": ["1 baguette (sliced)", "2 tbsp olive oil", "3 tomatoes (diced)", "2 cloves garlic (minced)", "1/4 cup fresh basil (chopped)", "1 tbsp balsamic vinegar", "Salt and pepper to taste"],
     "steps": [
         "Toast the baguette slices until golden and crispy.",
         "Mix tomatoes, garlic, basil, balsamic vinegar, salt, and pepper in a bowl.",
         "Spoon the mixture onto the toasted bread.",
         "Drizzle with olive oil and serve immediately!"
     ]},
     {"name": "Greek Gyro", "intro": "A classic Greek favorite! Let's make a Gyro!",
     "ingredients": ["1 lb lamb or chicken (sliced)", "1/4 cup olive oil", "2 cloves garlic (minced)", "1 tsp oregano", "1/2 tsp paprika", "Salt and pepper to taste", "Pita bread", "1/2 cup tzatziki sauce", "1/2 cup lettuce (shredded)", "1 tomato (sliced)"],
     "steps": [
         "Marinate the meat with olive oil, garlic, oregano, paprika, salt, and pepper for at least 1 hour.",
         "Grill or pan-fry the meat until fully cooked.",
         "Warm the pita bread and layer with tzatziki, meat, lettuce, and tomato.",
         "Wrap it up and enjoy your Greek Gyro!"
     ]},
     {"name": "Japanese Teriyaki Chicken", "intro": "Sweet and savory! Let's make Japanese Teriyaki Chicken!",
     "ingredients": ["2 boneless chicken thighs", "1/4 cup soy sauce", "2 tbsp mirin", "1 tbsp sugar", "1 tbsp sake", "1 tsp grated ginger", "1 tsp sesame seeds", "1 green onion (sliced)", "Steamed rice for serving"],
     "steps": [
         "Mix soy sauce, mirin, sugar, sake, and ginger in a bowl.",
         "Marinate the chicken in the sauce for at least 30 minutes.",
         "Heat a pan over medium heat and cook the chicken until browned.",
         "Pour in the remaining marinade and simmer until thickened.",
         "Slice the chicken, sprinkle with sesame seeds and green onions, and serve over rice."
     ]},
    {"name": "Indian Butter Chicken", "intro": "Rich and creamy! Let's make Indian Butter Chicken!",
     "ingredients": ["1 lb chicken (cubed)", "1/2 cup yogurt", "1 tbsp garam masala", "1 tsp turmeric", "1 tsp cumin", "2 tbsp butter", "1 onion (chopped)", "2 cloves garlic (minced)", "1 tbsp ginger (grated)", "1 can (14 oz) tomato puree", "1/2 cup heavy cream", "Salt and pepper to taste"],
     "steps": [
         "Marinate the chicken in yogurt, garam masala, turmeric, and cumin for 1 hour.",
         "Heat butter in a pan and sauté onion, garlic, and ginger until fragrant.",
         "Add the marinated chicken and cook until browned.",
         "Stir in the tomato puree and simmer for 15 minutes.",
         "Pour in heavy cream, mix well, and serve with rice or naan."
     ]},
    {"name": "Turkish Gozleme", "intro": "Crispy and delicious! Let's make Turkish Gozleme!",
     "ingredients": ["2 cups all-purpose flour", "1/2 cup water", "1/2 tsp salt", "1/2 cup feta cheese", "1/2 cup spinach (chopped)", "1 tbsp olive oil"],
     "steps": [
         "Mix flour, water, and salt to form a dough and let rest for 30 minutes.",
         "Roll out the dough into thin circles.",
         "Fill one side with feta and spinach, then fold over and seal.",
         "Heat a pan with olive oil and cook each side until golden brown.",
         "Serve hot and enjoy!"
     ]},
    {"name": "Brazilian Churrasco", "intro": "Grilled to perfection! Let's make Brazilian Churrasco!",
     "ingredients": ["2 lbs beef steak", "2 tbsp coarse salt", "1 tbsp black pepper", "1 tbsp olive oil"],
     "steps": [
         "Rub the steak with salt, pepper, and olive oil.",
         "Grill over high heat for 4-5 minutes per side until desired doneness.",
         "Rest for a few minutes, slice, and serve hot."
     ]},
    {"name": "Moroccan Chicken Tagine", "intro": "Aromatic and flavorful! Let's make Moroccan Chicken Tagine!",
     "ingredients": ["1 lb chicken thighs", "1 onion (sliced)", "2 cloves garlic (minced)", "1 tsp ground cumin", "1 tsp ground cinnamon", "1/2 tsp turmeric", "1 can (14 oz) diced tomatoes", "1/2 cup chicken broth", "1/4 cup dried apricots", "Salt and pepper to taste"],
     "steps": [
         "Heat oil in a pot and sauté onion and garlic until soft.",
         "Add chicken and brown on all sides.",
         "Stir in cumin, cinnamon, turmeric, tomatoes, and broth.",
         "Simmer for 40 minutes, then add dried apricots and cook for another 10 minutes.",
         "Serve with couscous and enjoy!"
     ]},
    {"name": "French Onion Soup", "intro": "A comforting classic! Let's make French Onion Soup!",
     "ingredients": ["4 large onions (thinly sliced)", "2 tbsp butter", "1 tbsp olive oil", "1 tsp sugar", "1/2 tsp salt", "4 cups beef broth", "1/2 cup white wine", "1 tsp thyme", "1 baguette (sliced)", "1 cup grated Gruyère cheese"],
     "steps": [
         "Heat butter and olive oil in a pot over medium heat.",
         "Add onions, sugar, and salt, and cook until caramelized (about 30 minutes).",
         "Pour in white wine and let it reduce for a few minutes.",
         "Add beef broth and thyme, and let simmer for 20 minutes.",
         "Toast baguette slices until golden brown.",
         "Ladle soup into oven-safe bowls, top with toasted baguette slices and Gruyère cheese.",
         "Broil in the oven until the cheese is melted and bubbly.",
         "Serve hot and enjoy your delicious French Onion Soup!"
     ]},
    
    # Dessert Dishes (50)

    {"name": "Chocolate Lava Cake", "intro": "Dessert alert! Chocolate Lava Cake time!",
     "ingredients": ["100g dark chocolate (70% cocoa)", "50g unsalted butter or coconut oil", "1/4 cup granulated sugar", "2 large eggs or 2 flax eggs (2 tbsp flax + 6 tbsp water)", "2 tbsp all-purpose flour", "1 tsp vanilla extract", "1/4 tsp salt", "1 tbsp cocoa powder (for dusting)", "1/4 cup powdered sugar", "Optional: 1/4 cup whipped cream or vegan cream", "1 tbsp chocolate chips"],
     "steps": [
         "Preheat your oven to 200°C and grease 4 ramekins with butter or oil—ready for lava!",
         "If using flax eggs, mix 2 tbsp ground flaxseed with 6 tbsp water—let it sit for 5 minutes!",
         "Chop the chocolate and melt it with the butter in a double boiler—stir until silky smooth!",
         "Remove from heat, stir in the sugar and vanilla—keep it moving!",
         "Add the eggs or flax eggs one at a time, whisking well—smooth batter time!",
         "Sift in the flour and salt, fold gently with a spatula—don’t overmix!",
         "Divide the batter into the ramekins—fill ‘em 3/4 full for that gooey center!",
         "Bake for 10-12 minutes until the edges are set but the middle’s soft—watch closely!",
         "Cool for 2 minutes, run a knife around the edges, invert onto plates—careful, hot!",
         "Dust with cocoa and powdered sugar, top with cream and chips if using—lava love awaits!"
     ]},
    {"name": "Mango Sticky Rice", "intro": "Tropical treat! Let’s make Mango Sticky Rice!",
     "ingredients": ["1 cup glutinous sticky rice", "1 can (14 oz) coconut milk", "1/4 cup granulated sugar", "1/2 tsp salt", "2 ripe mangoes (peeled and sliced)", "1 tsp sesame seeds (toasted)", "1 tbsp coconut cream (for topping)", "1 tsp cornstarch", "1/4 cup water", "1 pandan leaf (optional)", "1 tbsp shredded coconut (toasted)"],
     "steps": [
         "Rinse the sticky rice under cold water 3-4 times until clear—get that starch out!",
         "Soak the rice in water for 30 minutes—or overnight for best results!",
         "Drain and steam the rice in a steamer for 20-25 minutes until soft—check it!",
         "In a saucepan, heat the coconut milk over medium—don’t let it boil yet!",
         "Stir in the sugar, salt, and pandan leaf if using—dissolve everything!",
         "Mix cornstarch with water, stir into the coconut milk—thicken it for 2-3 minutes!",
         "Reserve half the sauce, mix the cooked rice into the other half—stir gently!",
         "Let the rice sit for 10 minutes to soak—cover it up!",
         "Scoop onto plates, add mango slices, drizzle with reserved sauce, sprinkle sesame and coconut—tropical yum!"
     ]},
    {"name": "Lemon Blueberry Muffins", "intro": "Muffin magic! Time for Lemon Blueberry Muffins!",
     "ingredients": ["1.5 cups all-purpose flour", "1 tsp baking powder", "1/2 tsp baking soda", "1/4 tsp salt", "1/2 cup granulated sugar", "1 lemon (zested and juiced)", "1/3 cup unsalted butter or coconut oil (melted)", "1 large egg or 1 flax egg (1 tbsp flax + 3 tbsp water)", "3/4 cup milk or almond milk", "1 cup fresh or frozen blueberries", "1 tsp vanilla extract", "1 tbsp coarse sugar (for topping)", "1/4 cup powdered sugar (for glaze)"],
     "steps": [
         "Preheat your oven to 180°C and line a muffin tin with 12 liners—baking time!",
         "If using a flax egg, mix 1 tbsp flax with 3 tbsp water—let it sit for 5 minutes!",
         "In a large bowl, whisk flour, baking powder, baking soda, and salt—dry mix done!",
         "In another bowl, rub the sugar and lemon zest together—release that citrus vibe!",
         "Add melted butter or oil, egg or flax egg, milk, lemon juice, and vanilla—whisk smooth!",
         "Pour wet into dry, stir gently until just combined—lumps are fine!",
         "Fold in the blueberries—don’t crush ‘em, keep ‘em whole!",
         "Scoop into liners, fill 3/4 full, sprinkle with coarse sugar—bake for 18-22 minutes until golden!",
         "Cool for 5 minutes in the tin, then move to a rack—mix powdered sugar with a splash of lemon juice for a glaze!",
         "Drizzle glaze over cooled muffins—lemony blueberry bliss!"
     ]},
    {"name": "Churros", "intro": "Sugar rush! Let’s fry some Churros!",
     "ingredients": ["1 cup water", "2 tbsp unsalted butter or vegan butter", "1 tbsp granulated sugar", "1/4 tsp salt", "1 cup all-purpose flour", "1 tsp vanilla extract", "1 large egg or 1 flax egg (1 tbsp flax + 3 tbsp water)", "Vegetable oil for frying", "1/2 cup sugar (for coating)", "1 tsp ground cinnamon", "1/4 cup chocolate sauce (for dipping)", "1 tbsp powdered sugar (optional)"],
     "steps": [
         "In a saucepan, heat water, butter, sugar, and salt over medium—bring to a boil!",
         "Remove from heat, stir in flour and vanilla—mix until a dough forms!",
         "If using a flax egg, mix 1 tbsp flax with 3 tbsp water—let sit for 5 minutes!",
         "Add the egg or flax egg to the dough—stir until smooth and thick!",
         "Heat 2 inches of oil in a deep skillet to 175°C—get it hot for frying!",
         "Spoon the dough into a piping bag with a star tip—pipe 4-inch strips into the oil!",
         "Fry for 2-3 minutes per side until golden—work in batches, don’t crowd!",
         "Drain on paper towels, mix sugar and cinnamon, roll warm churros in it—coat ‘em well!",
         "Dust with powdered sugar if using, serve with chocolate sauce—churro party time!"
     ]},
    {"name": "Baklava", "intro": "Sticky yum! Time for Baklava!",
     "ingredients": ["1 pack (16 oz) phyllo dough (thawed)", "1 cup unsalted butter or vegan butter (melted)", "1 cup walnuts (chopped)", "1 cup pistachios (chopped)", "1/2 cup sugar", "1 tsp ground cinnamon", "1/2 tsp ground cloves", "1 cup water", "1 cup honey", "1/2 cup granulated sugar (for syrup)", "1 tbsp lemon juice", "1 tsp vanilla extract", "1 tbsp rosewater (optional)"],
     "steps": [
         "Preheat your oven to 180°C—grease a 9x13-inch baking dish!",
         "Mix the walnuts, pistachios, 1/2 cup sugar, cinnamon, and cloves—nutty filling ready!",
         "Lay a phyllo sheet in the dish, brush with melted butter—repeat for 8 layers!",
         "Sprinkle a thin layer of nut mix over the phyllo—cover with 2 more sheets, brush with butter!",
         "Repeat layers—nuts, 2 sheets, butter—until all nuts are used, top with 8 buttered sheets!",
         "Cut into diamonds with a sharp knife—bake for 40-45 minutes until golden!",
         "In a saucepan, heat water, honey, 1/2 cup sugar, lemon juice, vanilla, and rosewater—simmer for 10 minutes!",
         "Pour the hot syrup over the baked baklava—let it soak for at least 2 hours!",
         "Serve sticky and sweet—baklava bliss achieved!"
     ]},
    {"name": "Tiramisu", "intro": "Coffee vibes! Let’s whip up Tiramisu!",
     "ingredients": ["200g mascarpone or vegan cream cheese", "1 cup strong coffee (cooled)", "1 pack (7 oz) ladyfingers", "1/2 cup granulated sugar", "2 large eggs or 1/2 cup aquafaba (whipped)", "1/4 cup coffee liqueur (optional)", "1 tsp vanilla extract", "1/4 tsp salt", "1/4 cup cocoa powder (for dusting)", "1 cup heavy cream or vegan cream (whipped)", "1 tbsp powdered sugar", "1 tbsp chocolate shavings"],
     "steps": [
         "Brew the coffee and let it cool—mix with coffee liqueur if using!",
         "In a bowl, beat the eggs or aquafaba with sugar until thick—about 5 minutes!",
         "Add mascarpone, vanilla, and salt—mix until smooth and creamy!",
         "Whip the cream with powdered sugar until stiff peaks form—fold into the mascarpone mix!",
         "Dip each ladyfinger into the coffee briefly—don’t soak, just a quick dip!",
         "Lay half the ladyfingers in a 9x9-inch dish—spread half the cream mix over them!",
         "Repeat with another layer of ladyfingers and cream—smooth the top!",
         "Chill in the fridge for 4 hours—let it set up nicely!",
         "Dust with cocoa powder, sprinkle with chocolate shavings, and serve—tiramisu heaven!"
     ]},
     {"name": "Apple Crumble", "intro": "Warm and comforting Apple Crumble!",
     "ingredients": ["6-8 medium apples (peeled and sliced)", "1/2 cup granulated sugar", "2 tbsp all-purpose flour", "1 tsp cinnamon", "1/4 tsp nutmeg", "1/4 tsp salt", "1/2 cup rolled oats", "1/2 cup brown sugar", "1/2 cup cold butter (cut into small pieces)"],
     "steps": [
         "Preheat oven to 375°F (190°C).",
         "Mix sliced apples with granulated sugar, flour, cinnamon, nutmeg, and salt.",
         "Transfer apple mixture to a baking dish.",
         "Combine oats, brown sugar, and cold butter until crumbly.",
         "Spread crumble mixture evenly over the apples.",
         "Bake for 35-40 minutes or until golden brown."
     ]},
    {"name": "Crème Brûlée", "intro": "Rich and creamy Crème Brûlée!",
     "ingredients": ["2 cups heavy cream", "1 cup granulated sugar", "1/2 cup whole milk", "1/4 cup granulated sugar (for caramelizing)", "1 tsp vanilla extract", "3 large egg yolks"],
     "steps": [
         "Preheat oven to 300°F (150°C).",
         "Whisk cream, sugar, milk, and vanilla in a saucepan.",
         "Cook over medium heat until sugar dissolves.",
         "In a separate bowl, whisk egg yolks.",
         "Temper egg yolks with the warm cream mixture.",
         "Pour into ramekins.",
         "Bake in a water bath for 25-30 minutes.",
         "Chill in the fridge.",
         "Sprinkle sugar on top and caramelize with a torch."
     ]},
    {"name": "Chocolate Brownie", "intro": "Fudgy and decadent Chocolate Brownie!",
     "ingredients": ["1 cup unsalted butter (melted)", "2 cups sugar", "4 large eggs", "1/2 cup unsweetened cocoa powder", "1 tsp vanilla extract", "1 1/4 cups all-purpose flour", "1 tsp salt", "1 cup semi-sweet chocolate chips", "Optional: nuts or espresso powder"],
     "steps": [
         "Preheat oven to 350°F (175°C).",
         "Grease an 8-inch square baking pan.",
         "Whisk together melted butter, sugar, eggs, cocoa powder, and vanilla.",
         "Add flour and salt—mix until just combined.",
         "Stir in chocolate chips and optional nuts or espresso powder.",
         "Pour into the prepared pan.",
         "Bake for 25-30 minutes or until a toothpick comes out with a few moist crumbs.",
         "Let cool completely before cutting into squares."
     ]},
    {"name": "Strawberry Shortcake", "intro": "Sweet and refreshing Strawberry Shortcake!",
     "ingredients": ["2 cups sliced strawberries", "1 cup granulated sugar", "2 cups all-purpose flour", "2 tsp baking powder", "1 tsp salt", "1/2 cup cold butter (cut into small pieces)", "3/4 cup heavy cream or buttermilk", "2 large eggs", "1 tsp vanilla extract", "Whipped cream or vanilla ice cream"],
     "steps": [
         "Preheat oven to 375°F (190°C).",
         "Mix sliced strawberries with granulated sugar—let it sit for 15 minutes.",
         "Combine flour, baking powder, and salt.",
         "Add cold butter and mix until crumbly.",
         "Stir in cream, eggs, and vanilla—mix until a dough forms.",
         "Drop by spoonfuls onto a baking sheet.",
         "Bake for 18-20 minutes or until golden brown.",
         "Split shortcakes in half horizontally.",
         "Fill with sweetened strawberries and top with whipped cream or ice cream."
     ]},
    {"name": "Chocolate Chip Cookie", "intro": "Classic and chewy Chocolate Chip Cookies!",
     "ingredients": ["2 1/4 cups all-purpose flour", "1 tsp baking soda", "1 tsp salt", "1 cup unsalted butter (softened)", "3/4 cup granulated sugar", "3/4 cup brown sugar", "2 large eggs", "2 tsp vanilla extract", "2 cups semi-sweet chocolate chips"],
     "steps": [
         "Preheat oven to 375°F (190°C).",
         "Whisk together flour, baking soda, and salt.",
         "Cream butter and sugars until light and fluffy.",
         "Beat in eggs and vanilla.",
         "Gradually mix in the flour mixture.",
         "Stir in chocolate chips.",
         "Scoop tablespoon-sized balls onto a baking sheet.",
         "Bake for 10-12 minutes or until lightly golden."
     ]},
    {"name": "No-Bake Buckeye Cheesecake Bars",
     "intro": "Creamy cheesecake bars with a peanut butter and chocolate twist.",
     "ingredients": [
            "1 1/2 cups graham cracker crumbs",
            "1/4 cup granulated sugar",
            "1/2 cup melted butter",
            "16 oz cream cheese (softened)",
            "1/2 cup granulated sugar",
            "1/2 cup sour cream",
            "1 tsp vanilla extract",
            "1 cup powdered sugar",
            "1 cup peanut butter cups (chopped)",
            "1 cup chocolate chips"
        ],
        "steps": [
            "Combine graham cracker crumbs and sugar. Add melted butter and mix until well combined.",
            "Press mixture into a lined baking dish.",
            "Beat cream cheese until smooth. Add granulated sugar, sour cream, and vanilla.",
            "Pour cheesecake mixture over crust.",
            "Refrigerate until set.",
            "Melt chocolate chips and spread over the top.",
            "Sprinkle with chopped peanut butter cups."
        ]
    },
    {"name": "Aperol Spritz Trifles",
     "intro": "A refreshing Italian-inspired dessert perfect for summer.",
     "ingredients": [
            "1 cup ladyfingers",
            "1 cup Aperol",
            "1 cup Prosecco",
            "1 cup whipped cream",
            "1 cup mixed berries",
            "1 cup mascarpone cheese",
            "1/4 cup granulated sugar"
        ],
        "steps": [
            "Dip ladyfingers in Aperol and Prosecco mixture.",
            "Layer ladyfingers, whipped cream, and mixed berries in glasses.",
            "Mix mascarpone with granulated sugar and layer on top.",
            "Chill until ready to serve."
        ]
    },
    { "name": "Drumstick Pie",
      "intro": "A creamy pie inspired by the classic ice cream treat.",
      "ingredients": [
            "1 cup graham cracker crumbs",
            "1/4 cup granulated sugar",
            "1/2 cup melted butter",
            "1 cup heavy cream",
            "1 cup powdered sugar",
            "1 tsp vanilla extract",
            "1 cup chocolate chips",
            "1 cup chopped peanuts"
        ],
        "steps": [
            "Combine graham cracker crumbs and sugar. Add melted butter and mix until well combined.",
            "Press mixture into a lined baking dish.",
            "Beat heavy cream until stiff peaks form. Add powdered sugar and vanilla.",
            "Pour whipped cream over crust.",
            "Melt chocolate chips and drizzle over the top.",
            "Sprinkle with chopped peanuts."
        ]
    },
    {"name": "Hostess Sheet Cake",
     "intro": "A classic sheet cake with a creamy filling and chocolate coating.",
     "ingredients": [
            "2 cups all-purpose flour",
            "1 tsp baking powder",
            "1 tsp salt",
            "1 cup granulated sugar",
            "1/2 cup unsalted butter (softened)",
            "2 large eggs",
            "2 tsp vanilla extract",
            "1 cup whole milk",
            "1 cup powdered sugar",
            "1 cup chocolate chips"
        ],
        "steps": [
            "Preheat oven to 350°F (180°C).",
            "Whisk together flour, baking powder, and salt.",
            "Beat sugar and butter until light. Add eggs one at a time.",
            "Gradually mix in flour mixture and milk.",
            "Pour into a lined baking sheet.",
            "Bake until a toothpick comes out clean.",
            "Mix powdered sugar with a little milk to make a glaze.",
            "Melt chocolate chips and spread over the top."
        ]
    },
    {"name": "Fruit Tart",
    "intro": "A colorful and elegant dessert perfect for any occasion.",
    "ingredients": [
            "1 sheet puff pastry (thawed)",
            "1 cup mixed berries",
            "1 cup sliced peaches",
            "1 cup sliced kiwi",
            "1/4 cup granulated sugar",
            "1 tsp vanilla extract"
        ],
        "steps": [
            "Roll out puff pastry and place on a baking sheet.",
            "Arrange mixed berries, peaches, and kiwi in a pattern.",
            "Sprinkle with granulated sugar and vanilla extract.",
            "Fold edges of pastry to form a crust.",
            "Bake at 400°F (200°C) until golden."
        ]
    },
    {"name": "Key Lime Pie Mousse",
    "intro": "A light and tangy dessert perfect for spring.",
    "ingredients": [
            "1 cup heavy cream",
            "1 cup powdered sugar",
            "1/2 cup key lime juice",
            "1/2 cup unsalted butter (softened)",
            "1 tsp vanilla extract",
            "1 cup whipped cream"
        ],
        "steps": [
            "Beat heavy cream until stiff peaks form. Set aside.",
            "Mix powdered sugar, key lime juice, and softened butter until smooth.",
            "Add vanilla extract and mix well.",
            "Fold whipped cream into the key lime mixture.",
            "Chill until set."
        ]
    },
    {"name": "Snickerdoodle Blondies",
    "intro": "Soft and chewy blondies with a cinnamon sugar crust.",
    "ingredients": [
            "2 1/4 cups all-purpose flour",
            "1 tsp baking powder",
            "1 tsp salt",
            "1 cup granulated sugar",
            "1/2 cup unsalted butter (softened)",
            "2 large eggs",
            "2 tsp vanilla extract",
            "3 tsp ground cinnamon",
            "1/4 cup granulated sugar (for topping)"
        ],
        "steps": [
            "Preheat oven to 350°F (180°C).",
            "Whisk together flour, baking powder, and salt.",
            "Beat sugar and butter until light. Add eggs one at a time.",
            "Gradually mix in flour mixture and vanilla.",
            "Mix cinnamon and sugar for topping.",
            "Pour batter into a lined baking dish.",
            "Sprinkle cinnamon sugar mixture on top.",
            "Bake until a toothpick comes out clean."
        ]
    },
    {"name": "Banana Pudding Pops",
    "intro": "A fun twist on classic banana pudding.",
    "ingredients": [
            "4 ripe bananas",
            "1 cup vanilla pudding mix",
            "1 cup milk",
            "1/4 cup granulated sugar",
            "1/4 cup unsalted butter (melted)",
            "1 tsp vanilla extract",
            "1 cup whipped cream",
            "Popsicle sticks"
        ],
        "steps": [
            "Mash bananas in a bowl.",
            "Mix pudding mix, milk, sugar, melted butter, and vanilla extract.",
            "Combine pudding mixture with mashed bananas.",
            "Pour into popsicle molds.",
            "Freeze until solid.",
            "Dip tops in whipped cream before serving."
        ]
    },
    {"name": "Oreo Cookie Cake",
    "intro": "A moist cake filled with Oreo goodness.",
    "ingredients": [
            "2 cups all-purpose flour",
            "1 tsp baking powder",
            "1 tsp salt",
            "1 cup granulated sugar",
            "1/2 cup unsalted butter (softened)",
            "2 large eggs",
            "2 tsp vanilla extract",
            "1 cup whole milk",
            "1 cup crushed Oreos",
            "1 cup powdered sugar"
        ],
        "steps": [
            "Preheat oven to 350°F (180°C).",
            "Whisk together flour, baking powder, and salt.",
            "Beat sugar and butter until light. Add eggs one at a time.",
            "Gradually mix in flour mixture and milk.",
            "Stir in crushed Oreos.",
            "Pour into a lined round cake pan.",
            "Bake until a toothpick comes out clean.",
            "Mix powdered sugar with a little milk to make a glaze."
        ]
    },
    {"name": "Chocolate Pudding Pizza",
    "intro": "A fun dessert pizza with a chocolate twist.",
    "ingredients": [
            "1 package cookie dough (homemade or store-bought)",
            "1 cup chocolate pudding mix",
            "1 cup milk",
            "1/4 cup granulated sugar",
            "1/4 cup unsalted butter (melted)",
            "1 tsp vanilla extract",
            "1 cup whipped cream",
            "Chocolate chips or shavings"
        ],
        "steps": [
            "Preheat oven to 350°F (180°C).",
            "Roll out cookie dough and place on a baking sheet.",
            "Bake until lightly golden.",
            "Mix pudding mix, milk, sugar, melted butter, and vanilla extract.",
            "Spread pudding mixture over the cooled cookie crust.",
            "Top with whipped cream and chocolate chips or shavings."
        ]
    },
    {"name": "Brownie Mocha Trifle",
    "intro": "A layered dessert perfect for coffee lovers.",
    "ingredients": [
            "1 package brownie mix",
            "1 cup strong brewed coffee",
            "1 cup whipped cream",
            "1 cup chocolate shavings",
            "1 cup mocha syrup"
        ],
        "steps": [
            "Prepare brownies according to package instructions.",
            "Cut brownies into cubes.",
            "Layer brownies, whipped cream, and chocolate shavings in glasses.",
            "Drizzle with mocha syrup between layers."
        ]
    },
    {"name": "Pecan Pie Bars",
    "intro": "A twist on the classic pecan pie in bar form.",
    "ingredients": [
            "2 cups all-purpose flour",
            "1 tsp baking powder",
            "1 tsp salt",
            "1 cup granulated sugar",
            "1/2 cup unsalted butter (softened)",
            "2 large eggs",
            "2 tsp vanilla extract",
            "1 cup chopped pecans",
            "1 cup caramel sauce"
        ],
        "steps": [
            "Preheat oven to 350°F (180°C).",
            "Whisk together flour, baking powder, and salt.",
            "Beat sugar and butter until light. Add eggs one at a time.",
            "Gradually mix in flour mixture and vanilla.",
            "Stir in chopped pecans.",
            "Pour into a lined baking dish.",
            "Bake until a toothpick comes out clean.",
            "Drizzle with caramel sauce before serving."
        ]
    },
    {"name": "Cherry Chewbilees",
    "intro": "A fruity and chewy cookie perfect for snacking.",
    "ingredients": [
            "2 1/4 cups all-purpose flour",
            "1 tsp baking soda",
            "1 tsp salt",
            "1 cup granulated sugar",
            "1/2 cup unsalted butter (softened)",
            "2 large eggs",
            "2 tsp vanilla extract",
            "1 cup dried cherries",
            "1 cup white chocolate chips"
        ],
        "steps": [
            "Preheat oven to 375°F (190°C).",
            "Whisk together flour, baking soda, and salt.",
            "Beat sugar and butter until light. Add eggs one at a time.",
            "Gradually mix in flour mixture and vanilla.",
            "Stir in dried cherries and white chocolate chips.",
            "Scoop tablespoon-sized balls onto a baking sheet.",
            "Bake for 10-12 minutes or until lightly golden."
        ]
    },
    {
        "name": "Chocolate Chiffon Cake",
        "intro": "A light and airy cake with a rich chocolate flavor.",
        "ingredients": [
            "2 1/4 cups all-purpose flour",
            "1 cup granulated sugar",
            "2 tsp baking powder",
            "1 tsp salt",
            "1/2 cup unsweetened cocoa powder",
            "1/2 cup vegetable oil",
            "4 large egg yolks",
            "4 large egg whites",
            "1 tsp vanilla extract"
        ],
        "steps": [
            "Preheat oven to 325°F (165°C).",
            "Whisk together flour, sugar, baking powder, and salt.",
            "Add cocoa powder and mix well.",
            "In a separate bowl, whisk together oil, egg yolks, and vanilla.",
            "Add egg yolk mixture to dry ingredients and mix until smooth.",
            "Beat egg whites until stiff peaks form.",
            "Fold egg whites into the batter.",
            "Pour into an ungreased tube pan.",
            "Bake until a toothpick comes out clean."
        ]
    },
    {
        "name": "Easy Ice Cream Sundae Dessert",
        "intro": "A simple yet indulgent sundae dessert perfect for gatherings.",
        "ingredients": [
            "1 pint vanilla ice cream",
            "1 cup hot fudge sauce",
            "1 cup caramel sauce",
            "1 cup whipped cream",
            "1 cup chopped nuts",
            "1 cup sprinkles",
            "1 cup maraschino cherries"
        ],
        "steps": [
            "Scoop ice cream into individual bowls.",
            "Drizzle with hot fudge and caramel sauces.",
            "Top with whipped cream, chopped nuts, sprinkles, and maraschino cherries."
        ]
    },
    {
        "name": "Chocolate Toffee Crunchies",
        "intro": "Crunchy cookies with a chocolate and toffee twist.",
        "ingredients": [
            "2 1/4 cups all-purpose flour",
            "1 tsp baking soda",
            "1 tsp salt",
            "1 cup granulated sugar",
            "1/2 cup unsalted butter (softened)",
            "2 large eggs",
            "2 tsp vanilla extract",
            "1 cup semi-sweet chocolate chips",
            "1 cup toffee bits"
        ],
        "steps": [
            "Preheat oven to 375°F (190°C).",
            "Whisk together flour, baking soda, and salt.",
            "Beat sugar and butter until light. Add eggs one at a time.",
            "Gradually mix in flour mixture and vanilla.",
            "Stir in chocolate chips and toffee bits.",
            "Scoop tablespoon-sized balls onto a baking sheet.",
            "Bake for 10-12 minutes or until lightly golden."
        ]
    },
    {
        "name": "Italian Wedding Cookies",
        "intro": "Soft and buttery cookies perfect for any occasion.",
        "ingredients": [
            "2 1/4 cups all-purpose flour",
            "1 tsp baking powder",
            "1 tsp salt",
            "1 cup granulated sugar",
            "1/2 cup unsalted butter (softened)",
            "2 large eggs",
            "2 tsp vanilla extract",
            "1 cup chopped walnuts",
            "1 cup powdered sugar"
        ],
        "steps": [
            "Preheat oven to 350°F (180°C).",
            "Whisk together flour, baking powder, and salt.",
            "Beat sugar and butter until light. Add eggs one at a time.",
            "Gradually mix in flour mixture and vanilla.",
            "Stir in chopped walnuts.",
            "Scoop tablespoon-sized balls onto a baking sheet.",
            "Bake for 10-12 minutes or until lightly golden.",
            "Roll in powdered sugar while still warm."
        ]
    },
    {
        "name": "Fudgy Macaroon Bars",
        "intro": "A twist on traditional macaroons with a fudgy center.",
        "ingredients": [
            "1 cup unsweetened shredded coconut",
            "1 cup sweetened condensed milk",
            "1/4 cup unsalted butter (melted)",
            "2 large eggs",
            "1 tsp vanilla extract",
            "1 cup semi-sweet chocolate chips"
        ],
        "steps": [
            "Preheat oven to 350°F (180°C).",
            "Mix coconut, sweetened condensed milk, melted butter, eggs, and vanilla.",
            "Press mixture into a lined baking dish.",
            "Bake until lightly golden.",
            "Melt chocolate chips and spread over the top.",
            "Refrigerate until set."
        ]
    },
    {
        "name": "Hidden Mint Morsels",
        "intro": "A refreshing cookie with a hidden mint surprise.",
        "ingredients": [
            "2 1/4 cups all-purpose flour",
            "1 tsp baking soda",
            "1 tsp salt",
            "1 cup granulated sugar",
            "1/2 cup unsalted butter (softened)",
            "2 large eggs",
            "2 tsp vanilla extract",
            "1 cup semi-sweet chocolate chips",
            "1 cup mint chocolate chips"
        ],
        "steps": [
            "Preheat oven to 375°F (190°C).",
            "Whisk together flour, baking soda, and salt.",
            "Beat sugar and butter until light. Add eggs one at a time.",
            "Gradually mix in flour mixture and vanilla.",
            "Stir in chocolate chips.",
            "Scoop tablespoon-sized balls onto a baking sheet.",
            "Press a mint chocolate chip into the center of each cookie.",
            "Bake for 10-12 minutes or until lightly golden."
        ]
    },
    {
        "name": "Cranberry-Orange Bars",
        "intro": "A sweet and tangy bar dessert perfect for fall.",
        "ingredients": [
            "2 cups all-purpose flour",
            "1 tsp baking powder",
            "1 tsp salt",
            "1 cup granulated sugar",
            "1/2 cup unsalted butter (softened)",
            "2 large eggs",
            "2 tsp vanilla extract",
            "1 cup fresh or frozen cranberries",
            "1 cup orange marmalade"
        ],
        "steps": [
            "Preheat oven to 350°F (180°C).",
            "Whisk together flour, baking powder, and salt.",
            "Beat sugar and butter until light. Add eggs one at a time.",
            "Gradually mix in flour mixture and vanilla.",
            "Stir in cranberries.",
            "Pour into a lined baking dish.",
            "Spread orange marmalade over the top.",
            "Bake until a toothpick comes out clean."
        ]
    },
    {
        "name": "Cashew Cookies",
        "intro": "Crunchy cookies with a nutty twist.",
        "ingredients": [
            "2 1/4 cups all-purpose flour",
            "1 tsp baking soda",
            "1 tsp salt",
            "1 cup granulated sugar",
            "1/2 cup unsalted butter (softened)",
            "2 large eggs",
            "2 tsp vanilla extract",
            "1 cup chopped cashews"
        ],
        "steps": [
            "Preheat oven to 375°F (190°C).",
            "Whisk together flour, baking soda, and salt.",
            "Beat sugar and butter until light. Add eggs one at a time.",
            "Gradually mix in flour mixture and vanilla.",
            "Stir in chopped cashews.",
            "Scoop tablespoon-sized balls onto a baking sheet.",
            "Bake for 10-12 minutes or until lightly golden."
        ]
    },
    {
        "name": "Peppermint Brownies",
        "intro": "Fudgy brownies with a refreshing peppermint twist.",
        "ingredients": [
            "1 cup unsalted butter (plus more for greasing)",
            "2 cups sugar",
            "4 large eggs",
            "1/2 cup unsweetened cocoa powder",
            "1 tsp vanilla extract",
            "1 1/4 cups all-purpose flour",
            "1 tsp salt",
            "1 cup semi-sweet chocolate chips",
            "1 cup crushed peppermint candies"
        ],
        "steps": [
            "Preheat oven to 350°F (180°C).",
            "Grease an 8-inch square baking pan.",
            "Melt butter and sugar in a saucepan.",
            "Remove from heat and stir in cocoa powder.",
            "Let cool slightly, then stir in eggs one at a time.",
            "Add vanilla extract and mix well.",
            "Whisk in flour and salt.",
            "Stir in chocolate chips.",
            "Pour into prepared pan.",
            "Sprinkle crushed peppermint candies on top.",
            "Bake until a toothpick comes out with a few moist crumbs."
        ]
    },
    {
        "name": "Applesauce Cake",
        "intro": "A moist and flavorful cake perfect for fall.",
        "ingredients": [
            "2 cups all-purpose flour",
            "1 tsp baking powder",
            "1 tsp salt",
            "1 cup granulated sugar",
            "1/2 cup unsalted butter (softened)",
            "2 large eggs",
            "2 tsp vanilla extract",
            "1 cup applesauce",
            "1 cup chopped walnuts"
        ],
        "steps": [
            "Preheat oven to 350°F (180°C).",
            "Whisk together flour, baking powder, and salt.",
            "Beat sugar and butter until light. Add eggs one at a time.",
            "Gradually mix in flour mixture and vanilla.",
            "Stir in applesauce and chopped walnuts.",
            "Pour into a lined round cake pan.",
            "Bake until a toothpick comes out clean."
        ]
    },
    {
        "name": "White Chocolate Macadamia Nut Cookies",
        "intro": "Crunchy cookies with a sweet white chocolate twist.",
        "ingredients": [
            "2 1/4 cups all-purpose flour",
            "1 tsp baking soda",
            "1 tsp salt",
            "1 cup granulated sugar",
            "1/2 cup unsalted butter (softened)",
            "2 large eggs",
            "2 tsp vanilla extract",
            "1 cup chopped macadamia nuts",
            "1 cup white chocolate chips"
        ],
        "steps": [
            "Preheat oven to 375°F (190°C).",
            "Whisk together flour, baking soda, and salt.",
            "Beat sugar and butter until light. Add eggs one at a time.",
            "Gradually mix in flour mixture and vanilla.",
            "Stir in chopped macadamia nuts and white chocolate chips.",
            "Scoop tablespoon-sized balls onto a baking sheet.",
            "Bake for 10-12 minutes or until lightly golden."
        ]
    },
    {
    "name": "Fudgy Brownie Recipe",
    "intro": "A classic fudgy brownie recipe perfect for any occasion.",
    "ingredients": [
        "1 cup unsalted butter (plus more for greasing)",
        "2 cups sugar",
        "4 large eggs",
        "1/2 cup unsweetened cocoa powder",
        "1 tsp vanilla extract",
        "1 1/4 cups all-purpose flour",
        "1 tsp salt",
        "1 cup semi-sweet chocolate chips"
    ],
    "steps": [
        "Preheat oven to 350°F (180°C).",
        "Grease an 8-inch square baking pan.",
        "Melt butter and sugar in a saucepan.",
        "Remove from heat and stir in cocoa powder.",
        "Let cool slightly, then stir in eggs one at a time.",
        "Add vanilla extract and mix well.",
        "Whisk in flour and salt.",
        "Stir in chocolate chips.",
        "Pour into prepared pan.",
        "Bake until a toothpick comes out with a few moist crumbs."
    ]
},
    {
    "name": "Dump Cake",
    "intro": "A simple and delicious dessert perfect for gatherings.",
    "ingredients": [
        "1 can of fruit (such as cherry or blueberry)",
        "1 box of cake mix",
        "1/2 cup unsalted butter (melted)",
        "1 cup chopped nuts (optional)"
    ],
    "steps": [
        "Preheat oven to 350°F (180°C).",
        "Pour fruit into a 9x13 inch baking dish.",
        "Sprinkle cake mix evenly over the fruit.",
        "Drizzle melted butter over the cake mix.",
        "Sprinkle chopped nuts on top if using.",
        "Bake until the top is golden brown."
    ]
},
{
    "name": "Poke Cake",
    "intro": "A moist and flavorful cake with a sweet surprise.",
    "ingredients": [
        "1 box of white cake mix",
        "1 cup sweetened condensed milk",
        "1 cup whipped cream",
        "1 cup mixed berries"
    ],
    "steps": [
        "Prepare cake according to package instructions.",
        "Let cake cool completely.",
        "Poke holes in the top of the cake with a skewer.",
        "Pour sweetened condensed milk over the cake.",
        "Top with whipped cream and mixed berries."
    ]
},
{
    "name": "No Bake Oreo Dessert",
    "intro": "A creamy and easy dessert perfect for Oreo lovers.",
    "ingredients": [
        "1 package of Oreos",
        "1 cup cream cheese (softened)",
        "1 cup powdered sugar",
        "1 cup whipped cream",
        "1 cup chocolate chips"
    ],
    "steps": [
        "Crush Oreos in a food processor.",
        "Mix cream cheese and powdered sugar until smooth.",
        "Fold in whipped cream.",
        "Layer crushed Oreos, cream cheese mixture, and chocolate chips in a dish.",
        "Refrigerate until set."
    ]
},
{
    "name": "Blueberry Lush",
    "intro": "A layered dessert perfect for spring.",
    "ingredients": [
        "1 cup graham cracker crumbs",
        "1/4 cup granulated sugar",
        "1/2 cup melted butter",
        "1 cup cream cheese (softened)",
        "1 cup powdered sugar",
        "1 cup whipped cream",
        "1 cup fresh blueberries"
    ],
    "steps": [
        "Combine graham cracker crumbs and sugar. Add melted butter and mix until well combined.",
        "Press mixture into a lined baking dish.",
        "Beat cream cheese until smooth. Add powdered sugar and mix well.",
        "Fold in whipped cream.",
        "Layer cream cheese mixture, blueberries, and whipped cream in the dish.",
        "Refrigerate until set."
    ]
},
{
    "name": "Key Lime Pie Cheesecake Dip",
    "intro": "A tangy and creamy dip perfect for parties.",
    "ingredients": [
        "1 cup cream cheese (softened)",
        "1 cup powdered sugar",
        "1/2 cup key lime juice",
        "1/4 cup unsalted butter (softened)",
        "1 tsp vanilla extract",
        "1 cup whipped cream"
    ],
    "steps": [
        "Beat cream cheese until smooth. Add powdered sugar and mix well.",
        "Add key lime juice and softened butter. Mix until combined.",
        "Add vanilla extract and mix well.",
        "Fold in whipped cream.",
        "Serve with graham crackers or cookies."
    ]
},
{
    "name": "Chocolate Cookies with Peanut Butter Chips",
    "intro": "Soft and chewy cookies with a peanut butter twist.",
    "ingredients": [
        "2 1/4 cups all-purpose flour",
        "1 tsp baking soda",
        "1 tsp salt",
        "1 cup granulated sugar",
        "1/2 cup unsalted butter (softened)",
        "2 large eggs",
        "2 tsp vanilla extract",
        "1 cup semi-sweet chocolate chips",
        "1 cup peanut butter chips"
    ],
    "steps": [
        "Preheat oven to 375°F (190°C).",
        "Whisk together flour, baking soda, and salt.",
        "Beat sugar and butter until light. Add eggs one at a time.",
        "Gradually mix in flour mixture and vanilla.",
        "Stir in chocolate chips and peanut butter chips.",
        "Scoop tablespoon-sized balls onto a baking sheet.",
        "Bake for 10-12 minutes or until lightly golden."
    ]
},
{
    "name": "Cranberry Sugar Cookies",
    "intro": "Soft and flavorful cookies perfect for the holidays.",
    "ingredients": [
        "2 1/4 cups all-purpose flour",
        "1 tsp baking powder",
        "1 tsp salt",
        "1 cup granulated sugar",
        "1/2 cup unsalted butter (softened)",
        "2 large eggs",
        "2 tsp vanilla extract",
        "1 cup dried cranberries"
    ],
    "steps": [
        "Preheat oven to 350°F (180°C).",
        "Whisk together flour, baking powder, and salt.",
        "Beat sugar and butter until light. Add eggs one at a time.",
        "Gradually mix in flour mixture and vanilla.",
        "Stir in dried cranberries.",
        "Scoop tablespoon-sized balls onto a baking sheet.",
        "Bake for 10-12 minutes or until lightly golden."
    ]
},
{
    "name": "Oatmeal Craisin Cookies",
    "intro": "Hearty cookies with a sweet and tangy twist.",
    "ingredients": [
        "2 1/4 cups all-purpose flour",
        "1 cup rolled oats",
        "1 tsp baking soda",
        "1 tsp salt",
        "1 cup granulated sugar",
        "1/2 cup unsalted butter (softened)",
        "2 large eggs",
        "2 tsp vanilla extract",
        "1 cup dried cranberries"
    ],
    "steps": [
        "Preheat oven to 375°F (190°C).",
        "Whisk together flour, oats, baking soda, and salt.",
        "Beat sugar and butter until light. Add eggs one at a time.",
        "Gradually mix in flour mixture and vanilla.",
        "Stir in dried cranberries.",
        "Scoop tablespoon-sized balls onto a baking sheet.",
        "Bake for 10-12 minutes or until lightly golden."
    ]
},
{
    "name": "Customizable Homemade Ice Cream Cake",
    "intro": "A fun and customizable dessert perfect for celebrations.",
    "ingredients": [
        "1 pint of your favorite ice cream",
        "1 cup crushed cookies or wafers",
        "1 cup whipped cream",
        "1 cup mixed toppings (such as sprinkles, nuts, or chocolate chips)"
    ],
    "steps": [
        "Scoop ice cream into a lined springform pan.",
        "Freeze until firm.",
        "Sprinkle crushed cookies or wafers over the top.",
        "Top with whipped cream and mixed toppings.",
        "Freeze until ready to serve."
    ]
},
{
    "name": "Chocolate Mousse",
    "intro": "A light and airy chocolate dessert perfect for any occasion.",
    "ingredients": [
        "8 oz dark chocolate (chopped)",
        "1 cup heavy cream",
        "1/2 cup granulated sugar",
        "2 large egg whites",
        "1 tsp vanilla extract"
    ],
    "steps": [
        "Melt chocolate in a double boiler.",
        "Beat heavy cream until stiff peaks form. Set aside.",
        "Beat egg whites until stiff peaks form.",
        "Add granulated sugar and vanilla to egg whites. Mix well.",
        "Fold egg whites into melted chocolate.",
        "Fold whipped cream into the chocolate mixture.",
        "Chill until set."
    ]
},
{
    "name": "Cinnamon Rolls",
    "intro": "Sweet and gooey pastries perfect for breakfast or dessert.",
    "ingredients": [
        "2 cups all-purpose flour",
        "2 tsp active dry yeast",
        "1 tsp salt",
        "1/4 cup granulated sugar",
        "1/2 cup warm water",
        "1/4 cup unsalted butter (melted)",
        "1/2 cup cinnamon sugar"
    ],
    "steps": [
        "Combine flour, yeast, salt, and sugar in a bowl.",
        "Add warm water and melted butter. Mix until a dough forms.",
        "Knead dough for 5 minutes.",
        "Roll out dough into a rectangle.",
        "Spread cinnamon sugar over the dough.",
        "Roll up the dough and cut into rounds.",
        "Place in a lined baking dish and let rise.",
        "Bake until golden."
    ]
},
{
    "name": "Phyllo Cakes",
    "intro": "Crispy and sweet pastries perfect for any occasion.",
    "ingredients": [
        "1 package phyllo dough (thawed)",
        "1/2 cup unsalted butter (melted)",
        "1 cup granulated sugar",
        "1 cup chopped nuts (optional)"
    ],
    "steps": [
        "Preheat oven to 350°F (180°C).",
        "Layer phyllo dough in a baking dish, brushing with melted butter between layers.",
        "Sprinkle granulated sugar and chopped nuts (if using) over the top.",
        "Bake until golden and crispy."
    ]
},
{
    "name": "Peach Cobbler",
    "intro": "A warm and comforting dessert perfect for summer.",
    "ingredients": [
        "3 cups sliced peaches",
        "1 cup granulated sugar",
        "1/4 cup all-purpose flour",
        "1 tsp cinnamon",
        "1/4 tsp nutmeg",
        "1/4 tsp salt",
        "1/2 cup unsalted butter (melted)",
        "1 cup biscuit or cobbler topping mix"
    ],
    "steps": [
        "Preheat oven to 375°F (190°C).",
        "Mix peaches, granulated sugar, flour, cinnamon, nutmeg, and salt in a bowl.",
        "Pour into a lined baking dish.",
        "Prepare biscuit or cobbler topping according to package instructions.",
        "Drop spoonfuls of topping over the peach mixture.",
        "Drizzle with melted butter.",
        "Bake until the topping is golden brown."
    ]
},
{
    "name": "Vanilla Cupcakes",
    "intro": "Classic and moist cupcakes perfect for any occasion.",
    "ingredients": [
        "1 1/2 cups all-purpose flour",
        "1 cup granulated sugar",
        "2 tsp baking powder",
        "1/2 tsp salt",
        "1/2 cup unsalted butter (softened)",
        "2 large eggs",
        "2 tsp vanilla extract",
        "1 cup whole milk"
    ],
    "steps": [
        "Preheat oven to 350°F (180°C).",
        "Line a muffin tin with cupcake liners.",
        "Whisk together flour, sugar, baking powder, and salt.",
        "Beat butter until creamy. Add eggs one at a time.",
        "Gradually mix in flour mixture and vanilla.",
        "Add milk and mix until smooth.",
        "Divide batter evenly among cupcake liners.",
        "Bake until a toothpick comes out clean.",
        "Let cool completely before frosting."
    ]
}
]

# Function to read a recipe aloud with error handling
def read_recipe(recipe):
    try:
        print(recipe["intro"])
        engine.say(recipe["intro"])
        engine.runAndWait()

        print("\nHere’s what you’ll need:")
        engine.say("Here’s what you’ll need:")
        engine.runAndWait()
        for ingredient in recipe["ingredients"]:
            print(f"- {ingredient}")
            engine.say(ingredient)
            engine.runAndWait()

        print("\nLet’s get cooking:")
        engine.say("Let’s get cooking:")
        engine.runAndWait()
        for i, step in enumerate(recipe["steps"], 1):
            print(f"Step {i}: {step}")
            engine.say(f"Step {i}: {step}")
            engine.runAndWait()

        print("All done! Enjoy your meal!")
        engine.say("All done! Enjoy your meal!")
        engine.runAndWait()
    except Exception as e:
        print(f"Oops, something went wrong: {e}")
        engine.say("Oops, something went wrong. Let’s try that again later!")
        engine.runAndWait()

# Main program: let user choose a recipe
print("Welcome to your Cooking Buddy! Pick a recipe:")

print("\nSavory Dishes (1-50):")
savory_recipes = recipes[:50]
for i, recipe in enumerate(savory_recipes, 1):
    print(f"{i}. {recipe['name']}")

print("\nDesserts (51-100):")
dessert_recipes = recipes[50:]
for i, recipe in enumerate(dessert_recipes, 51):
    print(f"{i}. {recipe['name']}")

try:
    choice = int(input("\nEnter the number of your recipe (1-100): "))
    if 1 <= choice <= 50:
        print(f"\nStarting {savory_recipes[choice - 1]['name']}...")
        read_recipe(savory_recipes[choice - 1])
    elif 51 <= choice <= 100:
        print(f"\nStarting {dessert_recipes[choice - 51]['name']}...")
        read_recipe(dessert_recipes[choice - 51])
    else:
        print("Oops, that’s not a valid choice! Try a number between 1 and 100.")
        engine.say("Oops, that’s not a valid choice! Try a number between 1 and 100.")
        engine.runAndWait()
except ValueError:
    print("Hey, enter a number, not words! Try again.")
    engine.say("Hey, enter a number, not words! Try again.")
    engine.runAndWait()


