import asyncio
import time
from datetime import datetime, timedelta
import os
from telethon import TelegramClient, events, Button
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import DeleteMessagesRequest
from telethon.tl.types import PeerUser, PeerChannel
from telethon.errors.rpcerrorlist import UserPrivacyRestrictedError

api_id = 27439390
api_hash = '3a12a02f9791a329acad1415d0f8eb7d'
OWNER_ID = 7050438297  # change to your own id

client = TelegramClient('darx_md_session', api_id, api_hash)

start_time = time.time()

def owner_only(func):
    async def wrapper(event):
        if event.sender_id != OWNER_ID:
            await event.respond("❌ This command is private. Owner only.")
            return
        await func(event)
    return wrapper
def get_readable_time(seconds: int) -> str:
    result = ""
    time_units = [("w", 604800), ("d", 86400), ("h", 3600), ("m", 60), ("s", 1)]
    for unit, unit_seconds in time_units:
        amount = seconds // unit_seconds
        if amount > 0:
            seconds -= amount * unit_seconds
            result += f"{amount}{unit} "
    return result.strip()

def format_mention(user):
    return f"[{user.first_name}](tg://user?id={user.id})"

@client.on(events.NewMessage(pattern='/start'))
@owner_only
async def start(event):
    text = (f"**ᴡᴀɢᴡᴀɴ {format_mention(await event.get_sender())} ɪ ᴀᴍ ᴛʜᴇ ᴅᴀʀx ᴍᴅ ʙᴏᴛ\n\n**"
            "`INFO: ʙᴏᴛ ᴄᴀɴ ʙᴇ ᴀᴅᴅᴇᴅ ᴛᴏ ɢʀᴏᴜᴘs/ᴄʜᴀɴɴᴇʟs ᴀs ᴀᴅᴍɪɴ`\n\n"
            "ᴛʏᴘᴇ /menu ᴛᴏ sᴇᴇ ᴏᴘᴛɪᴏɴs")
    await client.send_message(
            event.chat_id,
            text,
            file='https://i.imgur.com/Pisozu4.jpg',
            buttons=[[
                Button.url("VIEW CHANNEL", "https://t.me/darxtechs")
            ]],
            parse_mode='md'
        )
 
@client.on(events.NewMessage(pattern='/menu'))
@owner_only
async def menu(event):
    now = datetime.now()
    uptime_sec = int(time.time() - start_time)
    uptime = get_readable_time(uptime_sec)
    commands_count = 40 
    nigeria_tz = 'Africa/Lagos'
    nigeria_time = now.strftime('%H:%M:%S')
    nigeria_date = now.strftime('%Y-%m-%d')

    text =         (f"◇ 𝐃𝐀𝐑𝐗 𝐌𝐃 𝐁𝐎𝐓 ◇\n\n"
            f"╭─────────────◆\n"
            f"│ 👨‍💻ᴅᴇᴠ: ɪᴠᴇᴇ 𖦹 ɴᴀᴛɪᴏɴ\n"
            f"│\n"
            f"│ ⏱️ᴛɪᴍᴇ: {nigeria_time} (Nigeria)\n"
            f"│\n"
            f"│ 🗓ᴅᴀᴛᴇ: {nigeria_date}\n"
            f"│\n"
            f"│ ⏳ᴛɪᴍᴇᴢᴏɴᴇ: {nigeria_tz}\n"
            f"│\n"
            f"│ 🚀ᴜᴘᴛɪᴍᴇ: {uptime}\n"
            f"│\n"
            f"│ 🔉ᴄᴏᴍᴍᴀɴᴅs: {commands_count}\n"
            f"│\n"
            f"│ 👤ᴜsᴇʀ: {format_mention(await event.get_sender())}\n"
            f"╰─────────────◆\n\n"
        "            ⌘ 𝐀𝐋𝐋 𝐌𝐄𝐍𝐔 ⌘\n"
        "╭────────═━⊷⊷━═──━⊷\n"
        "│     \n"
        "│⊷ ᴏᴡɴᴇʀ ᴍᴇɴᴜ [/ownermenu]\n"
        "│\n"
        "│⊷ ɢʀᴏᴜᴘ ᴍᴇɴᴜ [/groupmenu]\n"
        "│\n"
        "│⊷ ᴏᴛʜᴇʀ ᴍᴇɴᴜ [/othermenu]\n"
        "│\n"
        "│⊷ ʙᴏᴛ ᴍᴇɴᴜ    [/botmenu]\n"
        "│ \n"
        "╰────────═━┈━═──━┈⊷\n"
        "`ᴜsᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ᴀʙᴏᴠᴇ ᴛᴏ ᴜɴʟᴏᴄᴋ ᴛʜᴇ ғᴜʟʟ ᴍᴇɴᴜ`"
    )

    try:
        await client.send_message(
            event.chat_id,
            text,
            file='https://i.imgur.com/frO2QqZ.jpg',
            buttons=[[
                Button.url("VIEW CHANNEL", "https://t.me/darxtechs")
            ]],
            parse_mode='md'
        )
    except Exception as e:
        await event.respond(f"⚠️ Failed to send menu: `{e}`")

