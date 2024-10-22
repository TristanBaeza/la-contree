from objects import Card
from random import shuffle
import pygame


colors = ["s", "c", "h", "d"]
values = ["7", "8", "9", "10", "J", "Q", "K", "A"]


def deck_creator() -> list[Card]:
    pack = []
    for i in range(len(values)):
        for j in range(len(colors)):
            card_image_extractor(values[i], colors[j])
            pack.append(Card(value = values[i], color = colors[j], card_image_extractor, card_image_extractor.get_rect()))
    shuffle(pack)
    return pack


def card_image_extractor(value: str, color: str) -> pygame.Surface:
    image_str = value + color + ".jpg"
    return pygame.image.load(image_str)
 
