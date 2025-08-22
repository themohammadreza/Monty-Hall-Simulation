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
    pass