#!usr/bin/env/python3

"""ddjefferson | AWS 
OLD MACDONALD HAD A FARM"""

# create a list of strings
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

#
NE_animals= farms[][]


# loop across the list called farms
for x in NE_animals:
    print(x)

# ask user for input


# Part 2: ask user to choose a farm (NE Farm, W Farm, or SE Farm)... but only return ANIMALS from that particular farm.
for farm in farms:
    print("-", farm["name"])
choice = input("Pick a farm!\n")

for farm in farms:
    if farm["name"].lower() == choice.lower():
        # TODO: complete

# Part 3: Ask a user to choose a farm (NE Farm, W Farm, or SE Farm)... but only return ANIMALS from that particular farm.

yuck= ["carrots", "celery"]

for farm in farms:
    print("-", farm["name"])
choice= input("Pick a farm!\n")

for farm in farms:
    if farm["name"].lower() == choice.lower():
        for ag_item in farm["agriculture"]:
            if ag_item not in yuck:
                 print(ag_item)


