from discord_components import DiscordComponents, Button
import discord
import os
from replit import db
import time
import discord.ext
from discord.ext import commands, tasks
import datetime
import random
from keepalive import keep_alive
from profile import make_profile

intent=discord.Intents.all()
intent.members = True 
keep_alive()

bot = commands.Bot(intents=intent, command_prefix = ['k.', 'kairos ', 'k ', 'k!'], case_insensitive=True)
ddb = DiscordComponents(bot)

def inv_append(user, item, amt):
  if amt == "delete":
    del db[user]["inventory"][item]
    return
  if item in db[user]["inventory"].keys():
    db[user]["inventory"][item] += amt
  else:
    db[user]["inventory"][item] = amt

def embed_builder(title, description="", url="", image=None, thumbnail=None, field=[None, None, None]):
  embed=discord.Embed(title=title, url=url, description=description, color=0xffad6e)
  embed.set_author(name="Kairos", icon_url="https://i.imgur.com/v7oz1uc.png")
  if thumbnail:
    embed.set_thumbnail(url=thumbnail)
  if image:
    embed.set_image(url=image)
  if field != [None, None, None]:
    for i in field:
      embed.add_field(name=i[0], value=i[1], inline=i[2])
  return embed

@bot.event
async def on_ready():
  global icono
  global icont
  global iconth
  global iconf
  global current_time

  print("on ready")
  with open('Server_Bot_PFP.png', 'rb') as one:
    icono = one.read()
  with open('Server_Bot_PFP_ED2.png', 'rb') as two:
    icont = two.read()
  with open('Server_Bot_PFP_ED3.png', 'rb') as three:
    iconth = three.read()
  with open('Server_Bot_PFP_ED4.png', 'rb') as four:
    iconf = four.read()
  await bot.change_presence(activity=discord.Game(name='with fate'), status=discord.Status.dnd)

  time_now = (datetime.datetime.now()-datetime.timedelta(hours=4)).time()
  guild = bot.get_guild(859474772654817320)
  if datetime.time(5, 00, 00) <= time_now <= datetime.time(9, 00, 00):
    current_time = 1
    await guild.edit(icon=icono)
  if datetime.time(9, 00, 00) <= time_now <= datetime.time(17, 00, 00):
    current_time = 2
    await guild.edit(icon=icont)
  if datetime.time(17, 00, 00) <= time_now <= datetime.time(20, 00, 00):
    current_time = 3
    await guild.edit(icon=iconth)
  if (datetime.time(20, 00, 00) <= time_now <= datetime.time(23, 59, 59) or (datetime.time(0, 00, 00) <= time_now <= datetime.time(5, 00, 00))):
    current_time = 4
    await guild.edit(icon=iconf)
  update_pfp.start()

@bot.event
async def on_member_join(member):
  await member.send(embed=embed_builder(title="Welcome to District Kairos, your safety is guranteed.", description="District Kairos shields you from danger!", field=[["To start, you can create a charcter with the following command:", "k.start", False], ["You can also see a list of places with:", "k.atlas", False]]))

@bot.command()
async def ping(ctx):
  await ctx.reply("pong")


## sussy khalid wrote this
@bot.command()
async def amogus(ctx):
  await ctx.reply("When the imposter is sus")

@bot.command()
async def super(ctx, idol="", de="", xiao="", rong=""):
  if idol == "idol":
    if de == "de":
      if xiao == "xiao":
        if rong == "rong":      
          await ctx.reply("https://www.youtube.com/watch?v=SGSMLApfe1o")
## sussy khalid wrote this

