# Program 2: Structured Representation Based Question Answering

# Structured form of text sentences
knowledge_base = [
    {
        "subject": "Mary",
        "action": "buy",
        "object": "a red coat",
        "time": "yesterday"
    },
    {
        "subject": "Mary",
        "action": "meet",
        "object": "John",
        "time": "evening"
    }
]

def answer_question(question):
    question = question.lower()

    # Question: What did Mary buy?
    if "what did mary buy" in question:
        for fact in knowledge_base:
            if fact["subject"] == "Mary" and fact["action"] == "buy":
                return fact["object"]

    # Question: Who did Mary meet?
    if "who did mary meet" in question:
        for fact in knowledge_base:
            if fact["subject"] == "Mary" and fact["action"] == "meet":
                return fact["object"]

    return "No answer found."

# Example Run
print("Structured Knowledge Base Loaded.")
user_question = input("Enter your question: ")
print("Answer:", answer_question(user_question))
