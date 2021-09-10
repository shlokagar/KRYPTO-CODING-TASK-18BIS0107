from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
from flask_restful import Resource, Api

app = Flask(__name__) 
api = Api(app) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///Alerts.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) 
ma = Marshmallow(app)

/* deleting the alert*/
@staticmethod
def delete():
    try: id = request.args['alertid']
    except Exception as _: id = None

    if not id:
        returnjsonify({ 'Message': 'Must provide the alert ID' })

    alert = Alerts.query.get(id)
    db.session.delete(alert)
    db.session.commit()

    return jsonify({
        'Message': f'Alert {str(id)} deleted.'
    })