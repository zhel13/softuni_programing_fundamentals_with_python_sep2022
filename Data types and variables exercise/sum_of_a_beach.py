from collections import Counter
word = input().casefold()
total_count = 0
water_count = word.count("water")
sun_count = word.count("sun")
sand_count = word.count("sand")
fish_count = word.count("fish")

total_count = water_count + sun_count + sand_count + fish_count
print(total_count)


