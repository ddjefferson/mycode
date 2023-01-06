#!/usr/bin/python3
"""ddjefferson | ddjefferson@yahoo.com

Lab 48: MINI PROJECT #1 IF-LOGIC SCRIPT

Welcome to the Roller Coaster"""

def main():
    """runtime"""
    # welcome user
    print("Welcome to the Roller Coaster!!")
    print("Step right up")

    # while loop
    while True:
        try:
            print("Would you like to ride today? (y/n) ")
            resp = input()

            # check input
            if resp.lower() != 'y':
                if resp.lower() != 'n':
                    raise ValueError
                else:
                    break
            # display error
        except ValueError:
            print("input Invalid..please enter 'y' or 'n'")
            continue

    # consumer input data
    height = int(input("What is your height in inches?"))
    if height >= 48:
        print("BUCKLE UP! You can ride the roller coaster!")
    else:
        print("Sorry, you have to grow taller before you can ride.")

    print("Thanks for choosing RollerCoaster")

    if __name__ == "__main__":
        main()

