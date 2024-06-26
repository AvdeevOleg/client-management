# Управление клиентами на Python.

Этот проект представляет собой программу на Python для управления информацией о клиентах с использованием PostgreSQL. Включает функции для создания структуры базы данных, добавления клиентов, добавления номеров телефонов, обновления информации о клиентах, удаления номеров телефонов, удаления клиентов и поиска клиентов по их данным.

## Функциональные возможности

- Создание структуры базы данных (таблицы)
- Добавление нового клиента
- Добавление номера телефона для существующего клиента
- Обновление информации о клиенте
- Удаление номера телефона для существующего клиента
- Удаление существующего клиента
- Поиск клиента по его данным (имя, фамилия, email или телефон)

## Требования

- Python 3.x
- Библиотека psycopg2

## Установка

Для работы программы необходимо установить библиотеку psycopg2: pip install psycopg2-binary

## Использование

- Обновите параметры подключения к базе данных в файле client_manager.py: conn = psycopg2.connect(database="yourdbname", user="yourdbuser", password="yourdbpass")
- Запустите файл client_manager.py: client_manager.py

## Демонстрация
Скрипт демонстрирует работу всех функций, включая создание структуры базы данных, добавление клиентов, добавление номеров телефонов, обновление информации о клиентах, удаление номеров телефонов, удаление клиентов и поиск клиентов по их данным.

## [Ссылка на файл с кодом](./client-management.py)