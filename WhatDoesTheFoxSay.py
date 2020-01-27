import sys
from typing import List, Any


def fox_says(test_case):
    line = test_case.split("\n")
    myline = iter(line)
    num_cases = int(next(myline))
    for x in range(0, num_cases):
        recording = next(myline).strip().split(" ")
        while True:
            animal_and_noise = next(myline).split(" ")
            # sys.stdout.write(str(animal_and_noise))
            # sys.stdout.write("\n")
            if animal_and_noise[0] == "what":
                # sys.stdout.write("WE SEE WHAT\n")
                break
            animal_noise = animal_and_noise[2].strip()
            # sys.stdout.write(animal_noise + "\n")
            not_this_animal_noise: List[str] = []
            for i in range(0, len(recording)):
                if recording[i] != animal_noise:
                    not_this_animal_noise.append(recording[i])
            recording = not_this_animal_noise
        for j in range(0, len(recording)):
            sys.stdout.write(recording[j] + " ")


def test():
    fox_says("""1
toot woof wa ow ow ow pa blub blub pa toot pa blub pa pa ow pow toot
dog goes woof
fish goes blub
elephant goes toot
seal goes ow
what does the fox say?
""")


def realtest():
    multiline_string = """"""
    num_tests = sys.stdin.readline()
    multiline_string += num_tests
    num_tests = int(num_tests)
    for p in range(0, num_tests):
        while True:
            help = sys.stdin.readline()
            multiline_string += help
            if help == "what does the fox say?\n":
                break
    fox_says(multiline_string)


realtest()
