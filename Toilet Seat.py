import sys


def main(toilet_seat):
    toilet_seat = toilet_seat.strip()
    toilet_seat = str(toilet_seat)
    up(toilet_seat)
    down(toilet_seat)
    want(toilet_seat)


def up(data):
    num_flips = 0
    if data[0] != data[1]:
        num_flips += 1
    if data[1] != "U":
        num_flips += 1
    for i in range(2, len(data)):
        if data[i] != "U":
            num_flips += 2
    sys.stdout.write(str(num_flips))
    sys.stdout.write("\n")


def down(data):
    num_flips = 0
    if data[0] != data[1]:
        num_flips += 1
    if data[1] != "D":
        num_flips += 1
    for i in range(2, len(data)):
        if data[i] != "D":
            num_flips += 2
    sys.stdout.write(str(num_flips))
    sys.stdout.write("\n")


def want(data):
    num_flips = 0
    for i in range(1, len(data)):
        if data[i] != data[i - 1]:
            num_flips += 1
    sys.stdout.write(str(num_flips))


def test():
    main("""UUUDDUDU
""")


def realtest():
    multiline_input = """"""
    multiline_input = sys.stdin.readline()
    main(multiline_input)


realtest()
