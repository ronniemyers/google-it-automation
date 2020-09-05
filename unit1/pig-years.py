class Piglet:
  years = 0
  def pig_years(self):
    return self.years * 18

piggy = Piglet()
print(piggy.pig_years())
piggy.years = 2
print(piggy.pig_years())