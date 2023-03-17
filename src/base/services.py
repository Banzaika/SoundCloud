from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, filename):
    '''Построение пути для загрузки изображения: (media)/avatar/user_id/photo.jpg
    '''
    return f'avatar/{instance.id}/{filename}'


def validate_size_image(file):
    """Проверка размера файла"""
    megabite_limit = 3
    if file.size > megabite_limit * 1024 * 1024:
        raise ValidationError('Файл должен быть меньше 3 Мб')
