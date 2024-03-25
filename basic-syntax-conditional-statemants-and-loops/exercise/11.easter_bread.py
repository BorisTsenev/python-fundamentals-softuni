budget = float(input())
flour_price = float(input())
egg_pack_price = 0.75 * flour_price
liter_milk_price = 1.25 * flour_price

flour_count = 0
egg_pack_count = 0
milk_count = 0
bread_count = 0
colored_eggs_count = 0

while True:
    if flour_count < 1:
        budget -= flour_price
        flour_count += 1
    if egg_pack_count < 1:
        budget -= egg_pack_price
        egg_pack_count += 1
    if milk_count < 1:
        budget -= liter_milk_price / 4
        milk_count += 1

    bread_count += 1
    flour_count -= 1
    egg_pack_count -= 1
    milk_count -= 1
    colored_eggs_count += 3

    if bread_count % 3 == 0 and colored_eggs_count > bread_count - 2:
        colored_eggs_count -= (bread_count - 2)

    if budget < flour_price + egg_pack_price + liter_milk_price:
        break

print(f"You made {bread_count} loaves of Easter bread! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.")
