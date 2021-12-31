import commands.standart

class command(commands.standart.command_standart):
    async def run(self, msg, cmd):
        if super().check(msg, cmd):
            print("Получилось!")