class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = list()

while True:
    command = input()
    if command == "Stop":
        break
    emails.append(command)

sent_indices = list(map(int, input().split(", ")))

current_index = 0
for current_email in emails:
    current_email = current_email.split()
    email = Email(current_email[0], current_email[1], current_email[2])
    if current_index in sent_indices:
        email.send()
    current_index += 1
    print(email.get_info())