@client.on(events.NewMessage(pattern='/ownermenu'))
@owner_only
async def owner_menu(event):
    text = ("╭────────═━⊷⊷━═──━⊷\n"
            "│     ⌘ 𝐎𝐖𝐍𝐄𝐑 𝐌𝐄𝐍𝐔 ⌘\n"
            "│\n"
            "│⊷ ʙʟᴏᴄᴋ\n"
            "│⊷ ᴠᴠ\n"
            "│⊷ ɢᴇᴛᴘᴘ\n"
            "│⊷ ᴜɴʙʟᴏᴄᴋ\n"
            "│⊷ ᴅᴇʟ\n"
            "│⊷ ᴠᴄᴅ\n"
            "╰────────═━┈━═──━┈⊷")
    await client.send_file(
        event.chat_id,
        'https://i.imgur.com/6t3TQfD.jpg',
        caption=text,
        buttons=[[Button.url("VIEW CHANNEL", "https://t.me/darxtechs")]]
        )
        
@client.on(events.NewMessage(pattern=r'^/uptime$'))
@owner_only
async def uptime(event):
    total_seconds = int(time.time() - start_time)
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    uptime_str = f"{hours}h {minutes}m {seconds}s"
    await event.respond(f"`⏱ DARX-MD has been running for {uptime_str}`")

@client.on(events.NewMessage(pattern='/block'))
@owner_only
async def block(event):
    if not event.is_reply:
        return await event.respond("Reply to a user to block.")
    reply = await event.get_reply_message()
    try:
        await client(functions.contacts.BlockRequest(reply.sender_id))
        await event.respond(f"Blocked {format_mention(reply.sender)}")
    except Exception as e:
        await event.respond(f"Failed to block: {str(e)}")

@client.on(events.NewMessage(pattern='/unblock'))
@owner_only
async def unblock(event):
    if not event.is_reply:
        return await event.respond("Reply to a user to unblock.")
    reply = await event.get_reply_message()
    try:
        await client(functions.contacts.UnblockRequest(reply.sender_id))
        await event.respond(f"Unblocked {format_mention(reply.sender)}")
    except Exception as e:
        await event.respond(f"Failed to unblock: {str(e)}")

@client.on(events.NewMessage(pattern=r'^/del$'))
@owner_only
async def delete_msg(event):
    if not event.is_reply:
        return await event.respond("Reply to a message or text.")
    msg = await event.get_reply_message()
    await msg.delete()
    await event.delete()

@client.on(events.NewMessage(pattern=r'^/vv$'))
@owner_only
async def vv(event):
    if not event.is_reply:
        return await event.respond("❌ Reply to a view-once photo / video.")

    reply = await event.get_reply_message()

    if reply.media and (reply.photo or reply.video):
        try:
            file = await client.download_media(reply.media)
            
            await client.send_file(
                event.chat_id,
                file,
                caption="view-once media saved\n\n
                `POWERED BY DARX TECH`",
                force_document=False
            )
            await event.respond("`ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴅᴀʀx ᴛᴇᴄʜ`.")
        except Exception as e:
            await event.respond(f"⚠️ Failed to save media: {e}")
    else:
        await event.respond("❌ That’s not a view-once photo / video.")

@client.on(events.NewMessage(pattern='/getpp'))
@owner_only
async def getpp(event):
    if not event.is_reply:
        return await event.respond("Reply to a user to get their profile picture.")
    reply = await event.get_reply_message()
    try:
        photos = await client.get_profile_photos(reply.sender_id)
        if not photos:
            return await event.respond("No profile photos found.")
        await client.send_file(event.chat_id, photos[0])
    except Exception as e:
        await event.respond(f"Failed: {str(e)}")

