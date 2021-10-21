import requests
from bs4 import BeautifulSoup
from time import sleep
import random
import json
import time
from urllib.request import quote
from urllib.request import unquote
from datetime import datetime
from math import floor
import csv
z = list()
po = 0
fd = 0
name_file = ''
cookie = '__cfduid=da6b6b5b9f01fd022f219ed53ac3935791610912291; sessid=ef757cc130c5cd228be88e869369c654.1610912291; _ga=GA1.2.559434019.1610912292; _gid=GA1.2.381990959.1610912292; _fbp=fb.1.1610912292358.1831979940; u=2oiycodt.1oaavs8.dyu0a4x7fxw0; v=1610912321; buyer_laas_location=641780; buyer_location_id=641780; luri=novosibirsk; buyer_selected_search_radius4=0_general; buyer_local_priority_v2=0; sx=H4sIAAAAAAACAxXLQQqAIBAF0Lv8dYvRLEdvU0MIBU0iKCHePXr71zGfefd1W5RLYick2kSakiB2VETclpf85n19RJMSp4vJOSlM%2F2BMOBDNaigE9taM8QH0oydNVAAAAA%3D%3D; dfp_group=100; _ym_uid=1610912323905107257; _ym_d=1610912323; _ym_visorc_34241905=b; _ym_isad=2; _ym_visorc_419506=w; _ym_visorc_188382=w; __gads=ID=2cff056a4e50a953-22d0341a94b900a6:T=1610912323:S=ALNI_MZMbOe0285QjW7EVvsYtSa-RA_Vpg; f=5.8696cbce96d2947c36b4dd61b04726f1a816010d61a371dda816010d61a371dda816010d61a371dda816010d61a371ddbb0992c943830ce0bb0992c943830ce0bb0992c943830ce0a816010d61a371dd2668c76b1faaa358c08fe24d747f54dc0df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b978e38434be2a23fac7b9c4258fe3658d831064c92d93c3903815369ae2d1a81d04dbcad294c152cb0df103df0c26013a20f3d16ad0b1c5462da10fb74cac1eab2da10fb74cac1eab3c02ea8f64acc0bdf0c77052689da50d2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab91e52da22a560f5503c77801b122405c48ab0bfc8423929a6d7a5083cc1669877def5708993e2ca678f1dc04f891d61e35b0929bad7c1ea5dec762b46b6afe81f200c638bc3d18ce60768b50dd5e12c30e37135e8f7c6b64dc9f90003c0354a346b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7acf8b817f3dc0c3f21c1eac53cc61955882da10fb74cac1eab2da10fb74cac1eab5e5aa47e7d07c0f95e1e792141febc9cb841da6c7dc79d0b' 
headers = {
    'content-type': "application/json;charset=utf-8",
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 YaBrowser/21.9.1.684 Yowser/2.5 Safari/537.36',
    }
#сначало запрос идет с телефона



if cookie:                                      
    headers['cookie'] = cookie


