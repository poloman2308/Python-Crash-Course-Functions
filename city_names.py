{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

def city_country(city, country):
	"""Return a string like 'Santiago, Chile'."""
	return(city.title() + ", " + country.title())

city = city_country('santiago', 'chile')
print(city)

city = city_country('ushuaia', 'argentina')
print(city)

city = city_country('longyearbyen', 'svalbard')
print(city)

