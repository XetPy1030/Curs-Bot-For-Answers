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
    main_prefix = conf.main_prefix
    prefix = ">"
    commands = {
        ""
    }
    
    async def on_ready(self):
        print("Бот начал работу")
        
    async def call_cmd(self, cmd):
        pass

    async def on_message(self, message):
        if message.author.id != self.user.id:
            if message.content.startswith(self.prefix):
                cmd = message[len(self.prefix):]
                await self.call_cmd(cmd)
            elif message.content.startswith(len(self.main_prefix)):
                cmd = message[len(self.main_prefix):]
                await self.call_cmd(cmd)
                
                
                msg = message.content[len(comPref+forBot):]
                if msg.replace(" ", "") != "":
                    if message.reference:
                        ms = await message.channel.fetch_message(message.reference.message_id)

                        await ms.reply(msg)
                    else:
                        await message.channel.send(msg)
                await message.delete()

client = DisBot()
client.prefix = load()
client.run(conf.token)