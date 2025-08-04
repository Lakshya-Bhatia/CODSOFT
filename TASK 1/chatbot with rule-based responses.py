


import re


patterns = {
    r"hi|hello|hey": [
        "Hello! How can I assist you today?",
        "Hi there! How may I help?"
    ],
    r"how are you": [
        "I'm just a bot code, but I'm doing well! And you?",
        "Doing fine! How about yourself?"
    ],
    r"my name is\s*(.*)": [
        "Nice to meet you, %1 🙂",
        "Hi %1, how can I help today?"
    ],
    r"what is your name": [
        "I’m RuleBot, your simple assistant.",
        "You can call me RuleBot."
    ],
    r"tell me a joke": [
        "Why did the robot go on vacation? It needed to recharge!",
        "Why are robots bad at soccer? They keep stopping to recharge!"
    ],
    r"(.*)\s*your (favorite|favourite) (.*)": [
        "I don’t have personal preferences, but I enjoy helping you!",
        "I like all kinds of conversations—but helping you is my favourite 😊"
    ],
    r"thank you|thanks": [
        "You're welcome!",
        "Anytime—glad to help."
    ],
    r"bye|goodbye": [
        "Goodbye! Have a fantastic day!",
        "See you later!"
    ]
}


default_responses = [
    "Sorry, I didn’t catch that—could you rephrase?",
    "I’m not sure how to reply. Try asking another way!"
]

def get_response(user_input: str) -> str:
    user_input = user_input.strip().lower()
    for pattern, responses in patterns.items():
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:

            response = responses[0]

            if "%1" in response and match.groups():
                response = response.replace("%1", match.group(1).strip())


            return response
    return default_responses[0]

def chat_loop():
    print("Chatbot: Hi! I’m your RuleBot. (type 'bye' to quit)\n")
    while True:
        user_input = input("You: ")
        if re.search(r"\b(bye|goodbye)\b", user_input, re.IGNORECASE):

            farewell = get_response(user_input)
            print(f"Chatbot: {farewell}")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat_loop()
