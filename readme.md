# 仕様
```
python run.py <追加先のチャンネル> <追加元のチャンネル>
```
と入力することで、指定したチャンネルのユーザをそれを行ったチャンネルに招待する

どこかにhostして、動かすには、`libs/joinChannelMembers.py`の`joinChannelMembers`に適切な引数を与えて呼び出してください。(引数にはチャンネル名を与えます。idを与える場合は`joinChannelMembersById`)

# 導入方法
##　A: botをslackに導入
1. `https://api.slack.com/`にアクセスし、アプリを作成する
2. 左側のカラムから、`Features`の`OAuth & Permissions`を開く
3. scopeに`channels:join`, `channels:manage`, `channels:read`を選択する
4. tokenを生成する。(このトークンはコピーしておく)
5. 任意のSlack workspaceにインストールを行う

## B: tokenの設定
1. `.env_sample`を `.env`という名前でコピー
2.  `.env`のtokenをA.4.でコピーしたtokenに書き換える