@client.on(events.NewMessage(pattern=r'^/vcd$'))
@owner_only
async def vcd(event):
    me = await client.get_me()
    vcard = (
        "BEGIN:VCARD\n"
        "VERSION:3.0\n"
        f"N:{me.last_name};{me.first_name};;;\n"
        f"FN:{me.first_name} {me.last_name}\n"
        f"TEL;TYPE=CELL:{me.phone if me.phone else ''}\n"
        "END:VCARD"
    )
    await event.respond(f"Here is your vCard:\n```\n{vcard}\n```")
    

@client.on(events.NewMessage(pattern='/groupmenu'))
@owner_only
async def group_menu(event):
    text = ("╭────────═━⊷⊷━═──━⊷\n"
            "│     ⌘ 𝐆𝐑𝐎𝐔𝐏 𝐌𝐄𝐍𝐔 ⌘\n"
            "│\n"
            "│⊷ ᴛᴀɢᴀʟʟ\n"
            "│⊷ ʟᴏᴄᴋ\n"
            "│⊷ ᴜɴʟᴏᴄᴋ\n"
            "│⊷ ᴘʀᴏᴍᴏᴛᴇ\n"
            "│⊷ ᴅᴇᴍᴏᴛᴇ\n"
            "│⊷ ᴋɪᴄᴋ\n"
            "│⊷ ᴅᴇʟ\n"
            "│⊷ ᴋɪᴄᴋᴀʟʟ\n"
            "│⊷ ᴛᴀɢᴀᴅᴍɪɴ\n"
            "│⊷ ɢᴇᴛɢᴘᴘ\n"
            "│⊷ ʟᴇғᴛ\n"
            "│⊷ ʟɪsᴛᴏɴʟɪɴᴇ\n"
            "│⊷ ᴀɴᴛɪʟɪɴᴋ\n"
            "│⊷ ᴀᴘᴘʀᴏᴠᴇ\n"
            "│⊷ ʀᴇᴊᴇᴄᴛ\n"
            "│⊷ ᴋɪᴄᴋɪɴᴀᴄᴛɪᴠᴇ\n"
            "│⊷ ɢᴄʟɪɴᴋ\n"
            "│⊷ ɢᴄɴᴀᴍᴇ\n"
            "│⊷ ʟɪsᴛɪɴᴀᴄᴛɪᴠᴇ\n"
            "╰────────═━┈━═──━┈⊷")
    await client.send_file(
        event.chat_id,
        'https://i.imgur.com/HKOI3GW.jpg',
        caption=text,
        buttons=[[Button.url("VIEW CHANNEL", "https://t.me/darxtechs")]]
        )

@client.on(events.NewMessage(pattern='/tagall'))
@owner_only
async def tagall(event):
    if not event.is_group:
        return await event.respond("This command works only in groups.")
    participants = await client.get_participants(event.chat_id)
    text = "╭────────═━⊷⊷━═──━⊷\n│     ⌘ 𝐓𝐀𝐆 𝐀𝐋𝐋 ⌘\n│\n"
    for user in participants:
        mention = f"@{user.username}" if user.username else format_mention(user)
        text += f"│⊷ {mention}\n"
    text += "╰────────═━┈━═──━┈⊷"
    await event.respond(text, parse_mode='md')

@client.on(events.NewMessage(pattern='/lock'))
@owner_only
async def lock(event):
    if not event.is_group:
        return await event.respond("Use this command in groups only.")
    try:
        await client.edit_permissions(event.chat_id, None, send_messages=False)
        await event.respond("Group locked. Only admins can send messages.")
    except Exception as e:
        await event.respond(f"Failed to lock group: {str(e)}")

@client.on(events.NewMessage(pattern='/unlock'))
@owner_only
async def unlock(event):
    if not event.is_group:
        return await event.respond("Use this command in groups only.")
    try:
        await client.edit_permissions(event.chat_id, None, send_messages=True)
        await event.respond("Group unlocked. All members can send messages.")
    except Exception as e:
        await event.respond(f"Failed to unlock group: {str(e)}")

