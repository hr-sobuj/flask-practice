from flask import Flask
from dotenv import load_dotenv
import os


app = Flask(__name__)

load_dotenv()


if __name__ == '__main__':
    app.run()

from controller import *


# import os 
# import glob 
# print(os.path.basename(__file__)[:-3])
