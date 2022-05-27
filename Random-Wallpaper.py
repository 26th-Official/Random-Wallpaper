from requests import ConnectionError
import requests
import urllib.request
import time
import ctypes
import os

client_id = input("Enter your Unsplash Access key:- ")
query = input("Enter your Query:- ")
orientation = input("Enter the Image Orientation (portrait or landscape):- ")
duration = int(input("Enter the desired time interval for wallpaper change(In Seconds):- "))



directory_path = r"D:\python\Unsplash\Wallpapers"
files = os.listdir(directory_path)
count = len(files)

def unsplash(count):
    url = "http://api.unsplash.com/photos/random/?client_id="+client_id+"&+query="+query+"&orientation="+orientation

    response = requests.post(url)
    jsons = response.json()
    file =jsons['urls']['raw']
    print(file)

    
    name = "wallpaper "+str(count)+".jpg"
    path = "D:\\python\\Unsplash\\Wallpapers\\"+name
    urllib.request.urlretrieve(file,path)
    
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)

    time.sleep(duration)

while True:
    try:
        count += 1
        unsplash(count)
    except ConnectionError:
        pass