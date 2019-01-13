from flask import Flask, render_template, request
from scraper import return_items

app = Flask(__name__)

@app.route('/')
def index():
    users = []
    users = request.args.get('users')
    items = return_items()
    return render_template(
        'index.html',
        items=items,
        users=users,
        )

if __name__ == '__main__':
    app.run(debug=True)
