from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run()

from controller import *


# import os 
# import glob 
# print(os.path.basename(__file__)[:-3])
