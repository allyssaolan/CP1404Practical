import os
import shutil


def main():
    path = "FilesToSort"
    print("1")
    print(os.listdir(path))

    source = "FilesToSort"
    destination = os.mkdir("FilesToSort/xlsx")
    for character in path:
        if character == "xlsx":
            shutil.move(source, destination)
    print("2")
    print((os.listdir(path)))

    # print("Path", dest)


main()
