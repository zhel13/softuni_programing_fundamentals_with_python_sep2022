countries = input().split(", ")
cities = input().split(", ")
dict_zip = dict(zip(countries, cities))
for key, values in dict_zip.items():
    print(f"{key} -> {values}")
