team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]

referee_input = input()
referee_red_cards = referee_input.split()
is_terminated = False

for current_red_card in referee_red_cards:
    if current_red_card[0] == "A":
        try:
            team_a.remove(current_red_card)
        except:
            pass
    else:
        try:
            team_b.remove(current_red_card)
        except:
            pass

    if len(team_a) < 7 or len(team_b) < 7:
        is_terminated = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if is_terminated:
    print("Game was terminated")
