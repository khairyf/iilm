from google import genai
from google.genai import types
from PIL import Image

from io import BytesIO

import zmq, zmq.auth
from zmq.auth.thread import ThreadAuthenticator



user = genai.Client(api_key="")


print("\nHello.\n")
print()
print("USING iilm:\n"
      "\tAccount required (Username + Password) to use iilm.\n"
      "\tInteraction with AI through text input, or image input, through path to file.\n"
      "\tClose software by typing \"close\" + \"Enter\" button.")
print()
print("\"Enter\" key to begin.")
if input() != "":
    quit()
print("\nWhat is the username :\n")
username = input()
print("\nEnter your password:\n")
password = input()

ctx = zmq.Context.instance()
auth = ThreadAuthenticator(ctx)
auth.start()
auth.allow("127.0.0.1")
auth.configure_curve(domain = "*", location = ".")
client = ctx.socket(zmq.REQ)
client_public, client_secret = zmq.auth.load_certificate("client_transfer.key_secret")
client.curve_secretkey = client_secret
client.curve_publickey = client_public
server_public, _ = zmq.auth.load_certificate("server_transfer.key")
client.curve_serverkey = server_public
client.connect("tcp://127.0.0.1:8089")

profile_authentication = (username + " " + password).encode()
client.send(profile_authentication)

if client.poll(10000):
    if client.recv().decode() != "success":
        print("Incorrect username and password. Please try again later.")
        exit()



undo = ""

print(f"\nHello, {username}, let's begin.\n\n"
      "What would you like to see/read?\n\nThe program will describe something you want to know about.\n\n"
      "Additionally, the program will show you an image you want to see.\n\n"
      "Average time of response from AI ~3 seconds. May take longer depending on bandwidth.\n\n"
      "Results will only show after hitting \"Enter\" button.\n")
response = input()
print()

while response != "close":
    if response == "redo":
        response = undo
    else:
        response = response.lower()
        undo = response

        ai = user.models.generate_content(
            model = "gemini-2.0-flash-preview-image-generation",
            contents = response,
            config = types.GenerateContentConfig(
                response_modalities = ["TEXT", 'IMAGE']
            )
        )
        
        for part in ai.candidates[0].content.parts:
            if part.text is not None:
                print(part.text)
            elif part.inline_data is not None:
                image = Image.open(BytesIO((part.inline_data.data)))
                image.show()

    print()
    print("Would you like to see/read anything else? Results will only show after hitting \"Enter\" button.\n\n"
          "To redo previous search, type \"redo\" + \"Enter\" button.\n\n"
          "Close software by entering \"close\".\n")
    print()
    response = input()
    print()

auth.stop()
print("Completed log out.\n")
print(f"See you, {username}.")