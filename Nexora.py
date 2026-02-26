from models.llm import LLM

if __name__ == "__main__":
    llm = LLM()
    
    while True:
        user_input = input("You: ")
        response = llm.generate(user_input)
        print("Nexora:", response)