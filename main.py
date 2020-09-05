import requests
import json


file_path = 'TEST2.txt'

with open(file_path) as f:
    mydata = f.read()

header = {'Authorization' : '#Введите токен'}


def upload():
  disc = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload?path=/file_path', headers = header)
  href = (disc.json()['href'])
  response = requests.put(href, data= mydata)
  print(f'Ваш {file_path} успешно загружен')


upload()
