import functools
numbers = [0, 2, 3, 4, 5, 6, -6, -5, -4, -3, -2, 0]
divisible = list(filter(lambda x: x % 2 == 0 and x % 4 != 0, numbers))
squares= list(map(lambda x : x ** 2, divisible))
sumofsquares = functools.reduce(lambda x, y: x + y, squares)
print(divisible)
print(squares)
print(sumofsquares)