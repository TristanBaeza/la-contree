from .constants import COLORS, VALUES
from objects import Card
from random import shuffle
import pygame


def deck_creator() -> tuple[list[Card], list[Card]]:
    pack = []
    for i in range(len(VALUES)):
        for j in range(len(COLORS)):
            image_card = card_image_extractor(VALUES[i], COLORS[j])
            pack.append(
                Card(
                    value=VALUES[i],
                    color=COLORS[j],
                    image=image_card,
                    rect=image_card.get_rect(),
                )
            )
    all_cards_pack = [element for element in pack]
    shuffle(pack)
    return (all_cards_pack, pack)


def card_image_extractor(value: str, color: str) -> pygame.Surface:
    image_str = value + color + ".gif "
    return pygame.image.load(image_str)
