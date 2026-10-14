import functools
numbers = [0, 2, 3, 4, 5, 6, -6, -5, -4, -3, -2, 0]
def my_map(items, callback):
  siyahi = []
  for i in items:
    siyahi.append(callback(i))
  return siyahi
def my_filter(items, predicate):
  siyahi2 = []
  for i in items:
    if predicate(i):
      siyahi2.append(i)
  return siyahi2
def sert(i):
  return i % 2 == 0 and i % 4 != 0
divisible = my_filter(numbers, sert)
squares = my_map(divisible, lambda i: i ** 2)
sumofsquares = functools.reduce(lambda x, y: x + y, squares)
print(divisible)
print(squares)
print(sumofsquares)