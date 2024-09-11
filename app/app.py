from flask import Flask, render_template

from database.queries import get_all_declarants, get_all_payers, get_all_categories, get_all_directors


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html', declarants=get_all_declarants())


if __name__ == '__main__':
    app.run(debug=True)