class Party:
    def __init__(self):
        self.people = list()

    def add_people(self, command):
        if command == "End":
            return f"Going: " + ", ".join(self.people) + "\n" + f"Total: {len(self.people)}"
        self.people.append(command)

party = Party()

while True:
    command = input()
    if command == "End":
        print(party.add_people(command))
        break

    party.add_people(command)
