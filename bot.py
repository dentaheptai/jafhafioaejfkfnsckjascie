import json
import os 

from pyrogram import Client

phone = str(os.environ.get('PHONE', ''))
api_id = int(os.environ.get('API_ID', 0))
api_hash = str(os.environ.get('API_HASH', ''))
passcode = str(os.environ.get('PASSWORD', ''))

def poster():


  with Client('new',api_id=api_id, api_hash=api_hash, phone_number=phone , password=passcode) as app:
    

    with open("newData.json",'r') as f:

      data = json.load(f)

      for d in data:

        print(d["title"],d["loadLink"])
    
        result = app.send_photo('HoneyBearPromotions', d["loadLink"], caption=f'<a href="https://roughamerican.blogspot.com">{d["title"]}</a>', parse_mode="HTML")

        break



if __name__ == '__main__':
  poster()
