import random

def monty_hall_game(switch: bool) -> bool:
    doors = ['car', 'goat', 'goat']
    random.shuffle(doors)

    initial_choice = random.choice(range(3))

    if switch:
        revealed_options = [i for i in range(3) if i != initial_choice and doors[i] != 'car']
        revealed_door = random.choice(revealed_options)

        final_choice = [i for i in range(3) if i != initial_choice and i != revealed_door][0]
    else:
        final_choice = initial_choice

    return doors[final_choice] == 'car'


def game_simulation(num_of_reapet: int, switch: bool) -> float:
    num_of_wins = 0
    for _ in range(num_of_reapet):
        if monty_hall_game(switch):
            num_of_wins += 1

    return num_of_wins / num_of_reapet


if __name__ == "__main__":
    print("Monty Hall Game Simulation")
    num_of_repeats = 100000
    switch_wins = game_simulation(num_of_repeats, switch=True)
    stay_wins = game_simulation(num_of_repeats, switch=False)

    print(f"Switching: {switch_wins:.2f}")
    print(f"Staying: {stay_wins:.2f}")

    assert switch_wins > stay_wins, "Switching should yield a higher win rate than staying."
