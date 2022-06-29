from YandexDisk import YandexDisk
from VK_foto import VK_foto

def foto_VK_loader():
    command = input('Хотите сделать резервную копию фотографий из ВКонтакет? (Оветьте: "да" либо "нет"): ')
    if command == 'да':
        print('Тогда начнем!')
        foto = VK_foto().get_foto_VK()
        YandexDisk().upload_foto_to_disk(foto)
    if command == 'нет':
        pass

# foto_VK_loader()


