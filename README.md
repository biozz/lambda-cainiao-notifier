# lambda-cainiao-notifier

This is a simple "lambda" script that is intended to run 
on [reddec/trusted-cgi](github.com/reddec/trusted-cgi) instance periodically.
It will check delivery status on https://global.cainiao.com/ and send notification
via telegram if the status has changed.

## Environment variables

```
TRACKING_NUMBER
TELEGRAM_BOT_TOKEN
TELEGRAM_CHAT_ID
USER_AGENT
```

## Caveats

- use `make requirements` to generate `requirements.txt` before deploying this script

## FAQ

> How to find telegram chat id?

Send a message to a bot and run `getUpdates` via browser or curl, like [this](https://gist.github.com/dideler/85de4d64f66c1966788c1b2304b9caf1).
