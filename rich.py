import pypresence
import time

CLIENT_ID = "EureClientID"

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
