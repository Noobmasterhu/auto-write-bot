# GITHUB: NOOBMASTERHU
# TELEGRAM: @THE_KAKASHI_COPY_NINJA // @CLANSLAYER 


# imports

from pyrogram import Client, filters
from pyrogram.types import Message, User
from time import sleep
import requests
from telegraph import upload_file
from bs4 import BeautifulSoup


apikey = "ur ocr api key"  # get from https://ocr.space/ocrapi
api_id = ur api id
api_hash = "ur api hash"

wordbot = Client("ur user string session", api_id, api_hash)



@wordbot.on_message(filters.photo & filters.user(1806208310))
async def autoword(client, message):

  userid = str(message.chat.id)

  img_path = (f"./DOWNLOADS/{userid}.jpg")

  img_path = await client.download_media(message=message, file_name=img_path)

  tlink = upload_file(img_path)

  url= f"https://telegra.ph{tlink[0]}"

  ur=f"https://api.ocr.space/parse/imageurl?apikey={apikey}&url={url}&language=eng&detectOrientation=True&filetype=JPG&OCREngine=1&isTable=True&scale=True"

  data = requests.get(ur).json()

  word = data['ParsedResults'][0]["TextOverlay"]['Lines'][0]["LineText"]

  await wordbot.send_message(text=word,chat_id=userid)

  os.remove(image_path)


wordbot.run()
