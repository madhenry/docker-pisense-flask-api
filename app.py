from flask import Flask
from sense_hat import SenseHat
from flask import json
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    try:
        sense = SenseHat()
        c = sense.get_temperature()
        humidity = sense.get_humidity()

        f = (c * 9/5) + 32 
        data = {}
        data["fahrenheit"] = f
        data["celsius"] = c
        data['humidity'] = humidity

        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    
    except OSError as ose:
        print("There was an OSError:  {}".format(ose))
    
    else:
        return response

@app.route('/temp')
def temp():
    try:
        sense = SenseHat()
        temp = sense.get_temperature()
        cpu_temp = subprocess.check_output("vcgencmd measure_temp", shell=True)
        temp_calibrated = temp - ((cpu_temp - temp)/5.466)

        response = app.response_class(
            response=json.dumps(temp_calibrated),
            status=200,
            mimetype='application/json'
        )
    
    except OSError as ose:
        print("There was an OSError:  {}".format(ose))
    
    else:
        return response

@app.route('/message/<string:message>')
def showMessage(message):
    try:
        sense = SenseHat()
        sense.show_message(message)

        response = app.response_class(
            response=json.dumps(True),
            status=200,
            mimetype='application/json'
        )
    
    except OSError as ose:
        print("There was an OSError:  {}".format(ose))
    
    else:
        return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')