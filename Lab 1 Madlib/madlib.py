#First we need to ask the questions that will later be placed into a Print out and introduced into a string
name = raw_input("Please enter your name:")
item1 = raw_input("What is your favorite item you own?")
item2 = raw_input("What is your best friends favorite item they own?")
friend = raw_input("Who is your best friend?")
food = raw_input("What is your least favorite food?")
time = raw_input("Enter a number between 0-5:")
length = raw_input("Enter a number between 0-5:")


#Now that we have some inputs we can throw some into an array
castaways = [name, friend]

#We can also make a directory
castaways_items = {'name':item1, 'friend':item2}

#It is time for a function and within the function we will run the conditional
def death(time, length):
    if time < length:
        return "you will be saved before you die!" #using the return rather then print so it doesnt show in the term
    elif time == length:
        return "you will ba saved but die on the way home sorry!"
    else:
        return "you will die before you are saved!"

# Lets now make a loop
i = 0
while i<1:
    i+=1
for i in range(0,2):# by changing this 2 to a 1 it would only run one text to the primary person AKA you

#Now lets send them both some text messages to let them know what is going on

    print castaways[i]+', You made it to the island.' + " Luckly " + name + " brought a " + castaways_items['name']\
      + " and " + friend + " brought a " + castaways_items['friend'] + " sadly the only food on the island is " + food\
      + "." + " The search for your rescue has begun " + str(death(int(time), int(length))) + ". The End."
