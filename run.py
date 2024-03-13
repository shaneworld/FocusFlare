from app import app, db

if __name__ == '__main__':
    with app.app_context():
        from app.models import User
        db.create_all()  # Create sql tables for our data models
    app.run(debug=True)
