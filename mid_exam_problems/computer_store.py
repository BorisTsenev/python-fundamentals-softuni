total_price = 0

while True:
    command = input()
    if command == "special" or command == "regular":
        break
    command = float(command)
    if command < 0:
        print("Invalid price!")
        continue
    total_price += command

if total_price > 0:
    taxes = total_price * 0.2
    print("Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          "-----------")
    total_price += taxes
    if command == "special":
        total_price *= 0.9

    print(f"Total price: {total_price:.2f}$")
else:
    print("Invalid order!")
