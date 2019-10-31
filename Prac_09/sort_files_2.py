import os


def main():
    categories = {}
    os.chdir("FilesToSort")
    for name in os.listdir('.'):
        if os.path.isdir(name):

    folders = name.split('.')[-1]
    if folders not in categories:
        user_input = input("What category would you like to sort" + folders + "files into?")
        categories[folders] = user_input
        try:
            os.mkdir(user_input)
        except FileExistsError:
            pass
