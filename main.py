import json
from jinja2 import Environment, FileSystemLoader

with open('data.json') as f:
    json_data = json.load(f)

def write_data(data):
    fileName = "new_form.html"
    with open(f"./templates/{fileName}", 'w') as f:
        f.write(data)
        
def create_html(data):
    env = Environment(loader=FileSystemLoader('templates'))
    temp = env.get_template("mytemplate.html")
    mesege = temp.render(data)
    return write_data(mesege)

create_html(json_data)