@bot.command()
async def start(ctx):
  authid = str(ctx.message.author.id)
  if authid in db.keys():
    await ctx.message.author.send(embed=embed_builder(title="You already have a charcter!"))
    return

  await ctx.reply(embed=embed_builder(title="Charcter builder is in your DMs!"))
  
  db[authid] = {}
  db[authid]["money"] = 0
  db[authid]["bank"] = 0
  db[authid]["location"] = "District Kairos"
  db[authid]["state"] = "normal"
  db[authid]["inventory"] = {}
  db[authid]["stats"] = {}
  await ctx.message.author.send(embed=embed_builder(title="Charcter type", description="Select charcter type from the following:", image="https://i.imgur.com/nMFC1b1.png"), components=[[Button(style=4, label="Strength"), Button(style=4, label="Speed"), Button(style=4, label="Alert"), Button(style=4, label="Adaptive")]])

  i = await bot.wait_for("button_click", check = lambda i: i.author == ctx.message.author)

  db[authid]["class"] = str(i.component.label).lower()
  if db[authid]["class"] == "strength":
    db[authid]["stats"]["attack"] = 12
    db[authid]["stats"]["defence"] = 12
    db[authid]["stats"]["speed"] = 6
    db[authid]["stats"]["health"] = 12
  if db[authid]["class"] == "speed":
    db[authid]["stats"]["attack"] = 10
    db[authid]["stats"]["defence"] = 10
    db[authid]["stats"]["speed"] = 25
    db[authid]["stats"]["health"] = 10
  if db[authid]["class"] == "alert":
    db[authid]["stats"]["attack"] = 11
    db[authid]["stats"]["defence"] = 11
    db[authid]["stats"]["speed"] = 22
    db[authid]["stats"]["health"] = 11
  if db[authid]["class"] == "adaptive":
    db[authid]["stats"]["attack"] = 13
    db[authid]["stats"]["defence"] = 14
    db[authid]["stats"]["speed"] = 14
    db[authid]["stats"]["health"] = 14

  await i.send(embed=embed_builder(title="Congratulations", description="you can now run k.profile!"))

@tasks.loop(seconds = 60)
async def update_pfp():
  global current_time
  time_now = (datetime.datetime.now()-datetime.timedelta(hours=4)).time()
  guild = bot.get_guild(859474772654817320)
  if datetime.time(5, 00, 00) <= time_now <= datetime.time(9, 00, 00) and current_time != 1:
    current_time = 1
    await guild.edit(icon=icono)
  if datetime.time(9, 00, 00) <= time_now <= datetime.time(17, 00, 00) and current_time != 2:
    current_time = 2
    await guild.edit(icon=icont)
  if datetime.time(17, 00, 00) <= time_now <= datetime.time(20, 00, 00) and current_time != 3:
    current_time = 3
    await guild.edit(icon=iconth)
  if (datetime.time(20, 00, 00) <= time_now <= datetime.time(23, 59, 59) and  current_time != 4) or (datetime.time(0, 00, 00) <= time_now <= datetime.time(5, 00, 00) and  current_time != 4):
    current_time = 4
    await guild.edit(icon=iconf)

@bot.command(aliases = ["pro"])
async def profile(ctx, member: discord.Member=None):
  if member == None:
    if str(ctx.message.author.id) not in db.keys():
      await ctx.reply(embed=embed_builder(title="You have to run `k.start` first!"))
      return
    make_profile(db[str(ctx.message.author.id)])
    file = discord.File("profile_out.png", filename="profile_out.png")
    await ctx.reply(file=file)
    return

  else:
    if str(member.id) not in db.keys():
      await ctx.reply(embed=embed_builder(title="User does not have a profile!"))
      return
    make_profile(db[str(member.id)])
    file = discord.File("profile_out.png", filename="profile_out.png")
    await ctx.reply(file=file)
    return

@bot.command()
async def atlas(ctx):
  await ctx.reply(embed=embed_builder(title="Atlas", description="A detailed atlas of District Kairos and it's surroundings.", thumbnail="https://media.discordapp.net/attachments/725736146000150538/901930425428090910/N.png?width=660&height=660", field=[
  ["Currect Location", db[str(ctx.message.author.id)]["location"], False], 
  ["District Kairos", "Protected region of the wasteland, hub of economy.", False],
  ["Fortune Street", "Survivor built community, inhumane living conditions.", True],
  ["District Nordton", "Old residential area, now lots of trees.", False],
  ["Metronoia", "Parent city of District Kairos, defination of the concrete jungle.", True]
  ]))

