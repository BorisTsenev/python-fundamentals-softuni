def data_types(data_type, data_input):
    if data_type == "int":
        data_input = int(data_input)
        data_input *= 2
        return data_input
    elif data_type == "real":
        data_input = float(data_input) * 1.5
        return f"{data_input:.2f}"
    else:
        data_input = "$" + data_input + "$"
        return data_input


input_type = input()
input_data= input()

print(data_types(input_type, input_data))
