from flask import Flask, jsonify
import boto3
import os

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({
        'status': 'ok'
    })

@app.route('/getrecord/<number>')
def record(number):

    bucketName = os.getenv('BUCKET')
    path = 'record-' + number + '.log'

    # falta a credencial aqui
    s3 = boto3.client('s3')

    try:
        
        response = s3.get_object(
            Bucket=bucketName, # type: ignore
            Key=path
        )

        return jsonify({
            'status': 'ok',
            'resultado': response['Body'].read().decode('utf-8')
        })

    except Exception as e:
        print("Something happened: ", e)
        return jsonify({
            'status': 'failed'
        })
