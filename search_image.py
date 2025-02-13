from googleapiclient.discovery import build


def show_image(search):
    search_google = build("customsearch", "v1", developerKey = "")

    results = (search_google.cse().list(q = search, fileType = ".jpg", num = 1).execute())

    image_link = results["items"][0]["pagemap"]["cse_image"][0]["src"]

    return image_link

