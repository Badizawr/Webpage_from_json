import json
from jinja2 import Environment, FileSystemLoader
import sqlite3


# поключение к БД и выполнение запроса
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('SELECT id, name')
results = cursor.fetchall()

# преобразование запроса в json
data = []
for row in results:
    data.append({
        'id': row[0],
        'title': row[1],
        'name': row[2]
    })
json_data = json.dumps(data)


fileLoader = FileSystemLoader("templates")
env = Environment(loader=fileLoader)

rendered = env.get_temlate("form.html").render(form=data)

fileName = "form.html"
with open(f"./new_form{fileName}", 'w') as f:
    f.write(rendered)

