"""Real-time YouTube channel monitor over WebSocket.

Prints new uploads / Shorts for the channels on your tracked list as they
publish. Set API_KEY and WS_URL from your 1322 dashboard. See README.
"""
import asyncio
import json
import os

import websockets

API_KEY = os.environ.get("API_KEY")
WS_URL = os.environ.get("WS_URL")


async def run():
    if not API_KEY or not WS_URL:
        raise SystemExit("set API_KEY and WS_URL (see README)")
    while True:
        try:
            async with websockets.connect(WS_URL, additional_headers={"X-Api-Key": API_KEY}) as ws:
                print("connected: youtube feed")
                async for raw in ws:
                    try:
                        event = json.loads(raw)
                    except ValueError:
                        continue
                    if event.get("platform") != "youtube":
                        continue
                    kind = event.get("videoKind", "upload")
                    handle = event.get("handle", "?")
                    print(f"[{event.get('timestamp', '')}] {handle} ({kind}): {event.get('title', '')}")
        except Exception as exc:  # noqa: BLE001 - keep the consumer alive
            print(f"disconnected ({exc}); reconnecting in 1s")
            await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(run())
