from mcbot import McBot
import requests 

bot = McBot("","","c:/...../.....",useRcon=False) 
# when useRcon is true, then you are able to:
# run a command or use tellraw
# if it's false, then you are able only to use 
# the information outside of minecraft 
# if u put it to false, the just leave the ip and RconPassword empty

chat_webhook = "https://discord.com/api/webhooks/............/..............................................."

logs_webhook = "https://discord.com/api/webhooks/............/..............................................."


def log(msg):
    r = requests.post(logs_webhook,headers={"content-type":"application/json"},json={
        "content":msg
    })

def chat(msg,username):
    r = requests.post(chat_webhook,headers={"content-type":"application/json"},json={
        "content":msg,
        "username":username
    })


def onJoin(event):
    print('onJoin triggered')
    print("username: "+event.get('username'))
    print("ip: "+event.get('ip'))

    player = event.get('username')
    ip = event.get('ip')
    
    log(f'[onJoin] {player} has joined and his ip is {ip}')

def onMessage(event):
    print('onMessage triggered')
    print("username: "+event.get('username'))
    print("message: "+event.get('message'))

    chat(f"[onMessage] [{event.get('username')}] {event.get('message')}",event.get('username'))

def onLeave(event):
    print('onLeave triggered')
    print("username: "+event.get('username'))
    log(f"[onLeave] {event.get('username')} has left!")

def onCommand(event):
    print('onCommand triggered')
    print("username: "+event.get('username'))
    print("command: "+event.get('command'))

    log(f"[onCommand] {event.get('username')} has ran {event.get('command')}")

def onOperator(event):
    print('onOperator triggered')
    print("username: "+event.get('username'))
    print("operatorNow: "+event.get('operatorNow'))

    log(f"[onOperator] {event.get('username')} has made {event.get('operatorNow')} a server op")


bot.on("onJoin",onJoin)

bot.on("onLeave",onLeave)

bot.on("onMessage",onMessage)

bot.on("onCommand",onCommand)

bot.on("onOperator",onOperator)






bot.run()