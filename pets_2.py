{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

def describe_pet(pet_name, animal_type='dog'):
	"""Display information about a pet."""
	print("I have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".\n")

describe_pet(pet_name='presley')
describe_pet(pet_name='squints')

