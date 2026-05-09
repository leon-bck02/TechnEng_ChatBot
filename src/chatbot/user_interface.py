from .llm_client import LLM_Client

def init_conversation ():
    user_exit = False
    llm_client = LLM_Client()
    print("- Funny Technical English Chatbot -")
    print("Type 'exit' to quit. \n")

    user_name = input("Enter your name: ")

    while not user_exit:    
        user_input = input("You: ")

        # Exit chat in case user types 'exit'
        if user_input.strip().lower() == "exit":
            user_exit = True
            print(f"Goodbye, {user_name}")
            break
        # Repeat input if no user input is given
        if not user_input:
            continue
        # If user input is given, try to call the llm
        try: 
            displayed_response = llm_client.get_llm_response(user_input)
            print(f"Bot: {displayed_response}")
        except Exception as e:
            print(type(e).__name__, e)
