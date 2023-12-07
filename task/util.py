import base64
import uuid

import bleach
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import re
import os
import requests


def download_and_save_image(url):
    response = requests.get(url)

    if response.status_code == 200:
        img_binary = ContentFile(response.content)
        # Сохранение изображения в папку img_in_tasks
        image_name = 'image_{}.png'.format(uuid.uuid4().hex[:8])
        image_path = default_storage.save(os.path.join('img_in_tasks', image_name), img_binary)
        return image_path
    else:
        return None

def process_and_save_images(text):
    img_src_regex = re.compile(r'<img.*?src=["\'](.*?)["\'].*?>')
    matches = img_src_regex.finditer(text)

    saved_image_paths = []

    for match in matches:
        image_url = match.group(1)

        # Проверка, является ли изображение встроенным (Data URL) или внешним URL
        if image_url.startswith('data:image'):
            img_data = image_url.split(',')[1]
            img_binary = ContentFile(base64.b64decode(img_data))
            # Сохранение изображения в папку img_in_tasks
            image_name = 'image_{}.png'.format(uuid.uuid4().hex[:8])
            image_path = default_storage.save(os.path.join('img_in_tasks', image_name), img_binary)
            saved_image_paths.append(image_path)
        else:
            # Если изображение внешнее (URL), загрузить и сохранить
            image_path = download_and_save_image(image_url)
            if image_path:
                saved_image_paths.append(image_path)

    return saved_image_paths

def get_clean_text(html_content):
    # Список разрешенных тегов, которые вы хотите сохранить
    #allowed_tags = ['p', 'a', 'strong', 'em', 'br', 'ul', 'ol', 'li']

    html_content = bleach.clean(html_content,strip_comments=True,   strip=True)
    html_content = html_content.replace('&nbsp;', ' ')
    return html_content




