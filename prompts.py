import openai

def generate_response(user_input, conversation_history):
    conversation_history.append({"role": "user", "content": user_input})
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=conversation_history,
        max_tokens=150,
        temperature=0.7
    )
    
    reply = response.choices[0].message['content'].strip()
    conversation_history.append({"role": "assistant", "content": reply})
    return reply
