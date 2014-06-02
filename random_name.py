import random
names_list = ["Yasha", "Kireem", "Andrew", "Nishaad", "Amy", "Davis"]
randIndex = random.randint(len(names_list))
print randIndex
randName = names_list[randIndex]
print randName
names_list.remove(randName)