@bot.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def travel(ctx, d1, d2=""):
  if d1+d2.lower() in ["kairos", "dk", "districtkairos"]:
    if db[str(ctx.message.author.id)]["location"] == "District Kairos":
      await ctx.reply(embed=embed_builder(title="Already Here"))
      return
    db[str(ctx.message.author.id)]["location"] = "District Kairos"
    await ctx.reply(embed=embed_builder(title="Traveling", description="Traveled to District Kairos"))
  if d1+d2.lower() in ["fortune", "fs", "fortunestreet"]:
    if db[str(ctx.message.author.id)]["location"] == "Fortune Street":
      await ctx.reply(embed=embed_builder(title="Already Here"))
      return
    db[str(ctx.message.author.id)]["location"] = "Fortune Street"
    await ctx.reply(embed=embed_builder(title="Traveling", description="Traveled to Fortune Street"))
  if d1+d2.lower() in ["nordton", "dn", "districtnordton"]:
    if db[str(ctx.message.author.id)]["location"] == "District Nordton":
      await ctx.reply(embed=embed_builder(title="Already Here"))
      return
    db[str(ctx.message.author.id)]["location"] = "District Nordton"
    await ctx.reply(embed=embed_builder(title="Traveling", description="Traveled to District Nordton"))
  if d1+d2.lower() in ["metronoia", "me", "m"]:
    if db[str(ctx.message.author.id)]["location"] == "Metronoia":
      await ctx.reply(embed=embed_builder(title="Already Here"))
      return
    db[str(ctx.message.author.id)]["location"] = "Metronoia"
    await ctx.reply(embed=embed_builder(title="Traveling", description="Traveled to Metronoia"))
@travel.error
async def travel_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
      await ctx.reply(embed=embed_builder(title="Woah, too fast!", description=f"You can't move that fast! Try again after {error.retry_after:.2f} s!"))

@bot.command()
async def hide(ctx):
  if db[str(ctx.message.author.id)]["state"] == "hiding":
    await ctx.reply(embed=embed_builder(title="You're already hiding!"))
    return
  db[str(ctx.message.author.id)]["state"] = "hiding"
  await ctx.reply(embed=embed_builder(title="Hiding", description="Danger?"))

@bot.command()
async def reveal(ctx):
  if db[str(ctx.message.author.id)]["state"] == "normal":
    await ctx.reply(embed=embed_builder(title="You're not hiding!"))
    return
  db[str(ctx.message.author.id)]["state"] = "normal"
  await ctx.reply(embed=embed_builder(title="Phew", description="Dodged a bullet!"))

