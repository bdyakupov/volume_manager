# 📦 Dummy Volume Manager CLI & API Client

CLI-инструмент и Python-клиент для взаимодействия с FastAPI-сервером управления томами.
---

## 🚀 Возможности


- 🔄 CRUD-операции над томами через API
- 🧱 SQLAlchemy ORM — хранение данных в БД
- 🐍 Pydantic-схемы для валидации
- ⚙️ AsyncClick CLI-интерфейс
- 🌐 HTTPX-клиент для запросов к API
- 🪵 Логгирование всех действий

---

## 📥 Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/bdyakupov/volume-manager-cli.git
cd volume-manager-cli
```
2. Установите зависимости
```bash
poetry install
```
или
```bash
pip install -r requirements.txt
```
3. Запуск сервера
```bash
poetry run uvicorn src.main:app --reload --no-access-log
```
или
```bash
uvicorn src.main:app --reload --no-access-log
```
4. Запуск CLI
```bash
cd cli
python cli.py [КОМАНДА] [ОПЦИИ]
```
## 📚 Примеры использования CLI
### 🔍 Получить список всех томов

```bash
python cli.py list-volumes
```

### ➕ Создать новый том

```bash
python cli.py create-volume --name backup --size 50
```

### 📄 Получить том по ID

```bash
python cli.py get-volume 1
```

### 🔁 Обновить размер тома

```bash
python cli.py update-volume 1 --size 100
```

### ❌ Удалить том

```bash
python cli.py delete-volume 1
```

# 🪵 Логирование

Действия CLI логируются в файл logs/cli.log:

```logs
[2025-06-19 15:22:01] [INFO] Команда: create-volume | Параметры: {'name': 'data', 'size': 100}
[2025-06-19 15:22:01] [INFO] Результат команды 'create-volume': Успешно
```

Журнал API - logs/api.log

```logs
2025-06-19 15:35:09,600 [INFO] GET /volumes/ -> 200 OK
2025-06-19 15:35:24,209 [INFO] DELETE /volumes/1 -> 200 OK
```