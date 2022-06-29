import requests

class VK_foto:

    def __init__(self):
        self.token = input('Введите токен ВКонтакте: ')

    def get_user_VK(self):
        params = {
            'owner_id': input('Введите id пользователя VK: '),
            'album_id': 'profile',
            'extended': 1,
            'access_token': self.token,
            'v': '5.131'}
        return(params)

    def get_foto_VK(self):
        foto_for_upload = []
        URL = 'https://api.vk.com/method/photos.get'
        params = self.get_user_VK()
        response = requests.get(URL, params=params)
        response.raise_for_status()
        if response.status_code == 200:
            print("Удалось успешно получить доступ к фотографиям указанного пользователя.")
        print(f"Количество фотографий в профиле пользователя: {(response.json()['response']['count'])}")
        foto_quantity = int(input('Какое количество из них хотите загрузить на ЯндексДиск? Введите число: '))
        for i in response.json()['response']['items']:
            if len(foto_for_upload) + 1 <= foto_quantity:
                sizes = {}
                for el in i['sizes']:
                    size = el['height'] * el['width']
                    sizes[size] = el['url']
                    foto_max_size = {'url': sizes[max(sizes)],
                            'size': max(sizes),
                            'id': i['id'],
                            'likes': i['likes']['count'] + i['likes']['user_likes'],
                            'date': (i['date'])}
                foto_for_upload.append(foto_max_size)
            else:
                pass
        return(foto_for_upload)


