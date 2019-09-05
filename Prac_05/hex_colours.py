HEX_COLOURS = {"aliceblue": "#f0f8ff",
               "antiquewhite": "#faebd7",
               "brown": "#a52a2a",
               "coral": "#ff7f50",
               "gainsboro": "#dcdcdc",
               "gray": "#bebebe",
               "lavender": "#e6e6fa",
               "light": "#eedd82",
               "aquamarine4": "#458b74",
               "azure1": "#f0ffff"}

colour = input("Enter colour name: ")
while colour != "":
    print("{} is {}".format(colour, HEX_COLOURS.get(colour)))
    colour = input("Enter another colour name: ")
