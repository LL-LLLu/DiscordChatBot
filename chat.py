import os
import openai
openai.organization = "org-D9yS4ViNOJQMhT46l60xezo2"
openai.api_key = "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"

openai.Model.list()

def respond(message):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ]
    )

    return completion.choices[0].message.content