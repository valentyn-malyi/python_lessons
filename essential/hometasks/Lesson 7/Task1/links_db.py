﻿"""Модуль основной логики приложения.
Предоставляет класс LinksDB -- хранилище ссылок.
"""

from urllib.parse import urlparse

class LinksDB(object):
    """Хранилище ссылок.
    Для простоты пока не используем настоящую базу данных,
    а лишь обычный словарь, поэтому после перезапуска сервера
    данные будут потеряны.
    """

    def __init__(self):
        """Конструктор класса"""

        self._links = {}  # словарь ссылок

    def get_url(self, name):
        """Метод получения ссылки по имени.
        Выбрасывает KeyError, если имя не найдено."""

        return self._links[name]

    def set_url(self, name, url):
        """Метод добавления новой ссылки.
        Выбрасывает KeyError, если имя уже существует или пустое.
        Выбрасывает ValueError, если URL пустой или некорректный."""

        url = self.normalize_url(url)

        if not name:
            raise KeyError('Link name cannot be empty', name)
        if not url:
            raise ValueError('Invalid link URL', url)
        if name in self._links:
            raise KeyError('Link already exists', name)

        self._links[name] = url

    def normalize_url(self, url):
        """Метод, который добавляет протокол, если он отсутствует,
        и возвращает исправленный или исходный URL, если он корректный,
        или None в ином случае."""

        if not urlparse(url).scheme:
            url = 'http://' + url
        if urlparse(url).netloc:
            return url
        else:
            return None
