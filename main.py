import pytchat
import time

# ライブストリームのIDを設定
VIDEO_ID = "XXXXXXXXXXX"

# コメントイテレータを作成
chat = pytchat.create(video_id=VIDEO_ID)

# チャットコメントを取得して表示
while chat.is_alive():
    for item in chat.get().items:
        message = item.message
        name = item.author.name
        print(f"{item.datetime} [{name}] {message}")
    time.sleep(3)