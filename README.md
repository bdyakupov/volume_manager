# 💾 Dummy Volume Manager CLI & API Client

CLI-инструмент и Python-клиент для взаимодействия с FastAPI-сервером управления томами.
---

## 🧩 Зависимости


- python ^3.12
- fastapi = "^0.115.13"
- uvicorn = "^0.34.3"
- sqlalchemy = "^2.0.41"
- logging = "^0.4.9.6"
- pytest = "^8.4.1"
- fastcrud = "^0.15.12"
- aiosqlite = "^0.21.0"
- asyncclick = "^8.1.8"
- httpx = "^0.28.1"
- rich = "^14.0.0"

---

## 📥 Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/bdyakupov/volume-manager.git
cd volume-manager
```
2. Установить poetry, установить зависимости

```bash
pip install poetry
poetry install
```
или
```bash
pip install -r requirements.txt
```
3. Запуск сервера

```bash
uvicorn src.main:app --reload --no-access-log
```
4. Запуск CLI

```bash
cd cli
python cli.py [command] [options]
```
---
## Примеры использования CLI
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
---
# 📝 Мониторинг

CLI операции > logs/cli.log:

```logs
[2025-06-19 15:22:01] [INFO] Команда: create-volume | Параметры: {'name': 'data', 'size': 100}
[2025-06-19 15:22:01] [INFO] Результат команды 'create-volume': Успешно
```

Серверные логи > logs/api.log

```logs
[2025-06-19 15:35:09] [INFO] GET /volumes/ -> 200 OK
[2025-06-19 15:35:24] [INFO] DELETE /volumes/1 -> 200 OK
```