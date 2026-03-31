# Updated app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
CORS(app)

class InputSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    age = fields.Int(required=True, validate=lambda x: x > 0)

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Validate input
        schema = InputSchema()
        input_data = schema.load(request.json)
        return jsonify({'message': 'Input is valid', 'data': input_data}), 200
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)