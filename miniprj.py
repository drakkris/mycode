# state bird guess

# Dictionary of state birds
state_birds = {
    "Alabama": "Yellowhammer",
    "Alaska": "Willow Ptarmigan",
    "Arizona": "Cactus Wren",
    "Arkansas": "Northern Mockingbird",
    "California": "California Quail",
    "Colorado": "Lark Bunting",
    "Connecticut": "American Robin",
    "Delaware": "Delaware Blue Hen",
    "Florida": "Northern Mockingbird",
    "Georgia": "Brown Thrasher",
    "Hawaii": "Nene (Hawaiian Goose)",
    "Idaho": "Mountain Bluebird",
    "Illinois": "Northern Cardinal",
    "Indiana": "Northern Cardinal",
    "Iowa": "Eastern Goldfinch",
    "Kansas": "Western Meadowlark",
    "Kentucky": "Northern Cardinal",
    "Louisiana": "Brown Pelican",
    "Maine": "Chickadee",
    "Maryland": "Baltimore Oriole",
    "Massachusetts": "Black-capped Chickadee",
    "Michigan": "American Robin",
    "Minnesota": "Common Loon",
    "Mississippi": "Northern Mockingbird",
    "Missouri": "Eastern Bluebird",
    "Montana": "Western Meadowlark",
    "Nebraska": "Western Meadowlark",
    "Nevada": "Mountain Bluebird",
    "New Hampshire": "Purple Finch",
    "New Jersey": "Eastern Goldfinch",
    "New Mexico": "Greater Roadrunner",
    "New York": "Eastern Bluebird",
    "North Carolina": "Northern Cardinal",
    "North Dakota": "Western Meadowlark",
    "Ohio": "Northern Cardinal",
    "Oklahoma": "Scissor-tailed Flycatcher",
    "Oregon": "Western Meadowlark",
    "Pennsylvania": "Ruffed Grouse",
    "Rhode Island": "Rhode Island Red",
    "South Carolina": "Carolina Wren",
    "South Dakota": "Ring-necked Pheasant",
    "Tennessee": "Northern Mockingbird",
    "Texas": "Northern Mockingbird",
    "Utah": "California Gull",
    "Vermont": "Hermit Thrush",
    "Virginia": "Northern Cardinal",
    "Washington": "American Goldfinch",
    "West Virginia": "Northern Cardinal",
    "Wisconsin": "American Robin",
    "Wyoming": "Western Meadowlark"
}




state = input("Choose a state: ").lower()
bird = input(f"What is the state bird of {state}: ").lower()
correct_bird = state_birds.get(state)

if correct_bird == bird:
    print("Correct!")

else:
    print("You pecked the wrong answer!")



