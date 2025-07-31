from flask import Blueprint, jsonify, request
from app.modules.item import service

item_bp = Blueprint('item_bp', __name__)

@item_bp.route('/', methods=['GET'])
def get_items():
    return jsonify(service.get_all_items())

@item_bp.route('/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = service.get_item_by_id(item_id)
    if item:
        return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

@item_bp.route('/', methods=['POST'])
def create_item():
    data = request.get_json()
    return jsonify(service.create_item(data)), 201

@item_bp.route('/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    item = service.update_item(item_id, data)
    if item:
        return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

@item_bp.route('/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if service.delete_item(item_id):
        return jsonify({'message': 'Item deleted successfully'})
    return jsonify({'error': 'Item not found'}), 404
