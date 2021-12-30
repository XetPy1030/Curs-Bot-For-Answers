# command = call Ktoto agas 123

class command_standart:
    def __init__(self):
        pass
    
    async def check(self):#replaced
        pass
    
    async def run(self):#not changed
        isError = await self.check() #return False if is correct, return Error if.. Yes
        
        if not isError:
            return True #all correct and succesful run
        else:
            return isError