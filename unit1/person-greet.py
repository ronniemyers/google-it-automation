class Person:
  def __init__(self, name):
    self.name = name

  def greeting(self):
    """Outputs a message with the name of the person."""
    return "Hi, my name is {}".format(self.name)
  help(greeting)
some_person = Person("Xiao Ou")
print(some_person.greeting())

