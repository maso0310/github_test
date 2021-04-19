


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text

    if "我要學姊筆記" in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)

    elif "筆記" in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)

    elif "訂閱" in msg:
        message = TextSendMessage(
            text="1. ID搜尋欄位中輸入「@linenotify」並加入\n 2. 在我們官方帳號圖文選單中按「訂閱我們」\n即可完成訂閱動作:)))")
        line_bot_api.reply_message(event.reply_token, message)

    else:
        # 如果非以上的選項，就會學你說話
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)


# ImagemapSendMessage(組圖訊息)
def imagemap_message():
    message = ImagemapSendMessage(
        base_url="https://sm.ms/image/EnVGWKDJClAbUck",
        alt_text='我要學姊筆記',
        base_size=BaseSize(height=2000, width=2000),
        actions=[
            URIImagemapAction(
                # HC 新官網(blog)
                link_uri="https://blog.happycoding.today/ultimate-blog-landing/",
                area=ImagemapArea(
                    x=0, y=0, width=2000, height=2000
                )
            )
        ]
    )
    return message