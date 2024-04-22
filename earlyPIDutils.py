import requests
from datetime import datetime
import threading
import tensorflow as tf
import numpy as np

from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input
import urllib.request
from PIL import Image
from io import BytesIO
from colorama import Fore,Style
import random


model = tf.keras.applications.InceptionV3(weights='imagenet')
lock = threading.Lock()

def log(content):
    with lock:
        print(f'[{datetime.now()}] {Fore.LIGHTBLUE_EX}{content}{Style.RESET_ALL}')

def log_success(content):
    with lock:
        print(f'[{datetime.now()}] {Fore.LIGHTGREEN_EX}{content}{Style.RESET_ALL}')

def get_proxy():
    
    proxies_list =[]
    with open('proxy.txt') as f:
        for line in f:
            proxies_list.append(line.strip())

    proxy_chosen = random.choice(proxies_list)
    proxy_ditails = proxy_chosen.split(":")
    proxy = proxy_ditails
    pelneproxy = proxy[2]+":"+proxy[3]+"@"+proxy[0]+":"+proxy[1]
    proxies = {
        'http': 'http://'+pelneproxy,
        'https': 'http://'+pelneproxy}
    return proxies

def scrap(pid) -> bool:
    for i in range(1,4):
        response  = requests.get(f"https://images.asos-media.com/products/cookerzy/{pid}-{i}",proxies=get_proxy())
        if response.ok:
            CorrectPID = True
        else:
            CorrectPID  = False
    return CorrectPID

def check(pid):    
    headers = {
                    'Host': 'www.asos.com',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/97.0.0.0',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'referer': 'https://www.asos.com/pl/mezczyzni/',
                    'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
                }

    response = requests.get(f'https://www.asos.com/pl/cookerzy/prd/{pid}',headers=headers,timeout=10,proxies=get_proxy())
    if not response.ok:
        log(f'[{response.status_code}] Connection error')

    return response

def fetch_link(pid) ->str:
    link = f'https://images.asos-media.com/products/cookerzy/{pid}-2'
    return link

def split_number_into_ranges(start_num, end_num):
    num = end_num - start_num + 1
    range_size = num / 300
    ranges = []
    for i in range(100):
        start = start_num + i * range_size
        end = start_num + (i+1) * range_size - 1 if i < 99 else end_num
        if i < 99:
            next_start = start_num + (i+1) * range_size
            end = next_start - 1
        ranges.append((int(start), int(end)))
    return ranges


def checkImage(url):
    log(f"Fetching image for {url}")
    with urllib.request.urlopen(url) as url_file:
        image_file = url_file.read()
    img = Image.open(BytesIO(image_file))

    img = img.resize((299, 299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    # preds = predict_fn(x)

    if np.argmax(preds[0]) == 770: # Check if image contain shoes
        return "SUCCESS"
    else:
        return "FAIL"

