century = int(input())
years = century * 100
days = int(365.2422*years)
hours = int(24*days)
minutes = 60*hours

print(f"{century} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")