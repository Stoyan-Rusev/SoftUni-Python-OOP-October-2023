from project.animals.mammals import Tiger, Cat
from project.animals.birds import Owl, Hen
from project.food import Food, Meat, Vegetable, Fruit

owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)
print()
hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)

# tiger = Tiger('Shirhan', 123.23, 'STZ')
# owl = Owl('Buh', 2, 30)
# cat = Cat('Tomcho', 10, 'Kazanlak')
# hen = Hen('Coco', 3, 15)
#
# meat = Meat(2)
# potato = Vegetable(2)
# print(cat.weight)
# print(cat.feed(meat))
# print(cat.weight)
# print(cat.feed(meat))
# print(cat.weight)
#
#
# # animals = [tiger, owl]
# # # for animal in animals:
# # #     print(animal.make_sound())
# #
# # # print(tiger.foods)
# # # print(owl.foods)
# # print(hen.foods)
# # potato = Vegetable(2)
# # meat = Meat(12)
# # for food_class in hen.foods:
# #     if isinstance(potato, food_class):
# #         print('Yes')
# #     else:
# #         print('No')
