import commands.standart

class command(commands.standart.command_standart):
    checklist = {"main": {"param": []}}
    
    async def run(self, message, cmd):
        if await super().check(message, cmd):
            if len(cmd)>1:
                if message.reference:
                    ms = await message.channel.fetch_message(message.reference.message_id)

                    await ms.reply(" ".join(cmd[1:]))
                else:
                    await message.channel.send(" ".join(cmd[1:]))
            await message.delete()