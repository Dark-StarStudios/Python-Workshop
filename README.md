# 🖥️ AutoTyper met Python

Dit is een simpel Python-script waarmee je automatisch een bericht kunt laten typen in elk programma (zoals WhatsApp Web, Word, Discord, etc.).

Handig voor standaardberichten, of gewoon voor de lol!

## 🚀 Wat doet dit script?

1. Laat jou een standaardbericht kiezen of een eigen bericht invoeren.
2. Geeft je 5 seconden om naar een ander programma te wisselen.
3. Typt het gekozen bericht automatisch, alsof jij het zelf doet!

## 🧰 Benodigdheden

- Python 3.x geïnstalleerd op je laptop
- Een teksteditor (zoals VS Code of Webstorm)
  - **Voor Visual Studio Code gebruikers:**
    - Installeer de officiële **Python-extensie** van Microsoft. Je kunt deze vinden in de Extensions view (Ctrl+Shift+X) door te zoeken naar `ms-python.python`.
    - Zorg ervoor dat je een Python-interpreter selecteert. VS Code zal je hier meestal om vragen, of je kunt dit handmatig doen via de Command Palette (Ctrl+Shift+P) en te zoeken naar "Python: Select Interpreter".
- De module `pyautogui`. (Installatie-instructies hiervoor vind je in de sectie "Downloaden en gebruiken".)

## 📥 Downloaden en gebruiken

1. Download of clone deze repository:
   ```bash
   git clone https://github.com/Rachelzm/Python-Workshop
   ```

2. Open je terminal of command prompt.

3. Navigeer naar de gedownloade map (waarschijnlijk `Python-Workshop`):
   ```bash
   cd Python-Workshop
   ```

4. Installeer de benodigde `pyautogui` module. Zorg ervoor dat je in de `Python-Workshop` map bent in je terminal of command prompt en voer dan het volgende commando uit:
   ```bash
   pip install pyautogui
   ```
   *(Tip: Het is een goede gewoonte om een [virtual environment](https://docs.python.org/3/tutorial/venv.html) te gebruiken voor Python projecten om afhankelijkheden geïsoleerd te houden.)*

5. Open het script `autotyper.py` in je editor (optioneel, als je de code wilt bekijken of aanpassen).

6. Run het script vanuit de `Python-Workshop` map in je terminal:
   ```bash

## ⚠️ Let op

Zodra je het script start en een bericht kiest, heb je **5 seconden** om naar het venster te gaan waar het bericht moet verschijnen. Zorg dat je op het juiste scherm zit!

## 💡 Tips

- Je kunt zelf berichten toevoegen aan de lijst in de code.
- Pas de `interval` aan om langzamer of sneller te typen.
- Combineer het met muisacties (bijv. klikken of scrollen) met `pyautogui`.


Veel plezier met automatiseren!