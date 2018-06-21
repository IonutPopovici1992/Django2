age = 27

name = 'Matt'

def greetings(name = 'Sean', age = 20):
    print("Hello {}, you are {} years old.".format(name, age))

greetings('Adam', 30)
greetings('Bob', 40)
greetings('Chris', 50)
greetings()
