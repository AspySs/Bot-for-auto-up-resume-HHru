import time
from telethon import TelegramClient

# Вставляем api_id и api_hash
api_id = <api_id>
api_hash = '<api_hash>'

with TelegramClient('hh_session', api_id, api_hash, system_version="4.16.30-vxCUSTOM") as client:
    async def main():
        await client.send_message('hh_rabota_bot', '/start')
        time.sleep(5)
        await client.send_message('hh_rabota_bot', '👤 Личный кабинет')
        time.sleep(5)
        await client.send_message('hh_rabota_bot', 'Поднять резюме в поиске')
        time.sleep(5)
        await client.send_message('hh_rabota_bot', 'Поднять')
        f = open("log.txt", 'a')
        f.write('поднял резюме : ' + str(time.ctime(time.time())) + '\n')
        f.close()




client.start()
print('STARTED')

import win32gui, win32con

the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide, win32con.SW_HIDE)

while True:
    client.loop.run_until_complete(main())
    time.sleep(60*60*4 + 60)




