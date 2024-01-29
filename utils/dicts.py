# файл dicts.py
def get_val(collection, key, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default
    :param collection: словарь
    :param key: значение ключа
    :param default: значение, возвращаемое по умолчанию
    """
    if len(collection) != 0:
        return (collection.get(key, default))

    return (default)

# Проверка
# col = {"vcs": "mercurial"}
# ky = "vcs"
# print(get_val(col, ""))
