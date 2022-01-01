import commands.standart

class command(commands.standart.command_standart):
    checklist = {"main": {"param": ["noMention"]}}
    
    async def run(self, msg, cmd):
        if await super().check(self.checklist, msg, cmd):
            print("Получилось!")