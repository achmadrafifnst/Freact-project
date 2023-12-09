from flask import Flask, request, jsonify
from flask_cors import CORS
from tflitelib import TensorflowLiteClassificationModel
import os
import json

model = TensorflowLiteClassificationModel(model_path='static/model/model_tes.tflite',labels=['Fake','Real','Undetect'])
app = Flask(__name__)
CORS(app)
app.secret_key = "projekakhir"
app.config['UPLOAD_FOLDER'] = 'static/img_check/'

@app.route("/api/freact",methods = ['POST'])
def start():
    file = request.files
    if file:
        for photo in file:
            filesave = file[photo]
            filesave.save(os.path.join('static/img_check/'+filesave.filename))
    #     img = request.files['image_input']
    #     img_path = os.path.join(app.config['UPLOAD_FOLDER'],img.filename)
    #     img.save(img_path)
        label = model.run_from_filepath(os.path.join(app.config['UPLOAD_FOLDER'],filesave.filename))
        print(label)
        hasil = max([label[1][1],label[2][1]])
        if hasil==label[1][1]:
            dataReturn = {
                'Prediksi':str(label[1][0]),
                'Probabilitas':str(label[1][1])
            }
    #         # return render_template('running.html',uploaded_image = 'img_check/'+img.filename,prediksi = label[1][0],prob = label[1][1])    
        elif hasil==label[2][1]:
            dataReturn = {
                'Prediksi':str(label[2][0]),
                'Probabilitas':str(label[2][1])
            }
    #         # return render_template('running.html',uploaded_image = 'img_check/'+img.filename,prediksi = label[2][0],prob = label[2][1])
    # # elif request.method == 'GET':
    # #     return render_template('running.html')
    # dataReturn={
    #     'probabilitas':'100%',
    #     'prediksi':'berhasil'
    # }
    return jsonify(dataReturn), 200

# @app.route('/contact_us',methods = ['POST','GET'])
# def contact():
#     return render_template('contact_us.html')
# def send_uploaded_image(filename = ''):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

if __name__=="__main__":
    # from waitress import serve
    app.run(debug = True,port=5002)
    # serve(app, host="0.0.0.0", port=5002)