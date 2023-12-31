from website import create_app, db, create_database

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        create_database()
    app.run(debug=True)
