from flask import Flask
import serial
import serial.tools.list_ports
import time

app = Flask(__name__)


@app.route("/serial/", methods=["GET"])
def run_bubbles():
    with serial.Serial(
        "COM4", 115200, bytesize=8, parity="N", stopbits=1, timeout=1
    ) as ser:
        time.sleep(4)
        ser.write(b"q")
        ser.flush()


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
    
