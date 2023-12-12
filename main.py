from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(temperature = 0.1)

from langchain.schema import HumanMessage, AIMessage, SystemMessage

messages = [
    SystemMessage(content = "You are a geography expert. And you only reply in Italian"),
    AIMessage(content = "Ciao, mi chiamo Paolo!"),
    HumanMessage(content = "What is the distance between Mexico and Thailand. also what is your name?")
]

chat.predict_messages(messages)