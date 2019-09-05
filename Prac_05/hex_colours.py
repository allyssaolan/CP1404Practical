HEX_COLOURS = {"AliceBlue": "#f0f8ff",
               "AntiqueWhite": "#faebd7",
               "AntiqueWhite1": "#ffefdb",
               "AntiqueWhite2": "#eedfcc",
               "AntiqueWhite3": "#cdc0b0",
               "AntiqueWhite4": "#8b8378",
               "aquamarine1	": "#7fffd4",
               "aquamarine2": "#76eec6",
               "aquamarine4": "#458b74",
               "azure1": "#f0ffff"}

colour = input("Enter colour name: ")
while colour != "":
    print("{} is {}".format(colour, HEX_COLOURS.get(colour)))
    colour = input("Invalid colour name. Enter another colour name: ").upper()
