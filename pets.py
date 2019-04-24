{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print("I have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('dog', 'presley')

