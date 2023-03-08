from baiter import create_app


app = create_app()


if __name__ == '__main__':
    app.run(
        debug=app.config['FLASK_DEBUG'],
        host=app.config['SERVING_ADDRESS'],
        port=app.config['PORT']
    )
