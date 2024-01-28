# This is a sample Python script.
import random
from typing import List


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    file = "Darius-13-100m-Fly.txt"
    folder = "swimdata/"

    swimmer,age,distance,stroke = file.removesuffix(".txt").split("-")

    with open(folder+file) as file:
        lines = file.readlines()
        times = lines[0].split(",")
        converts = []
        for t in times:
            minutes, rest = t.split(":")
            seconds, hundredths = rest.split(".")
            converts.append(int(minutes)*60*100+int(seconds)*100+int(hundredths))

        print(converts)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
        print_hi()

