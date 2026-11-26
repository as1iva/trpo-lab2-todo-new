"""Простой список задач с сохранением в JSON."""
import argparse
import json
from pathlib import Path

class TaskList:
    def __init__(self, path):
        self.path = Path(path)
        self.items = json.loads(self.path.read_text(encoding='utf-8')) if self.path.exists() else []

    def save(self):
        self.path.write_text(json.dumps(self.items, ensure_ascii=False, indent=2), encoding='utf-8')

    def add(self, title):
        title = title.strip()
        if not title:
            raise ValueError('Название задачи не может быть пустым')
        self.items.append({'title': title, 'done': False})
        self.save()

    def search(self, query):
        return [item for item in self.items if query.casefold() in item["title"].casefold()]

    def complete(self, number):
        if number < 1 or number > len(self.items):
            raise ValueError('Задача не найдена')
        self.items[number - 1]['done'] = True
        self.save()

    def remove(self, number):
        if number < 1 or number > len(self.items):
            raise ValueError('Задача не найдена')
        self.items.pop(number - 1)
        self.save()

def main():
    parser = argparse.ArgumentParser(description='Список задач')
    parser.add_argument('--file', default='tasks.json')
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('list')
    sub.add_parser('search').add_argument('query')
    sub.add_parser('add').add_argument('title')
    sub.add_parser('done').add_argument('number', type=int)
    sub.add_parser('remove').add_argument('number', type=int)
    args = parser.parse_args()
    tasks = TaskList(args.file)
    try:
        if args.command == 'add': tasks.add(args.title)
        elif args.command == 'done': tasks.complete(args.number)
        elif args.command == 'remove': tasks.remove(args.number)
        else:
            items = tasks.search(args.query) if args.command == 'search' else tasks.items
            for n, item in enumerate(items, 1):
                print(f"{n}. [{'x' if item['done'] else ' '}] {item['title']}")
    except ValueError as exc:
        parser.error(str(exc))

if __name__ == '__main__': main()