@client.on(events.NewMessage(pattern=r'^/promote$'))
@owner_only
async def promote(event):
    user = await get_target_user(event)
    if not user:
        return await event.respond("Reply or mention a user to promote.")
    if not await is_admin(event.chat_id, OWNER_ID):
        return await event.respond("bot  must be an admin to do this.")
    try:
        await client(functions.channel.EditAdminRequest(
            channel=event.chat_id,
            user_id=user.id,
            admin_rights=types.ChatAdminRights(
                change_info=True,
                post_messages=True,
                edit_messages=True,
                delete_messages=True,
                ban_users=True,
                invite_users=True,
                pin_messages=True,
                add_admins=False
            ),
            rank="Admin"
        ))
        await event.respond(f"Promoted {format_mention(user)} to admin.")
    except Exception as e:
        await event.respond(f"Failed to promote: {e}")

@client.on(events.NewMessage(pattern=r'^/demote$'))
@owner_only
async def demote(event):
    user = await get_target_user(event)
    if not user:
        return await event.respond("Reply or mention a user to demote.")
    if not await is_admin(event.chat_id, OWNER_ID):
        return await event.respond("bot must be an admin to do this.")
    try:
        await client(functions.is_group.EditAdminRequest(
            channel=event.chat_id,
            user_id=user.id,
            admin_rights=types.ChatAdminRights(
                change_info=False,
                post_messages=False,
                edit_messages=False,
                delete_messages=False,
                ban_users=False,
                invite_users=False,
                pin_messages=False,
                add_admins=False
            ),
            rank=""
        ))
        await event.respond(f"Demoted {format_mention(user)} from admin.")
    except Exception as e:
        await event.respond(f"Failed to demote: {e}")
        
@client.on(events.NewMessage(pattern=r'^/kickall$'))
@owner_only
async def kickall(event):
    if not event.is_group:
        return await event.respond("This command only works in groups.")
    participants = await client.get_participants(event.chat_id)
    count = 0
    for user in participants:
        if not (user.bot or user.id == OWNER_ID):
            try:
                await client.kick_participant(event.chat_id, user)
                count += 1
            except:
                pass
    await event.respond(f"Kicked {count} users.")
    
    
@client.on(events.NewMessage(pattern='/kickinactive'))
@owner_only
async def kickinactive_handler(event):
    if not event.is_group:
        await event.respond("This command is only for groups.")
        return

    me = await client.get_me()
    chat = await event.get_input_chat()

    try:
        permissions = await client.get_permissions(chat, me.id)
        if not permissions.is_admin:
            await event.respond("Bot must be admin to do this.")
            return
    except:
        await event.respond("Couldn't verify admin status.")
        return

    inactive_users = []
    async for user in client.iter_participants(event.chat_id):
        if user.bot:
            continue

        try:
            user_status = user.status
            if hasattr(user_status, 'was_online'):
                if user_status.was_online < datetime.now() - timedelta(days=5):
                    inactive_users.append(user)
        except:
            continue

    if not inactive_users:
        await event.respond("No inactive members found.")
        return

    boxed_mentions = [f"│⊷ @{u.username}" if u.username else f"│⊷ {u.first_name}" for u in inactive_users]
    boxed_text = (
        "╭────────═━⊷⊷━═──━⊷\n"
        "│ ⌘ 𝐊𝐈𝐂𝐊𝐈𝐍𝐆 𝐈𝐍𝐀𝐂𝐓𝐈𝐕𝐄𝐒 ⌘\n│\n" +
        "\n│\n".join(boxed_mentions) +
        "\n╰────────═━┈━═──━┈⊷"
    )
    await event.respond(boxed_text)

    for user in inactive_users:
        try:
            await client.kick_participant(event.chat_id, user.id)
            await asyncio.sleep(1)
        except:
            continue
      

@client.on(events.NewMessage(pattern=r'^/botmenu$'))
@owner_only
async def botmenu(event):
    text = (
        "╭────────═━⊷⊷━═──━⊷\n"
        "│     ⌘ 𝐁𝐎𝐓 𝐌𝐄𝐍𝐔 ⌘\n"
        "│\n"
        "│⊷ ᴘɪɴɢ\n"
        "│⊷ ᴜᴘᴛɪᴍᴇ\n"
        "│⊷ sᴛɪᴄᴋᴇʀ\n"
        "│⊷ ᴛʀᴀɴsʟᴀᴛᴇ\n"
        "│⊷ ᴀɪ\n"
        "│⊷ ɪᴍɢ\n"
        "│⊷ ᴋɪʟʟ\n"
        "╰────────═━┈━═──━┈⊷"
    )

    await client.send_file(
        event.chat_id,
        'https://i.imgur.com/Pisozu4.jpg',
        caption=text,
        buttons=[[Button.url("VIEW CHANNEL", "https://t.me/darxtechs")]]
        )

