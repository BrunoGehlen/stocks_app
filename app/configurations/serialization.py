from . import Flask, Marshmallow

marsh = Marshmallow()


def init_app(app: Flask):
    marsh.init_app(app)
    app.marsh = marsh
