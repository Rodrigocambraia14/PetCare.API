from model.entities.pet import Pet
from utils.helper import Helper
from flask import Blueprint, jsonify, request
from model.entities.user import User
from flask import url_for

pet_controller = Blueprint('pet_controller', __name__)

@pet_controller.route("/pet/add", methods=['POST'])
def pet_add():
    
    required_params = ['name', 'age', 'gender', 'color', 'user_id']
    if not all(param in request.json for param in required_params):
        return jsonify({'error': 'Alguns parametros nao foram preenchidos corretamente!'}), 400

    name = request.json['name']
    age = request.json['age']
    gender = request.json['gender']
    color = request.json['color']
    user_id = request.json['user_id']
    
    pet = Pet(Helper.get_new_id(), name, age, gender, color, user_id)
    
    pet.add()

    return jsonify({'message': 'Pet adicionado com sucesso.'}), 201

@pet_controller.route("/pet/update", methods=['PUT'])
def pet_update():
    
    required_params = ['name', 'age', 'gender', 'color', 'user_id', 'pet_id']
    if not all(param in request.json for param in required_params):
        return jsonify({'error': 'Alguns parametros nao foram preenchidos corretamente!'}), 400

    name = request.json['name']
    age = request.json['age']
    gender = request.json['gender']
    color = request.json['color']
    user_id = request.json['user_id']
    pet_id = request.json['pet_id']
    
    pet = Pet(pet_id, name, age, gender, color, user_id)
    
    pet.update()

    return jsonify({'message': 'Aumigo atualizado com sucesso.'}), 200

@pet_controller.route("/pet/delete", methods=['POST'])
def pet_delete():
    
    required_params = ['pet_id']
    if not all(param in request.json for param in required_params):
        return jsonify({'error': 'Alguns parametros nao foram preenchidos corretamente!'}), 400

    pet_id = request.json['pet_id']
    
    Pet.delete(pet_id)
    
    return jsonify({'message': 'Pet removido com sucesso.'}), 200


@pet_controller.route("/pet/list", methods=['GET'])
def pet_list():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'O ID do usuario e obrigatorio.'}), 400
    
    pets = Pet.list(user_id)
    
    return jsonify(pets), 200
