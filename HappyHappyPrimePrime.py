import sys


def main(input, num_input):
    is_happy_prime = []
    input = input.strip().split("\n")
    numbers = []
    for x in range(0, len(input)):
        input[x] = input[x].strip()
        numbers += input[x].split(" ")
    for x in range(0, num_input):
        if is_prime(numbers[x*2+1]):
            is_happy_prime.append(happy_prime(numbers[x*2+1]))
        else:
            is_happy_prime.append(False)
    output(input, is_happy_prime)


def output(numbers, yesno):
    for x in range(0, len(yesno)):
        sys.stdout.write(str(numbers[x]))
        if yesno[x]:
            sys.stdout.write(" YES\n")
        else:
            sys.stdout.write(" NO\n")


def is_prime(input):
    input = abs(int(input))

    if input < 2:
        return False
    if input % 2 == 0:
        return False
    if not input & 1:
        return False
    for x in range(3, int(input**0.5)+1, 2):
        if input % x == 0:
            return False
    return True


def test():
    main("""1 1
2 7
3 13
4 19
5 23
6 31
7 79
8 97
9 103
10 109
11 871837
""", 11)


def real_test():
    input = """"""
    num_input = int(sys.stdin.readline().strip())
    for x in range(0, num_input):
        input += sys.stdin.readline()
    main(input, num_input)


def happy_prime(input):
    num = 0
    if input == 1:
        return True
    if input == 4:
        return False
    else:
        place = str(input)
        for x in range(0, len(place)):
            num += int(place[x])**2
        return happy_prime(num)


real_test()