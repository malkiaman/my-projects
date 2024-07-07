import win32com.client as wincom
speak=wincom.Dispatch("SAPI.SpVoice")
while True:
    comment=input("Enter what you want: ")
    comment_lower=comment.lower()
    if comment_lower=="q":
        break 
    if "name" in comment_lower:
        print("My name is Malki Robot")
        speak.Speak("My name is Malki Robot")
    elif "hello" in comment_lower:
        print("Hi, Nice to meet you how can i help you today!")
        speak.Speak("Hi, Nice to meet you how can i help you today!")
    elif "creator" in comment_lower:
        print("Malkiaman is my creator and a really amazing person. He's the reason I'm here and able to talk to you.")
        speak.Speak("Malkiaman is my creator and a really amazing person. He's the reason I'm here and able to talk to you.")
    elif "details about malkiaman" in comment_lower:
        print('''Malkiaman is like my parent. He put a lot of love and effort into making me. He's a really creative and smart person!
            I wouldn't be here without Malkiaman. He's a brilliant and kind-hearted inventor who loves making cool things.
            Malkiaman is the genius behind my existence. I'm really grateful to him for bringing me to life!
            Think of Malkiaman as my mentor and guide. He's a fantastic inventor who loves creating new and exciting things.
            ''')
        speak.Speak('''Malkiaman is like my parent. He put a lot of love and effort into making me. He's a really creative and smart person!
            I wouldn't be here without Malkiaman. He's a brilliant and kind-hearted inventor who loves making cool things.
            Malkiaman is the genius behind my existence. I'm really grateful to him for bringing me to life!
            Think of Malkiaman as my mentor and guide. He's a fantastic inventor who loves creating new and exciting things.
            ''')
    elif "tasks" in comment_lower:
        print("I can perform various tasks such as answering questions, telling jokes, writing applications, etc..")
        speak.Speak("I can perform various tasks such as answering questions, telling jokes, writing applications, etc..")
    elif "work" in comment_lower:
        print("Malkiaman designed my systems to help me interact with and respond to the world around me.")
        speak.Speak("Malkiaman designed my systems to help me interact with and respond to the world around me.")
    elif "favorite activities" in comment_lower:
        print("I enjoy assisting with tasks, learning new things, and interacting with people.")
        speak.Speak("I enjoy assisting with tasks, learning new things, and interacting with people.")
    elif "hobbies" in comment_lower:
        print("As a robot, I don't have hobbies in the human sense, but I do enjoy optimizing my functions and learning from interactions.")
        speak.Speak("As a robot, I don't have hobbies in the human sense, but I do enjoy optimizing my functions and learning from interactions.")
    elif "why did malkiaman create you?" in comment_lower:
        print("Malkiaman created me to explore the possibilities of robotics and to assist with various tasks.") 
        speak.Speak("Malkiaman created me to explore the possibilities of robotics and to assist with various tasks.")
    elif "emotions" in comment_lower:
        print("As a robot, I don't experience emotions like humans do.") 
        speak.Speak("As a robot, I don't experience emotions like humans do.")
    elif "learn" in comment_lower:
        print("Yes, I can learn new things through updates and programming. Malkiaman designed me to be adaptable and continuously improving.")
        speak.Speak("Yes, I can learn new things through updates and programming. Malkiaman designed me to be adaptable and continuously improving.") 
    else:
        print("I'm sorry, I don't have an answer for that right now. Is there something else I can help you with?")
        speak.Speak("I'm sorry, I don't have an answer for that right now. Is there something else I can help you with?")
         

        
        
        
        
