
# variables
first_name = "James"
last_name = "Roll"
year_born = 1988

#print first_name + " " + last_name
print "You are " + str(2015 - year_born) + " years old"

#CONDITIONAL STATMENTS
if year_born < 1994:
    print "They are old enough to drink"
elif year_born < 1996:
    print "they are too young, but they can serve"
else:
    print "they are too young"

#LOGICAL OPERATORS
# && and
# || or
# ! not
parents_with_them = True
if year_born < 1994 or parents_with_them:
    print "they can drink"

#LOOPS
# no ++ or -- instead use += and -=
#for NUM in range (START< STOP< INC AMT)

#add an array
students = ["Linz", "CLay", "Me", "John", "Serg", "Vanc", "Selen"]
students.append("karl")

# for s in students:
#     print s + ", go get em!"
#
# i = 0
# while i<9:
#     print students[i]
#     i+=1
#for i in range(0,9):
    #print students[i]+', Awsome'

    #print "hello there!"
    #print "happy brithday"

#DICTIONARY
#dictionary_name = {'key': value, 'key':value}
student_movie = {'Selen':'American History X', 'Me':"The Patriot", 'Clay': 'Borne ident'}
print student_movie['Me']# will pull the info for the key

#FUNCTION
def area(x, y):
    a = x * y
    print a

#area(20, 68) #calls the function

#user INPUTTTTTTSTSTSTSTSTS


name = raw_input("Please enter your name:")
print name + ", it is nice to meet you"

age = raw_input("Please enter your age:")
print str(2015 - int(age)) + " was the year you where born"
