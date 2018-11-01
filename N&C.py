import discord
from os import getenv
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = ".")

client.q = " "
client.w = " "
client.e = " "
client.a = " "
client.s = " "
client.d = " "
client.z = " "
client.x = " "
client.c = " "
game = 0
turn = 0

@client.event
async def on_ready():
    print("Bot:N&C is ready!")

@client.event
async def on_message(message):
    print_grid = False
    noughts_won = False
    crosses_won = False
    print_result = False
    game_start_no = False
    not_your_turn = False
    global game
    global turn
    if message.content.startswith(".startgame"):
        game = 1
        file = open('noughts.txt', 'w')
        file.write("0")
        file.close()
        file = open('crosses.txt','w')
        file.write("0")
        file.close()
        file = open('noughts.txt', 'r')
        n = file.read(1)
        file.close()
        file = open('crosses.txt', 'r')
        c = file.read(1)
        file.close()
        await client.send_message(message.channel, """```NAUGHTS & CROSSES```""")
        time.sleep(0.2)
        await client.send_message(message.channel, """```CURRENT SCORE FOR NOUGHTS IS: """ + n + """ \nCURRENT SCORE FOR CROSSES IS: """ + c + """```""")
        time.sleep(0.2)
        await client.send_message(message.channel, """```NAUGHTS GO FIRST```""")
        time.sleep(0.2)
        client.q = " "
        client.w = " "
        client.e = " "
        client.a = " "
        client.s = " "
        client.d = " "
        client.z = " "
        client.x = " "
        client.c = " "
        print_grid = True

    if message.content.startswith(".grid"):
        if game == 1:
            print_grid = True
        else:
            game_start_no = True
    if message.content.startswith(".egrid"):
        client.q = " "
        client.w = " "
        client.e = " "
        client.a = " "
        client.s = " "
        client.d = " "
        client.z = " "
        client.x = " "
        client.c = " "
        print_grid = True
    elif message.content.startswith(".nq"):
        if game == 1:
            if turn == 0:
                if client.q == " ":
                    client.q = "O"
                    print_grid = True
                    turn = turn + 1
                else:
                    await client.send_message(message.channel, "```ALREADY TAKEN```")
            else:
                not_your_turn = True
        else:
            game_start_no = True
    elif message.content.startswith(".nw"):
        if game == 1:
            if turn == 0:
                if client.w == " ":
                    client.w = "O"
                    print_grid = True
                    turn = turn + 1
                else:
                    await client.send_message(message.channel, "```ALREADY TAKEN```")
            else:
                not_your_turn = True
        else:
            game_start_no = True
    elif message.content.startswith(".ne"):
        if game == 1:
            if turn == 0:
                if client.e == " ":
                    client.e = "O"
                    print_grid = True
                    turn = turn + 1
                else:
                    await client.send_message(message.channel, "```ALREADY TAKEN```")
            else:
                not_your_turn = True 
        else:
            game_start_no = True
    elif message.content.startswith(".na"):
        if game == 1:
            if turn == 0:
                if client.a == " ":
                    client.a = "O"
                    print_grid = True
                    turn = turn + 1
                else:
                    await client.send_message(message.channel, "```ALREADY TAKEN```")
            else:
                not_your_turn = True
        else:
            game_start_no = True
    elif message.content.startswith(".ns"):
        if game == 1:
            if turn == 0:
                if client.s == " ":
                    client.s = "O"
                    print_grid = True
                    turn = turn + 1
                else:
                    await client.send_message(message.channel, "```ALREADY TAKEN```")
            else:
                not_your_turn = True
        else:
            game_start_no = True
    elif message.content.startswith(".nd"):
        if game == 1:
            if turn == 0:
                if client.d == " ":
                    client.d = "O"
                    print_grid = True
                    turn = turn + 1
                else:
                    await client.send_message(message.channel, "```ALREADY TAKEN```")
            else:
                not_your_turn = True
        else:
            game_start_no = True
    elif message.content.startswith(".nz"):
        if game == 1:
            if turn == 0:
                if client.z == " ":
                    client.z = "O"
                    print_grid = True
                    turn = turn + 1
                else:
                    await client.send_message(message.channel, "```ALREADY TAKEN```")
            else:
                not_your_turn = True
        else:
            game_start_no = True
    elif message.content.startswith(".nx"):
        if game == 1:
            if turn == 0:
                if client.x == " ":
                    client.x = "O"
                    print_grid = True
                    turn = turn + 1
                else:
                    await client.send_message(message.channel, "```ALREADY TAKEN```")
            else:
                not_your_turn = True
        else:
            game_start_no = True
    elif message.content.startswith(".nc"):
        if game == 1:
            if turn == 0:
                if client.c == " ":
                    client.c = "O"
                    print_grid = True
                    turn = turn + 1
                else:
                    await client.send_message(message.channel, "```ALREADY TAKEN```")
            else:
                not_your_turn = True
        else:
            game_start_no = True
    elif message.content.startswith(".cq"):
        if game == 1:
            if turn == 1:
                if client.q == " ":
                    client.q = "X"
                    print_grid = True
                    turn = turn - 1
                else:
                    await client.send_message(message.channel, "```ALREADY TAKEN```")
            else:
                not_your_turn = True
        else:
            game_start_no = True
    elif message.content.startswith(".cw"):#
        if game == 1:
            if turn == 1:
                if client.w == " ":
                    client.w = "X"
                    print_grid = True
                    turn = turn - 1
                else:
                    await client.send_message(message.channel, "```ALREADY TAKEN```")
            else:
                not_your_turn = True
        else:
            game_start_no = True
    elif message.content.startswith(".ce"):
        if game == 1:
            if turn == 1:
                if client.e == " ":
                    client.e = "X"
                    print_grid = True
                    turn = turn - 1
                else:
                    await client.send_message(message.channel, "```ALREADY TAKEN```")
            else:
                not_your_turn = True
        else:
            game_start_no = True
    elif message.content.startswith(".ca"):
        if game == 1:
            if turn == 1:
                if client.a == " ":
                    client.a = "X"
                    print_grid = True
                    turn = turn - 1
                else:
                    await client.send_message(message.channel, "```ALREADY TAKEN```")
            else:
                not_your_turn = True
        else:
            game_start_no = True
    elif message.content.startswith(".cs"):
        if game == 1:
            if turn == 1:
                if client.s == " ":
                    client.s = "X"
                    print_grid = True
                    turn = turn - 1
                else:
                    await client.send_message(message.channel, "```ALREADY TAKEN```")
            else:
                not_your_turn = True
        else:
            game_start_no = True
    elif message.content.startswith(".cd"):
        if game == 1:
            if turn == 1:
                if client.d == " ":
                    client.d = "X"
                    print_grid = True
                    turn = turn - 1
                else:
                    await client.send_message(message.channel, "```ALREADY TAKEN```")
            else:
                not_your_turn = True
        else:
            game_start_no = True
    elif message.content.startswith(".cz"):
        if game == 1:
            if turn == 1:
                if client.z == " ":
                    client.z = "X"
                    print_grid = True
                    turn = turn - 1
                else:
                    await client.send_message(message.channel, "```ALREADY TAKEN```")
            else:
                not_your_turn = True
        else:
            game_start_no = True
    elif message.content.startswith(".cx"):
        if game == 1:
            if turn == 1:
                if client.x == " ":
                    client.x = "X"
                    print_grid = True
                    turn = turn - 1
                else:
                    await client.send_message(message.channel, "```ALREADY TAKEN```")
            else:
                not_your_turn = True
        else:
            game_start_no = True
    elif message.content.startswith(".cc"):
        if game == 1:
            if turn == 1:
                if client.c == " ":
                    client.c = "X"
                    print_grid = True
                    turn = turn - 1
                else:
                    await client.send_message(message.channel, "```ALREADY TAKEN```")
            else:
                not_your_turn = True
        else:
            game_start_no = True

    elif message.content.startswith(".testnwin"):
        noughts_won = True

    elif message.content.startswith(".testcwin"):
        crosses_won = True

    elif message.content.startswith(".testfull"):
        client.q = "O"
        client.w = "O"
        client.e = "X"
        client.a = "X"
        client.s = "X"
        client.d = "O"
        client.z = "O"
        client.x = "O"
        client.c = "X"

    if client.q == "O" and client.w == "O" and client.e == "O":
        noughts_won = True

    elif client.a == "O" and client.s == "O" and client.d == "O":
        noughts_won = True

    elif client.z == "O" and client.x == "O" and client.c == "O":
        noughts_won = True

    elif client.q == "O" and client.a == "O" and client.z == "O":
        noughts_won = True

    elif client.w == "O" and client.s == "O" and client.x == "O":
        noughts_won = True

    elif client.e == "O" and client.d == "O" and client.c == "O":
        noughts_won = True

    elif client.q == "O" and client.s == "O" and client.c == "O":
        noughts_won = True

    elif client.e == "O" and client.s == "O" and client.z == "O":
        noughts_won = True


    elif client.q == "X" and client.w == "X" and client.e == "X":
        crosses_won = True

    elif client.a == "X" and client.s == "X" and client.d == "X":
        crosses_won = True

    elif client.z == "X" and client.x == "X" and client.c == "X":
        crosses_won = True

    elif client.q == "X" and client.a == "X" and client.z == "X":
        crosses_won = True

    elif client.w == "X" and client.s == "X" and client.x == "X":
        crosses_won = True

    elif client.e == "X" and client.d == "X" and client.c == "X":
        crosses_won = True

    elif client.q == "X" and client.s == "X" and client.c == "X":
        crosses_won = True

    elif client.e == "X" and client.s == "X" and client.z == "X":
        crosses_won = True

    elif not client.q == " " and not client.w == " " and not client.e == " " and not client.a == " " and not client.s == " " and not client.d == " " and not client.z == " " and not client.x == " " and not client.c == " ":
        client.q = " "
        client.w = " "
        client.e = " "
        client.a = " "
        client.s = " "
        client.d = " "
        client.z = " "
        client.x = " "
        client.c = " "
        await client.send_message(message.channel, """```GRID FILLED UP\nRESTARTING...```""")
        time.sleep(1)
        await client.send_message(message.channel, """```css
READY```""")

    grid = """``` """ + client.q + """ ¦ """ + client.w + """ ¦ """ + client.e + """ 
-----------
 """ + client.a + """ ¦ """ + client.s + """ ¦ """ + client.d + """ 
-----------
 """ + client.z + """ ¦ """ + client.x + """ ¦ """ + client.c + """ ```"""
    if print_grid:
        await client.send_message(message.channel, grid)

    elif noughts_won:
        client.q = " "
        client.w = " "
        client.e = " "
        client.a = " "
        client.s = " "
        client.d = " "
        client.z = " "
        client.x = " "
        client.c = " "
        await client.send_message(message.channel, "```NOUGHTS WIN```")
        file = open('noughts.txt', 'r')
        no_of_times = int(file.read())
        new_value = int(no_of_times + 1)
        file = open('noughts.txt', 'w')
        file.write(str(new_value))
        file = open('noughts.txt', 'r')
        result_to_print = file.read()
        file.close()
        print_result = True

    elif crosses_won:
        client.q = " "
        client.w = " "
        client.e = " "
        client.a = " "
        client.s = " "
        client.d = " "
        client.z = " "
        client.x = " "
        client.c = " "
        await client.send_message(message.channel, "```CROSSES WIN```")
        file = open('crosses.txt', 'r')
        no_of_times = int(file.read())
        new_value = int(no_of_times + 1)
        file = open('crosses.txt', 'w')
        file.write(str(new_value))
        file = open('crosses.txt', 'r')
        result_to_print = file.read()
        file.close()
        print_result = True

    if print_result:
        await client.send_message(message.channel, "```AND THEY HAVE: " + result_to_print + " POINTS```")

    if message.content.startswith(".score"):
        if game == 1:
            file = open('noughts.txt', 'r')
            n = file.read()
            file.close()
            file = open('crosses.txt', 'r')
            c = file.read()
            file.close()
            await client.send_message(message.channel, """```NOUGHTS HAVE: """ + n + """ POINTS \nCROSSES HAVE: """ + c + """ POINTS```""")      
        else:
            game_start_no = True
    elif message.content.startswith(".oscore"):
        if game == 1:
            file = open('noughts.txt', 'r')
            n = file.read()
            file.close()
            await client.send_message(message.channel, "```NOUGHTS HAVE: " + n + " POINTS```")
        else:
            game_start_no = True

    elif message.content.startswith(".xscore"):
        if game == 1:
            file = open('crosses.txt', 'r')
            c = file.read()
            file.close()
            await client.send_message(message.channel, "```CROSSES HAVE: " + c + " POINTS```")
        else:
            game_start_no = True

    if message.content.startswith(".endgame"):
        if game == 1:
            file = open('noughts.txt', 'r')
            n = file.read()
            file.close()
            file = open('crosses.txt', 'r')
            c = file.read()
            file.close()
            if n < c:
                w = "CROSSES WIN"
            elif c < n:
                w = "NOUGHTS WIN"
            else:
                w = "DRAW"
            await client.send_message(message.channel, """```NOUGHTS HAVE: """ + n + """ POINTS \nCROSSES HAVE: """ + c + """ POINTS\n SO THEREFORE THE OVERALL RESULT IS:\n """ + w + """```""")        
            file = open('noughts.txt', 'w')
            file.write("0")
            file.close()
            file = open('crosses.txt','w')
            file.write("0")
            file.close()
            game = 0
        else:
            game_start_no = True

    if game_start_no:
        await client.send_message(message.channel, "```GAME HASN'T STARTED, PLEASE START GAME FIRST```")
        await client.send_message(message.channel, """```css
TO START GAME, TYPE .startgame```""")

    if not_your_turn:
        await client.send_message(message.channel, "IT IS NOT YOUR TURN, BE PATIENT")



client.run(getenv("token"))

