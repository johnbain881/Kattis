import sys

temps_below_zero = 0
num_temps = int(sys.stdin.readline())
temps = sys.stdin.readline().split(" ")

for x in range (0, num_temps):
    temps[x] = int(temps[x])
    if temps[x] < 0:
        temps_below_zero = temps_below_zero + 1
temps_below_zero = str(temps_below_zero)
sys.stdout.write(temps_below_zero)