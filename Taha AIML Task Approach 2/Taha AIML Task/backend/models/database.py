from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    app.config.from_object('config.Config')
    db.init_app(app)
    with app.app_context():
        db.create_all()
