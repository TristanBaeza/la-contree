from .constants import ATOUT_VALUES, VALUES, ATOUT_VALUES_POINTS, VALUES_POINTS
from objects import Player, Card
from typing import Tuple, List, Union


def pli(
    players: List[Player],
    all_cards_pack: List[Card],
    player_turn: Player,
    atout: str,
) -> Tuple[List[Player], List[Card], Player, int]:
    cards_played_during_pli = []
    first_input = input("première carte jouée")
    first_card = input_to_card(first_input, all_cards_pack)
    index_first_player = players.index(player_turn)
    cards_played_during_pli.append(first_card)
    best_card = first_card
    winner = player_turn
    points_during_pli = 0
    for i in range(1, 4):
        real_index = (index_first_player + i) % 4
        card_played = card_to_play(
            players[real_index], all_cards_pack, cards_played_during_pli, atout
        )
        cards_played_during_pli.append(card_played)
        players[real_index].deck.remove(card_played)
        points_during_pli = counting_points(card_played, atout, points_during_pli)
        winner, best_card = determine_best_card(
            best_card, atout, card_played, players, real_index, winner
        )
    return (
        players,
        cards_played_during_pli,
        winner,
        points_during_pli,
    )


def input_to_card(player_input: str, all_cards_pack: List[Card]) -> Card:
    for card in all_cards_pack:
        if card.value == player_input[0] and card.color == player_input[1]:
            return card
    raise ValueError(f"Card {player_input} not found in the deck.")


def card_to_play(
    player: Player,
    all_cards_pack: List[Card],
    cards_played_during_pli: List[Card],
    atout: str,
) -> Card:
    breaker = True
    player_input = input("carte jouée")
    player_card = input_to_card(player_input, all_cards_pack)
    while not is_card_playable(
        player, player_card, cards_played_during_pli, atout=atout
    ):
        player_input = input("carte jouée car erreur")
        player_card = input_to_card(player_input, all_cards_pack)
    return player_card


def is_card_playable(
    player: Player, player_card: Card, cards_played_during_pli: List[Card], atout: str
) -> bool:
    if not player_card in player.deck:
        return False
    colors = [card.color for card in player.deck]
    if cards_played_during_pli[0].color in colors:
        if player_card.color != cards_played_during_pli[0].color:
            return False
        return True
    if atout in colors:
        if player_card.color != atout:
            return False
        return True
    return True


def is_atout_higher_when_atout_played(
    player: Player, player_card: Card, cards_played_during_pli: List[Card], atout: str
) -> bool:
    height_cards = []
    player_card_height = ATOUT_VALUES.index(player_card.value)
    for card in cards_played_during_pli:
        if card.color == atout:
            height_cards.append(ATOUT_VALUES.index(card.value))
    if height_cards == []:
        return True
    if max(height_cards) > player_card_height:
        for card in player.deck:
            if max(height_cards) < ATOUT_VALUES.index(card.value):
                return False
        return True
    return True


def determine_best_card(
    best_card: Card,
    atout: str,
    card_played: Card,
    players: List[Player],
    index: int,
    winner: Player,
) -> Tuple[Player, Card]:
    if best_card.color != atout and card_played.color == atout:
        best_card = card_played
        winner = players[index]
    elif best_card.color == card_played.color:
        if best_card.color == atout:
            if ATOUT_VALUES.index(best_card.value) < ATOUT_VALUES.index(
                card_played.value
            ):
                best_card = card_played
                winner = players[index]
        else:
            if VALUES.index(best_card.value) < VALUES.index(card_played.value):
                best_card = card_played
                winner = players[index]
    return winner, best_card


def counting_points(card_played: Card, atout: str, points_during_pli: int) -> int:
    if card_played.color == atout:
        points_during_pli += ATOUT_VALUES_POINTS[ATOUT_VALUES.index(card_played.value)]
    else:
        points_during_pli += VALUES_POINTS[ATOUT_VALUES.index(card_played.value)]
    return points_during_pli
