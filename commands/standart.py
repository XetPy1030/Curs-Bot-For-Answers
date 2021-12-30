# command = call Ktoto agas 123

class command_standart:
    manifest = {"name": "base", "desc": "Base class for commands"}
    checklist_types = {"standart": {"main": ["NoBot", "NoI"]},
                       }
    checklist = {"main": []} # {"main": [], "0": [], "1": []}
    
    def __init__(self):
        pass
    
    async def check(self, msg, cmd):
        pass
    
    async def run(self, msg, cmd):#not changed
        isError = await self.check(msg, cmd) #return False if is correct, return Error if.. Yes
        
        if not isError:
            return True #all correct and succesful run
        else:
            return isError
        
    def __str__(self):
        print("Команда: {}\nОписание: {}".format(self.manifest["name"], self.manifest["desc"]))