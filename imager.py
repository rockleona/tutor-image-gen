import requests
from io import BytesIO # 解析照片用
from PIL import Image # 編輯照片用
from os import getenv # 取得 API KEY 用
from dotenv import load_dotenv

load_dotenv()

RANDOM_PHOTO_URL = 'https://api.unsplash.com/photos/random'
API_KEY = getenv("UNSPLASH_API_KEY")

def listImageURL(raw_data):

    links = [photo["urls"]["full"] for photo in raw_data]
    return links

def downloadImages(links):

    image_list = []

    for link in links:
        download = requests.get(link)
        if download.status_code == 200:
            image = Image.open(BytesIO(download.content))
            image_list.append(image)

    return image_list


def getBackground(weather, count):
    global RANDOM_PHOTO_URL

    url = RANDOM_PHOTO_URL + f'?query={weather}&count={count}'

    get_background_request = requests.get(url, headers={
        "Authorization": f'Client-ID {API_KEY}'
    })

    if get_background_request.status_code == 200:
        url_list = listImageURL(get_background_request.json())
        image_list = downloadImages(url_list)
        
        return image_list
    return None
        # for index, image in enumerate(image_list):
        #     image.save(f'download/{weather}_{index}.jpg')