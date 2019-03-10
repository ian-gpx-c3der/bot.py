# -*- coding: utf-8 -*-
import requests,random,re,discord,asyncio,json
c = discord.Client()
prefix = "::"

@c.event
async def on_ready():
    print("online")
@c.event
async def on_member_join(member):
    embed=discord.Embed(title="Novo membro",colour=discord.Colour.gold())
    embed.set_thumbnail(url="https://66.media.tumblr.com/ff6830101337178a58f86d2013cdcf8a/tumblr_pdbzuwtSIe1xc799do1_400.gif")
    embed.add_field(name="seja bem vindo ao servidor",value=''.join(member.mention),inline=True)
    await c.send_message(c.get_channel("550157161280569345"),embed=embed)
@c.event
async def on_member_remove(member):
    embed=discord.Embed(title="-1 membro",colour=discord.Colour.gold())
    embed.set_thumbnail(url="https://66.media.tumblr.com/ff6830101337178a58f86d2013cdcf8a/tumblr_pdbzuwtSIe1xc799do1_400.gif")
    embed.add_field(name="ate mais",value=member.mention,inline=True)
    await c.send_message(c.get_channel("550414256936583168"),embed=embed)
@c.event

async def on_message(msg):
    args = msg.content.split(" ")[1:]
    if prefix+"ban" in msg.content:
        try:
            await c.ban(msg.mentions[0])
            embed=discord.Embed(title="banido com sucesso",colour=discord.Colour.red())
            embed.set_thumbnail(url="https://66.media.tumblr.com/ff6830101337178a58f86d2013cdcf8a/tumblr_pdbzuwtSIe1xc799do1_400.gif")
            embed.add_field(name="quem  foi banido",value=msg.mentions[0],inline=True)
            await c.send_message(msg.channel,embed=embed)
        except Exception as e:
            embed=discord.Embed(title="erro ao banir",colour=discord.Colour.gold())
            embed.set_thumbnail(url="https://66.media.tumblr.com/ff6830101337178a58f86d2013cdcf8a/tumblr_pdbzuwtSIe1xc799do1_400.gif")
            embed.add_field(name="erro:",value=e,inline=True)
            await c.send_message(msg.channel,embed=embed)
 
    elif prefix+"help" in msg.content:
        embed=discord.Embed(title="ajuda", url="https://1.bp.blogspot.com/-Ip3W56EM0_w/Wi01iPSvI6I/AAAAAAAADcs/aRCYi-ov1ycsk2wvcvg1fhkuBJ_12VARwCLcBGAs/s640/jaz.jpg")
        embed.set_thumbnail(url="https://1.bp.blogspot.com/-Ip3W56EM0_w/Wi01iPSvI6I/AAAAAAAADcs/aRCYi-ov1ycsk2wvcvg1fhkuBJ_12VARwCLcBGAs/s640/jaz.jpg")
        embed.add_field(name="ajuda", value="::help", inline=True)
        embed.add_field(name="ajuda5", value="::memes", inline=True)
        embed.add_field(name="ajuda5", value="::gasosa", inline=True)
        await c.send_message(msg.channel,embed=embed)

    elif prefix+"memes" in msg.content:
        url = "http://api.giphy.com/v1/gifs/search?api_key=&q=memes"
        cl = bytes.decode(requests.get(url).content)
        c1 = json.loads(cl)
        urls = []
        for i in c1["data"]:
            u = i["images"]
            r = u["original"]
            l = r["url"]
            urls.append(l)
        embed=discord.Embed(title="bot", url="https://1.bp.blogspot.com/-Ip3W56EM0_w/Wi01iPSvI6I/AAAAAAAADcs/aRCYi-ov1ycsk2wvcvg1fhkuBJ_12VARwCLcBGAs/s640/jaz.jpg")
        embed.set_thumbnail(url="https://1.bp.blogspot.com/-Ip3W56EM0_w/Wi01iPSvI6I/AAAAAAAADcs/aRCYi-ov1ycsk2wvcvg1fhkuBJ_12VARwCLcBGAs/s640/jaz.jpg")
        embed.set_footer(text="feito por The End ritmo carnavale#8057",icon_url="https://1.bp.blogspot.com/-Ip3W56EM0_w/Wi01iPSvI6I/AAAAAAAADcs/aRCYi-ov1ycsk2wvcvg1fhkuBJ_12VARwCLcBGAs/s640/jaz.jpg")
        embed.add_field(name="memes",value='xd',inline=True)
        embed.set_image(url=random.choice(urls))



        await c.send_message(msg.channel,embed=embed)
    elif prefix+"gasosa" in msg.content:
        url = "http://api.giphy.com/v1/gifs/search?api_key=&q=hot%20boobs"
        cl = bytes.decode(requests.get(url).content)
        c1 = json.loads(cl)
        urls = []
        for i in c1["data"]:
            u = i["images"]
            r = u["original"]
            l = r["url"]
            urls.append(l)
        embed=discord.Embed(title="bot", url="https://1.bp.blogspot.com/-Ip3W56EM0_w/Wi01iPSvI6I/AAAAAAAADcs/aRCYi-ov1ycsk2wvcvg1fhkuBJ_12VARwCLcBGAs/s640/jaz.jpg")
        embed.set_thumbnail(url="https://1.bp.blogspot.com/-Ip3W56EM0_w/Wi01iPSvI6I/AAAAAAAADcs/aRCYi-ov1ycsk2wvcvg1fhkuBJ_12VARwCLcBGAs/s640/jaz.jpg")
        embed.set_footer(text="feito por The End ritmo carnavale#8057",icon_url="https://1.bp.blogspot.com/-Ip3W56EM0_w/Wi01iPSvI6I/AAAAAAAADcs/aRCYi-ov1ycsk2wvcvg1fhkuBJ_12VARwCLcBGAs/s640/jaz.jpg")
        embed.add_field(name="gasosa",value='xd',inline=True)
        embed.set_image(url=random.choice(urls))
        print(random.choice(urls))
        await c.send_message(msg.channel,embed=embed)


    elif prefix+"free fire" in msg.content:
        embed=discord.Embed(title="bot", url="https://1.bp.blogspot.com/-Ip3W56EM0_w/Wi01iPSvI6I/AAAAAAAADcs/aRCYi-ov1ycsk2wvcvg1fhkuBJ_12VARwCLcBGAs/s640/jaz.jpg")
        embed.set_thumbnail(url="https://1.bp.blogspot.com/-Ip3W56EM0_w/Wi01iPSvI6I/AAAAAAAADcs/aRCYi-ov1ycsk2wvcvg1fhkuBJ_12VARwCLcBGAs/s640/jaz.jpg")
        embed.set_footer(text="feito por The End ritmo carnavale#8057",icon_url="https://1.bp.blogspot.com/-Ip3W56EM0_w/Wi01iPSvI6I/AAAAAAAADcs/aRCYi-ov1ycsk2wvcvg1fhkuBJ_12VARwCLcBGAs/s640/jaz.jpg")
        embed.add_field(name="memes",value='xd',inline=True)
        embed.set_image(url="https://pm1.narvii.com/7046/cc5bb01271fcb10dc11cde929248c87082a8ce42r1-717-470v2_00.jpg")
        await c.send_message(msg.channel,embed=embed)
   c.run('')
