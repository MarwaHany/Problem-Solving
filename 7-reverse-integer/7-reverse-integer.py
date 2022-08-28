def get_reversed_r(x):
    rev_x = []
    multiplier = 1
    reversed_number = 0
    while (x):
        remainder = x % 10
        x = (x - remainder)//10
        rev_x.append(remainder)
        if x:
          multiplier *= 10
    while (rev_x):
        reversed_number = reversed_number + multiplier * rev_x.pop(0)
        multiplier //= 10
    return reversed_number

class Solution:
    def reverse(self, x):
      res = 0
      rev_x = []
      if x < 0:
          x = -1 * x
          res = -1 * get_reversed_r(x)
      else:
          res = get_reversed_r(x)
      if (res < -(2**31)) or (res > 2**31-1) or not res:
        return 0
      return res