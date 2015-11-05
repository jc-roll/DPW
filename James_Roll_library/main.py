import library #This imports my library one cannot work without the other

class Main_Handler:
	#constructor func
	def __init__(self):
        #declaring attributes from library
        self.printer = library.Printer()
        self.library = library.Library()

        #Lets get some inputs
        cows = int(raw_input("How many cows would you like on your farm? "))
        milk = self.library.produce_milk(cows)
        chickens = int(raw_input("How many chickens would you like on your farm? "))
        eggs = self.library.produce_eggs(chickens)

        #Lets set some paths for the variables for the printer
        self.printer.cows = cows
        self.printer.milk = milk
        self.printer.chickens = chickens
        self.printer.eggs = eggs

        #DIsplay function from library
        self.printer.display_function()

#last but not least call the controller function so it all runs
main_handler = Main_Handler()
