# A recursive function will usually have this structure

def sum_positive_numbers(n):
  if (n==0) or (n==1):
    return n
  return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3))