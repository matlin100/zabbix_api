from flask import Blueprint, jsonify, request
from operation.zabbix_operation import get_host

hosst_routes_blueprint  = Blueprint('host_routes', __name__)

@hosst_routes_blueprint.route('/api/get_host', methods=['GET'])
def get_host_route():
    host_name = request.args.get('hostName')
    # if not host_name:
    #     return jsonify({'error': 'host name is required'})
    host_info = get_host(host_name)
    return jsonify(host_info)

