from flask import Blueprint, request, jsonify
from ..services.google_service import GoogleService

sheets_bp = Blueprint('sheets_api', __name__)
google_service = GoogleService()

@sheets_bp.route('/update_sheet', methods=['POST'])
def update_sheet():
    data = request.json
    success = google_service.update_sheet(sheet_name='Sheet1', values=[data['value1'], data['value2']])
    return jsonify({"success": success}), 200

@sheets_bp.route('/search_files', methods=['GET'])
def search_files():
    name = request.args.get('name', None)
    mime_type = request.args.get('mime_type', None)
    files = google_service.search_files(name=name, mime_type=mime_type)
    return jsonify(files), 200
