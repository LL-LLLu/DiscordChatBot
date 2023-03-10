import random
import chat

def handle_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '!help':
        return "`!help` - shows this message`"

    response = chat.respond(message)

    
    
    return response
    