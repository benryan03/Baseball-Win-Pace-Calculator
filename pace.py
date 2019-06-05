wins = int(input("Enter the number of wins: "))
losses = int(input("Enter the number of losses: "))
total = wins + losses
ratio = wins / losses

win_pace = (162 / total) * wins
loss_pace = (162 / total) * losses

print("Pace: " + str(int(win_pace)) + "-" + str(int(loss_pace)))