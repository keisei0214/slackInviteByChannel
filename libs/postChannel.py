import requests
from .getChannelInfo import getChannelMember

def joinChannel(token, channel_id):
  res = requests.post('https://slack.com/api/conversations.join', params={
    'token': token,
    'channel': channel_id
  })

  res_info = res.json()

  return res_info['ok']

def inviteChannel(token, channel_id, users, check=True):
  if check:
    already_member = getChannelMember(token, channel_id)
    users = [u for u in users if u not in already_member]

  print(f'{len(users)}人のユーザを招待します')
  if len(users) == 0:
    return True

  if len(users) > 1000:
    for i in range(0, len(users), 1000):
      inviteChannel(token, channel_id, users[i: i + 1000], check=False)

  
  res = requests.post('https://slack.com/api/conversations.invite', params={
    'token': token,
    'channel': channel_id,
    'users': ','.join(users)
  })

  res_info = res.json()

  return res_info['ok']
