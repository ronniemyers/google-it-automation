wardrobe = {"shirt":["red", "blue", "white"], "jeans":["blue", "black"]}
for w in wardrobe:
  for color in wardrobe[w]:
    print("{} {}".format(color, w))