from flask import Flask

# Blueprint import 
from controller.main import main_blueprint



app = Flask(__name__)
app.config.from_object('setting')

# Register blueprint
app.register_blueprint(main_blueprint)



