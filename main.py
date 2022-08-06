from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
import requests
import hostfollow
import pySocks

adminbot = config.adminbot
user_accept = config.useraccept
adminid = config.admin_id

proxies = {     'http': 'socks5://152.206.85.205:59902' }

app = Client("bot",
api_id = config.apiid,
api_hash = config.apihash,
bot_token = config.token
)

print("GOOD")

@app.on_message()
async def bot(c: Client, msj: Message):
    username = msj.from_user.username
    usertext =  msj.text
    group_id = -709691117
    
    if username == adminbot or username == user_accept:
    #Elimine el comentado para que el bot se use con seguridad
        msg = "Leyendo.."

        if '/start' in usertext:
            msg6 = await msj.reply("Iniciando sesion...")
            await msg6.edit("Sesion iniciada correctamente :D",
            reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("Desarrollador",url = "https://t.me/rockstar984")]
            ]))     
            await app.send_message(group_id,f"Usuario {username} inicio sesion")
            return
        elif '/adduser' in usertext:
            if adminbot == username:
                user = usertext.split(" ")[1]
                list.append(config.useraccept,user )
                await msg.edit(f"Usuario: @{user} añadido correctamente") 
                return
            else: msj.reply("No eres admin")
        elif '/banuser' in usertext:
             if adminbot == username:
                user = usertext.split(" ")[1]    
                if user in config.useraccept:
                    list.remove(config.useraccept, user)
                    await msj.reply(f"Usario:{user} fue baneado")     
                else: await msj.reply("El usuariono no tiene acceso")
             else: await msj.reply("No eres admin")          
        elif '/watch' in usertext:
            url = usertext.split(" ")[1]
            msjscan = await msj.reply("Monitoreando..")
            if "https" or "http" in usertext:
                r = requests.head(url, proxies=proxies)
                if r.status_code == 200 or r.status_code == 303:
                    await msjscan.edit(f"Escaneo completado:\n [{url} is UP]",
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton("Check Page",url=f"{url}")
                        ]]))
                elif r.status_code == 404:
                    await msjscan.edit(f"Escaneo completado:\n [{url}] is Error..\nType Error = (404-Page Not Found)")    
                elif r.status_code == 403:
                    await msjscan.edit(f"Escaneo completado:\n [{url}] is Error..\nType Error = (403-Forbidden)")
                elif r.status_code == 502:
                    await msjscan.edit(f"Escaneo completado:\n [{url}] is Error..\nType Error = (502-Bad Gateway)")
                elif r.status_code == 500:
                    await msjscan.edit(f"Escaneo completado:\n [{url}] is Error..\nType Error = (500-Internal Server Error)")  
                elif r.status_code == 503:
                    await msjscan.edit(f"Escaneo completado:\n [{url}] is Error..\nType Error = (503-Service Unavailable)")
                else:
                    await msjscan.edit(f"Escaneo completado:\n [{url}] is Error..\nType Error = ({r.status_code})")     
            else:
                await msg.edit(f"[{url}] No se ha podido monitorear")
            return    
        elif '/addhost' in usertext:
            host = str(usertext).split(" ")[1]
            if 'https' or 'http' in usertext:
                list.append(hostfollow.followhost, host)
                await msj.reply(f"Monitorando: {host}")
            else: await msg.edit("No se ha podido agregar el sitio")
        elif '/see_host' in usertext:
            await msj.reply(f"Paginas agregadas:\n{hostfollow.followhost}")
        elif '/del_host' in usertext:
            host = str(usertext).split(" ")[1]    
            if host in hostfollow.followhost:
                list.remove(hostfollow.followhost, host)
                await msj.reply(f"Host: {host} eliminado :(")
            else: await msj.reply(f"Host no se ha guardado")      
        elif "/clear_host" in usertext:
           list1 = hostfollow.followhost
           try: 
            if list1 == []:
                await msj.reply("No se pudo limpiar, no posee ningun elemento en la lista") 
            else: 
                list.clear(list1)
                await msj.reply("Lista limpiada correctamente")     
           except:pass 
    else: await msj.reply("Acceso denegado")         

if __name__ == '__main__':
    app.run()            
