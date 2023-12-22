# Test_Elvees
## Первый этап
Создание виртуального окружения:
```python
python -m venv venv
```
Устанавливаем зависимости из файла requirements.txt:
```python
pip install -r requirements.txt
```
## Второй этап
[В папке](https://github.com/kirillkelin/Test_Elvees/tree/main/first_part) находится решение первой части тестового задания

Для запуска bash-скрипта сначала сделайте его исполняемым:
```python
chmod +x repository.sh
./repository.sh
```
[В папке](https://github.com/kirillkelin/Test_Elvees/tree/main/second_part) находится решение второй части тестового задания

В качестве базы данных использовалась PostgreSQL

Сначала в pgadmin нужно локально создать БД TestTask. 

В файле .env находятся все основные переменные для подключения к БД.

Затем нужно запустить файл main.py.
