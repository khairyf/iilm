from google import genai
import PIL.Image

user = genai.Client(api_key="")

def knowledge(what_to_know):

    if ".jpg" in what_to_know:
        image = PIL.Image.open(what_to_know)
        ai = user.models.generate_content(
            model = "gemini-2.0-flash", 
            contents=["What is this image?", image]
        )
    else:
        ai = user.models.generate_content(
            model = "gemini-2.0-flash", 
            contents=what_to_know
        )
    return ai.text



