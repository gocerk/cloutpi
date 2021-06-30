from flask import jsonify, Flask, request, redirect, render_template
from utils.utils import Sign_Transaction

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home(): 
    return jsonify({'message': 'please make a post request to the /sign-transaction url'});

@app.route('/sign-transaction', methods=['POST' , 'GET'])
def signTransaction():
    try:   
        content = request.json
        seedHex = content['seedHex'] #returnin None
        transactionHex = content['transactionHex'] 
    except KeyError: 
        return jsonify({'message': 'there are no given parameters', 'code': 400}), 400 

    try: 
        signedTransactionHex = Sign_Transaction(seedHex, transactionHex)
    except: 
        return 404
        
    return jsonify({'SignedTransactionHex': signedTransactionHex})
    

@app.errorhandler(404)
def errorHandler(error):
    return jsonify({'message': error, 'code': 404})


@app.errorhandler(400)
def errorHandler(error): 
    return jsonify({'message': error, 'code': 404})

app.run()