def square(x):
  result = 0
  for i in range(x):
    result += x
  return result

if __name__ == "__main__":
  for i in range(5):
    print("The square of %s is %s" % (i, square(i)))
