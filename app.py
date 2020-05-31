from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>Hello World :)</h1>"


if __name__ == '__main__':
    app.run()


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/f/<celsius_value>')
def convert_celsius_to_fahrenheit(celsius_value=''):
    fahrenheit_value = float(celsius_value) * 9.0 / 5 + 32
    return "{}°C converted to fahrenheit would equal: {}°F".format(celsius_value, fahrenheit_value)
