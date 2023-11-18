# McBot.py (Minecraft bot.py)
[![Discord](https://img.shields.io/discord/1103066670576193627?style=for-the-badge&color=%235562EA)](https://discord.gg/Q6UYNawvaF)
 ![GitHub contributors](https://img.shields.io/github/contributors/happyendermangit/mcgen-launcher?style=for-the-badge) ![GitHub issues](https://img.shields.io/github/issues/happyendermangit/mcgen-launcher?style=for-the-badge)

## 🚀 The best minecraft servers logger bot.

### Star the repo if it helped you!

**PYTHON is required for the bot to work**

## How to use?
1. clone the repo:
```sh
$ git clone https://github.com/happyendermangit/mcbot-py.git
```

2. Install modules
```sh
$ pip -r reqs.txt
```
3. Change the config
```py
bot = McBot("localhost","password","c:/.../...",useRcon=True) 
            # ip         # password # server path # use rcon or not
```

4. Run the example
```sh
python example.py
```
5. enjoy!


## NOTE:

If you plan to make the bot send messages, then you need to edit your server.propities file 

```diff
# updated:
- enable-rcon=false
+ enable-rcon=true
- rcon.password=
+ rcon.password= SECURE_PASSWORD_HERE (DONT PUT A NOT SECURE PASSWWORD)
```


**If you plan to use it onlly for logs, then it's not required** 

## Events:

- _``onJoin``_:
    - **`username`**: the username of the player that joined
    - **`ip`**: the ip of the player that joined
    
- _``onLeave``_:
    - **`username`**: the username of the player that left

- _``onMessage``_:
    - **`username`**: the username of the player that sent the message
    - **`message`**: the message that got sent 
- _``onCommand``_:
    - **`username`**: the username of the player that ran the command
    - **`command`**: the command that got ran 
- _``onOperator``_:
    - **`username`**: the username of the player that made the user a server operator
    - **`operatorNow`**: the user that is turned into a operator

- _``Defaut variables``_:
    - **`date`**: the date of the event 
    - **`type`**: the type of the event that is in minecraft console
    - **`text`**: the text of the event that is in minecraft consol 







Made by happy enderman™️
