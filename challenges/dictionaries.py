"""Challenge Dictionaries"""


def main():

# dictionary
    marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }

# save a user's input to the var char_name
# Which character do you want to know about? (Starlord, Mystique, Hulk)
char_name = input("what name?")




# Save a user's input to the variable char_stat from the following question:
# What statistic do you want to know about? (real name, powers, archenemy)
char_stat = input("what stat?")


# Create a print function that combines that information into this output:
#  <char_name>'s <char_stat> is: <value>
print(marvelchars.get(char_name).get(char_stat))
print(char_name + "'s", char_stat, "is:", marvelchars.get(char_name.get(char_stat)))

main()
