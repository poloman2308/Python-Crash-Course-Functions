{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

def describe_city(city, country='chile'):
	"""Describe a city."""
	msg = city.title() + " is in " + country.title() + "."
	print(msg)

describe_city('santiago')
describe_city('reykjavik', 'iceland')
describe_city('punta arenas')