@bot.command(aliases = ["n", "act", "continue"])
async def next(ctx):
  
  event = random.randint(1, 7)
  location = db[str(ctx.message.author.id)]["location"]
  user = db[str(ctx.message.author.id)]
  user_id = str(ctx.message.author.id)

  if user["stats"]["health"] < 2:
    await ctx.reply(embed=embed_builder(title="Health too low!"))
    return

  if location == "District Kairos":
    if event > 5:
      await ctx.reply(embed=embed_builder(title="Nothing happened"))
    if event == 1:
      plus = random.randint(2, 4)
      user["money"] += plus
      await ctx.reply(embed=embed_builder(title = "Lucky day", description=f"You walked around District Kairos and got {str(plus)} credits!"))
    if event == 2:
      inv_append(user_id, "Pebble", 1)
      await ctx.reply(embed=embed_builder(title = "Not very useful", description="You walked around District Kairos and found Pebble x1."))
    if event == 3:
      if random.randint(1, 233) == 1:
        inv_append(user_id, "Jack'o Lantern", 1)
        await ctx.reply(embed=embed_builder(title = "Jack'o Lantern!", description="You found a Jack'o Lantern x1!"))
      else:
        await ctx.reply(embed=embed_builder(title="Nothing happened"))
    if event == 4:
      inv_append(user_id, "Coffee", 1)
      await ctx.reply(embed=embed_builder(title="Thanks!", description="You got a free cup of Coffee!"))
    if event == 5:
      inv_append(user_id, "Milk", 1)
      await ctx.reply(embed=embed_builder(title="Thanks!", description="You got a free cup of Milk!"))

  if location == "District Nordton":
    if event > 5:
      await ctx.reply(embed=embed_builder(title="Nothing happened"))
    if event == 1:
      inv_append(user_id, "Scrap Battery", 1)
      await ctx.reply(embed=embed_builder(title = "It's.. eh?", description="You walked around District Nordton and found Scrap Battery x1."))
    if event == 2:
      inv_append(user_id, "Pebble", 2)
      await ctx.reply(embed=embed_builder(title = "Not very useful", description="You walked around District Nordton and found Pebble x2."))
    if event == 3:
      user["stats"]["health"] -= random.randint(2, 5)
      if user["stats"]["health"] < 2:
        user["stats"]["health"] = 1
        await ctx.reply(embed=embed_builder(title = "Danger!", description="You were attack by a group of infected! You barely escaped with 1 health left!"))
      else:
        await ctx.reply(embed=embed_builder(title = "Danger!", description=f"You were attack by a group of infected! You fought with {str(user['stats']['health'])} health left!"))
    if event == 4:
      inv_append(user_id, "Scrap Metal", 1)
      await ctx.reply(embed=embed_builder(title = "Nice?", description="You walked around District Nordton and found Scrap Metal x1."))
    if event == 5:
      if random.randint(1, 25) == 1:
        user["money"] += 50
        await ctx.reply(embed=embed_builder(title = "Jack pot!", description="You found 50 credits from an abandoned house!"))
      else:
        await ctx.reply(embed=embed_builder(title="Nothing happened"))

  if location == "Fortune Street":
    if event > 4:
      await ctx.reply(embed=embed_builder(title="Nothing happened"))
    if event == 1:
      if user["money"] > 0:
        user["money"] -= 1
        inv_append(user_id, "Stale Bread", 1)
        await ctx.reply(embed=embed_builder(title = "Morality", description="You gave a begger 1 credit, in exchange you received Stale Bread x1."))
      else:
        await ctx.reply(embed=embed_builder(title="Nothing happened"))
    if event == 2:
      if user["money"] > 5:
        user["money"] -= 6
        inv_append(user_id, "Cotton", 1)
        await ctx.reply(embed=embed_builder(title = "Purchase", description="You bought Cotton x1 from a farmer for 6 credits."))
      else:
        await ctx.reply(embed=embed_builder(title="Nothing happened"))
    if event == 3:
      user["money"] = int(0.9 * user["money"])
      await ctx.reply(embed=embed_builder(title = "Tyranny", description=f"The ruler of Fortune Street forced a 10% tax, you now have {str(user['money'])} credits."))
    if event == 4:
      if random.randint(1, 5) == 1:
        user["stats"]["attack"] += 1
        await ctx.reply(embed=embed_builder(title = "Mobsters", description="You fought off an angry mob; Attack + 1."))
      else:
        await ctx.reply(embed=embed_builder(title="Nothing happened"))

  if location == "Metronoia":
    if event > 2:
      user["stats"]["health"] = 1
      await ctx.reply(embed=embed_builder(title="Danger!", description="You were attacked by a mutant, you escaped with 1 health left."))
    if event == 1:
      user["stats"]["speed"] += 1
      await ctx.reply(embed=embed_builder(title="Danger!", description="You were attacked by a mutant, you escaped by outrunning it; Speed + 1."))
    if event == 2:
      user["stats"]["defence"] += 1
      await ctx.reply(embed=embed_builder(title="Danger!", description="You were attacked by a mutant, you escaped unscathed; Defence + 1."))
      

@bot.command()
@commands.cooldown(1, 120, commands.BucketType.user)
async def rest(ctx):
  amt = random.randint(2, 5)
  if db[str(ctx.message.author.id)]["stats"]["health"] < 10:
    db[str(ctx.message.author.id)]["stats"]["health"] += amt
    await ctx.reply(embed=embed_builder(title=f"you rested and gained {str(amt)} health!"))
    return
  await ctx.reply(embed=embed_builder(title="you rested but didn't gain any health."))

@rest.error
async def rest_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
      await ctx.reply(embed=embed_builder(title="Woah, too fast!", description=f"You can rest again after {error.retry_after:.2f} s!"))

@bot.command(aliases = ["inv", "i"])
async def inventory(ctx, member: discord.Member=None):
  if member == None:
    if str(ctx.message.author.id) not in db.keys():
      await ctx.reply(embed=embed_builder(title="You have to run `k.start` first!"))
      return
    name = ctx.message.author.name
    inventory = db[str(ctx.message.author.id)]["inventory"]
  else:
    if str(member.id) not in db.keys():
      await ctx.reply(embed=embed_builder(title="User does not have a profile!"))
      return
    name = member.name
    inventory = db[str(member.id)]["inventory"]
  if inventory != {}:
    await ctx.reply(embed=embed_builder(title="Inventory", description=f"{name}'s inventory", field=[[f"{i}", f" x{inventory[i]}", True] for i in sorted(inventory)]))
  else:
    await ctx.reply(embed=embed_builder(title="Inventory", description=f"{name}'s inventory is empty!"))

