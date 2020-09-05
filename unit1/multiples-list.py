#List Comprehension

multiples = [x*7 for x in range(1,11)]
print(multiples)

langauges = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in langauges]
print(lengths)

z = [x for x in range(0,101) if x % 3 == 0]
print(z)

def odd_numbers(n):
  return [x for x in n if n % 2 == 1]

print(odd_numbers(5))