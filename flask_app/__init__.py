from flask import Flask
app = Flask(__name__)
app.secret_key = "frogs are mostly green"
DATABASE =  'eab_db'