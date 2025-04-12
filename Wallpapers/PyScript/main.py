import requests
import json

from bs4 import BeautifulSoup


cookies = {
    'remixlang': '3',
    'remixstlid': '9120272466101273979_V0rkpegEiQE7rvIxJggSB3veoFALPTJ2XpXrhif01T4',
    'remixlgck': '47f031a0234cdd7e6f',
    'remixstid': '1882133725_FmZEz4zt9fv5yNxDWZ9zStnKzOzCcYApZpbFLQ46GiD',
    'remixscreen_width': '1920',
    'remixscreen_height': '1200',
    'remixscreen_dpr': '1',
    'remixscreen_depth': '24',
    'remixscreen_orient': '1',
    'remixscreen_winzoom': '1.98',
    'remixsf': '1',
    'remixgp': '02a0128cfbfee9d7e26f8525e032e0f8',
    'remixdark_color_scheme': '1',
    'remixcolor_scheme_mode': 'auto',
    'remixdt': '0',
    'tmr_lvid': '2b5dcf5879ed50c1ab33d06fa45f6cf7',
    'tmr_lvidTS': '1744459425231',
    'domain_sid': 'xdjOgYRxeSdi9o8KBJkfD%3A1744459427071',
    'tmr_detect': '0%7C1744460921197',
    'remixua': '190%7C-1%7C333%7C242191955',
    'remixsts': '%7B%22data%22%3A%5B%5B1744460923%2C%22unique_adblock_users%22%2C0%2C%22web2%22%2C%22false%22%2Cnull%2C%22photos%22%5D%2C%5B1744460923%2C%22unique_adblock_users%22%2C0%2C%22web2%22%2C%22false%22%2Cnull%2C%22photos%22%5D%2C%5B1744460924%2C%22unique_adblock_users%22%2C0%2C%22web2%22%2C%22false%22%2Cnull%2C%22photos%22%5D%5D%2C%22uniqueId%22%3A896778544.0323479%7D',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://vk.com',
    'Connection': 'keep-alive',
    'Referer': 'https://vk.com/album-216821352_304258456',
    # 'Cookie': 'remixlang=3; remixstlid=9120272466101273979_V0rkpegEiQE7rvIxJggSB3veoFALPTJ2XpXrhif01T4; remixlgck=47f031a0234cdd7e6f; remixstid=1882133725_FmZEz4zt9fv5yNxDWZ9zStnKzOzCcYApZpbFLQ46GiD; remixscreen_width=1920; remixscreen_height=1200; remixscreen_dpr=1; remixscreen_depth=24; remixscreen_orient=1; remixscreen_winzoom=1.98; remixsf=1; remixgp=02a0128cfbfee9d7e26f8525e032e0f8; remixdark_color_scheme=1; remixcolor_scheme_mode=auto; remixdt=0; tmr_lvid=2b5dcf5879ed50c1ab33d06fa45f6cf7; tmr_lvidTS=1744459425231; domain_sid=xdjOgYRxeSdi9o8KBJkfD%3A1744459427071; tmr_detect=0%7C1744460921197; remixua=190%7C-1%7C333%7C242191955; remixsts=%7B%22data%22%3A%5B%5B1744460923%2C%22unique_adblock_users%22%2C0%2C%22web2%22%2C%22false%22%2Cnull%2C%22photos%22%5D%2C%5B1744460923%2C%22unique_adblock_users%22%2C0%2C%22web2%22%2C%22false%22%2Cnull%2C%22photos%22%5D%2C%5B1744460924%2C%22unique_adblock_users%22%2C0%2C%22web2%22%2C%22false%22%2Cnull%2C%22photos%22%5D%5D%2C%22uniqueId%22%3A896778544.0323479%7D',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}






vk_url = "https://vk.com"

global img_container

img_container = []

def get_images(offset):

    data = {
        'al': '1',
        'al_ad': '0',
        'offset': offset,
        'part': '1',
        'rev': '',
    }

    response = requests.post('https://vk.com/album-216821352_304258456', cookies=cookies, headers=headers, data=data)
    response = response.json()

    soup = BeautifulSoup(response["payload"][1][1], "lxml")
    data_img = soup.find_all("div", class_="photos_row")

    print(offset, len(data_img))

    if len(data_img) <= 0:
        return

    for item in data_img:
        img_url = vk_url + item.find("a").get("href")
        img_container.append(img_url)


    get_images(offset+40)

def load_img_url_not_istalled():
    global img_container
    with open("img_not_installed.json", "r") as file:
        img_container = json.load(file)


def save_img_url_not_installed():
    with open("img_not_installed.json", "w") as file:
        json.dump([], file, indent=4)
    set_img_container = list(set(img_container))
    with open("img_not_installed.json", "w") as file:
        json.dump(set_img_container, file, indent=4)


def get_img_url_for_install(offset):
    try:



        params = {
            'act': 'show',
        }

        data = {
            'act': 'show',
            'al': '1',
            'al_ad': '0',
            'dmcah': '',
            "offset": offset,
            'list': 'album-216821352_304258456',
            'module': 'photos',
            #'photo': '-216821352_457259422',
        }

        response = requests.post('https://vk.com/al_photos.php', params=params, cookies=cookies, headers=headers, data=data).json()

        for item in response["payload"][1][3]:
            try:
                img_container.append(item["w_src"])
            except:
                pass

        if offset >= 1000:
            return

        get_img_url_for_install(offset+10)

    except:
        pass


def load_img_url_for_istalled():
    global img_container
    with open("img_for_installed.json", "r") as file:
        img_container = json.load(file)


def save_img_url_for_installed():
    with open("img_for_installed.json", "w") as file:
        json.dump([], file, indent=4)
    set_img_container = list(set(img_container))
    with open("img_for_installed.json", "w") as file:
        json.dump(set_img_container, file, indent=4)


def install_img():

    for i in range(len(img_container)):
        image_name = f'../photo{i+1}.jpg'
        url = img_container[i]
        try:
            r = requests.get(url, stream=True)
            with open(image_name, 'wb') as f:
                for chunk in r.iter_content():
                    f.write(chunk)
        except:
            pass



def main():
    #load_img_url_not_istalled()
    #get_images(0)
    #save_img_url_not_installed()
    #load_img_url_for_istalled()
    #get_img_url_for_install(0)
    #save_img_url_for_installed()
    #install_img()
    pass


if __name__ == "__main__":
    main()
