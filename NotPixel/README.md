
## Recommendation before use

# 🔥🔥 Use PYTHON 3.10 🔥🔥



## Features  
| Feature                                                   | Supported |
|-----------------------------------------------------------|:---------:|
| Multithreading                                            |     ✅     |
| Proxy binding to session                                  |     ✅     |
| User-Agent binding to session                             |     ✅     |
| Support for tdata / pyrogram .session / telethon .session |     ✅     |
| Registration in bot                                       |     ✅     |
| Auto-paint                                                |     ✅     |
| Auto-tasks                                                |     ✅     |
| Auto-claim mining rewards                                 |     ✅     |
| Auto-upgrade boosters                                     |     ✅     |




## [Settings]
| Settings                |                                 Description                                 |
|-------------------------|:---------------------------------------------------------------------------:|
| **API_ID / API_HASH**   | Platform data from which to run the Telegram session (by default - android) |
| **SLEEP_TIME**          |            Sleep time between cycles (by default - [3200, 3600])            |
| **START_DELAY**         |           Delay between sessions at start (by default - [5, 20])            |
| **AUTO_PAINT**          |                      Auto painting (by default - True)                      |
| **AUTO_UPGRADE**        |                  Auto upgrade boosters (by default - True)                  |
| **AUTO_MINING**         |                Auto claim mining reward (by default - True)                 |
| **AUTO_TASK**           |                       Auto tasks (by default - True)                        |
| **AUTO_UPGRADE_PAINT**  |                Auto upgrade paint reward (by default - True)                |
| **MAX_PAINT_LEVEL**     |                Max level for paint booster (by default - 5)                 |
| **AUTO_UPGRADE_CHARGE** |               Auto upgrade recharge speed (by default - True)               |
| **MAX_CHARGE_LEVEL**    |               Max level for recharge booster (by default - 5)               |
| **AUTO_UPGRADE_ENERGY** |                Auto upgrade energy limit (by default - True)                |
| **MAX_ENERGY_LEVEL**    |                Max level for energy booster (by default - 2)                |
| **REF_ID**              |                          Ref link for registration                          |


## Quick Start 📚

To fast install libraries and run bot - open run.bat on Windows or run.sh on Linux

## Prerequisites
Before you begin, make sure you have the following installed:
- [Python](https://www.python.org/downloads/) **version 3.10**

## Obtaining API Keys
1. Go to my.telegram.org and log in using your phone number.
2. Select "API development tools" and fill out the form to register a new application.
3. Record the API_ID and API_HASH provided after registering your application in the .env file.



# Linux manual installation
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env-example .env
nano .env  # Here you must specify your API_ID and API_HASH, the rest is taken by default
python3 main.py
```

You can also use arguments for quick start, for example:
```shell
~/NotPixelBot >>> python3 main.py --action (1/2)
# Or
~/NotPixelBot >>> python3 main.py -a (1/2)

# 1 - Run clicker
# 2 - Creates a session
```

# Windows manual installation
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env-example .env
# Here you must specify your API_ID and API_HASH, the rest is taken by default
python main.py
```

You can also use arguments for quick start, for example:
```shell
~/NotPixelBot >>> python main.py --action (1/2)
# Or
~/NotPixelBot >>> python main.py -a (1/2)

# 1 - Run clicker
# 2 - Creates a session
```

### Usages
When you first launch the bot, create a session for it using the 'Creates a session' command. It will create a 'sessions' folder in which all accounts will be stored, as well as a file accounts.json with configurations.
If you already have sessions, simply place them in a folder 'sessions' and run the clicker. During the startup process you will be able to configure the use of a proxy for each session.
User-Agent is created automatically for each account.

Here is an example of what accounts.json should look like:
```shell
[
  {
    "session_name": "name_example",
    "user_agent": "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.165 Mobile Safari/537.36",
    "proxy": "type://user:pass:ip:port"  # "proxy": "" - if you dont use proxy
  }
]
```




