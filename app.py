from flask import Flask
from sense_hat import SenseHat
from flask import json

app = Flask(__name__)

@app.route('/')
def index ():


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

if __name__ == '__main__':
    app.run(host='0.0.0.0')