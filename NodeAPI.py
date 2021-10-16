from flask import Flask
from flask.globals import request
from flask.json import jsonify
from flask_classful import FlaskView, route
from Utils import Utils

node = None

class NodeAPI(FlaskView):
    def __init__(self):
        self.app = Flask(__name__)

    def start(self, apiPort, injectedNode):
        NodeAPI.register(self.app, route_base='/')
        global node
        node = injectedNode
        self.app.run(host='localhost', port=apiPort)

    @route('/info', methods=['GET'])
    def info(self):
        return 'This is a communication interface to a node in blockchain', 200

    @route('/blockchain', methods=['GET'])
    def blockchain(self):
        return node.blockchain.toJson(), 200  

    @route('/transactionPool', methods=['GET'])
    def transactionPool(self):
        transactions = {}
        for id, transaction in enumerate(node.transactionPool.transactions):
            transactions[id] = transaction.toJson()
        return jsonify(transactions), 200

    @route('transaction', methods=['POST'])
    def transaction(self):
        values = request.get_json()
        if not 'transaction' in values:
            return 'Missing transaction value', 400
        transaction = Utils.decode(values['transaction'])
        node.handleTransaction(transaction)
        response = {'message': 'Received transaction'}
        return jsonify(response), 200