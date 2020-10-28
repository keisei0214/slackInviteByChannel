from dotenv import load_dotenv
import os
from libs.joinChannelMembers import joinChannelMembers
import sys

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_TOKEN = os.environ.get('TOKEN')

if __name__ == "__main__":
  args = sys.argv
  if joinChannelMembers(API_TOKEN, args[1], args[2]):
    print(f'チャンネル{args[2]}から、チャンネル{args[1]}への招待に成功しました')