@client.on(events.NewMessage(pattern=r'^/ping$'))
@owner_only
async def ping(event):
    start = time.time()
    msg = await event.respond("Pong...")
    end = time.time()
    ms = int((end - start)*1000)
    await msg.edit(f"Pong! `{ms} ms`")
    

@client.on(events.NewMessage(pattern=r'^/sticker$'))
@owner_only
async def sticker(event):
    if not event.is_reply:
        return await event.respond("Reply to a photo.")
    reply = await event.get_reply_message()
    if not reply.photo:
        return await event.respond("Reply to a photo.")
    await event.respond("Converting to sticker...")
    await client.send_file(event.chat_id, reply.sticker, force_document=False, voice_note=False)
    await event.delete()


@client.on(events.NewMessage(pattern=r'^/translate (.+)'))
@owner_only
async def translate(event):
    text_to_translate = event.pattern_match.group(1)
    await event.respond(f"Translation (stub): {text_to_translate}")

@client.on(events.NewMessage(pattern=r'^/ai (.+)'))
@owner_only
async def ai(event):
    prompt = event.pattern_match.group(1)
    response = f"AI Response to: {prompt}"
    await event.respond(response)


@client.on(events.NewMessage(pattern=r'^/kill$'))
@owner_only
async def kill(event):
    await event.respond("`Goodbye friend, until we meet again!`")
    await client.disconnect()
    exit()



@client.on(events.NewMessage(pattern=r'^/img (.+)'))
@owner_only
async def img(event):
    query = event.pattern_match.group(1)
    await event.respond(f"Searching image for: {query} (stub)")

@client.on(events.NewMessage(pattern=r'^/channel$'))
async def channel(event):
    dialogs = await client.get_dialogs()
    channels = [d.name for d in dialogs if d.is_channel and (d.is_admin or d.is_creator)]
    await event.respond("Channels you admin:\n" + "\n".join(channels))

@client.on(events.NewMessage(pattern='/othermenu'))
@owner_only
async def other_menu(event):
    text = ("╭────────═━⊷⊷━═──━⊷\n"
            "│     ⌘ 𝐎𝐓𝐇𝐄𝐑 𝐌𝐄𝐍𝐔 ⌘\n"
            "│\n"
            "│⊷ ʏᴛ\n"
            "│⊷ ᴍᴘ3\n"
            "│⊷ sᴏɴɢ\n"
            "│⊷ ɪɢ\n"
            "│⊷ ᴛᴛ\n"
            "│⊷ ᴄᴏɴᴠ\n"
            "╰────────═━┈━═──━┈⊷")
    await client.send_file(
        event.chat_id,
        'https://i.imgur.com/J3TYmjj.jpg',
        caption=text,
        buttons=[[Button.url("VIEW CHANNEL", "https://t.me/darxtechs")]]
        )

@client.on(events.NewMessage(pattern=r'^/yt (.+)'))
@owner_only
async def yt(event):
    url = event.pattern_match.group(1)
    await event.respond(f"Downloading YouTube video from: {url} (stub)")

@client.on(events.NewMessage(pattern=r'^/tt (.+)'))
@owner_only
async def tt(event):
    url = event.pattern_match.group(1)
    await event.respond(f"Downloading TikTok video from: {url} (stub)")

@client.on(events.NewMessage(pattern=r'^/mp3 (.+)'))
@owner_only
async def mp3(event):
    url = event.pattern_match.group(1)
    await event.respond(f"Downloading MP3 from: {url} (stub)")

@client.on(events.NewMessage(pattern=r'^/ig (.+)'))
@owner_only
async def ig(event):
    url = event.pattern_match.group(1)
    await event.respond(f"Downloading Instagram media from: {url} (stub)")


def format_mention(user):
    return f"[{user.first_name}](tg://user?id={user.id})"

print("starting bot...")
client.start()
print("darx-md is now running")
client.run_until_disconnected()
