# Консольное приложение "Заметки"

Консольное приложение на языке программирования Python, позволяющее пользователю создавать, просматривать, редактировать и удалять заметки.

## Функциональность
- Добавление новых заметок с указанием заголовка и текста.
- Просмотр всех созданных заметок с указанием идентификатора, заголовка, текста и даты/времени создания.
- Редактирование существующих заметок по их идентификатору.
- Удаление существующих заметок по их идентификатору.

## Зависимости
Это приложение не требует установки дополнительных библиотек Python.

## Использование
1. Запустите скрипт `notes.py`.
2. Следуйте инструкциям в консоли для выбора действий из меню.

## Формат файла заметок
Заметки сохраняются в файле `notes.csv` в формате CSV (Comma Separated Values). Каждая заметка представлена отдельной строкой, где значения разделены точкой с запятой (`;`). Структура заметки в файле: 

id; title; body; timestamp


- `id`: Идентификатор заметки (целое число).
- `title`: Заголовок заметки (строка).
- `body`: Текст заметки (строка).
- `timestamp`: Дата и время создания или последнего изменения заметки в формате `YYYY-MM-DD HH:MM:SS`.





