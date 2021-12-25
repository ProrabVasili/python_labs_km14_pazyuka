from numpy import cbrt
def root2(n):
      if n<0:
        return "You can't find the square root of a negative number"
      else:
        return n ** 0.5
def root3(n):
    return cbrt(n)

