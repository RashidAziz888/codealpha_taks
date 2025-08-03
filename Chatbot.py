def chatbot():
    print("Hi, I am Chatbot!")
    print("How I can assist you?")

    while True:
        user_input = input("You: ").lower()

        if user_input == 'hello':
            print('Hi!')
        elif user_input == 'hi':
            print('Hi!')
        elif user_input == 'how are you':
            print("I'm fine, thanks!")
        elif user_input == 'what is your name':
            print("I'm just a simple chatbot.")
        elif user_input == 'what can you do':
            print("I can chat with you using simple rules!")
        elif user_input == 'bye':
            print("Goodbye!")
            break
        else:
            print("Sorry, I can't understand.")

chatbot()




