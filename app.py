from flask import Flask, request
from flask import send_file
from image_transformation import ImageTransformation
from flask_cors import CORS, cross_origin
import numpy
import cv2

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/negativo", methods=['POST'])
def imageNegativeTransformation():
    file_bytes = numpy.fromfile(request.files['image'], numpy.uint8)
    file = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    x = ImageTransformation(file)
    x.imageNegativeTransformation()
    return send_file('./assets/cat-edited.png', mimetype='image/png')

@app.route("/logaritmica", methods=['POST'])
def imageLogTransformation():
    file_bytes = numpy.fromfile(request.files['image'], numpy.uint8)
    file = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    x = ImageTransformation(file)
    x.logarithmicTransformation()
    return send_file('./assets/cat-edited.png', mimetype='image/png')

@app.route("/potencia", methods=['POST'])
def imagePowerLawTransformation():
    file_bytes = numpy.fromfile(request.files['image'], numpy.uint8)
    file = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    x = ImageTransformation(file)
    x.powerLawTransformation(0.5)
    return send_file('./assets/cat-edited.png', mimetype='image/png')

# @app.route("/XXXXXXXXXXXXXXXXXXXXXXXXX", methods=['POST'])
# def XXXXXXXXXXXXXXXXXXXXXXXXXXX():
#     file_bytes = numpy.fromfile(request.files['image'], numpy.uint8)
#     file = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
#     x = ImageTransformation(file)
#     x.XXXXXXXXXXXXXXXXXXXXXXXXXXXXX(0.5)
#     return send_file('./assets/cat-edited.png', mimetype='image/png')

@app.route("/piecewise", methods=['POST'])
def pieceWiseTransformation():
    file_bytes = numpy.fromfile(request.files['image'], numpy.uint8)
    file = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    x = ImageTransformation(file)
    x.piecewiseLinearTransformation(50, 100, 150, 200)
    return send_file('./assets/cat-edited.png', mimetype='image/png')

@app.route("/histograma-local", methods=['POST'])
def histogramaLocal():
    file_bytes = numpy.fromfile(request.files['image'], numpy.uint8)
    file = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    x = ImageTransformation(file)
    x.localHistogramEqualization()
    return send_file('./assets/cat-edited.png', mimetype='image/png')

@app.route("/histograma-global", methods=['POST'])
def histogramaGlobal():
    file_bytes = numpy.fromfile(request.files['image'], numpy.uint8)
    file = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    x = ImageTransformation(file)
    x.globalHistogramEqualization()
    return send_file('./assets/cat-edited.png', mimetype='image/png')

@app.route("/mediana-espacial", methods=['POST'])
def medianaEspacial():
    file_bytes = numpy.fromfile(request.files['image'], numpy.uint8)
    file = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    x = ImageTransformation(file)
    x.espacialMedianFilter( 9 )
    return send_file('./assets/cat-edited.png', mimetype='image/png')

@app.route("/media-espacial", methods=['POST'])
def mediaEspacial():
    file_bytes = numpy.fromfile(request.files['image'], numpy.uint8)
    file = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    x = ImageTransformation(file)
    x.espacialMeanFilter( 9 )
    return send_file('./assets/cat-edited.png', mimetype='image/png')

@app.route("/laplacian", methods=['POST'])
def laplacian():
    file_bytes = numpy.fromfile(request.files['image'], numpy.uint8)
    file = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    x = ImageTransformation(file)
    x.laplacianFilter()
    return send_file('./assets/cat-edited.png', mimetype='image/png')

@app.route("/high-boost", methods=['POST'])
def highBoost():
    file_bytes = numpy.fromfile(request.files['image'], numpy.uint8)
    file = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    x = ImageTransformation(file)
    x.highBoostFilter(0.5)
    return send_file('./assets/cat-edited.png', mimetype='image/png')

@app.route("/roberts", methods=['POST'])
def robert():
    file_bytes = numpy.fromfile(request.files['image'], numpy.uint8)
    file = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    x = ImageTransformation(file)
    x.RobertsFilter()
    return send_file('./assets/cat-edited.png', mimetype='image/png')

@app.route("/sobel", methods=['POST'])
def sobel():
    file_bytes = numpy.fromfile(request.files['image'], numpy.uint8)
    file = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    x = ImageTransformation(file)
    x.sobelFilter()
    return send_file('./assets/cat-edited.png', mimetype='image/png')

    




