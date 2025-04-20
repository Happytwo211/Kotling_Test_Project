from flask import Flask, render_template, url_for
import sqlite3


main = Flask(__name__)

@main.route('/about_me')
def show_about_me():
    return render_template('about_me.html')



if __name__ == '__main__':
    main.run(debug=True)