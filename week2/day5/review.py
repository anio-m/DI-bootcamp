# def get_fullname (firstname, lastname) :
#     fullname_user = firstname + " " + lastname
#     return fullname_user

# def inform_user (): 
#     username = get_fullname("John", "Smith")
#     #print(username) # John Smith
#     print(f"Your fullname is {username}")

# inform_user()
                              
#args
def get_names(*names) :
    print(names) #tuple

get_names("David", "Jane") #('David', 'Jane')
get_names("John", "Lea", "Sara", "Dan") #('John', 'Lea', 'Sara', 'Dan')

def get_names(my_name, *other_names) :
    print(my_name) #Lise
    print(other_names) #('David', 'Jane')

get_names("Lise", "David", "Jane") 
get_names("Lise", "John", "Lea", "Sara", "Dan") 

# keyword arguments
# def get_values (name, age) :
#     print("name :", name) 
#     print("age :", age)

# get_values(age = 23, name = "John")

#kwargs
# keyword argument
def get_values (**info) :
    print("info :", info) 
