from googleapiclient.discovery import build
import webbrowser
import pprint

def show_image(search):
    search_google = build("customsearch", "v1", developerKey = "")

    results = (search_google.cse().list(q = search, cx = "", num = 1).execute())

    image_link = results["items"][0]["pagemap"]["cse_image"][0]["src"]

    return image_link

# image = show_image("Show me a picture of University of Washington")
# pprint.pprint(image)
# # webbrowser.open(image)