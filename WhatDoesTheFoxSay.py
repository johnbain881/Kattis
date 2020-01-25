import sys
from typing import List, Any







num_cases = int(sys.stdin.readline())



def test_function(list_of_str):
    while True:
        animal_and_noise = sys.stdin.readline().split(" ")
        sys.stdout.write(str(animal_and_noise))
        sys.stdout.write("\n")
        if animal_and_noise[0] == "what":
            sys.stdout.write("WE SEE WHAT\n")
            break
        animal_noise = animal_and_noise[2].strip()
        sys.stdout.write(animal_noise + "\n")
        not_this_animal_noise: List[str] = []
        for i in range(0, len(recording)):
            if recording[i] != animal_noise:
                not_this_animal_noise.append(recording[i])
        recording = not_this_animal_noise
    for j in range(0, len(recording)):
        sys.stdout.write(recording[j] + " ")






for x in range(0, num_cases):
    recording = sys.stdin.readline().strip().split(" ")