from flask import Flask
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    ## host="0.0.0.0" - helps to access out local address as well as our host address.
    ## on cmd - type ipconfig to see local address...which is below.
    ## IPv4 Address. . . . . . . . . . . : 172.23.64.1