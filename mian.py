import threading
from bot import run

from app import app

def start_bot():
    run()

if name == "__main__":
    threading.Thread(target=start_bot).start()
    app.run(host="0.0.0.0", port=10000)