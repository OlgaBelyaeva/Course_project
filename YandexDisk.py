import requests
from progress.bar import IncrementalBar
import json

class YandexDisk:

    def __init__(self):
        self.token = input('Введите токен с Полигона ЯндексДиска: ')
        self.headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}

    def folder_creation(self):
        folder = input('Введите название новой папки для фото на ЯндексДиске и поставьте знак "/": ')
        path = input('Укажите путь к каталогу на ЯндексДиске, в котором будет лежать новая папка, в конце поставьте знак "/": ')
        folder_path = (path.strip() + folder.strip())
        params = {"path": folder_path, "overwrite": "true"}
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
        response = requests.put(url=upload_url, headers=self.headers, params=params)
        if response.status_code == 201:
            print(f'Папка для фото успешно создана.')
        elif response.status_code == 409:
            print('Папка c таким именем уже существуе. Введите другое название.')
        else:
            print('При получении ссылки для загрузки на ЯДиск что-то пошло не так, попробуте снова')
        return(folder_path)

    def upload_foto_to_disk(self, foto_for_upload):
        folder_path = self.folder_creation()
        uploaded_foto_json = []
        status_bar = IncrementalBar('Upload process', max=len(foto_for_upload))
        for i in foto_for_upload:
            url_foto = i['url']
            file_name = str(i['likes']) + '_' + str(i['date']) + '.jpg'
            disk_file_path = folder_path + file_name
            params = {'path': disk_file_path, 'overwrite': 'true', 'url': url_foto}
            upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
            response = requests.post(upload_url, headers=self.headers, params=params)
            response.raise_for_status()
            if response.status_code != 202:
                print('Что-то пошло не так')
            foto_info = {"file_name": file_name, 'size': i['size']}
            uploaded_foto_json.append(foto_info)
            status_bar.next()
        status_bar.finish()
        with open('uploaded_files.json', 'w') as file_obj:
            json.dump(uploaded_foto_json, file_obj)
        print('Фото успешно загружены.')