@bot.command()
async def use(ctx, qty: int, item1="", item2="", item3=""):
  inventory = db[str(ctx.message.author.id)]["inventory"]
  user = db[str(ctx.message.author.id)]
  user_id = str(ctx.message.author.id)
  item = item1+item2+item3
  if qty < 1:
    await ctx.reply(embed=embed_builder(title="Quantity must be greater than one."))
    return
  if item == "":
    await ctx.reply(embed=embed_builder(title="What item are you trying to use?"))
    return

  if item.lower() == "stalebread":
    if "Stale Bread" in inventory.keys() and inventory["Stale Bread"] >= qty:
      await ctx.reply(embed=embed_builder(title="Crunchy...", description=f"you received {str(qty*2)} health!"))
      user["stats"]["health"] += qty*2
      if qty == inventory["Stale Bread"]:
        inv_append(user_id, "Stale Bread", "delete")
      else:
        inv_append(user_id, "Stale Bread", -qty) 
    else:
      await ctx.reply(embed=embed_builder(title="You don't have that much!"))
      return

  elif item.lower() == "coffee":
    if "Coffee" in inventory.keys() and inventory["Coffee"] >= qty:
      await ctx.reply(embed=embed_builder(title="Bitterness", description=f"you received {str(qty)} speed!"))
      user["stats"]["speed"] += qty
      if qty == inventory["Coffee"]:
        inv_append(user_id, "Coffee", "delete")
      else:
        inv_append(user_id, "Coffee", -qty)  
    else:
      await ctx.reply(embed=embed_builder(title="You don't have that much!"))
      return

  elif item.lower() == "milk":
    if "Milk" in inventory.keys() and inventory["Milk"] >= qty:
      await ctx.reply(embed=embed_builder(title="Gulp.. gulp", description=f"you received {str(qty)} defence!"))
      user["stats"]["defence"] += qty
      if qty == inventory["Milk"]:
        inv_append(user_id, "Milk", "delete")
      else:
        inv_append(user_id, "Milk", -qty)  
    else:
      await ctx.reply(embed=embed_builder(title="You don't have that much!"))
      return

  elif item.lower() == "latte":
    if "Latte" in inventory.keys() and inventory["Latte"] >= qty:
      await ctx.reply(embed=embed_builder(title="That's good", description=f"you received {str(qty)} defence and {str(qty)} speed!"))
      user["stats"]["defence"] += qty
      user["stats"]["speed"] += qty      
      if qty == inventory["Latte"]:
        inv_append(user_id, "Latte", "delete")
      else:
        inv_append(user_id, "Latte", -qty)  
    else:
      await ctx.reply(embed=embed_builder(title="You don't have that much!"))
      return

  else:
    await ctx.reply(embed=embed_builder(title="Item does not exist, or is unusable."))
    return
  
@bot.command(aliases = ["dep"])
async def deposit(ctx, amt: int):
  if amt < 0:
    await ctx.reply(embed=embed_builder(title="Amount must be greater than zero!"))
    return
  if amt > db[str(ctx.message.author.id)]["money"]:
    await ctx.reply(embed=embed_builder(title = "You don't have that much!"))
    return
  db[str(ctx.message.author.id)]["money"] -= amt
  db[str(ctx.message.author.id)]["bank"] += amt
  await ctx.reply(embed=embed_builder(title = "Deposit", description=f"You deposited {str(amt)} credits."))

@bot.command(aliases = ["with"])
async def withdraw(ctx, amt: int):
  if amt < 0:
    await ctx.reply(embed=embed_builder(title="Amount must be greater than zero!"))
    return
  if amt > db[str(ctx.message.author.id)]["bank"]:
    await ctx.reply(embed=embed_builder(title = "You don't have that much!"))
    return
  db[str(ctx.message.author.id)]["bank"] -= amt
  db[str(ctx.message.author.id)]["money"] += amt
  await ctx.reply(embed=embed_builder(title = "Withdraw", description=f"You withdrew {str(amt)} credits."))


@bot.command()
async def craftbook(ctx):
  await ctx.reply(embed=embed_builder(
    title = "Craftbook",
    description = "A craftbook for everything",
    field=[
      ["Latte", "A warm coffee drink - Milk x1, Coffee x1", False],
      ["Metal Chunk", "Compressed scrap metal - Scrap Metal x4", False]





    ]
  ))


