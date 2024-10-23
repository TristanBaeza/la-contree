from .constants import ATOUT_VALUES
from objects import Player, Card
from pack_creator import card_image_extractor


def pli(
    players: list[Player],
    pack: list | list[Card],
    all_cards_pack: list[Card],
    player_turn: Player, atout: str
) -> tuple[list[Player], list[Card], Player]:
    cards_played_during_pli = []
    first_input = input("première carte jouée")
    first_card = input_to_card(first_input, all_cards_pack)
    index_first_player = players.index(player_turn)
    cards_played_during_pli.append(first_card)
    for index in range(1, 4):
        card_played = 
        cards_played_during_pli.append(card_played)
        players[(index + index_first_player) % 4].deck.remove(card_played)

    winner = 
    pack += cards_played_during_pli
    return players, pack , winner


def input_to_card(player_input: str, all_cards_pack: list[Card]) -> Card:
    for card in all_cards_pack:
        if card.value == player_input[0] and card.color == player_input[1]:
            return card
    raise ValueError(f"Card {player_input} not found in the deck.")


def card_to_play(player: Player, all_cards_pack: list[Card], cards_played_during_pli: list[Card], atout: str) -> Card:
    breaker = True
    while breaker:
        player_input = input('carte jouée')
        player_card = card_image_extractor(player_input[0], player_input[1])
        

def is_card_playable(player: Player, player_card: Card, cards_played_during_pli: list[Card], atout: str) -> bool:
    if not player_card in player.deck:
        return False
    if cards_played_during_pli[0].color == atout:
        return is_atout_higher_when_atout_played_first(player, player_card, cards_played_during_pli, atout)
    if cards_played_during_pli[0].color == player_card.color:
        return True
    if 


def is_atout_higher_when_atout_played_first(player: Player, player_card: Card, cards_played_during_pli: list[Card], atout: str) -> bool:
    number_of_atout = sum(1 for card in player.deck if card.color == atout)
    if number_of_atout == 0:
        return True
    if player_card.color != atout:
        return False
    if number_of_atout == 1 : 
        return True
    index_max_played = ATOUT_VALUES.index(cards_played_during_pli[0].value)
    index_max_player = 0
    for card in cards_played_during_pli:
        if ATOUT_VALUES.index(card.value) > index_max_played:
            index_max_played = ATOUT_VALUES.index(card.value)
    if ATOUT_VALUES.index(player_card.value) > index_max_played:
        return True
    for card in player.deck:
        if ATOUT_VALUES.index(card.value) > index_max_player:
            index_max_player = ATOUT_VALUES.index(card.value)
    if index_max_player < index_max_played:
        return True
    return False
    
    