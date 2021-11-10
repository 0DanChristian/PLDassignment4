def getNameAgeAddress():
	name_ = input("Name: ")
	age_  = int(input("Age: "))
	add_  = input("Address: ")
	return name_, age_, add_

def display(nameF, ageF, addF):
    print(f"Hi, my name is {nameF}. I am {ageF} years old and I live in {addF} .")


# steps
# ask for name, age and address
name, age, add = getNameAgeAddress()

# display
display(name, age, add)
