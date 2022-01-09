"""import discord.ext.commands as y;a=y.Bot(command_prefix="|~|")
@a.command()
async def r(c):
 e=c.message;g=e.content[4:];j=e.reference;await e.delete()
 if j:n=await c.fetch_message(j.message_id);await n.reply(g)
 else:await c.send(g)
a.run("OTI2NzUwODc4NDQ5NDAxOTE2.YdAOAw.O-v1QVdCuNGuQvAb-J6wZLr2OjE")
"""

"""import re
print(re.findall(r"<@!(\d{18})>", "<@!718082902696525995>"))"""



def makebold(fn):
    print("1")
    def wrapped(текст):
        return "<b>" + fn(текст) + "</b>"
    return wrapped

@makebold
def hi(текст):
    return текст

print(hi("лгыураглуыалгн"))