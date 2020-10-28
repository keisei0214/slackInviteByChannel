import requests

def get(url, params):
  res = requests.get(url, params=params)
  info = res.json()

  if res.status_code != 200:
    print(info)
    raise Exception('エラーが発生しました')

  return info


def getChannelList(token, exclude_archived=True):
  ret = {}

  channel_info = get(
    'https://slack.com/api/conversations.list',
    {
      'token': token,
      'exclude_archived': exclude_archived
    }
  )

  ret.update({c['name']: c['id'] for c in channel_info['channels']})

  while channel_info['response_metadata']['next_cursor']:
    channel_info = get(
      'https://slack.com/api/conversations.list',
      {
        'token': token,
        'exclude_archived': exclude_archived,
        'cursor': channel_info['response_metadata']['next_cursor']
      }
    )
    ret.update({c['name']: c['id'] for c in channel_info['channels']})

  return ret

def getChannelMember(token, channel_id):
  members = []

  member_info = get('https://slack.com/api/conversations.members', params={
    'token': token,
    'channel': channel_id
  })

  members.extend(member_info['members'])

  while member_info['response_metadata']['next_cursor']:
    member_info = get('https://slack.com/api/conversations.members', params={
      'token': token,
      'channel': channel_id
    })

    members.extend(member_info['members'])

  return members
