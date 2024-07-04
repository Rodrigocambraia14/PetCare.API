from model.entities.vaccine_calendar import VaccineCalendar
from utils.helper import Helper
from flask import Blueprint, jsonify, request
from model.entities.user import User
from flask import url_for

vaccine_calendar_controller = Blueprint('vaccine_calendar_controller', __name__)

@vaccine_calendar_controller.route("/vaccine_calendar/add", methods=['POST'])
def vaccine_calendar_add():
    
    required_params = ['date', 'description', 'user_id']
    if not all(param in request.json for param in required_params):
        return jsonify({'error': 'Alguns parametros nao foram preenchidos corretamente!'}), 400

    date = request.json['date']
    description = request.json['description']
    user_id = request.json['user_id']
    
    vaccine_calendar = VaccineCalendar(Helper.get_new_id(), date, description, user_id)
    
    vaccine_calendar.add()

    return jsonify({'message': 'data adicionada com sucesso.'}), 201

@vaccine_calendar_controller.route("/vaccine_calendar/update", methods=['PUT'])
def vaccine_calendar_update():
    
    required_params = ['date', 'description', 'user_id', 'vaccine_calendar_id']
    if not all(param in request.json for param in required_params):
        return jsonify({'error': 'Alguns parametros nao foram preenchidos corretamente!'}), 400

    date = request.json['date']
    description = request.json['description']
    vaccine_calendar_id = request.json['vaccine_calendar_id']
    user_id = request.json['user_id']

    vaccine_calendar = VaccineCalendar(vaccine_calendar_id, date, description, user_id)
    
    vaccine_calendar.update()

    return jsonify({'message': 'Data atualizada com sucesso.'}), 200

@vaccine_calendar_controller.route("/vaccine_calendar/delete", methods=['POST'])
def vaccine_calendar_delete():
    
    required_params = ['vaccine_calendar_id']
    if not all(param in request.json for param in required_params):
        return jsonify({'error': 'Alguns parametros nao foram preenchidos corretamente!'}), 400

    vaccine_calendar_id = request.json['vaccine_calendar_id']
    
    VaccineCalendar.delete(vaccine_calendar_id)
    
    return jsonify({'message': 'data removida com sucesso.'}), 200


@vaccine_calendar_controller.route("/vaccine_calendar/list", methods=['GET'])
def vaccine_calendar_list():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'O ID do usuario e obrigatorio.'}), 400
    
    dates = VaccineCalendar.list(user_id)
    
    return jsonify(dates), 200
