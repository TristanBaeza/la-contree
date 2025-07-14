from ast import List
from pli_progress import counting_points, pli
from objects import Card, Player
from typing import Tuple, List


def mene(
    players: List[Player], player_turn: Player, all_cards_pack: List[Card], atout: str
) -> Tuple[int, int, List[Card]]:
    announcement = announcements(players, player_turn)
    result = result_mene(players, all_cards_pack, player_turn, atout, announcement)
    return result


def announcements(players: List[Player], player_turn: Player) -> Tuple[int, str, int]:
    consecutive_passes = 0
    attempt = (0, "", 0)
    while consecutive_passes < 3:
        if input("Wanna talk ?").lower() == "yes":
            value = int(input("Value = "))
            color = input("Color = ")
            attempt = (value, color, player_turn.team)
            consecutive_passes = 0
        else:
            consecutive_passes += 1
        player_turn = players[(players.index(player_turn) + 1) % 4]
    return attempt


def result_mene(
    players: List[Player],
    all_cards_pack: List[Card],
    player_turn: Player,
    atout: str,
    announcement: Tuple[int, str, int],
) -> Tuple[int, int, List[Card]]:
    taking_team_points = 0
    all_cards_played = []
    for _ in range(8):
        current_pli = pli(players, all_cards_pack, player_turn, atout)
        players = current_pli[0]
        all_cards_played += current_pli[1]
        if announcement[2] == current_pli[2].team:
            taking_team_points += current_pli[3]
    return taking_team_points, announcement[0], all_cards_played
