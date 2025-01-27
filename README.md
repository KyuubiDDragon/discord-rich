# StreamUnity Rich Presence

Dieses Skript setzt eine benutzerdefinierte **Rich Presence** für Discord mit **pypresence** und der Twitch-Community **StreamUnity** um. Damit wird ein individueller Status mit **Buttons** für Twitch und StreamUnity angezeigt.

## 💾 Installation

### 1. **Python herunterladen**
Falls Python nicht installiert ist, lade es hier herunter und installiere es:
[https://www.python.org/downloads/](https://www.python.org/downloads/)

Achte darauf, dass du bei der Installation **"Add Python to PATH"** auswählst!

### 2. **Benötigte Bibliotheken installieren**

Installiere die benötigten Python-Pakete mit folgendem Befehl:
```bash
pip install pypresence
```

Falls `pip` nicht erkannt wird, versuche:
```bash
python -m pip install pypresence
```

## 💪 Nutzung

### 1. **Skript ausführen**
Starte das Skript mit folgendem Befehl:
```bash
python rich_presence.py
```

Wenn alles funktioniert, sollte in Discord die **Rich Presence** angezeigt werden!

## 🎮 Funktionen
- **Custom Rich Presence** mit Name, Beschreibung und Bild
- **Buttons für Twitch & StreamUnity**
- **Automatische Aktualisierung alle 15 Sekunden**

## 🎮 Das Skript (rich_presence.py)
```python
import pypresence
import time

CLIENT_ID = "1333466319215132763"

rpc = pypresence.Presence(CLIENT_ID)
rpc.connect()

print("Rich Presence läuft...")

while True:
    rpc.update(
        state="StreamUnity",
        details="Deine Community für Streamer und Zuschauer",
        large_image="logo",
        large_text="StreamUnity",
        start=int(time.time()),
        buttons=[
            {"label": "Twitch", "url": "https://twitch.tv/KyuubiDDragon"},
            {"label": "StreamUnity", "url": "https://streamunity.live"}
        ]
    )
    time.sleep(15)
```

## 🛠️ Erstellen einer EXE-Datei
Falls du das Skript in eine **Windows-EXE-Datei** umwandeln willst, nutze `pyinstaller`:

1. **Installiere pyinstaller**
```bash
pip install pyinstaller
```

2. **Erstelle die EXE-Datei**
```bash
pyinstaller --onefile --windowed rich_presence.py
```

Nach der Erstellung findest du die `.exe` im Ordner **`/dist/`**.

Falls du ein eigenes **Icon** für die EXE-Datei willst:
```bash
pyinstaller --onefile --windowed --icon=icon.ico rich_presence.py
```
(Achte darauf, dass `icon.ico` im gleichen Ordner ist.)

## 🌟 Support
Falls du Fragen oder Probleme hast, kannst du dich an die **StreamUnity Community** wenden:
[https://streamunity.live](https://streamunity.live)

Viel Spaß mit deiner Discord Rich Presence! 🚀
