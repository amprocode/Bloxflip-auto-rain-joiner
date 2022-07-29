import json, os, time, cloudscraper, webbrowser, pyautogui, random
from win10toast import ToastNotifier
from discord_webhook import DiscordWebhook, DiscordEmbed

os.system(f'title Bloxflip Auto Rain Joiner ^')

with open("config.json", "r") as config:
  config = json.load(config)

storage = []
scraper = cloudscraper.create_scraper()
webhook_enable = config['webhook_enabled']
webhookurl = config['webhook']
minimum = config['minimum_amount']
ping = config['webhook_ping']
refresh = config['refresh_rate']
auth = config['authorization']
winnotif = config['windows_notification']
mouse_move = config['mouse_movement']

if webhook_enable == "True":
  webhook = DiscordWebhook(url=webhookurl, content=f"{ping}")

toast = ToastNotifier()

try:
  get = scraper.get("https://rest-bf.blox.land/user", headers = {"origin": "https://bloxflip.com", "x-auth-token": auth})
  info = get.json()['user']
  print(f"Logged in as {info['robloxUsername']}\nCurrent balance: {info['wallet']}\n\n")
except:
  input("Invalid Auth Token\nPress enter to exit.")
  quit()
if webhook_enable == "True":
    thumburl = (f"https://www.roblox.com/headshot-thumbnail/image?userId={info['robloxId']}&height=50&width=50&format=png")
    embed = DiscordEmbed(title=f"Logged in!", url="https://bloxflip.com", color=0x37bf19)
    embed.add_embed_field(name="Logged into bloxflip as", value=f"{info['robloxUsername']}")
    embed.add_embed_field(name="Current balance", value=f"{info['wallet']}")
    embed.set_timestamp()
    embed.set_thumbnail(url=thumburl)
    webhook.add_embed(embed)
    webhook.execute()
    webhook.remove_embed(0)
        
while True:
    try:
      r = scraper.get('https://rest-bf.blox.land/chat/history').json()
      check = r['rain']
      if check['active'] == True:
          if check['prize'] >= minimum:
            store = scraper.get("https://rest-bf.blox.land/user", headers = {"x-auth-token": f"{auth}"}).json()['user']['wallet']
            storage.append(store)
            grabprize = str(check['prize'])[:-2]
            prize = (format(int(grabprize),","))
            host = check['host']
            getduration = check['duration']
            convert = (getduration/(1000*60))%60
            duration = (int(convert))
            waiting = (convert*60+10)
            sent = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(int(time.time())))
            url = 'https://bloxflip.com'
            webbrowser.get().open(url, new=0, autoraise=True)
            time.sleep(1)
            while True:
              join = pyautogui.locateCenterOnScreen('assets/pro.png', confidence = 0.7)
              if join:
                time.sleep(1)
                pyautogui.moveTo(join)
                time.sleep(0.5)
                pyautogui.click()
                if mouse_move == "True":
                  for i in range(3):
                    number1 = random.randint(0, 1000)
                    number2 = random.randint(0, 1000)
                    pyautogui.moveTo(number1, number2, 2)
                time.sleep(waiting/3)
                pyautogui.hotkey('ctrl', 'w')
                break
            info = scraper.get("https://rest-bf.blox.land/user", headers = {"x-auth-token": f"{auth}"}).json()['user']
            checker = scraper.get("https://rest-bf.blox.land/chat/history").json()['rain']['players']
            if info['robloxId'] in checker:
              print(f"Successfully joined rain!\nRain amount: {prize} R$\nExpiration: {duration} minutes\nHost: {host}\nTimestamp: {sent}\n\n")
              if webhook_enable == "True":
                thumburl = (f"https://i.giphy.com/media/l41YevbrMDaHgismI/200.gif")
                embed = DiscordEmbed(title=f"Successfully joined a rain!", url="https://bloxflip.com", color=0xFFC800)
                embed.add_embed_field(name="Rain Amount", value=f"{prize} R$")
                embed.add_embed_field(name="Expiration", value=f"{duration} minutes")
                embed.set_timestamp()
                embed.set_thumbnail(url=thumburl)
                webhook.add_embed(embed)
                webhook.execute()
                webhook.remove_embed(0)
              if winnotif == "True":
                toast.show_toast("Bloxflip Rain!", f"Rain amount: {prize} R$\nExpiration: {duration} minutes\nHost: {host}\n\n", icon_path="assets/tick.ico", duration=10)
            else:
              print(f"Failed to join rain!\nRain amount: {prize} R$\nExpiration: {duration} minutes\nHost: {host}\nTimestamp: {sent}\n\n")
              if webhook_enable == "True":
                thumburl = (f"https://i.giphy.com/media/l41YevbrMDaHgismI/200.gif")
                embed = DiscordEmbed(title=f"Failed to join rain!", url="https://bloxflip.com", color=0xde1414)
                embed.add_embed_field(name="Rain Amount", value=f"{prize} R$")
                embed.add_embed_field(name="Expiration", value=f"{duration} minutes")
                embed.set_timestamp()
                embed.set_thumbnail(url=thumburl)
                webhook.add_embed(embed)
                webhook.execute()
                webhook.remove_embed(0)
              if winnotif == "True":
                toast.show_toast("Bloxflip Rain!", f"Rain amount: {prize} R$\nExpiration: {duration} minutes\nHost: {host}\n\n", icon_path="assets/cross.ico", duration=10)
            time.sleep(waiting)
      elif check['active'] == False:
        time.sleep(refresh)
    except Exception as e:
      print(e)
      time.sleep(refresh)
