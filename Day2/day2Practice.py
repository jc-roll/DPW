# x = 4
# y = 2
# z = 3
# w = 5
#
# def get_average(amount):
#     total = 0
#     for i in amount:
#         total += i
#
#     avg = total / len(amount)
#     return avg
#
# print get_average(4,9,333)




import random


class Dog:
    def __init__(self):
        print "Dog Created"
        self.color = ""
        self.name = ""
        self.name = 0
    def bark(self):
        return "Woof!"

kennel = []
names = ["a", "b", "c", "d", "e"]
for d in range(100):
    dog = Dog()
    dog.name = names[random.randrange(0, len(names))]
    kennel.append(dog)
    print dog.name

