from google import genai

user = genai.Client(api_key="AIzaSyCKvJjsyuSb7aYUedKRFDxGoqLU9C9mVZs")

def knowledge(what_to_know):

    ai = user.models.generate_content(
        model = "gemini-2.0-flash", 
        contents=what_to_know
    )
    return ai.text



