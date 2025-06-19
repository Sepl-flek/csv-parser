# CSV Parser

Простой парсер CSV-файлов с возможностью фильтрации и агрегации данных из командной строки.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Sepl-flek/csv-parser
   cd csv-parser
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```


## Использование

### Фильтрация данных

Вывести все продукты с рейтингом выше 4.7:
```bash
python main.py products.csv --where rating ">" 4.7
```

### Агрегация данных

Найти максимальную цену среди продуктов с рейтингом выше 4.7:
```bash
python main.py products.csv --where rating ">" 4.7 --aggregate price max
```

Возможные функции агрегации: `max`, `min`, `avg`.


## Примеры вывода

В папке `code usage exmaples/` находятся скриншоты примеров работы и покрытия тестов.
