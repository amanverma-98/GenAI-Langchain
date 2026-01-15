from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    email: str

new_person : Person = {
    'name': "Aman",     # it is showing what value should be given when we click on the key but we can give any value it only suggests 
    'age': 21,
    'email': "abc@gmail.com"
}    

print(new_person)