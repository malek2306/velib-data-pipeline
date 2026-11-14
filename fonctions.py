def filtrer_stations(stations, min_velos=1):
    """Garde les stations qui ont au moins min_velos vélos."""
    return [s for s in stations if s["velos"] >= min_velos]


def compter_mots(texte):
    """Renvoie un dictionnaire mot -> nombre d'occurrences."""
    comptes = {}
    for mot in texte.lower().split():
        comptes[mot] = comptes.get(mot, 0) + 1
    return comptes


def lire_fichier(chemin):
    """Renvoie les lignes d'un fichier texte, ou [] s'il n'existe pas."""
    try:
        with open(chemin, encoding="utf-8") as f:
            return [ligne.strip() for ligne in f]
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    stations = [
        {"nom": "Bastille", "velos": 12},
        {"nom": "Republique", "velos": 0},
        {"nom": "Nation", "velos": 25},
    ]
    print(filtrer_stations(stations))
    print(filtrer_stations(stations, min_velos=20))
    print(compter_mots("le velo le plus rapide est le velo vert"))
    print(lire_fichier("absent.txt"))