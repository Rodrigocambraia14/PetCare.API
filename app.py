# -*- coding: utf-8 -*-
from flask import Flask, jsonify, Response
from api.controllers.user_controller import user_controller
from api.controllers.pet_controller import pet_controller
from api.controllers.food_routine_controller import food_routine_controller
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from infrastructure.database.constants import *
from infrastructure.database.base_setup import BaseSetup
from infrastructure.database.seed import Seed
from model.core.food_routine_setup import FoodRoutineSetup
import json, os, schedule, threading


app = Flask(__name__)

app.register_blueprint(user_controller, url_prefix='/api')
app.register_blueprint(pet_controller, url_prefix='/api')
app.register_blueprint(food_routine_controller, url_prefix='/api')

CORS(app)

# Configure Swagger UI
SWAGGER_URL = '/swagger'
API_URL = '/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API da petgoReminderUI"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/swagger.json')
def swagger():
    with open('swagger.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return jsonify(data)
    

if not os.path.isfile(DB_NAME):
    BaseSetup.create_tables()
    Seed.run_database_seeding()
    
app.run()