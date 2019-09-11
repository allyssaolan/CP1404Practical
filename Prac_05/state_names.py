"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
STATE_NAMES = {"QLD": "Queensland",
               "NSW": "New South Wales",
               "NT": "Northern Territory",
               "WA": "Western Australia",
               "ACT": "Australian Capital Territory",
               "VIC": "Victoria",
               "TAS": "Tasmania"}
# print(STATE_NAMES)
for short_state, state_name in STATE_NAMES.items():
    print("{} is {}".format(short_state, state_name))

state_name = input("Enter short state: ").upper()
while state_name != "":
    if state_name in STATE_NAMES:
        print(state_name, "is", STATE_NAMES[state_name])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()
