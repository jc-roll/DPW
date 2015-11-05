class Printer():
    #constructor function
    def __init__(self):

        #chosen variables 
        self.cows = 0
        self.milk = 0
        self.chickens = 0
        self.eggs = 0

    #Display function
    def display_function(self):
  
        print "Lets see if you could make it as a farmer..."
        #Must use str() value == int
        print 'You decided to have ' + str(self.cows) + 'cows so now you will have ' + str(self.milk) + 'gallons of milk a day!.'
        print 'In addition to your cows you decided to have ' + str(self.chicken) + 'chickens that will produce a total of ' + str(self.eggs) + 'eggs a day yum!'
        print "Do you have enough to make a living or will you be needing more animals?"


class Library():
    #constructor function
    def __init__(self):
        pass

    #Each cow makes 3 gallons of milk a day 
    def produce_milk(self, x):
        return x * 3

    #Each chicken can produce 2 eggs a day
    def produce_eggs(self, y):
        return y * 2