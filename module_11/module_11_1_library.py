import requests

# Отправляем GET-запрос на URL
url = "https://yandex.ru/pogoda/"
response = requests.get(url)

# Проверяем, что запрос был успешным (код ответа 200)
if response.status_code == 200:
    # Получаем содержимое ответа в виде текста
    data = response.text

    # Выводим данные в консоль
    print(data)
else:
    print(f"Ошибка при запросе: {response.status_code}")

# ----------------------------------------------------------


from PIL import Image, ImageFilter

# Открываем изображение
image = Image.open("waterfall.jpg")

# Изменяем размер изображения
new_size = (800, 600)
resized_image = image.resize(new_size)

# Применяем эффект "размытие"
blurred_image = resized_image.filter(ImageFilter.BLUR)

# Сохраняем изображение в другом формате
blurred_image.save("output_image.png")