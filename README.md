## Docker container for Raspberry Pi Sensehat with Flask API for getting temp/humidity

```
docker build -t sensehat .
docker run --privileged --name sensehat -ti sensehat bash
python test.py
```
Running test.py validates the installation.  See the [SenseHat API docs](https://pythonhosted.org/sense-hat/) for more SenseHat calls.

