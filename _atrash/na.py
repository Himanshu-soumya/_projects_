#first we are going to import some
# liraries like flask , render templates requests and marhup
from flask import Flask, render_template, request, Markup
#we are importing panda
import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
#we have a utils folder and in that folder
# we have file fertilizer we are importing that list
from utils.fertilizer import fertilizer_dict
import os
import numpy as np
#importing other libraries that will required in our project
from keras.preprocessing import image
from keras.models import load_model
import pickle
#creating a varible called calculator that will load our trained model from the file
#generated file
calculator = load_model('Trained_model.h5')
calculator._make_predict_function()
#creating crmp and crm that will work accordingly (loading the generated pkl file )
crmp = 'Crop_Recommendation.pkl'
crm = pickle.load(open(crmp, 'rb'))
#creatng variable web as this help our website to run
web = Flask(__name__)
#post request for fertlizer prediction method
@ web.route('/fertilizer-predict', methods=['POST'])
#creating function that is going  to recommend us our fertilizer according to the soil type
def fertilizer_recommend():
    #variables that ill take the values when we enter in the form
    crop_name = str(request.form['cropname'])
    fillednitrogen = int(request.form['nitrogen'])
    filledpotassium = int(request.form['phosphorous'])
    filledpota = int(request.form['potassium'])
    #that will read the data from the below file and will act accordingly
    #this below file contain data of crops and there nitrogen , phosphorus and posttasium conents
    df = pd.read_csv('Data/Crop_NPK.csv')
    desirynitrogen = df[df['Crop'] == crop_name]['N'].iloc[0]
    desiryphosphorus = df[df['Crop'] == crop_name]['P'].iloc[0]
    desirypotassium = df[df['Crop'] == crop_name]['K'].iloc[0]
    n = desirynitrogen- fillednitrogen
    p = desiryphosphorus - filledpotassium
    k = desirypotassium - filledpota
    #here we are checking the conditions for nitrogen , phosphporus and potasium
    # according to their desired values
    if n < 0:
        key1 = "NHigh"
    elif n > 0:
        key1 = "Nlow"
    else:
        key1 = "NNo"
    if p < 0:
        key2 = "PHigh"
    elif p > 0:
        key2 = "Plow"
    else:
        key2 = "PNo"
    if k < 0:
        key3 = "KHigh"
    elif k > 0:
        key3 = "Klow"
    else:
        key3 = "KNo"
#we are taking the absolute values
    abs_n = abs(n)
    abs_p = abs(p)
    abs_k = abs(k)
    #these are the responses that will done like first response , second res , third response
    responsibleboy1 = Markup(str(fertilizer_dict[key1]))
    responsibleboy2 = Markup(str(fertilizer_dict[key2]))
    responsibleboy3 = Markup(str(fertilizer_dict[key3]))
    return render_template('Fertilizer-Result.html', recommendation1=responsibleboy1,
                           recommendation2=responsibleboy2, recommendation3=responsibleboy3,
                           diff_n = abs_n, diff_p = abs_p, diff_k = abs_k)
# now we are going to create our another funcion that is going to predict the pest
# when we gave the input data or the input image
def pred_pest(pest):
    try:
        ourimagetest = image.load_img(pest, target_size=(64, 64))
        ourimagetest = image.img_to_array(ourimagetest)
        ourimagetest = np.expand_dims(ourimagetest, axis=0)
        result = calculator.predict_classes(ourimagetest)
        return result
    except:
        return 'x'
# these pages will be rendered from the templates dependingon teh need
@web.route("/")
@web.route("/index.html")
def index():
    return render_template("index.html")
@web.route("/CropRecommendation.html")
def crop():
    return render_template("CropRecommendation.html")
@web.route("/FertilizerRecommendation.html")
def fertilizer():
    return render_template("FertilizerRecommendation.html")
@web.route("/PesticideRecommendation.html")
def pesticide():
    return render_template("PesticideRecommendation.html")
#this is for the identification of the identifications of the pests
@web.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        file = request.files['image']  # fetch input
        filename = file.filename
        file_path = os.path.join('static/user uploaded', filename)
        file.save(file_path)
        pred = pred_pest(pest=file_path)
        if pred == 'x':
            return render_template('unaptfile.html')
        if pred[0] == 0:
            pest_identified = 'aphids'
        elif pred[0] == 1:
            pest_identified = 'armyworm'
        elif pred[0] == 2:
            pest_identified = 'beetle'
        elif pred[0] == 3:
            pest_identified = 'bollworm'
        elif pred[0] == 4:
            pest_identified = 'earthworm'
        elif pred[0] == 5:
            pest_identified = 'grasshopper'
        elif pred[0] == 6:
            pest_identified = 'mites'
        elif pred[0] == 7:
            pest_identified = 'mosquito'
        elif pred[0] == 8:
            pest_identified = 'sawfly'
        elif pred[0] == 9:
            pest_identified = 'stem borer'
        return render_template(pest_identified + ".html",pred=pest_identified)
#this function is going to predict the crop that will be best suited fro
# our crop and will render on the webpage but it first it will take the input
# of teh values like nitrogen phosphorus , potassium humidity  , ph , rainfall , tempretature ,etc
# and it will in the end will give the result and will render the result of teh crop on the
# on the required web page
@ web.route('/crop_prediction', methods=['POST'])
def crop_prediction():
    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['potassium'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        my_prediction = crm.predict(data)
        final_prediction = my_prediction[0]
        return render_template('crop-result.html', prediction=final_prediction, pred='img/crop/'+final_prediction+'.jpg')
if __name__ == '__main__':
    web.run(debug=True)