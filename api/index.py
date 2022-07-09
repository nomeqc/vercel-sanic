from pathlib import Path

from sanic import Sanic
from sanic_template import template as Template

app = Sanic("api")
template = Template(path=Path(__file__).parent.joinpath("templates"))
print('外面')

@app.route("/")
async def html(request):
    print(f'template: {template.path}')
    vars = {'title': 'hello world', 'name': 'Tom'}
    return await template.render_template("test.html", **vars)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888)
