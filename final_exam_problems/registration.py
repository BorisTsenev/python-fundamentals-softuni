class Username:
    def __init__(self, name):
        self.name = name

    def case_of_name(self, case):
        if case == "Lower":
            self.name = self.name.lower()
        else:
            self.name = self.name.upper()
        print(self.name)

    def reverse(self, start_index, end_index):
        start_index = int(start_index)
        end_index = int(end_index)
        if -1 < end_index < len(self.name) and start_index > -1:
            output = ""
            for i in range(end_index, start_index - 1, -1):
                output += self.name[i]
            print(output)

    def substring(self, substring):
        if substring in self.name:
            self.name = self.name.replace(substring, "")
            print(self.name.replace(substring, ""))
        else:
            print(f"The username {self.name} doesn't contain {substring}.")

    def replace(self, char):
        while True:
            if char not in self.name:
                break

            self.name = self.name.replace(char, "-")
        print(self.name)

    def is_valid(self, char):
        if char in self.name:
            print("Valid username.")
        else:
            print(f"{char} must be contained in your username.")


first_username = input()
username = Username(first_username)
while True:
    command = input()
    if command == "Registration":
        break

    command = command.split()
    action = command[0]
    if action == "Letters":
        username.case_of_name(command[1])
    elif action == "Reverse":
        username.reverse(command[1], command[2])
    elif action == "Substring":
        username.substring(command[1])
    elif action == "Replace":
        username.replace(command[1])
    else:
        username.is_valid(command[1])


