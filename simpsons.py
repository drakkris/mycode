challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

eyes = challenge[2][1]
goggles = challenge[2][0]
nothing = challenge[3]

print(f"My {eyes}! The {goggles} do {nothing}!")

trial_eyes = trial[2].get("goggles")
trial_goggles = trial[2]["eyes"]
trial_nada = trial[3]

print(f"My {trial_eyes}! The {trial_goggles} do {trial_nada}!")

night_eyes = nightmare[0].get("user").get("name").get("first")
night_goggles = nightmare[0].get("kumquat")
night_nada = nightmare[0]["d"]

print(f"My {night_eyes}! The {night_goggles} do {night_nada}!")
