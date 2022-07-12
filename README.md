# Bloxflip-auto-rain-joiner

## Update v1.0:
- Initial release

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Information:
- When there is a rain at [bloxflip](https://bloxflip.com) this program will join the rain and let you know some information about it
- If you want to use it check license so you know your limits
- If you dont trust it, its literally open source

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Installation:
1) First download the latest version of the program, either the exe or the python version.
2) Extract the files to a foler of your choice
3) Now run the **"installer.bat"** file and it should start running, now you can minimise the chrome browser and the program and do some work while waiting for a notification. 
- Any problems open up a new issue on this github respitory!

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Notes:
- If you want to donate you can donate via BTC however i am not going to force you to. All features are free.
- BTC Address: **bc1q4ktqs0xa0xsgwk9lyymkux2739c4azey2crvtu**
- If you have any questions, bugs or issues, make an [issuse](https://github.com/amprocode/Bloxflip-auto-rain-joiner/issues) or join the [discord](https://discord.gg/cuUtsgMUPb)
- Enjoy!

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Config guide:

Default config.json file:
```json
{
  "minimum_amount": 500,
  "refresh_rate": 30,
  "windows_notification": "True",
  "webhook_enabled": "False",
  "webhook_ping": "<@1234567890987654>",
  "webhook": "https://discord.com/api/webhooks/xxxxxxxx/xxxxxxxxxxxxxx",
  "authorization": "auth_token"
}
```
### minimum_amount:
Minimum rain amount intended for the program required to send you a notification. If you dont want this and want to be notified of all rains leave it at 500

Example: If you set it to 1000 it will only notify you of rains that are bigger then or equal to 1000 R$

### refresh_rate:
How often you want it to check if there is a rain currently happening (in seconds)

⚠️ WARNING ⚠️
- Recommended to not go below 15 seconds because you dont want your potato PC to crash
- Experiment with this feature, see what works for you

### windows_notification:
If set to "True" then a popup on the bottom right on your screen will display showing you information about the current rain

Here is an example:

![image](https://user-images.githubusercontent.com/79641603/178537964-61a167b9-4013-4ef2-8519-d2c45c48a170.png)

- A green tick indicates it joined the rain successfully.
- The red cross indicates it failed to join the rain.

### webhook_enabled:
Should be obvious but if you want the rain notifier to send a message to your discord webhook set it to "True"

### webhook_ping:
You can now ping a role or user instead of @everyone. If you need help getting an ID im sure this will help:

https://youtu.be/KVLdpboY7bg

Setting up ping:

If you want to ping **@everyone** or **@here** make sure your webhook_ping setting looks something like this:
```
"webhook_ping": "@everyone",
```
If you want to ping a **user** make sure your webhook_ping setting looks something like this:
```
"webhook_ping": "<@747719812054253568>",
```
If you want to ping a **role** just put a **&** symbol infront of the numbers. It should look something like this:
```
"webhook_ping": "<@&690632567663575090>",
```

**Obviously these are examples, replace the numbers with your own**

### webhook:
If you set webhook_enabled to "True" input your webhook into here to it can actually send it to you

Example of webhook:

![image](https://user-images.githubusercontent.com/79641603/178446758-7e8a5e90-cc56-45d5-bac3-35062bcb4bb6.png)

### authorization:
This is your bloxflip login token, this is used to get your username and robloxid.

- To get this head to [bloxflip](https://bloxflip.com).
- Next press the "F12" key on your keyboard or "CTRL + SHIFT + I"
- Now make sure "console" is selected, if not just click on it (image attached)

![image](https://user-images.githubusercontent.com/79641603/178447705-533c36c2-d3c1-4019-ab0c-8cd7770e4350.png)

- Next paste in the code below
```
copy(localStorage.getItem('_DO_NOT_SHARE_BLOXFLIP_TOKEN'))
```
- You should now have your bloxflip token copied to your clipboard, just open your config file and paste it inbetween the quotation marks.

## Current Issues:
- None
