import discord
import config.config as conf

def load():
    try:
        with open("config/prefix", "r") as f:
            return f.read()
    except:
        return conf.main_prefix

#немного фактов: Курц ты крут:D
class DisBot(discord.Client):
    main_prefix = conf.main_prefix #prefix not will change
    prefix = ">" #prefix will change
    commands = {
        ""
    }
    
    async def on_ready(self):
        print("Бот начал работу")
        
    async def call_cmd(self, msg, full_cmd):
        # команда - imperior call 1827
        cmd = []
        full_cmd_s = full_cmd.split(" ")
        i = 0
        while i < len(full_cmd_s):
            if full_cmd_s[i] == "":
                pass
            else:
                cmd += full_cmd_s[i]
            i += 1
            
        if not len(cmd):
            raise "Not command"
        
        for i in self.commands.keys():
            if cmd[0].lower() == i:
                await self.commands[i].run(msg, cmd[1:])
        
        

    async def on_message(self, message):
        if message.author.id != self.user.id:
            if message.content.startswith(self.prefix):
                cmd = message.content[len(self.prefix):]
                await self.call_cmd(message, cmd)
            elif message.content.startswith(len(self.main_prefix)):
                cmd = message.content[len(self.main_prefix):]
                await self.call_cmd(message, cmd)
                
                
"""                msg = message.content[len(comPref+forBot):]
                if msg.replace(" ", "") != "":
                    if message.reference:
                        ms = await message.channel.fetch_message(message.reference.message_id)

                        await ms.reply(msg)
                    else:
                        await message.channel.send(msg)
                await message.delete()"""

if __name__ == "__main__":
    client = DisBot()
    client.prefix = load()
    client.run(conf.token)