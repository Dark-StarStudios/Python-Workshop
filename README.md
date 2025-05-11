# 🖥️ AutoTyper met Python

Dit is een simpel Python-script waarmee je automatisch een bericht kunt laten typen in elk programma (zoals WhatsApp Web, Word, Discord, etc.).

Handig voor standaardberichten, of gewoon voor de lol!

## 🚀 Wat doet dit script?

1.  Laat jou een standaardbericht kiezen of een eigen bericht invoeren.
2.  Geeft je 5 seconden om naar een ander programma te wisselen.
3.  Typt het gekozen bericht automatisch, alsof jij het zelf doet!

## 🧰 Benodigdheden

-   Python 3.x geïnstalleerd op je laptop.
    -   Zorg ervoor dat Python (en daarmee `pip`) is toegevoegd aan de PATH-omgevingsvariabele van je systeem tijdens de installatie.
-   Een teksteditor (zoals VS Code of Webstorm).
    -   **Voor Visual Studio Code gebruikers:**
        -   Installeer de officiële **Python-extensie** van Microsoft. Je kunt deze vinden in de Extensions view (Ctrl+Shift+X) door te zoeken naar `ms-python.python`.
        -   Zorg ervoor dat je een Python-interpreter selecteert. VS Code zal je hier meestal om vragen, of je kunt dit handmatig doen via de Command Palette (Ctrl+Shift+P) en te zoeken naar "Python: Select Interpreter".
-   De module `pyautogui`. Installatie-instructies volgen hieronder.

## 📥 Downloaden en gebruiken

Volg deze stappen om het script op te zetten en te gebruiken:

1.  **Clone de Repository:**
    *   Open een terminal (zoals Command Prompt, PowerShell, of Git Bash) op een locatie naar keuze.
    *   Clone de repository met het volgende commando:
        ```bash
        git clone https://github.com/Rachelzm/Python-Workshop
        ```
    *   Dit zal een map genaamd `Python-Workshop` aanmaken met daarin de projectbestanden.

2.  **Open het Project in je Editor:**
    *   Open Visual Studio Code (of je favoriete teksteditor).
    *   Open de `Python-Workshop` map die je zojuist hebt gecloned (via `File` > `Open Folder...` of de equivalente optie in je editor).

3.  **Open de Geïntegreerde Terminal in je Editor:**
    *   **In VS Code:** Open de geïntegreerde terminal. Dit kan meestal via het menu (`Terminal` > `New Terminal`).

4.  **Installeer de Benodigde Module (`pyautogui`) via de Geïntegreerde Terminal:**
    *   Voer in de geïntegreerde terminal (die nu in de `Python-Workshop` map zou moeten staan) het volgende commando uit:
        ```bash
        pip install pyautogui
        ```
    *   **Problemen met `pip`?**
        *   Als het commando `pip` niet wordt herkend, probeer dan:
            ```bash
            python -m pip install pyautogui
            ```
            Of voor Python 3 specifiek (soms nodig op systemen met meerdere Python-versies):
            ```bash
            python3 -m pip install pyautogui
            ```
        *   Als je een permissiefout krijgt (vooral in PowerShell of andere terminals op Windows), probeer dan je editor (en daarmee de geïntegreerde terminal) als **administrator** uit te voeren en het installatiecommando opnieuw te proberen.

5.  **Bekijk of Pas het Script Aan (Optioneel):**
    *   Het script `autotyper.py` bevindt zich in de projectmap en is nu zichtbaar in je editor. Je kunt het openen om de code te bekijken of aanpassingen te maken (bijvoorbeeld eigen standaardberichten toevoegen).

6.  **Run het Script via de Geïntegreerde Terminal:**
    *   Voer in de geïntegreerde terminal het volgende commando uit om het script te starten:
        ```bash
        python autotyper.py
        ```

## ⚠️ Let op

Zodra je het script start en een bericht kiest, heb je **5 seconden** om naar het venster te gaan waar het bericht moet verschijnen. Zorg dat je op het juiste scherm en in het juiste invoerveld klikt!

## 💡 Tips

-   Je kunt zelf berichten toevoegen aan de `predefined_messages` lijst in het `autotyper.py` script.
-   Pas de `interval` parameter in de `pyautogui.typewrite()` functie aan om de typsnelheid te veranderen (een kleinere waarde is sneller, een grotere waarde is langzamer).
-   Experimenteer met andere `pyautogui` functies om bijvoorbeeld ook muisklikken of andere acties te automatiseren.

Veel plezier met automatiseren!