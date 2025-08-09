# name = 'khadija'
# for i in name:
#     print(i)
#     if(i=="a"):
#         print("this is using single or maybe double time")
# color = ["red","green","teal "]
# for color in color:
#  print(color)
#  for i in color:
#     print(i)
# Range function is basically used for that ky how many times u want to
# run the loop or how many u want.
# for k in range(1 , 12, 4):
#     print(k)
# 
# k=int(input("Enter the number : "))
# while (k<=10):
#     k=int(input("Enter the number :  "))
#     print(k)

# print("Done with loop perfectly")
# name = input("Enter your name: ")
# print("Hello, " + name)
# class Programmers:
#               company = "microsoft"    
#               def __init__(self , name , salary , pin):
#                   self.name = name
#                   self.salary = salary
#                   self.pin = pin
# p = Programmers("khadija",130000,245)
# print(p.name,p.salary,p.pin,p.company)
# class Student:
#     def __init__(self, name, age, pin):
#         self.name = name          # public
#         self._age = age           # protected
#         self.__pin = pin          # private

#     def show_details(self):
#         print("Name:", self.name)
#         print("Age:", self._age)
#         print("PIN (inside class):", self.__pin)

# s1 = Student("Ali", 18, 1234)
# s1.show_details()

# print(s1.name)     # ✅ public
# print(s1._age)     # ✅ protected (not recommended but possible)
# print(s1.__pin)  ❌ private, will give error
# class Student:
#     def __init__(self, name, age):
#         print("Constructor called!")
#         self.name = name
#         self.age = age

#     def __del__(self):
#         print("Destructor called!")
        
# # Create object (constructor called)
# s1 = Student("Ali", 18)
 
# # Deleting object (destructor called)
# del s1
# print(s1.name,s1.age)
# Writing to a file
# with open("sample.txt", "w") as file:
#     file.write("Hello, this is a test file!")

# # Reading from a file
# with open("sample.txt", "r") as file:
#     content = file.read()
#     print("Content of file after writing:")
#     print(content)

# # Appending to a file
# with open("sample.txt", "a") as file:
#     file.write("\nThis is a new line added to the file.")

# # Reading again to show the appended content
# with open("sample.txt", "r") as file:
#     content = file.read()
#     print("\nContent of file after appending:")
#     print(content)
class MyClass:
    def __init__(self):
        self.__secret = "Hidden value"

obj = MyClass()
print(obj._MyClass__secret)  # Still accessible (name mangling)
