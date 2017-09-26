def square(x):
  result = 0
  for i in range(x):
    result += x
  return result

def power(x, y):
  if x == 0:
    return 0
  if y == 0:
    return 1
  result = 0
  for i in range(x):
    result += power(x, y-1)
  return result

def cube(x):
  result = square(x) * x
  return result

if __name__ == "__main__":
  for i in range(5):
    print("The square of %s is %s" % (i, square(i)))
    print("The cube of %s is %s", i, cube(i))

  for i in range(5):
    for j in range(4):
      print ("%s to the %sth power is %s" % (i, j, power(i, j)))







