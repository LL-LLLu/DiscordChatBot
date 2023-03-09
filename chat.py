import os
import openai
openai.organization = "org-D9yS4ViNOJQMhT46l60xezo2"
openai.api_key = os.getenv("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")
openai.Model.list()