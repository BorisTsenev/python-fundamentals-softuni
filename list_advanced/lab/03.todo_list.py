todo_notes = list()
while True:
    note = input()
    if note == "End":
        break
    todo_notes.append(note)

sorted_notes = sorted(todo_notes, key=lambda x: int(x.split('-')[0]))
notes = [note.split('-')[1] for note in sorted_notes]
print(notes)
