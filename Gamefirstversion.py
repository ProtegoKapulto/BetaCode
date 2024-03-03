from Fightingsystem import *
def animated_text(text):  # Animation von ChatGPT erstellt
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.01) # Zeit für nächsten Buchstaben hier konfigurierbar
    return ("")


def game_opening():
    print(animated_text(f"""In einer Welt, die nicht ganz unserer ähnelt, lebte ein gewöhnlicher Mensch namens {player_name}. 
{player_name} war nicht nur ein begeisterter Computerbenutzer, sondern auch ein leidenschaftlicher Spieleentwickler. 
Er verbrachte die meiste Zeit vor dem Bildschirm, vertieft in die komplexe Kunst des Programmierens.
Eines Tages arbeitete {player_name} an seinem neuesten Projekt, einem Spiel, das so anspruchsvoll und detailliert war, dass es die Grenzen seiner Hardware auf die Probe stellte. 
Die Leistung war so hoch, dass die Temperatur des PCs stetig anstieg. {player_name} bemerkte die Warnzeichen nicht, so vertieft war er in seine Arbeit.
Plötzlich erfüllte ein greller Lichtblitz den Raum, gefolgt von einer gewaltigen Explosion, die von seinem Computer ausging. {player_name} fühlte einen stechenden Schmerz, dann Dunkelheit.
Als {player_name} die Augen öffnete, war alles anders. Der graue Bürostuhl und der blinkende Computerbildschirm waren verschwunden. 
Stattdessen fand er sich in einer Welt wieder, die aussah wie eine lebendige Version des Spiels, an dem er gearbeitet hatte. 
Er war in einer Fantasiewelt wiedergeboren worden."""))
def game_start():
    global player_name
    global monster
    player_name = input(animated_text("What is your Name? "))
    if player_name.lower() == "monika":
        monster = monika
        monika()
    else:
        game_opening()