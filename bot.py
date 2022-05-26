import json
import os 
import traceback
from pyrogram import Client

session = str(os.environ.get('STRING_SESSION', ''))
api_id = int(os.environ.get('API_ID', 0))
api_hash = str(os.environ.get('API_HASH', ''))


def poster():
  
  
  try:

    with Client(api_id=api_id, api_hash=api_hash, session_string=session) as app:


      with open("newData.json",'r') as f:

        data = json.load(f)

        for d in data:

          print(d["title"],d["loadLink"])

          result = app.send_photo('HoneyBearPromotions', d["loadLink"], caption=f'<a href="https://roughamerican.blogspot.com">{d["title"]}</a>')

          break

  except:
    print(traceback.format_exc())


if __name__ == '__main__':
  poster()
