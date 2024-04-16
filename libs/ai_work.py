from openai import OpenAI

def shorted_text(text):
    client = OpenAI(api_key='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')
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user",
             "content": f"Ты должен сокращать тексты которые тебе отправляют. Ты можешь додумать что либо, но не изменять смысл текста. Вот сам текст: {text}"}
        ]
    )
    return completion.choices[0].message.content