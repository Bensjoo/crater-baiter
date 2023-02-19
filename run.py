from baiter import create_app


app = create_app()


if __name__ == '__main__':
    app.run(debug=True, host=app.config['HOST'], port=app.config['PORT'])
