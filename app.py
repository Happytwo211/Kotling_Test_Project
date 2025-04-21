from flask import Flask, render_template, request,  redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import desc

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
@app.errorhandler(405)
def method_not_allowed(e):
    return render_template("method_not_allowed.html"), 405

@app.route('/about_me')
def show_about_me():
    return render_template('about_me.html')

@app.route('/players')
def show_player():
    players = Player.query.order_by(Player.name).all()
    return render_template('players.html', players=players)
@app.route('/leader_board')
def show_leader_board():
    users_in_leader_board = LeaderBoard.query.order_by(desc(LeaderBoard.score)).all()
    return render_template('leader_board.html', users=users_in_leader_board)

@app.route('/new_player/<int:id>', methods = ['POST'])
def new_player(name, position_x, position_y, joined_time, coins_collected):
    new_player = Player(
        name=name,
        position_x=position_x,
        position_y=position_y,
        joined_time=joined_time,
        coins_collected=coins_collected
    )
    try:
        db.session.add(new_player)
        db.session.commit()
        return (redirect('/players'))

    except Exception as e:
        return (f'Произишла ошибка'
                f'\n{e}', render_template('default.html'))

@app.route('/new_player_leader_board/<int:id>', methods = ['POST'])
def initial_new_user(name, game_last, score):
    new_user = LeaderBoard(
        name=name, game_last=game_last, score=score
    )
    try:
        db.session.add(new_user)
        db.session.commit()
        return (redirect('/leader_board'))


    except Exception as e:
        return (f'Произишла ошибка'
                f'\n{e}', render_template('default.html'))



class LeaderBoard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    game_last = db.Column(db.Integer)
    score = db.Column(db.Integer)

    def __repr__(self):
        return f"<LeaderBoard(id={self.id}, name='{self.name}', game_last={self.game_last}, score={self.score})>"

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    position_x = db.Column(db.Integer)
    position_y = db.Column(db.Integer)
    joined_time = db.Column(db.DateTime)
    coins_collected = db.Column(db.Integer)

    def __repr__(self):
        return (
            f"<Player(id={self.id}, "
            f"name='{self.name}', "
            f"position=({self.position_x}, {self.position_y}), "
            f"joined_at={self.joined_time.strftime('%Y-%m-%d %H:%M:%S')}, "
            f"coins={self.coins_collected})"
        )

if __name__ == '__main__':
    app.run(debug=True)
