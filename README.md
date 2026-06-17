# youtube-realtime

[![License: MIT](https://img.shields.io/github/license/SisoSol/youtube-realtime?style=flat-square&color=blue)](LICENSE) [![Last commit](https://img.shields.io/github/last-commit/SisoSol/youtube-realtime?style=flat-square)](https://github.com/SisoSol/youtube-realtime/commits) [![CI](https://github.com/SisoSol/youtube-realtime/actions/workflows/ci.yml/badge.svg)](https://github.com/SisoSol/youtube-realtime/actions/workflows/ci.yml) [![Built for 1322.io](https://img.shields.io/badge/built%20for-1322.io-3b82f6?style=flat-square)](https://1322.io) [![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](https://github.com/SisoSol/youtube-realtime/pulls)

Real-time **YouTube** channel monitor over **WebSocket**. Get new uploads, Shorts
and video deletions for the channels you track the moment they publish, without
the YouTube Data API quota or polling loops.

The official **YouTube Data API v3 has no real-time push** for new uploads, so
monitoring means polling, and every poll burns quota units. WebSub
(PubSubHubbub) gives best-effort upload pings only — no delivery guarantee, you
host and renew the callback yourself, and the ping is too thin to use without
calling the quota-limited Data API anyway. This is the managed alternative: each
upload arrives as a normalized JSON event over a persistent WebSocket.

These clients run against the [1322](https://1322.io/platforms/youtube) managed
YouTube feed (the same socket also carries X, Truth Social, Instagram, Binance
Square and news). The consumer pattern is generic, so you can point it at any
compatible WebSocket source.

- YouTube monitoring (coverage, pricing): https://1322.io/platforms/youtube
- Data API vs WebSub vs 1322: https://1322.io/compare/youtube-api-alternatives
- Event schema / docs: https://1322.io/docs

## What you get per event

```json
{
  "platform": "youtube",
  "eventType": "upload",
  "handle": "examplechannel",
  "title": "New video title",
  "videoKind": "upload",
  "timestamp": "2026-06-17T12:00:00Z"
}
```

`videoKind` distinguishes regular uploads from Shorts.

## Python

```bash
pip install websockets
API_KEY=your-key WS_URL=wss://1322.io/your-ws-path python main.py
```

## Node

```bash
npm install ws
API_KEY=your-key WS_URL=wss://1322.io/your-ws-path node index.js
```

Get an API key and your WebSocket path from the dashboard after signup
(plans from $250/mo): https://1322.io/pricing

## Why WebSocket instead of polling the Data API

Polling caps worst-case latency at your poll interval and drains the daily quota
budget; across many channels the quota runs out. A WebSocket pushes the upload
the instant it is detected, which is what alert bots and dashboards need. More:
https://1322.io/compare/youtube-api-alternatives

## Related

- All six platforms: https://github.com/SisoSol/social-monitor-examples
- Twitter/X: https://github.com/SisoSol/twitter-websocket-client
- Truth Social: https://github.com/SisoSol/truthsocial-stream
- Instagram: https://github.com/SisoSol/instagram-realtime
- Binance Square: https://github.com/SisoSol/binance-square-realtime

MIT licensed.
