print("running server file")
from flask_app import app
from flask_app.controllers import characters #based off table name

if __name__=="__main__":
    app.run(debug=True)
