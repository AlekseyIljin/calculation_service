from flask_restful import Resource, request
from .models import Calculation
from decimal import Decimal
from .config import db



class Calculate(Resource):
    def post(self):
        calculation = Calculation()
        data = self.get("api/calc")
        contract = data.get("contract_id")
        calculation.project_id = data.get("project_id")
        rules = request.get("rules")
        cost = data.get("price").get("currency_value")
        result = 0
        for key in data:
            if key in rules:
                result += (data.get(key) * (rules.get(key) * cost))

        currency = data.get('price').get('currency')
        calculation.result = Decimal(result)
        db.session.add(calculation)
        db.session.commit()
        self.put('/api/calc', contract, 'completed')

        return result

    def get(self):
        calculation = model.project_id
        return model.result
