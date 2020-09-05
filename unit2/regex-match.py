import re
result = re.search(r"aza", "plaza")
print(result)
print(re.search(r"^x", "xenon"))
print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))

# Wildcards and Character Classes
print(re.search(r"[Pp]ython", "Python"))
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))
print(re.search(r"cat|dog", "I like cats."))
print(re.findall(r"cat|dog", "I like both cats and dogs."))

# Repetition Qualifiers
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))
print(re.search(r"\.com", "Welcome"))
print(re.search(r"\w*", "This is an example"))
print(re.search(r"^A.*a$", "Argentina"))
print(re.search(r"[a-zA-Z_][a-zA-Z0-9_]", "Argentina"))
print(re.search(r"[a-zA-Z]{5}", "A scary ghost appeared"))
print(re.search(r"\w{5,10}", "I really like strawberries"))
print(re.search(r"\w{,20}", "I really like strawberries"))

# Capturing Groups
result = print(re.search(r"^(\w*).(\w*)$", "Lovelace, Ada"))
print(result)
print(result.groups())
print(result[0])

# Splaitting and Replacing
re.split(r"[.?!]", "One sentence. Another one? And the last on!")
re.split(r"([.?!])", "One sentence. Another one? And the last on!")
re.sub(r"[\w/%+-]+@[\w.-]", "[REDACTED]", "Received an email for gonuts95@domain.com")
re.sub(r"^([\w.-]*), ([\w.-]*)$", r"\2\1", "Lovelace, Ada")