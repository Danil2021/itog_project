from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

chat = GigaChat(
    credentials='ZTJlYjNhYWEtYTAwYi00YTllLWE3ZDQtMWZiOTcxNDhlZDQ4OmFhNGY1YmEwLTc3ZTgtNGYwMS1hZTc5LTlkODQwNTQyNjBlZg==',
    verify_ssl_certs=False)


def ai_work(text):
    messages = [
        SystemMessage(
            content="Ты программа сокращатель текста. Ты сокращаешь тексты которые тебе присылают."
                    "Знай что тексты приходять тебе от программы распознователя голоса из за чего в сообщении "
                    "могут быть ошибки. Давай краткую выжимку из текста."
        )
    ]
    messages.append(HumanMessage(content=text))
    res = chat(messages)
    return res.content