@bot.command()
async def craft(ctx, qty: int, item1="", item2="", item3=""):
  inventory = db[str(ctx.message.author.id)]["inventory"]
  user_id = str(ctx.message.author.id)
  item = item1+item2+item3
  item = item.lower()



  if qty < 1:
    await ctx.reply(embed=embed_builder(title="Quantity must be greater than zero."))
    return
  if item == "":
    await ctx.reply(embed=embed_builder(title="What are you trying to craft?"))
    return

  if item == "latte":
    if "Milk" in inventory.keys() and inventory["Milk"] >= 1*qty:
      if "Coffee" in inventory and inventory["Coffee"] >= 1*qty:

        if 1*qty == inventory["Milk"]:
          inv_append(user_id, 'Milk', "delete")
        else:
          inv_append(user_id, 'Milk', -1*qty)
        
        if 1*qty == inventory["Coffee"]:
          inv_append(user_id, 'Coffee', "delete")
        else:
          inv_append(user_id, 'Coffee', -1*qty)

        inv_append(user_id, 'Latte', qty)
        await ctx.reply(embed=embed_builder(title="Crafting", description=f"You crafted Latte x{str(qty)}!"))
    else:
      await ctx.reply(embed=embed_builder(title="Failed", description=f"Crafting {str(qty)} Latte requires Milk x{str(1*qty)} and Coffee x{str(1*qty)}!"))

  if item == "metalchunk":
    if "Scrap Metal" in inventory.keys() and inventory["Scrap Metal"] >= 4*qty:
      if 4*qty == inventory["Scrap Metal"]:
        inv_append(user_id, 'Scrap Metal', "delete")
      else:
        inv_append(user_id, 'Scrap Metal', -4*qty)

      inv_append(user_id, 'Metal Chunk', qty)
      await ctx.reply(embed=embed_builder(title="Crafting", description=f"You crafted Metal Chunk x{str(qty)}!"))
    else:
      await ctx.reply(embed=embed_builder(title="Failed", description=f"Crafting {str(qty)} Metal Chunk requires Scrap Metal x{str(4*qty)}!"))

  else:
    await ctx.reply(embed=embed_builder(title="Item does not exist or cannot be crafted"))

