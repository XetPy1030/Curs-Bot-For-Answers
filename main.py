import discord
import config.config as conf

import commands.sendFromYourself

def load():
    try:
        with open("config/prefix", "r") as f:
            return f.read()
    except:
        return conf.main_prefix

#немного фактов: Курц ты крут:D
class DisBot(discord.Client):
    debug = True
    main_prefix = conf.main_prefix #prefix not will change
    prefix = ">" #prefix will change
    commands = {
        "r": commands.sendFromYourself.command()
    }
    
    async def on_ready(self):
        print("Бот начал работу")
        
    async def call_cmd(self, msg, full_cmd):
        if self.debug:
            print("Call cmd")
        
        # команда - imperior call 1827
        cmd = []
        full_cmd_s = full_cmd.split(" ")
        i = 0
        while i < len(full_cmd_s):
            if full_cmd_s[i] == "":
                pass
            else:
                cmd.append(full_cmd_s[i])
            i += 1
            
        if not len(cmd):
            raise "Not command"
        
        if self.debug:
            print("ЦМД 2")
            print(full_cmd)
            print(full_cmd_s)
            print(cmd)
            print(self.commands.keys())
        
        for i in self.commands.keys():
            if cmd[0].lower() == i:
                if self.debug:
                    print("Команда равняется")
                await self.commands[i].run(msg, cmd)

    async def on_message(self, message):
        if self.debug:
            print(message.reference)
            print(message.mentions)
        #if message.author.id != self.user.id:
        if message.content.startswith(self.prefix):
            if self.debug:
                print("Команда 1")
            cmd = message.content[len(self.prefix):]
            await self.call_cmd(message, cmd)
        elif message.content.startswith(self.main_prefix):
            if self.debug:
                print("Команда 2")
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