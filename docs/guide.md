# Список задач

Приложение хранит задачи в JSON. Требуется Python 3.12 или новее.

## Команды

- `python todo.py add "Название"` — добавить задачу.
- `python todo.py list` — показать список.
- `python todo.py done 1` — отметить задачу выполненной.
- `python todo.py remove 1` — удалить задачу.
- `python todo.py search хлеб` — поиск без учёта регистра.

Тестирование: `python -m unittest discover -s tests -v`.
