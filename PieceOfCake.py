import sys

numbers_string = sys.stdin.readline()
numbers = numbers_string.split(" ")
length = int(numbers[0])
horizontal1 = int(numbers[1])
vertical1 = int(numbers[2])
horizontal2 = length - horizontal1
vertical2 = length - vertical1
if horizontal1 >= horizontal2:
    side1 = horizontal1
else:
    side1 = horizontal2
if vertical1 >= vertical2:
    side2 = vertical1
else:
    side2 = vertical2

volume = side1 * side2 * 4
volume = str(volume)
sys.stdout.write(volume)
