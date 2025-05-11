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
- De module `pyautogui`
  - Installeren via terminal of command prompt:

```bash
pip install pyautogui
```

## 📥 Downloaden en gebruiken

1. Download of clone deze repository:
```bash
git clone https://github.com/jouwgebruikersnaam/auto-typer.git
```

2. Ga naar de map en open het script `autotyper.py` in je editor.

3. Run het script:
```bash
python autotyper.py
```

4. Kies een bericht of typ zelf iets, wissel daarna naar het programma waarin je het bericht wil laten typen.

## ⚠️ Let op

Zodra je het script start en een bericht kiest, heb je **5 seconden** om naar het venster te gaan waar het bericht moet verschijnen. Zorg dat je op het juiste scherm zit!

## 💡 Tips

- Je kunt zelf berichten toevoegen aan de lijst in de code.
- Pas de `interval` aan om langzamer of sneller te typen.
- Combineer het met muisacties (bijv. klikken of scrollen) met `pyautogui`.

## 📸 Voorbeeld

> (Je kunt hier eventueel een screenshot toevoegen van hoe het script eruitziet in gebruik.)

---

Veel plezier met automatiseren!