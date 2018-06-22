class Dog:

    def __init__(self, name = "", age = 0, furcolor = ""):
        self.name = name
        self.age = age
        self.furcolor = furcolor

    def bark(self, string):
        print("BARK! " + string)

mydog = Dog()
print(mydog.age)
