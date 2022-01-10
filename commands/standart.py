import commands_other.checklist_types_file
import re

# command = call Ktoto agas 123
class command_standart:
    work = True
    manifest = {"name": "base", "desc": "Base class for commands"}
    checklist_types = commands_other.checklist_types_file.checklist_types
    checklist = {"main": {"param": [], "paramEqual": {
                                                   "author": [],
                                                   "embeds": [],
                                                   "channel": [],
                                                   "reference": [],
                                                   "mention": [],
                                                   "channel_mentions": [],
                                                   "role_mentions": [],
                                                   "attachments": [],
                                                   "guild": [],
                                                   "created_at": []
                                                   }}} # {"main": [], "0": [], "1": []}
    
    def __init__(self):
        pass
    
    async def check(self, msg, cmd):
        try:
            if "noBot" in self.checklist["main"]["param"]:
                if msg.author.bot:
                    raise "ErrorCheck"
            if "isBot" in self.checklist["main"]["param"]:
                if not msg.author.bot:
                    raise "ErrorCheck"
            if "iam" in self.checklist["main"]["param"]:
                if not msg.author.id == self.user.id:
                    raise "ErrorCheck"
            if "noI" in self.checklist["main"]["param"]:
                if not msg.author.id != self.user.id:
                    raise "ErrorCheck"
            if "msgReference" in self.checklist["main"]["param"]:
                if not msg.reference != None:
                    raise "ErrorCheck"
            if "noReference" in self.checklist["main"]["param"]:
                if not msg.reference == None:
                    raise "ErrorCheck"
            if "doMention" in self.checklist["main"]["param"]:
                if not len(re.findall(r"<@!(\d{18})>", msg.content))>0:
                    raise "ErrorCheck"
            if "noMention" in self.checklist["main"]["param"]:
                if len(re.findall(r"<@!(\d{18})>", msg.content))!=0:
                    raise "ErrorCheck"
            return True
        except:
            return False
    
    async def run(self, msg, cmd):#not changed
        isError = await self.check(msg, cmd) #return False if is correct, return Error if.. Yes
        
        if not isError:
            return True #all correct and succesful run
        else:
            return isError
        
    def __str__(self):
        print("Команда: {}\nОписание: {}".format(self.manifest["name"], self.manifest["desc"]))