from dataclasses import dataclass, field
import pygame


@dataclass
class Card:
    value : str
    color : str
    image: pygame.Surface
    rect: pygame.Rect


@dataclass
class Asset:
    color : str


@dataclass
class Player:
    name : str
    position : str
    team : int
    deck : list[Card] = field(default_factory = list)
