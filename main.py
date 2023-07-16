import random
from games import Games

def ChooseGame(numPlayers, *drawing):

    game_list = []
    even_players = False

    if int(numPlayers) % 2 == 0:
        even_players = True

    for game in Games:
        if(int(numPlayers) >= game[1] and int(numPlayers) <= game[2]):
            if even_players == False and game[0] == "Quixort":
                continue
            elif even_players == False and game[0] == "Poll mine":
                continue
            else:
                game_list.append(game)

    return game_list[random.randint(0, len(game_list) - 1)]


if __name__ == "__main__":
    numPlayers = input("Number of players?: ")
    print(ChooseGame(numPlayers))