@bot.command()
async def give(ctx, member: discord.Member, qty: int, item1="", item2="", item3=""):
  inventory = db[str(ctx.message.author.id)]["inventory"]
  user = db[str(ctx.message.author.id)]
  other = db[str(member.id)]
  user_id = str(ctx.message.author.id)
  member_id = str(member.id)
  item = item1+item2+item3

  if qty < 1:
    await ctx.reply(embed=embed_builder(title="Quantity must be greater than zero."))
    return

  if str(ctx.message.author.id) not in db.keys():
      await ctx.reply(embed=embed_builder(title="You have to run `k.start` first!"))
      return

  if member_id not in db.keys():
      await ctx.reply(embed=embed_builder(title="User does not have a profile!"))
      return
  
  if item == "":
    if user["money"] < qty:
      await ctx.reply(embed=embed_builder(title="You don't have that much cash!"))
      return
    user["money"] -= qty
    other["money"] += qty
    await ctx.reply(embed=embed_builder(title=f"You paid {member.name} {qty} credits!"))
  else:
    if item.lower() == "stalebread":
      if "Stale Bread" in inventory.keys() and inventory["Stale Bread"] >= qty:
        if qty == inventory["Stale Bread"]:
          inv_append(user_id, "Stale Bread", "delete")
        else:
          inv_append(user_id, "Stale Bread", -qty)
        inv_append(member_id, "Stale Bread", qty)
        await ctx.reply(embed=embed_builder(title="Gratitude", description=f"You gave {member.name} {str(qty)}x Stale Bread"))
      else:
        await ctx.reply(embed=embed_builder(title="You don't have that much!"))
        return

    elif item.lower() == "coffee":
      if "Coffee" in inventory.keys() and inventory["Coffee"] >= qty:
        if qty == inventory["Coffee"]:
          inv_append(user_id, "Coffee", "delete")
        else:
          inv_append(user_id, "Coffee", -qty)
        inv_append(member_id, "Coffee", qty)
        await ctx.reply(embed=embed_builder(title="Gratitude", description=f"You gave {member.name} {str(qty)}x Coffee"))
      else:
        await ctx.reply(embed=embed_builder(title="You don't have that much!"))
        return

    elif item.lower() == "milk":
      if "Milk" in inventory.keys() and inventory["Milk"] >= qty:
        if qty == inventory["Milk"]:
          inv_append(user_id, "Milk", "delete")
        else:
          inv_append(user_id, "Milk", -qty)
        inv_append(member_id, "Milk", qty)
        await ctx.reply(embed=embed_builder(title="Gratitude", description=f"You gave {member.name} {str(qty)}x Milk"))

      else:
        await ctx.reply(embed=embed_builder(title="You don't have that much!"))
        return

    elif item.lower() == "latte":
      if "Latte" in inventory.keys() and inventory["Latte"] >= qty:
        if qty == inventory["Latte"]:
          inv_append(user_id, "Latte", "delete")
        else:
          inv_append(user_id, "Latte", -qty)
        inv_append(member_id, "Latte", qty)
        await ctx.reply(embed=embed_builder(title="Gratitude", description=f"You gave {member.name} {str(qty)}x Latte"))

      else:
        await ctx.reply(embed=embed_builder(title="You don't have that much!"))
        return

    elif item.lower() == "scrapmetal":
      if "Scrap Metal" in inventory.keys() and inventory["Scrap Metal"] >= qty:
        if qty == inventory["Scrap Metal"]:
          inv_append(user_id, "Scrap Metal", "delete")
        else:
          inv_append(user_id, "Scrap Metal", -qty)
        inv_append(member_id, "Scrap Metal", qty)
        await ctx.reply(embed=embed_builder(title="Gratitude", description=f"You gave {member.name} {str(qty)}x Scrap Metal"))

      else:
        await ctx.reply(embed=embed_builder(title="You don't have that much!"))
        return
    
    elif item.lower() == "scrapbattery":
      if "Scrap Battery" in inventory.keys() and inventory["Scrap Battery"] >= qty:
        if qty == inventory["Scrap Battery"]:
          inv_append(user_id, "Scrap Battery", "delete")
        else:
          inv_append(user_id, "Scrap Battery", -qty)
        inv_append(member_id, "Scrap Battery", qty)
        await ctx.reply(embed=embed_builder(title="Gratitude", description=f"You gave {member.name} {str(qty)}x Scrap Battery"))

      else:
        await ctx.reply(embed=embed_builder(title="You don't have that much!"))
        return
    
    elif item.lower() == "pebble":
      if "Pebble" in inventory.keys() and inventory["Pebble"] >= qty:
        if qty == inventory["Pebble"]:
          inv_append(user_id, "Pebble", "delete")
        else:
          inv_append(user_id, "Pebble", -qty)
        inv_append(member_id, "Pebble", qty)
        await ctx.reply(embed=embed_builder(title="Gratitude", description=f"You gave {member.name} {str(qty)}x Pebble"))

      else:
        await ctx.reply(embed=embed_builder(title="You don't have that much!"))
        return

    elif item.lower() == "metalchunk":
      if "Metal Chunk" in inventory.keys() and inventory["Metal Chunk"] >= qty:
        if qty == inventory["Metal Chunk"]:
          inv_append(user_id, "Metal Chunk", "delete")
        else:
          inv_append(user_id, "Metal Chunk", -qty)
        inv_append(member_id, "Metal Chunk", qty)
        await ctx.reply(embed=embed_builder(title="Gratitude", description=f"You gave {member.name} {str(qty)}x Metal Chunk"))

      else:
        await ctx.reply(embed=embed_builder(title="You don't have that much!"))
        return

    else:
      await ctx.reply(embed=embed_builder(title="Item does not exist, or is not giveable."))
      return

@bot.command()
@commands.has_permissions(administrator=True)
async def clear_all(ctx, member: discord.Member):
  del db[str(member.id)]
  await ctx.reply(embed=embed_builder(title="removed key"))

@bot.command()
@commands.has_permissions(administrator=True)
async def list_keys(ctx, member: discord.Member):
  await ctx.reply(embed=embed_builder(title="Keys", description=db[str(member.id)]))


bot.run(os.getenv("TOKEN"))