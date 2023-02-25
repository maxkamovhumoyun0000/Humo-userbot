from telethon import events
from .. import loader, utils
from asyncio import sleep
import random

a = """•"""
ab = """••"""
abc = """•••"""

__version__ = (1, 0, 0)

# meta developer: @the_xisache
# meta channel: @umodules

def register(cb):
	cb(OvozMemlarMod())
	
class OvozMemlarMod(loader.Module):
	"""Qiziqarli ovoz memlar🔊"""
	
	strings = {
		"name": "@the_xisache - Ovoz Memlar🥷🏻",
		}

	async def ovozcmd(self, message):
		"""Ovoz Memlar Ro'yxati"""
		
		royhat = """
<i>📖Buyruqlarning tartib roʻyhati:</i>

<code>.alish</code> - <b>Alish qattasan krisa</b>
<code>.auff</code> - <b>AUFF</b>
<code>.gruppa</code> - <b>Gruppengayam</b>
<code>.gucci</code> - <b>Gucci Flip Flaps</b>
<code>.like</code> - <b>Like bosingo/b>
<code>.maqtov</code> - <b>Maqtov yorliq berilar</b>
<code>.mazzami</code> - <b>Mazzami silaga mazzami</b>
<code>.nmagap</code> - <b>Nima gap</b>
<code>.pubgban</code> - <b>PUBG Ban Music</b>
<code>.rostan</code> - <b>Rostan seryozni</b>
<code>.tugadi</code> - <b>Tugadi...</b>
<code>.vapsheo/code> - <b>Vapshe malades</b>
<code>.xexe</code> - <b>Xe xe boi</b>
<code>.yedir</code> - <b>Yedirganda...</b>
<code>.yozila</code> - <b>Eee yozmislami gurpaga</b>

<i>Yangi ovoz memlar hali oldinda...</i>

<b>🥷🏻Yaratuvchi:</b> @Programmer_uzN1
<b>📖Kanalimiz:</b> @Humo_userbot"""
		await message.edit(royhat)
		return

	async def nmagapcmd(self, message):
		"""Nima gap"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/10", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def rostancmd(self, message):
		"""Rostan seryozni"""
		
		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/12", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def maqtovcmd(self, message):
		"""Maqtov yorliq berilar"""
		
		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/13", voice_note=True, reply_to=reply.id if reply else None)
		return
		
		
	async def mazzamicmd(self, message):
		"""Mazzami silaga mazzami"""
		
		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/15", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def likecmd(self, message):
		"""Like bosing"""
		
		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/16", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def gruppacmd(self, message):
		"""Gruppengayam"""
		
		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/17", voice_note=True, reply_to=reply.id if reply else None)
		return
				
	async def tugadicmd(self, message):
		"""Tugadi..."""
		
		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/19", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def vapshecmd(self, message):
		"""Vapshe malades"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/20", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/22", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def xexecmd(self, message):
		"""Xe xe boi"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/23", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def alishcmd(self, message):
		"""Alish qattasan krisa"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/24", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def blacmd(self, message):
		"""Ux Blaaa..."""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/25", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def auffcmd(self, message):
		"""AUFF"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/27", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def theendcmd(self, message):
		"""Directed By"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/28", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def guccicmd(self, message):
		"""Gucci Flip Flaps"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/29", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def yozilacmd(self, message):
		"""Eee yozmislami gurpaga"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/30", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def yepsancmd(self, message):
		"""Qo'**mi yepsan (18+)"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/31", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def baqirmacmd(self, message):
		"""Baqirma oneni s***lar (18+)"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/32", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def bekcorecmd(self, message):
		"""Bahorlarda (18+)"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/33", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def sekscmd(self, message):
		"""Seks ko'ryapsanmi (18+)"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/34", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def poxuycmd(self, message):
		"""Похуй (18+)"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/35", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def chichibkele2cmd(self, message):
		"""Chichib kele 2"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/39", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def isqirtcmd(self, message):
		"""Isqirt(18+)"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/36", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def chiqlarincmd(self, message):
		"""Chiqlarin bu gruppadan(18+)"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/37", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def pubgbancmd(self, message):
		"""PUBG Ban Music"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/38", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def siucmd(self, message):
		"""Siuuu"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/41", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def siu2cmd(self, message):
		"""Siuuu 2"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/42", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def toxtacmd(self, message):
		"""To'xta sen ey"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/43", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def chiqcmd(self, message):
		"""Buyoqqa chiqqin oneni s***"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/44", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def oggcmd(self, message):
		"""Not Send Voice🔊"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/45", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def babjicmd(self, message):
		"""Fortnite Or Babaji"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/46", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def omgcmd(self, message):
		"""OOOMG!!!"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/47", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def babji2cmd(self, message):
		"""Fortnite Or Babaji 2"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/48", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def kulishcmd(self, message):
		"""Kulishni jinnisi"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/49", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def b11md(self, message):
		"""11-B Haqida Qisqacha..."""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/50", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def yangiyilcmd(self, message):
		"""Yangi Yil"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/51", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def writecmd(self, message):
		"""Write or down"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/52", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def write2cmd(self, message):
		"""Write or down 2"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/53", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def uztelecomcmd(self, message):
		"""Uztelecom"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/54", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def zornarsacmd(self, message):
		"""Zo'r narsa aytemi?"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/55", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def yedir1cmd(self, message):
		"""Yedirganda..."""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/56", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def saviyacmd(self, message):
		"""Saviyang yo'q..."""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/goloslarhostingi/57", voice_note=True, reply_to=reply.id if reply else None)
		return