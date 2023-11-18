from mcrcon import MCRcon as r
import time,re 

PATTERN = r"\[(.*?)\] \[(.*?)\]:"


class McBot:
    def __init__(self,ip,Rconpassword,serverPath,useRcon=True):
        self.ip = ip 
        self.Rconpassword = Rconpassword
        self.serverPath = serverPath
        self.mcr = None 
        self.useRcon = useRcon 
        self.functions = {}
    def detectEvent(self,text):
        event = {}
        event['date'] = text.split(']')[0].replace('[','').strip()
        event['type'] = text.split(']')[1].replace('[','').strip() 
        log = text.replace(re.match(PATTERN,text)[0],"")
        print(event['type'])
        event['text'] = log

        # onJoin 

        if "logged in with entity id" in log:
            event['username'] = log.split('[')[0].strip()
            event['ip'] = log.split('[')[1].split(' ')[0]
            
            if self.functions.get('onJoin') and event['type'] == "Server thread/INFO": 
                self.functions.get('onJoin')(event)

        # onMessage 

        if "Async Chat Thread" in event['type']:
            event['username'] = log.split('<')[1].split('>')[0].strip()
            event['message'] = log.split('<')[1].split('>')[1]
                
            if self.functions.get('onMessage'): 
                self.functions.get('onMessage')(event)

        # onLeave 

        if "left the game" in log and event['type'] == "Server thread/INFO":
            event['username'] = log.split('left the game')[0].strip()
            if self.functions.get('onLeave'): 
                self.functions.get('onLeave')(event)

        # onOperator

        if "a server operator" in log and event['type'] == "Server thread/INFO":
            event['operatorNow'] = log.split('[')[1].split(':')[1].split('Made')[1].split('a ')[0].strip()
            event['username'] = log.split('[')[1].split(':')[0].strip()
            if self.functions.get('onOperator'): 
                self.functions.get('onOperator')(event)

        print(log)

        # onCommand 
        if "issued server command:" in log and event['type'] == "Server thread/INFO":
            d = log.split('issued server command:')
            event['username'] = d[0].strip()
            event['command'] = d[1].strip()

            if self.functions.get('onCommand'): 
                self.functions.get('onCommand')(event)



    def run(self):
        if self.useRcon:
            with r(self.ip, self.Rconpassword) as mcr:
                self.mcr = mcr 
                resp = mcr.command('tellraw @a {"text":"ServerBot is running and working fine.","color":"green"}')
                print(resp)
                print('Listening for logs.')
                oldLog = None
                while True:
                    with open(f'{self.serverPath}/logs/latest.log','r') as f:
                        latestLog = f.read().splitlines()[-1]
                        if latestLog != oldLog:
                            self.detectEvent(latestLog)
                            oldLog = latestLog
        else:
            print('Listening for logs.')
            oldLog = None
            while True:
                with open(f'{self.serverPath}/logs/latest.log','r') as f:
                    latestLog = f.read().splitlines()[-1]
                    if latestLog != oldLog:
                        self.detectEvent(latestLog)
                        oldLog = latestLog
    def on(self,event,callback):
        self.functions[event] = callback


    def sendMsg(self,text,color,selector):
        d = self.mcr.command(f'tellraw {selector} '+'{"text":"'+text+'","color":"'+color+'"'+"}")
        print(d) 




