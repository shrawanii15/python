import random

names = ["Alex", "Riya", "Sam", "John"]
places = ["park", "school", "space", "beach"]
actions = ["found a treasure", "met an alien", "built a robot", "saved a puppy"]

name = random.choice(names)
place = random.choice(places)
action = random.choice(actions)

print("Random Story:")
print(name, "went to the", place, "and", action)