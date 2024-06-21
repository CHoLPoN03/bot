import os

# Укажите путь к файлу базы данных
db_path = 'db.sqlite'

try:
    # Попытка удалить файл базы данных
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"База данных '{db_path}' успешно удалена.")
    else:
        print(f"Файл базы данных '{db_path}' не найден.")

except Exception as e:
    print(f"Ошибка при удалении базы данных: {e}")
