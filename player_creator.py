from objects import Player


def player_creation() -> list[Player]:
    with open("joueurs_position.txt", "r", encoding="utf-8") as fichier:
        lignes = fichier.readlines()
    joueurs = []
    for ligne in lignes:
        position, nom = ligne.strip().split(" = ")
        if position in ["Sud", "North"]:
            joueurs.append(Player(name=nom, position=position, team=1))
        else:
            joueurs.append(Player(name=nom, position=position, team=2))
    return joueurs
