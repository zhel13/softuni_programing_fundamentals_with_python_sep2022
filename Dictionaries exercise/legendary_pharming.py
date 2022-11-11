key_materials = {
    "shards": 0,
    "fragments": 0,
    "motes": 0,
}

materials = input().split()
obtained_materials = False
while not obtained_materials:
    for index in range(0, len(materials), 2):
        value = materials[index]
        key = materials[index+1].lower()
        if key not in key_materials:
            key_materials[key] = 0
        key_materials[key] += int(value)

        if key_materials["shards"] >= 250:
            print("Shadowmourne obtained!")
            key_materials["shards"] -= 250
            obtained_materials = True

        elif key_materials["fragments"] >= 250:
            print("Valanyr obtained!")
            key_materials["fragments"] -= 250
            obtained_materials = True

        elif key_materials["motes"] >= 250:
            print("Dragonwrath obtained!")
            key_materials["motes"] -= 250
            obtained_materials = True

        if obtained_materials:
            break
    if obtained_materials:
        break
    materials = input().split()
for material, quantity in key_materials.items():
    print(f"{material}: {quantity}")
