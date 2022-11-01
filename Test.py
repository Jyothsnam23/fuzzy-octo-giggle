# Positional Arguments 

# The Arguments that are passed based on their postiion are known as postional arguemnts. 

def add_numbers (n1,n2):
    sum = n1 + n2
    return (sum)

result = add_numbers (7.8,9.3)
print(result)

# Default Arguments 

# We can also provide default values to arguments. The default values are used if we do not pass arguments 
# during a function call. 

def add_numbers (n1 = 200, n2 = 300):
    sum = n1 + n2
    print (sum)

result = add_numbers(5.7)
print (result)

#Keyword Arguments

# If we give names to arguements, they are keyword arguemtents. The order of arguemtne doesn't matter for
# keyword arguments. 

def greet (name, message):
    print ("Hello", name )
    print (message)

# Function calling

greet ("Niri", "How are you?")
greet (message = "Whatsup", name = "AV")    

# Arbitary Arguments

# Python allows us to have a the arbitary numbers of arguemnts 

# If you do not know how many arguments that will be passed into your function, add a*
# before the parameters name in the function defiction. 

def greet (*msg):
    for m in msg:
        print (m)

greet ('Hey', 'How are you?', 'Welcome', 'To Minneapolis')      



    
