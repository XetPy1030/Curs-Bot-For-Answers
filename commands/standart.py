import commands_other.checklist_types_file

# command = call Ktoto agas 123
class command_standart:
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
    
    async def check(self, cl, msg, cmd):
        try:
            if "noBot" in cl["main"]["param"]:
                if msg.author.bot:
                    raise "ErrorCheck"
            if "isBot" in cl["main"]["param"]:
                if not msg.author.bot:
                    raise "ErrorCheck"
            if "iam" in cl["main"]["param"]:
                if not msg.author.id == self.user.id:
                    raise "ErrorCheck"
            if "noI" in cl["main"]["param"]:
                if not msg.author.id != self.user.id:
                    raise "ErrorCheck"
            if "msgReference" in cl["main"]["param"]:
                if not msg.reference != None:
                    raise "ErrorCheck"
            if "noReference" in cl["main"]["param"]:
                if not msg.reference == None:
                    raise "ErrorCheck"
            if "doMention" in cl["main"]["param"]:
                if not len(msg.mentions)>0:
                    raise "ErrorCheck"
            if "noMention" in cl["main"]["param"]:
                if not len(msg.mentions)==0:
                    raise "ErrorCheck"
            return True
        except:
            return False
    
    async def run(self, msg, cmd):#not changed
        isError = await self.check(self.checklist, msg, cmd) #return False if is correct, return Error if.. Yes
        
        if not isError:
            return True #all correct and succesful run
        else:
            return isError
        
    def __str__(self):
        print("Команда: {}\nОписание: {}".format(self.manifest["name"], self.manifest["desc"]))