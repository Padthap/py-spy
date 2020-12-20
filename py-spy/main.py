import discord
import random
from discord.ext import commands

 


client = commands.Bot(command_prefix = 'py-')


client.remove_command('help')

@client.command()
async def on_ready(): 
  await client.change_presence(activity = discord.Game('Fortnight'))
print('py-spy is ready')

@client.command()
async def ping(ctx):
      pingembed = discord.Embed(title="Hello world🌎", description="here are some bot commands", 
      colour= random.randint(0, 0xffffff))
      await ctx.channel.send(embed=pingembed)
       
@client.command()
async def luck(ctx, *, question):
 
    responses = ['yeah',
                 'sure',
                 '100%',
                 'fix',
                 'maybe',
                 'idk',
                 'anything can happen',
                 'felling lazy, try again  later',
                 'found a error',
                 'dont disturb me',
                 'I am busy',
                 'nope ',
                 'never',
                 'not even close',
                 'provably no',
                 
                 ]
    await ctx.send(f'{random.choice(responses)}')


@client.command(aliases=['flipcoin'])
async def toss(ctx, *, question):
    responses = ["heads",
                 "tails",
                 ]
    await ctx.send(f'{random.choice(responses)}')

@client.command(pass_context=True, aliases=['delete'])
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=1):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount):
              messages.append(message)

    await channel.delete_messages(messages)

@client.command(aliases=['b'])
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'`Banned {member} for {reason}` by {ctx.author}')
  
@client.command(aliases=['ub'])
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user} has been Unbanned')
            return

@client.command(aliases=['k'])
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
  
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member}')


@client.command(aliases=['commands'])
async def help(ctx):
      embed = discord.Embed(title="bot commands", description="here are some bot commands", colour = random.randint(0, 0xffffff))
      embed.add_field(name="`ping`", value="Get reply as hello world", inline=False)
      embed.add_field(name="`clear`", value="clears given messages", inline=False)
      embed.add_field(name="`kick`", value="kicks member who is pinged", inline=False)
      embed.add_field(name="`ban`", value="bans member who is pinged", inline=False)
      embed.add_field(name="`unban`", value="unbans member whos id is typed", inline=False)
      embed.add_field(name="`userifo`", value="get user's info", inline=False)
      embed.add_field(name="`punch`", value="mention user to punch with reason", inline=False)
      embed.add_field(name="`print`", value="get message back", inline=False)

      
      await ctx.channel.send(embed=embed)



@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('**`Non-sense! mention a valid member`**')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("**`drunk man! permissions.......`**")
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("**`stupid! mention a member to ban`**")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("**`WTF! U can't do it baby...`**")
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('**`NOOB ! U dont have those permissions`**')
    
@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("**`stupid! enter valid memeber(who is banned)`**")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("**`WTF! U can't do it baby...`**")


@client.command(aliases=["whois"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=random.randint(0, 0xffffff), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id, inline=False)
    embed.add_field(name="Name:", value=member.display_name, inline=False)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
   
    embed.add_field(name="Roles:", value=" ".join([role.mention for role in roles]), inline=False)
    embed.add_field(name="Highest Role:", value=member.top_role.mention, inline=False)
    print(member.top_role.mention)
    await ctx.send(embed=embed)

@client.command(aliases=["ava"])
async def avatar(ctx, member: discord.Member = None):

    embed = discord.Embed(colour=random.randint(0, 0xffffff), title=f"Your Avatar {ctx.author}") 
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_image(url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@client.command(aliases=["print"])
async def reply(ctx, *, arg):
    await ctx.send(arg)

@client.command()
async def punch(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('{} just got punched for {}'.format(slapped, reason))

@client.command(aliases=["stats"])
async def serverinfo(ctx):
  name = str(ctx.guild.name)

  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)


  icon = str(ctx.guild.icon_url)
   
  embed = discord.Embed(
      title=name + " Server Information",
      color=random.randint(0, 0xffffff)
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Server ID", value=id, inline=False)
  embed.add_field(name="Region", value=region, inline=False)
  embed.add_field(name="Member Count", value=memberCount, inline=False)


  await ctx.send(embed=embed)

client.run('Nzg4NzEwMDQ1NDQ1MjU5Mjg1.X9ndeA.aP5952eXy6vQZkJo3ZnzhNxjjUo')
#Padthap