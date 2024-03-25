materials_with_quantities = {"shards": 0, "fragments": 0, "motes": 0}

while True:
    input_materials = input().split()
    quantities = [int(input_materials[x]) for x in range(len(input_materials)) if x % 2 == 0]
    materials = [input_materials[x] for x in range(len(input_materials)) if x % 2 == 1]
    to_break = False

    for i in range(len(quantities)):
        material = materials[i].lower()
        quantity = quantities[i]
        if material in materials_with_quantities.keys():
            materials_with_quantities[material] += quantity
        else:
            materials_with_quantities[material] = quantity

        if materials_with_quantities["shards"] >= 250:
            materials_with_quantities["shards"] -= 250
            print("Shadowmourne obtained!")
            to_break = True
            break
        if materials_with_quantities["fragments"] >= 250:
            materials_with_quantities["fragments"] -= 250
            to_break = True
            print("Valanyr obtained!")
            break
        if materials_with_quantities["motes"] >= 250:
            materials_with_quantities["motes"] -= 250
            to_break = True
            print("Dragonwrath obtained!")
            break

    if to_break:
        break

print(f"shards: {materials_with_quantities.pop('shards')}\n"
      f"fragments: {materials_with_quantities.pop('fragments')}\n"
      f"motes: {materials_with_quantities.pop('motes')}")

for (material, quantity) in materials_with_quantities.items():
    print(f"{material}: {quantity}")
