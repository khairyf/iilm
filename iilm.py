import ai_google_gemini as ai

print("Let's begin. What would you like to read?")
response = input()

while response != "close":
    print(ai.knowledge(response))
    print("Would you like to read anything else? Close software with \"close\"")
    response = input()
