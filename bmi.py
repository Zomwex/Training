name = Andrey
height = 2
weight = 20
bmi height / (weight ** 2)
print("индекс массы тела: " + str(bmi))

if bmi < 25:
  print("У " + name + " нетлишнего веса")
else:
  print("У " + name + " есть лишний вес")
