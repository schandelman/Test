import math

with open("input6.txt") as f:
    times = [int(x) for x in f.readline().split()[1:]]
    distances = [int(x) for x in f.readline().split()[1:]]

def quadratic_formula(a, b, c):
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a) + .00001
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a) - .00001
    return x1, x2

total = 1
for time, distance in zip(times, distances):
    little, big = quadratic_formula(-1, time, -distance)
    answer = math.floor(big) - math.ceil(little) + 1
    total *= answer

print(total)