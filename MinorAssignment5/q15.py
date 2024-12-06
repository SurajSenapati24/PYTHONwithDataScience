import random

def roll():
    return (random.randint(1, 6) + random.randint(1, 6))

def play():
    wins, losses = {}, {}
    total_games = 1000000
    total_wins = 0
    total_losses = 0
    resolved_games = 0

    for _ in range(total_games):
        roll_count = 1
        first_roll = roll()

        if first_roll in {7, 11}:  # Win on first roll
            wins[roll_count] = wins.get(roll_count, 0) + 1
            total_wins += 1
        elif first_roll in {2, 3, 12}:  # Loss on first roll
            losses[roll_count] = losses.get(roll_count, 0) + 1
            total_losses += 1
        else:  # Continue with point
            point = first_roll
            while True:
                current_roll = roll()
                roll_count += 1
                if current_roll == point:  # Win by matching point
                    wins[roll_count] = wins.get(roll_count, 0) + 1
                    total_wins += 1
                    break
                elif current_roll == 7:  # Loss by rolling a 7
                    losses[roll_count] = losses.get(roll_count, 0) + 1
                    total_losses += 1
                    break

        resolved_games += 1
        if roll_count not in wins:
            wins[roll_count] = 0
        if roll_count not in losses:
            losses[roll_count] = 0

    win_percentage = (total_wins / total_games) * 100
    loss_percentage = (total_losses / total_games) * 100

    print(f"Percentage of wins: {win_percentage:.1f}%")
    print(f"Percentage of losses: {loss_percentage:.1f}%")
    print("Percentage of wins/losses based on total number of rolls:")

    print(f"Rolls | % Resolved on this roll | Cumulative % of games resolved")
    cumulative_percentage = 0
    for roll in range(1, max(wins.keys()) + 1):
        resolved_on_this_roll = wins.get(roll, 0) + losses.get(roll, 0)
        percentage_resolved_on_roll = (resolved_on_this_roll / total_games) * 100
        cumulative_percentage += percentage_resolved_on_roll

        print(f"{roll} | {percentage_resolved_on_roll:.2f}% | {cumulative_percentage:.2f}%")

play()
