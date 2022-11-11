people = {"Peter": 21, "George": 18, "Zhel": 40}

print({key: value for key, value in people.items() if value % 2 != 0})
