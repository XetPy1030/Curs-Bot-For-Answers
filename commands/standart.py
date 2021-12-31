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
    
    async def check(self, msg, cmd):
        isCor = True
        if "noBot" in self.checklist["main"]["param"]:
            isCor = not msg.author.bot
        if "isBot" in self.checklist["main"]["param"]:
            isCor = msg.author.bot
        if "iam" in self.checklist["main"]["param"]:
            isCor = msg.author.id == self.user.id
        if "noI" in self.checklist["main"]["param"]:
            isCor = msg.author.id != self.user.id
        if "msgReference" in self.checklist["main"]["param"]:
            isCor = msg.reference != None
        if "noReference" in self.checklist["main"]["param"]:
            isCor = msg.reference == None
        if "doMention" in self.checklist["main"]["param"]:
            isCor = len(msg.mentions)>0
        if "noMention" in self.checklist["main"]["param"]:
            isCor = len(msg.mentions)==0
    
    async def run(self, msg, cmd):#not changed
        isError = await self.check(msg, cmd) #return False if is correct, return Error if.. Yes
        
        if not isError:
            return True #all correct and succesful run
        else:
            return isError
        
    def __str__(self):
        print("Команда: {}\nОписание: {}".format(self.manifest["name"], self.manifest["desc"]))