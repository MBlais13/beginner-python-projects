import random
from importlib import reload

# made by mblais
# if you use my code please give me credit or something. yeh thats bassically it, enjoy :))

game_genre = [
    "sandbox",
    "open world",
    "strategy",
    "shooter",
    "third-person shooter",
    "battle arena",
    "role-playing",
    "simulation",
    "puzzler",
    "party",
    "adventure",
    "survival",
    "horror",
    "platformer",
    "card game",
    "pinball",
    "arcade",
    "art game",
    "stealth"
]

game_environment = [
    "foggy night",
    "snow storm",
    "forest",
    "city",
    "another planet",
    "military",
    "world war",
    "simulated reality",
    "medieval",
    "cyberpunk",
    "modern-day",
    "western",
    "steampunk",
    "alternate history",
    "space"
]

game_goal = [
    "die",
    "survive",
    "control a point",
    "revenge",
    "overcoming of fear",
    "power and corruption",
    "race to the finish",
    "treasure hunt",
    "excape",
    "destroy all objects",
    "capture",
    "reach a destination"
]

game_modifiers = [
    "limited inventory",
    "must not be seen",
    "search for identity",
    "stolen identity",
    "detective",
    "superhero",
    "start with nothing",
    "immortality",
    "isolation",
    "the world shrinks",
    "one minute",
    "don't stop moving",
    "you are the enemy",
    "no weapons allowed",
    "safe in the dark",
    "you are the weapon",
    "1hp",
    "indirect control",
    "color changes everything",
    "limited visibility",
    "build the level you play",
    "death is a new beginning",
    "expanding world",
    "keep it alive",
    "limited capacity",
    "a single resource",
    "you're being chased"
]

# gets a random idea from the specified list above
rand_genre = random.choice(game_genre)
rand_environment = random.choice(game_environment)
rand_goal = random.choice(game_goal)
rand_modifiers = random.choice(game_modifiers)

# enjoy :))
print("a", rand_genre,"game in a", rand_environment,"where the goal is to", rand_goal, "but", rand_modifiers) # kinda scuffed lol... in sentence form to better understand the shit idea.
#point form the keep things organized
print(
"-----------------------------"
"\n","genre:", rand_genre,
"\n","environment:", rand_environment,
"\n","goal:", rand_goal,
"\n","modifiers:", rand_modifiers
)

input("\nClick to exit.")