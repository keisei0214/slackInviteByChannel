from .getChannelInfo import getChannelList, getChannelMember
from .postChannel import inviteChannel, joinChannel

def joinChannelMembersById(token, to_channel_id, from_channel_id):
  if not joinChannel(token, to_channel_id):
    raise Exception(f'招待先のチャンネルにbotが入れません')

  invite_members = getChannelMember(token, from_channel_id)
  result = inviteChannel(token, to_channel_id, invite_members)

  if not result:
    raise Exception('ユーザの招待に失敗しました')

  return True

def joinChannelMembers(token, to_channel_name, from_channel_name):
  '''
  from_channel_nameに指定したチャンネルのユーザを、to_channel_nameで指定したチャンネルに招待する
  '''
  channel_list = getChannelList(token)

  if to_channel_name not in channel_list:
    raise Exception(f'チャンネル{to_channel_name}が存在しません')
  if from_channel_name not in channel_list:
    raise Exception(f'チャンネル{from_channel_name}が存在しません')

  return joinChannelMembersById(token, channel_list[to_channel_name], channel_list[from_channel_name])
