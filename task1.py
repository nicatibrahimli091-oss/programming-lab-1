numbers = [0, 2, 3, 4, 5, 6, -6, -5, -4, -3, -2, 0]
count = {"divisible" : 0, "notdivisible" : 0}
for i in numbers:
  if i % 3 == 0:
    count["divisible"] += 1
  else:
    count["notdivisible"] += 1
numbers2 = []
for i in numbers:
  if i % 2 == 0 and i % 4 != 0:
    numbers2.append(i)
print(count)
print(numbers2)