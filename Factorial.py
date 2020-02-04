import sys




def main(data):
    output = recursive_factorial(data)
    sys.stdout.write(str(output) + "\n")


def factorial(data):
    currentvalue = data

    for x in range(1, data):
        currentvalue = currentvalue * (data - x)
    return currentvalue


def recursive_factorial(data):
    if data == 1:
        return data
    else:
        return data * recursive_factorial(data - 1)


def test():
    main(9)



test()