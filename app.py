from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

    def __repr__(self):
        # returns a String for every new task element that has been created
        return '<Task %r>' % self.id


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
