from app import create_app


#creating the instance of the app
app = create_app('development')


if __name__ == '__main__':
    app.run()
