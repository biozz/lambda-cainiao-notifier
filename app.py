import json
import os

import pickledb
import requests

TRACKING_NUMBER = os.getenv("TRACKING_NUMBER")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
USER_AGENT = os.getenv("USER_AGENT")


def main():
    db = pickledb.load("state.db", auto_dump=True)
    cainiao_response = requests.get(
        f"https://slw16.global.cainiao.com/trackRefreshRpc/refresh.json?mailNo={TRACKING_NUMBER}",
        headers={
            "User-Agent": USER_AGENT,
        },
    )
    data = json.loads(cainiao_response.text[1:-1])
    db_data = db.get(TRACKING_NUMBER)
    if db_data and db_data.get("status") == data.get("status"):
        # nothing changed, exit
        return
    # status changed, store and notify
    db.set(TRACKING_NUMBER, data)
    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
        json={"chat_id": TELEGRAM_CHAT_ID, "text": f"{TRACKING_NUMBER}: {data.get('status')}"},
    )


if __name__ == "__main__":
    main()
