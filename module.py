#tg: @little_senpai
import random
import logging
from .. import loader, utils
from random import randint, choice
logger = logging.getLogger(__name__)


def register(cb):
    cb(ArtsMod())

class ArtsMod(loader.Module):
    """Юникод арты"""
    strings = {'name': 'Arts'}

    async def вжухcmd(self, message):
        """Используй .вжух <текст>."""
        text = utils.get_args_raw(message)
        if not text:
            text = ("Вжух и ты подпишешься @little_senpai")
            vjuh = ("∧＿∧\n"
            "( ･ω･｡)つ━☆・*。\n"
            "⊂  ノ    ・゜ .\n"
            "しーＪ   °。  *´¨)\n"
            "             .· ´¸.·*´¨) ¸.·*¨)\n"
            "                     (¸.·´ (¸.·'* ☆\n\n"
            "\n"
            f"<b>{text}</b>")
            await message.edit(vjuh)
        else:
            vjuh = ("∧＿∧\n"
            "( ･ω･｡)つ━☆・*。\n"
            "⊂  ノ    ・゜ .\n"
            "しーＪ   °。  *´¨)\n"
            "             .· ´¸.·*´¨) ¸.·*¨)\n"
            "                     (¸.·´ (¸.·'* ☆\n\n"
            "\n"
            f"<b>Вжух и ты {text}</b>")
            await message.edit(vjuh)


    async def cowsaycmd(self, message):
        """Используй .cowsay <текст>."""
        text = utils.get_args_raw(message)
        if not text:
            await message.edit('<b>Нет текста после команды :c</b>')
            return
        else:
            cowsay = ("<code> "
                      f"< {text} >\n"
                      "\n"
                      "     \   ^__^\n"
                      "	     \  (oo)\_______\n"
                      "         (__)\       )\/\n"
                      "             ||----w||\n"
                      "	            ||     ||</code>")
            await message.edit(cowsay)


    async def падаюcmd(self, message):
        """Используй .падаю <текст>; ничего."""
        text = utils.get_args_raw(message)
        if not text:
            text = ("И камнем вниз. С крыши дома!")
            padayu = ("┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      f"┛┗┛┗┛┃ <b>{text}</b>!\n"
                      "┓┏┓┏┓┃ ＼○／\n"
                      "┛┗┛┗┛┃ /\n"
                      "┓┏┓┏┓┃ノ)\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n")
            await message.edit(padayu)
        else:
            padayu = ("┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      f"┛┗┛┗┛┃ <b>{text}</b>!\n"
                      "┓┏┓┏┓┃ ＼○／\n"
                      "┛┗┛┗┛┃ /\n"
                      "┓┏┓┏┓┃ノ)\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n")
            await message.edit(padayu)


    async def прилетелcmd(self, message):
        """Используй .прилетел <текст>; ничего."""
        text = utils.get_args_raw(message)
        if not text:
            text = ("Я ЛЮБЛЮ ТВОЮ МАМУ♥️")
            prilitel = ("▬▬▬.◙.▬▬▬\n"
                        "  ═▂▄▄▓▄▄▂\n"
                        "◢◤ █▀▀████▄▄▄▄◢◤\n"
                        "█▄ █ █▄ ███▀▀▀▀▀▀▀╬\n"
                        "◥█████◤ прилетел сказать что-то важное...\n"
                        "══╩══╩═\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        f"╬═╬☻/ - <b>{text}</b>\n"
                        "╬═╬/▌\n"
                        "╬═╬/ \ ")
            await message.edit(prilitel)
        else:
            prilitel = ("▬▬▬.◙.▬▬▬\n"
                        "  ═▂▄▄▓▄▄▂\n"
                        "◢◤ █▀▀████▄▄▄▄◢◤\n"
                        "█▄ █ █▄ ███▀▀▀▀▀▀▀╬\n"
                        "◥█████◤ прилетел сказать что-то важное...\n"
                        "══╩══╩═\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        f"╬═╬☻/ - <b>{text}</b>\n"
                        "╬═╬/▌\n"
                        "╬═╬/ \ ")
            await message.edit(prilitel)


    async def хуйтебеcmd(self, message):
        """Используй .хуйтебе <текст>; ничего."""
        text = utils.get_args_raw(message)
        if not text:
            text = ("ХУЙ ТЕБЕ!")
            huytebe = (".................▄▄▄▄▄\n"
                       "..............▄▌░░░░▐▄\n"
                       "............▐░░░░░░░▌\n"
                       "....... ▄█▓░░░░░░▓█▄\n"
                       "....▄▀░░▐░░░░░░▌░▒▌\n"
                       ".▐░░░░▐░░░░░░▌░░░▌\n"
                       "▐ ░░░░▐░░░░░░▌░░░▐\n"
                       "▐ ▒░░░ ▐░░░░░░▌░▒▒▐ \n"
                       "▐ ▒░░░░▐░░░░░░▌░▒▐\n"
                       "..▀▄▒▒▒▒▐░░░░░░▌▄▀\n"
                       "........ ▀▀▀ ▐░░░░░░▌\n"
                       "....................▐░░░░░░▌\n"
                       "....................▐░░░░░░▌\n"
                       "....................▐░░░░░░▌\n"
                       "....................▐░░░░░░▌\n"
                       "....................▐▄▀▀▀▀▀▄▌\n"
                       "..................▐▒▒▒▒▒▒▒▒▌\n"
                       ".................▐▒▒▒▒▒▒▒▒▌\n"
                       "...................▐▒▒▒▒▒▒▒▌\n"
                       "......................▀▄▄▀▄▄▀\n"
                       "\n"
                       f"<b>{text}</b>")
            await message.edit(huytebe)
        else:
            huytebe = (".................▄▄▄▄▄\n"
                       "..............▄▌░░░░▐▄\n"
                       "............▐░░░░░░░▌\n"
                       "....... ▄█▓░░░░░░▓█▄\n"
                       "....▄▀░░▐░░░░░░▌░▒▌\n"
                       ".▐░░░░▐░░░░░░▌░░░▌\n"
                       "▐ ░░░░▐░░░░░░▌░░░▐\n"
                       "▐ ▒░░░ ▐░░░░░░▌░▒▒▐ \n"
                       "▐ ▒░░░░▐░░░░░░▌░▒▐\n"
                       "..▀▄▒▒▒▒▐░░░░░░▌▄▀\n"
                       "........ ▀▀▀ ▐░░░░░░▌\n"
                       "....................▐░░░░░░▌\n"
                       "....................▐░░░░░░▌\n"
                       "....................▐░░░░░░▌\n"
                       "....................▐░░░░░░▌\n"
                       "....................▐▄▀▀▀▀▀▄▌\n"
                       "..................▐▒▒▒▒▒▒▒▒▌\n"
                       ".................▐▒▒▒▒▒▒▒▒▌\n"
                       "...................▐▒▒▒▒▒▒▒▌\n"
                       "......................▀▄▄▀▄▄▀\n"
                       "\n"
                       f"<b>{text}</b>")
            await message.edit(huytebe)


    async def lolcmd(self, message):
        """Используй .lol."""
        lol = ("┏━┓┈┈╭━━━━╮┏━┓┈┈\n"
               "┃╱┃┈┈┃╱╭╮╱┃┃╱┃┈┈\n"
               "┃╱┗━┓┃╱┃┃╱┃┃╱┗━┓\n"
               "┃╱╱╱┃┃╱╰╯╱┃┃╱╱╱┃\n"
               "┗━━━┛╰━━━━╯┗━━━┛\n")
        await message.edit(lol)


    async def fuckyoucmd(self, message):
        """Используй .fuckyou."""
        fuckyou = ("┏━┳┳┳━┳┳┓\n"
                   "┃━┫┃┃┏┫━┫┏┓\n"
                   "┃┏┫┃┃┗┫┃┃┃┃\n"
                   "┗┛┗━┻━┻┻┛┃┃\n"
                   "┏┳┳━┳┳┳┓┏┫┣┳┓\n"
                   "┣┓┃┃┃┃┣┫┃┏┻┻┫\n"
                   "┃┃┃┃┃┃┃┃┣┻┫┃┃\n"
                   "┗━┻━┻━┻┛┗━━━┛\n")
        await message.edit(fuckyou)


    async def домcmd(self, message):
        """Используй .дом"""
        house = ("╯▅╰╱▔▔▔▔▔▔▔╲╯╯\n"
                 "▕▕╱╱╱╱╱╱╱╱╱╲╲╭╭\n"
                 "▕▕╱╱╱╱╱╱╱╱┛▂╲╲╭\n"
                 "╱▂▂▂▂▂▂╱╱┏▕╋▏╲╲\n"
                 "▔▏▂┗┓▂▕▔┛▂┏▔▂▕▔\n"
                 "▕▕╋▏▕╋▏▏▕┏▏▕╋▏▏\n"
                 "▕┓▔┗┓▔┏▏▕┗▏ ┓▔┏\n")
        await message.edit(house)


    async def hellocmd(self, message):
        """Используй .hello."""
        hello = ("┈┏┓┏┳━┳┓┏┓┏━━┓┈\n"
                 "┈┃┃┃┃┏┛┃┃┃┃┏┓┃┈\n"
                 "┈┃┗┛┃┗┓┃┃┃┃┃┃┃┈\n"
                 "┈┃┏┓┃┏┛┃┃┃┃┃┃┃┈\n"
                 "┈┃┃┃┃┗┓┗┫┗┫╰╯┃┈\n"
                 "┈┗┛┗┻━┻━┻━┻━━┛┈\n")
        await message.edit(hello)


    async def кофеcmd(self, message):
        """Используй .кофе <текст>; ничего."""
        text = utils.get_args_raw(message)
        if not text:
            text = ("Это тебе :з")
            coffee = ("─▄▀─▄▀\n"
                      "──▀──▀\n"
                      "█▀▀▀▀▀█▄\n"
                      "█░░░░░█─█\n"
                      "▀▄▄▄▄▄▀▀\n\n"
                      f"<b>{text}</b>")
            await message.edit(coffee)
        else:
            coffee = ("─▄▀─▄▀\n"
                      "──▀──▀\n"
                      "█▀▀▀▀▀█▄\n"
                      "█░░░░░█─█\n"
                      "▀▄▄▄▄▄▀▀\n\n"
                      f"<b>{text}</b>")
            await message.edit(coffee)


    async def твcmd(self, message):
        """Используй .тв <текст>; ничего."""
        text = utils.get_args_raw(message)
        if not text:
            text = ("ТЕЛЕВИЗОР ГОВОРИТ ЧТО ТЫ ДОЛБОЁБ!")
            tv = ("░▀▄░░▄▀\n"
                  "▄▄▄██▄▄▄▄▄░▀█▀▐░▌\n"
                  "█▒░▒░▒░█▀█░░█░▐░▌\n"
                  "█░▒░▒░▒█▀█░░█░░█\n"
                  "█▄▄▄▄▄▄███══════\n\n"
                  f"<b>{text}</b>")
            await message.edit(tv)
        else:
            tv = ("░▀▄░░▄▀\n"
                  "▄▄▄██▄▄▄▄▄░▀█▀▐░▌\n"
                  "█▒░▒░▒░█▀█░░█░▐░▌\n"
                  "█░▒░▒░▒█▀█░░█░░█\n"
                  "█▄▄▄▄▄▄███══════\n\n"
                  f"<b>{text}</b>")
            await message.edit(tv)


    async def гранатаcmd(self, message):
        """Используй .граната <текст>; ничего."""
        text = utils.get_args_raw(message)
        if not text:
            text = ("ТИКАЙ НАХУЙ!")
            gren = ("─▄▀▀███═◯\n"
                    "▐▌▄█████▄\n"
                    "█▐███████▌\n"
                    "█▐███████▌\n"
                    "▀ ▀█████▀\n\n"
                    f"<b>{text}</b>")
            await message.edit(gren)
        else:
            gren = ("─▄▀▀███═◯\n"
                    "▐▌▄█████▄\n"
                    "█▐███████▌\n"
                    "█▐███████▌\n"
                    "▀ ▀█████▀\n\n"
                    f"<b>{text}</b>")
            await message.edit(gren)


    async def bruhcmd(self, message):
        """Используй .bruh."""
        bruh = ("╭━━╮╱╱╱╱╱╭╮\n"
                "┃╭╮┃╱╱╱╱╱┃┃\n"
                "┃╰╯╰┳━┳╮╭┫╰━╮\n"
                "┃╭━╮┃╭┫┃┃┃╭╮┃\n"
                "┃╰━╯┃┃┃╰╯┃┃┃┃\n"
                "╰━━━┻╯╰━━┻╯╰╯\n")
        await message.edit(bruh)


    async def unocmd(self, message):
        """Используй .uno."""
        uno = ("⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n"
               "⣿⣿⡟⡴⠛⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n"
               "⣿⡏⠴⠞⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n"
               "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n"
               "⣿⣿⣿⣿⣿⣿⣿⡏⠩⣭⣭⢹⣿⣿⣿⣿⡇\n"
               "⣿⣿⣿⣿⣿⣿⠟⣵⣾⠟⠟⣼⣿⣿⣿⣿⡇\n"
               "⣿⣿⣿⣿⣿⠿⠀⢛⣵⡆⣶⣿⣿⣿⣿⣿⡇\n"
               "⣿⣿⣿⣿⡏⢸⣶⡿⢋⣴⣿⣿⣿⣿⣿⣿⡇\n"
               "⣿⣿⣿⣿⣇⣈⣉⣉⣼⣿⣿⣿⣿⣿⣿⣿⡇\n"
               "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n"
               "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢣⠞⢺⣿⡇\n"
               "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢡⡴⣣⣿⣿⡇\n"
               "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⡇")
        await message.edit(uno)


    async def держиcmd(self, message):
        """Используй .держи <emoji>; ничего."""
        emoji = utils.get_args_raw(message)
        huy = ("🍆🍆\n"
               "🍆🍆🍆\n"
               "  🍆🍆🍆\n"
               "    🍆🍆🍆\n"
               "     🍆🍆🍆\n"
               "       🍆🍆🍆\n"
               "        🍆🍆🍆\n"
               "         🍆🍆🍆\n"
               "          🍆🍆🍆\n"
               "          🍆🍆🍆\n"
               "      🍆🍆🍆🍆\n"
               " 🍆🍆🍆🍆🍆🍆\n"
               " 🍆🍆🍆  🍆🍆🍆\n"
               "    🍆🍆        🍆🍆")
        if emoji:
            huy = huy.replace('🍆', emoji)
        await message.edit(huy)


    async def impscmd(self, message):
        """Используй .imps <@ или реплай>."""
        reply = await message.get_reply_message()
        args = utils.get_args_raw(message)
        if not args and not reply:
            user = await message.client.get_me()
        if reply:
            user = await utils.get_user(await message.get_reply_message())
        if args:
            user = await message.client.get_entity(args)
        imps = ['wasn`t the impostor', 'was the impostor']
        imp = ("<code>.      　。　　　　•　    　ﾟ　　.      .     。\n"
               "　　.　　　.　　　  .　　　.　　　　　。　　   。　   .\n"
               "　.　　      。        ඞ   。　    .     　.　      •      .\n"
               f"•     {user.first_name} {choice(imps)} 。　   .\n"
               f"　 。     {randint(1, 5)} impostor(s) remains.　　　.　 　.\n"
               ",　　　　.　 .　　       .        •   •    。.\n"
               "。  •　   .   　ﾟ 　  •  　ﾟ .        .    　.</code>")
        await message.edit(imp)


    async def fcmd(self, message):
        """Используй .f"""
        r = random.randint(0, 6)
        logger.debug(r)
        if r == 0:
            await utils.answer(message, "┏━━━┓\n┃┏━━┛\n┃┗━━┓\n┃┏━━┛\n┃┃\n┗┛")
        elif r == 1:
            await utils.answer(message, "╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃┃\n╰╯")
        elif r == 2:
            await utils.answer(message,
                               "̫͍F̥̼F͈̫F͔̱F͓̤F̭̺F̙F͍͕F͚̩F̣̱F͖ͅF̣͙F̗͕F̦͚F̯͍F̰̹F̦̩F͙ͅF̙̹F̝͚͍̭\n"
                               "̹̖F̲͔F̜F̭̰F̰̭F̼͍F̹̞F̱͉F͓͓F̬F̤͔F̦͉FF̦̹F͚̠FF̪̝̩̗F͇͓F̟̙F͎͎͉͚\n"
                               "̯̻F͓͈F̮͔F͉̫F͕̥\n"
                               "̞̖F̝̗F͙͓F̟͓F̖̝̤͙\n"
                               "͔͓F̠F̖ͅF̰̹F\n"
                               "͓͕F̹͙F̙̠F͇̯F̖̗\n"
                               "̜͚FF̥̝F̖̦F͇͔̪̹\n"
                               "̩̗F̬̟F̰F̙͇FF͉̖F̼ͅF̬͔F͇͖F̞̥F̙̺F̖̮F̜͔F̩̜F͎̣F̲̤F̪̙F\n"
                               "͎͙F̘F͍̲F͇͇F̜̥F͖͖F̪̟̤̩F̠̩F̬͕F̪̰̪F̫͍F͕̤F̰ͅF̮̼FF͓̟F̻͔F̪\n"
                               "̙F͎̞F̻F͖͔F͕̮F̯͖FF̪͕F̫͚F̣̣̗̣F̩F̥F̗̮F̻̫F͍̺F̞͉F͚̩F͕̤͙\n"
                               "͍͙F̯̬F̲̻F̥̟F̝̙\n"
                               "̦̝̝̬F̝͍F̖͚F̥͚F̖͉\n"
                               "͓̪F̝͉F̜ͅF̦ͅF͓͕\n"
                               "͖FF̩͕F̻͖F̯̼\n"
                               "͍̱FF̹̥F̭͓F̦̺̖͎\n"
                               "̥̜F̞͎F̖̲F̦̹F̬̘\n"
                               "̦̬F̺̭F͖̗F͕͍F̟͙")
        elif r == 3:
            await utils.answer(message, "🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕\n"
                                        "🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕\n"
                                        "🌕🌕🌗🌑🌑🌑🌑🌑🌓🌕🌕\n"
                                        "🌕🌕🌗🌑🌑🌑🌑🌑🌕🌕🌕\n"
                                        "🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕\n"
                                        "🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕\n"
                                        "🌕🌕🌗🌑🌑🌑🌑🌓🌕🌕🌕\n"
                                        "🌕🌕🌗🌑🌑🌑🌑🌕🌕🌕🌕\n"
                                        "🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕\n"
                                        "🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕\n"
                                        "🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕\n"
                                        "🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕\n"
                                        "🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕")
        elif r == 4:
            await utils.answer(message, "┏━━━┓╋╋╋╋╋╋╋╋╋╋╋┏━━━┓\n"
                                        "┃┏━┓┃╋╋╋╋╋╋╋╋╋╋╋┃┏━━┛\n"
                                        "┃┗━┛┣━┳━━┳━━┳━━┓┃┗━━┓\n"
                                        "┃┏━━┫┏┫┃━┫━━┫━━┫┃┏━━┛\n"
                                        "┃┃╋╋┃┃┃┃━╋━━┣━━┃┃┃\n"
                                        "┗┛╋╋┗┛┗━━┻━━┻━━┛┗┛")
        elif r == 5:
            await utils.answer(message, "<code>FFFFFFFFFFFFFFFFFFFFFF\n"
                                        "F::::::::::::::::::::F\n"
                                        "F::::::::::::::::::::F\n"
                                        "FF::::::FFFFFFFFF::::F\n"
                                        "  F:::::F       FFFFFF\n"
                                        "  F:::::F\n"
                                        "  F::::::FFFFFFFFFF\n"
                                        "  F:::::::::::::::F\n"
                                        "  F:::::::::::::::F\n"
                                        "  F::::::FFFFFFFFFF\n"
                                        "  F:::::F\n"
                                        "  F:::::F\n"
                                        "FF:::::::FF\n"
                                        "F::::::::FF\n"
                                        "F::::::::FF\n"
                                        "FFFFFFFFFFF</code>")
        else:
            await utils.answer(message, "██████╗\n"
                                        "██╔═══╝\n"
                                        "████╗░░\n"
                                        "██╔═╝░░\n"
                                        "██║░░░░\n"
                                        "╚═╝░░░░")
                                        
                                        
    async def улиткаcmd(self, message):
        """Используй .улитка"""
        snail = ("༎ຶ‿༎ຶ༼メ༽\n"
                 "\﹏﹏﹏/ \n")
        await message.edit(snail)        
        

    async def черепcmd(self, message):
        """Используй .череп"""
        scull = ("ᅠ╔══════════╗\n"
"ᅠ║▒▒▒▒▒▒▒▒▒▒║\n"
"ᅠ║▒▒▒▒▒▒▒▒▒▒║\n"
"ᅠ║▒▒▒▒▒▒▒▒▒▒║\n"
"ᅠ║▒▒▒▒▒▒▒▒▒▒║\n"
"ᅠ║▒▒▒▒▒▒▒▒▒▒║\n"
"ᅠ║▒▒▒▒▒▒▒▒▒▒║\n"
"╔═════════════╗ \n"
"╚═════════════╝\n"
" ║██████████╚╗\n"
" ║██╔══╗█╔═╗█║\n"
" ║██║╬╔╝█╚╗║█║\n"
" ║██╚═╝█║█╚╝█║\n"
" ╚╗█████████═╝\n"
"    ╚╗║╠╩╩╩╩╩╝\n"
"       ║║┈┈┈█▐█████▒.｡oO\n"
"       ║██╠╦╦╦╗\n"
"       ╚╗██████\n"
"         ╚════╝")
        await message.edit(scull)
        
    async def анимеcmd(self, message):
        """Используй .аниме"""
        anime = ("⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄\n" "⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥\n" "⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿\n" "⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄\n" "⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿\n" "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥\n" "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n" "⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿\n" "⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵\n" "⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿\n" "⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁\n" "⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄\n" "⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄")
        await message.edit(anime)        