def url_and_name_file(): #функция дляполучения ссылки и название файла куда все сохронять
    global name_file
    a = input('ссылка ') 
    name_file = str(input('введите название csv файла куда все всатвлять '))
    url = a+'&p=' #теперь в ссылку можно подставлять страницы
    req = requests.get(url , headers = headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    #сделали обычный запрос на страницу
    all_predmet_and_pages(soup , url)



def all_predmet_and_pages(beautifulsoup , urls):
    all_predmet = beautifulsoup.find(class_='page-title-count-oYIga')
    all_predmet = all_predmet.text
    all_predmet = int(all_predmet)
    #нашли сколько всего предметов на странице
    try:
            pages = int(beautifulsoup.find('span', {'data-marker': 'pagination-button/next'}).previous_element)
    except:
            pages = 1
    #кол-во страниц , если таковые присутсвуют
    print('Количество найденных страниц: ', pages)
    getting_all_links_from_a_page(urls , pages , all_predmet)



def getting_all_links_from_a_page(urlk , pag , al):
    global fd
    global po
    for k in range(1 , pag+1):
        #пробегаемся по страницам
        k = str(k)
        print(k)
        req = requests.get(urlk+k, headers = headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        #обычный запрос на сайт
        all_links = soup.find_all('a',class_='link-link-MbQDP link-design-default-_nSbv title-root-j7cja iva-item-title-_qCwt title-listRedesign-XHq38 title-root_maxHeight-SXHes')
        #нашли все сылки на карточке на данной странице
        for link in all_links:
            if  fd < al:
                jk = ('https://m.avito.ru'+link.get('href'))
                z.append(jk)
                print(jk)
                po += 1
                print(f'всего ссылок пройдено {po}')
                fd = fd + 1
                #пробегаемся по ссылкам и добавляем их в список
    adding_the_first_line_in_excel()


def adding_the_first_line_in_excel():
    # создание excel файла с полями указанами ниже
    Product = 'номер телефона'
    Calorie = 'заголовок обьявления'
    Proteins = 'контактное лицо'
    Fats = 'цена'
    ljk = 'ссылка на фотографию'
    hgf ='описание'
    with open(f"{name_file}.csv", "w" , encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                        Product,
                        Calorie,
                        Proteins,
                        Fats,
                        ljk,
                        hgf,
                        )
                    )
    filling_in_the_table_with_parameters()



def filling_in_the_table_with_parameters():
    for m in z:
        # пробегаемся по каждой ссылке которая у нас в списке
          k =m.split('_')
          k = k[-1]
          #берем Id товара для получения номера
          params = {	'pkey':'dfed69290bc453b834e2e0e2f16bf630',	
          'vsrc':'r',
          'searchHash':'ttv948zc8v4kg0oc4k0o8wok04w8ook'
          }
          headers = {
          'cookie': 'u=2oxvcqpg.m3vlga.fzlxckmkbcg0; buyer_laas_location=636700; _gcl_au=1.1.1437463742.1634655997; _ym_uid=1634655997879810682; _ym_d=1634655997; _gid=GA1.2.1716957583.1634655997; tmr_lvid=a89bb818055b95eb1c55d69fd8e50175; tmr_lvidTS=1634655997496; _fbp=fb.1.1634656029979.542827822; lastViewingTime=1634656167480; showedStoryIds=75-74-71-69-68-66-63-61-59-49; sx=H4sIAAAAAAACAw3LMQ6AIAwAwL90dkCgUvmN2pZEY4yDBCH8XXPzNXCoqPSzYROZR0eLGLuSMtM4uRligwwRir5H8Vr3dHLGi8QyJy5YjTvL%2FcAAAvEPPnjrDfb%2BAYxOv8RbAAAA; buyer_location_id=644560; __gads=ID=613253b5bcb9e0ff:T=1634656043:S=ALNI_MYBfKzhmiUNe6DkClR6q3boSM1NWg; f=5.0c4f4b6d233fb90636b4dd61b04726f147e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b984dcacfe8ebe897bfa4d7ea84258c63d59c9621b2c0fa58f915ac1de0d034112ad09145d3e31a56946b8ae4e81acb9fae2415097439d4047fb0fb526bb39450a46b8ae4e81acb9fa34d62295fceb188dd99271d186dc1cd03de19da9ed218fe2d50b96489ab264edd50b96489ab264ed87829363e2d856a246b8ae4e81acb9fa38e6a683f47425a8352c31daf983fa077a7b6c33f74d335c84df0fd22b85d35f06e113d6c5cb1aef559cdfa553ffd7ff0a4917fb21ab64d7d1297c90daba5db723d9f5f135037643f300180cdfbaaac844ff86f19f0957ace2415097439d404746b8ae4e81acb9fa786047a80c779d5146b8ae4e81acb9fae973e9df8c3c44af2d38179306cb93212da10fb74cac1eab3fdb0d9d9f6f145bd1ce76042dff8395312f8fecc8ca5e543486a07687daa291; ft="cL84MtqehrUi4VPeOTMrxAsF+hEt/SaD73XINpcGWFlkwqQaAl+H+f2ahRNgY1eDdgh3crdFYR1HFBXdPMMCKrSI7p7LxXId+/Z62ihZp7CQdJ/BtDJv2rdz0ok8sf1TnpG7oTZoW7PicYOzaUWB4HY5umA5VqH9+5INFMhK+jtChBJM+BN2P/Ar+D2uxjQT"; _ym_isad=2; tmr_detect=0%7C1634818590066; _ga=GA1.1.2069816690.1634655997; v=1634820768; cto_bundle=GiXBCF9Rc05rRGUlMkI4SHdRRVpLUHYwWVZzRFZDbGdpNXpzWVpMVXNwSnlrYnNtVnp5MldhOEFqNWRYcWE2aFlKR3Vrejd5OG1Xck1UWWFyZ24yWFZkcnluS1JLbmlzcjltanZjZXJkWElGUnRuTUlHcDMlMkZ1cFNtRmNEQ1IlMkJDSG9VdndvVHh1JTJGTThqSUNGJTJGYyUyRlNGN1BqTGcwZHclM0QlM0Q; _mlocation=621540; _mlocation_mode=default; _ga_9E363E7BES=GS1.1.1634820753.8.0.1634820753.60; _ym_visorc=b; tmr_reqNum=29',
          'referer':m,
          'accept':'application/json, text/plain, */*',
          'user-agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36',
    }
          # теперь запрос идет с пк
          req = requests.get(m, params=params , headers = headers )
          soup = BeautifulSoup(req.text , 'html.parser')
          #обычный запрос
          try:
            name_title = soup.find(class_='gtOYy')
            name_title = name_title.text
            print(name_title)
            #название товара
          except:
           name_title = 'ошибка'
          try:
            lk = f'https://m.avito.ru/api/1/items/{k}/phone?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
            resp = requests.get(f'https://m.avito.ru/api/1/items/{k}/phone?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir')
            resp = resp.json()
            gf = resp['result']['action']['uri'].split('=')[-1]
            gf = gf.split('B')
            gf=gf[1]
            #телефон 
          except:
            phone  = 'номера нету'
            print(requests.get(f'https://m.avito.ru/api/1/items/{k}/phone?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'))
            gf = phone
          try:
              face_title = soup.find(class_='UZhDR')
              face_title = face_title.text
              print(face_title)
              #контактное лицо
          except:
              face_title = 'контактное лицо отсутствует'
          try:
              price = soup.find(class_='vDskN')
              price = price.text
              print(price)
              #цена
          except:
              price ='похоже цена не указана'
          try:
              text2 = soup.find(class_='_nTsP phT_N')
              text2 = text2.text
              print(text2)
              #описание
          except:
              text2= 'описания нету'
          try:
              achref_foto = soup.find(class_='hVzCV')
              achref_foto = achref_foto.get('src')
              print(achref_foto)
              #ссылка на фотку
          except:
              achref_foto = 'картинок нету'
          print('fsfs')
          sleep(random.randrange(11 , 15))
          #засыпаем что бы не банило
          print('hgfh')
          with open(f"{name_file}.csv", "a" , encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(
                           (
                            gf,
                            name_title,
                            face_title,
                            price,
                            achref_foto,
                            text2,
                           )
                        )
                    #открываем файл и записываем туда полученные данные с каждой карточки
def main():
    url_and_name_file()
if __name__=='__main__':
    main()
