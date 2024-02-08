from flask import Flask, render_template, Response,request,jsonify
import cv2
import base64
import io
import numpy as np

app = Flask(__name__,template_folder='template')


@app.route('/')
def index():
    return render_template('scanner.html')

@app.route('/reward/<data>')
def reward(data):
    return render_template('reward-page.html', data=data)

@app.route('/scan', methods=['POST'])
def scan():
    image_data = request.json['image']
    image_bytes = base64.b64decode(image_data.split(',')[1])
    image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    qr_codes = cv2.QRCodeDetector().detectAndDecodeMulti(gray)
    
    if qr_codes[0]:
        data = 'hello'  # Extract the data from the first QR code found
        return jsonify({'qrCodeFound': True, 'qrCodeData': data})
    else:
        return jsonify({'qrCodeFound': False})

if __name__ == '__main__':
    app.run(debug=True)
