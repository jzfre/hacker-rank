#!/bin/python3
import sys

# Find how many of characters are same
def appendAndDelete(s, t, k):
  it_len = len(t)

  if len(s) > len(t):
    it_len = len(s)
      
  for i in range(it_len):
    # current less than desired
    if (i >= len(s)):
      diff = len(s) - len(t)
      if (diff == k) or (k % 2 == 0 and diff % 2 == 0) or (k % 2 == 1 and diff % 2 == 1):
        return 'Yes'
      else:
        return 'No'
    # current more then desired      
    if (i >= len(t)):
      diff = len(s) - len(t)
      if (diff == k) or (k % 2 == 0 and diff % 2 == 0) or (k % 2 == 1 and diff % 2 == 1):
        return 'Yes'
      else:
        return 'No'

    if (s[i] == t[i]):
      continue

    if (s[i] != t[i]):
      min_req_op_cnt = (len(s) - i) + (len(t) - i)
      diff = len(s) - len(t)
      if (i == 0) and (min_req_op_cnt <= k):
        return 'Yes'

      if (min_req_op_cnt == k) or (k % 2 == 0 and diff % 2 == 0) or (k % 2 == 1 and diff % 2 == 1):
        return "Yes"
      else:
        return "No"

  return 'Yes'

if __name__ == '__main__':
    fptr = sys.stdout

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
