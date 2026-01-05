country_code = {"India" : "0091",
            "Australia" : "0025",
            "Nepal" : "00977"}


# search dictionary for country code of India
print("Country code for India -")
print(country_code.get("India", "Not Found"))

# search dictionary for country code of japan
print("Country Code for Japan -")
print(country_code.get("Japan", "Not Found"))