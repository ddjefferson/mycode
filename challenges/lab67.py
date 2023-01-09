#!usr/bin/env python3
"""ddjefferson | ddjefferson@yahoo.com
Looping Vampires"""

counter = 0
## create file object in "r"ead mode
with open("dracula.txt", "r") as foo:
    ## create second file in "w"rite mode
    with open("vampytimex.txt", "w") as fang:
    ## loop through line that contains word vampire
        for line in foo:
            if "vampire" in line.lower():
                print(line)
                counter += 1
                fang.write(line)

print(counter)

