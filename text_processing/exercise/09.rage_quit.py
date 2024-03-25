rage_text = input()
current_text = ""
output_text = ""
for ch in rage_text:
    if ch.isdigit():
        output_text += current_text.upper() * int(ch)
        current_text = ""
    else:
        current_text += ch

symbols = [x for x in output_text]
symbols_count = len(set(symbols))
print(f"Unique symbols used: {symbols_count}\n{output_text}")
