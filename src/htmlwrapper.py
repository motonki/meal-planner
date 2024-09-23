from jinja2 import Environment, FileSystemLoader, select_autoescape

def write_html(recipes):
    env = Environment(
    loader = FileSystemLoader("templates"),
    autoescape=select_autoescape()
    )
    template = env.get_template("basic.html")
    output = template.render(recipes=recipes)
    with open("meals.html", 'w') as outputf:
        outputf.write(output)
    