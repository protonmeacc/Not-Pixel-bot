[![Static Badge](https://img.shields.io/badge/Telegram-Bot%20Link-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/notpixel/app?startapp=f411905106)

## ⚡⚡ Get 3x rewards with fully automatic art parsing and smart pixel selection 🆕 ⚡⚡

## Recommendation before use

## 🔥🔥 Use PYTHON 3.10 🔥🔥

## Features  
| Feature                                                  | Supported |
|----------------------------------------------------------|:---------:|
| Asynchronous processing                                  |     ✅     |
| Proxy binding to session                                 |     ✅     |
| User-Agent binding to session                            |     ✅     |
| Support pyrogram .session                                |     ✅     |
| Registration in bot                                      |     ✅     |
| Auto-tasks                                               |     ✅     |
| Daily rewards                                            |     ✅     |
| Pause feature on reaching maximum error threshold 🆕     |     ✅     |
| Drawing specified image 🆕                               |     ✅     |
| Fully automatic art parsing and smart pixel selection 🆕 |     ✅     |

## Settings  
| **Parameter**                      | **Description**                                                 |
|------------------------------------|:----------------------------------------------------------------|
| **API_ID / API_HASH**              | Your API_ID / API_HASH                                          |
| **SLEEP_TIME**                     | Sleep time between cycles (by default - [426, 4260])            |
| **START_DELAY**                    | Delay between sessions at start (by default - [1, 240])         |
| **ERROR_THRESHOLD**                | Maximum number of errors allowed before action (default - 5)    |
| **TIME_WINDOW_FOR_MAX_ERRORS**     | Time duration in which the maximum error count can be reached   |
| **ERROR_THRESHOLD_SLEEP_DURATION** | Sleep duration after reaching the maximum error threshold       |
| **SLEEP_AFTER_EACH_ERROR**         | Sleep time after each individual error occurrence               |
| **AUTO_DRAW**                      | Auto-drawing pixels (default - True)                            |
| **AUTO_UPGRADE**                   | Auto-upgrading your mining stuff (default - True)               |
| **CLAIM_REWARD**                   | Claim daily reward (default - True)                             |
| **AUTO_TASK** DANGEROUS            | Auto tasks (default - True)                                     |
| **TASKS_TO_DO** AUTOTASK           | List of tasks for auto-task (default - all tasks)               |
| **JOIN_TG_CHANNELS**               | Automatically join Telegram channels (default - True)           |
| **REF_ID**                         | Thing that goes after startapp=                                 |
| **IGNORED_BOOSTS**                 | List of boosts to ignore (default - empty list)                 |
| **IN_USE_SESSIONS_PATH**           | Path to the file where the currently active sessions are stored |
| **PALETTE**                        | List of colors used for drawing                                 |
| **DRAW_IMAGE**                     | Enable drawing of specified image (default - False)             |
| **DRAWING_START_COORDINATES**      | Starting coordinates for drawing the image (e.g., [10, 5])      |
| **IMAGE_PATH**                     | Path to the image file to be drawn                              |
| **ENABLE_3X_REWARD**               | Enable or disable the 3x reward feature (default - True)        |


## Quick Start 📚

To quickly install libraries and run the bot - open `run.bat` on Windows or `run.sh` on Linux.

## Prerequisites
Before you begin, make sure you have the following installed:
- [Python](https://www.python.org/downloads/) **version 3.10**

## Obtaining API Keys
1. Go to my.telegram.org and log in using your phone number.
2. Select "API development tools" and fill out the form to register a new application.
3. Record the `API_ID` and `API_HASH` provided after registering your application in the `.env` file.

## Installation
You can download the [**repository**](https://github.com/WubbaLubbaDubDubDev/notpixel_bot_advanced) by cloning it to your system and installing the necessary dependencies:
git clone https://github.com/WubbaLubbaDubDubDev/notpixel_bot_advanced


Then you can do automatic installation by typing:

### Windows:
```shell
./run.bat
```

### Linux:
```shell
chmod +x run.sh
./run.sh
```

### Running in Docker

To run the project in Docker, navigate to the root directory of the script and execute the following command:
```shell
docker-compose up --build
```

## Linux manual installation
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env-example .env
nano .env  # Here you must specify your API_ID and API_HASH, the rest is taken by default
python3 main.py
# 1 - Run clicker
# 2 - Creates a session
```

## Windows manual installation
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env-example .env
# Here you must specify your API_ID and API_HASH, the rest is taken by default
python main.py
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
