from telethon import TelegramClient, events, sync, functions, types, Button

import zeus.client
client = zeus.client.client
@events.register(events.NewMessage(outgoing=True, pattern=".help"))
async def help(event):
	await event.edit("""
🛠 Umumiy modullar: 61
⚒ Berkitilgan modullar:  0

Humo_userbot HELP MENU
[01] Bombs - Animation emojise — .bombs
[02] Help - Help menu — .help
[03] Loading  - Animation loading — .loading
[04] Emoji  -  Emoji text editor - .emoji <here text>
[05] Dump - Candy dump animate - .dump
[06] Typer - Animation write text - .type <here text>
[07] Lul - animatsia lul - .lul
[08] Snake - Snake animation - .snake 
[09] Nothappy - Abimation Nothappy - .nothappy
[10] Clock - animation clock - .clock
[11] Muah - animation - .muah
[12] Heart - animation - .heart
[13] Gym - animation gymnastic - .gym
[14] Earth - animation globus - .earth
[15] Moon - animation - .moon
[16] Candy - Animatiln - .candy
[17] Smoon - animation - .smoon
[18] Tmoon - animation - .tmoon
[19] Clown - animation - .clown
[20] Star - batterfly and star animation - .star
[21] Boxs - Color animation - .boxs
[22] Rain - water animation - .rain
[23] Clol - "What?" snimation - .clol
[24] Odra - Animation - .odra 
[25] Fleaveme - animation - .fleaveme
[26] Loveu - love animation - .loveu
[27] Plane - animation - .plane
[28] Police - animation sirena - .police
[29] Jio - animation - .jio
[30] Solarsystem - animation - .solarsystem
[31] Chatinfo - function scan chatinfo - .chatinfo  
[32] M.Q - Memocyte Quote - .mq <reply text>
[33] Mute - Admin function - .mute (m, h, d )
[34] N.Q - Nedo Quote - .nq <reply text>
[35] Fuck - Fuck you - .fuck
[36] Rev - reverse - .rev
[37] Tr - Translator - .tr <language code > <reply message>
[38] Userinfo - Username information - .userinfo <reply>
[39] Base64 - encode and decode  text messages - .b64 en <reply text> .b64 de <reply encoded message>
[40] React - reactions - .react help
[41] Snow - animation snow - .snow
[42] Tts - text to voice - .tts <lang code> reply text message
[43] Itp - image to pdf - .itp reply to image
[44] About clock - datetime - .aboutclock <number>
[45] clocku - firstname clock - .clocku <number> <nickname>
[46] timer - timer animation - .timer <number>
[47] Afk - Afk mode - .afkon <text> / .afkoff / .afkstatus
[48] numbers - Numbers - .numbers <number>
[49] tag all - tag group members - .tagall
[50] magic - animation hearts - .magic
[51] sda - find delete accounts - .sda
[52] drc - o'chib ketuvchi rasmni saqlash' - .rcd
[53] rda - remove delete accounts - .rda
[54] ip trace - ip osint - .iptrace <ip addres>
[55] rename - Rename firstname and last name - .rename <nick> // <first name>
[56] Alive - information gojo userbot - .alive
[57] Qr code - qr code creator - .qrc create <reply>
[58] Sms flood - Spam message  - .spam <time> <count> <text>
[59] rts - save  message - .rts
[60] rgm - reload get message - rgm
[61] valyuta - valyuta - .val
[62] photo chat - photo chat saver - .poto
OVOZ MEMLAR
[63] Alish qattasan krisa - .alish
[64] AUFF - .auff
[65] Gruppengayam - .gruppa
[66] Gucci Flip Flap - .gucci
[67] Like bosingo - .like
[68] Maqtov yorliq berilar - .maqtov
[69] Mazzami silaga mazzami - .mazzami
[70] Nima gap - .nmagap
[71] PUBG Ban Music - .pubgban
[72] Rostan seryozni - .rostan
[73] Tugadi... - .tugadi
[74]Vapshe malades - .vapsheo
[75]Xe xe boi - .xexe
[76]Yedirganda... - .yedir
[77]Eee yozmislami gurpaga - .yozila
	""")
