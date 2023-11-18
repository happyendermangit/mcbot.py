from mcbot import McBot

bot = McBot("localhost","password","c:/.../...",useRcon=True) 
# when useRcon is true, then you are able to:
# run a command or use tellraw
# if it's false, then you are able only to use 
# the information outside of minecraft 
# if u put it to false, the just leave the ip and RconPassword empty

def onJoin(event):
    print('onJoin triggered')
    print("username: "+event.get('username'))
    print("ip: "+event.get('ip'))

    player = event.get('username')
    ip = event.get('ip')
    
    bot.sendMsg(f'[onJoin test] {player} has joined and his ip is {ip}','yellow',"@a")

def onMessage(event):
    print('onMessage triggered')
    print("username: "+event.get('username'))
    print("message: "+event.get('message'))

    bot.sendMsg(f"[onMessage test] [{event.get('username')}] {event.get('message')}","#f59842","@a")

def onLeave(event):
    print('onLeave triggered')
    print("username: "+event.get('username'))
    bot.sendMsg(f"[onLeave test] {event.get('username')} has left!","red","@a")

def onCommand(event):
    print('onCommand triggered')
    print("username: "+event.get('username'))
    print("command: "+event.get('command'))

    bot.sendMsg(f"[onCommand test] {event.get('username')} has ran {event.get('command')}","blue","@a")

def onOperator(event):
    print('onOperator triggered')
    print("username: "+event.get('username'))
    print("operatorNow: "+event.get('operatorNow'))

    bot.sendMsg(f"[onOperator test] {event.get('username')} has made {event.get('operatorNow')} a server op","#4287f5","@a")


bot.on("onJoin",onJoin)

bot.on("onLeave",onLeave)

bot.on("onMessage",onMessage)

bot.on("onCommand",onCommand)

bot.on("onOperator",onOperator)






bot.run()