# Используем базовый образ с Python 3.12
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект в контейнер
COPY . .

# Указываем порт, на котором будет работать приложение
EXPOSE 8000

# Команда запуска Gunicorn
CMD ["gunicorn", "--workers=3", "--bind=0.0.0.0:8000", "classify_prk.wsgi:application"]
