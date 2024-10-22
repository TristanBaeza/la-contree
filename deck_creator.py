from objects import Player, Card


def deck_creator(players: list[Player], pack: list[Card]) -> list[Player]:
    for i in range(2):
        for player in players:
            for j in range(3):
                player.deck.append(pack.pop())
    for player in players:
        for j in range(2):
            player.deck.append(pack.pop())
    return players

