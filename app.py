from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

def prediction(list):
    filename = 'model\\predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)   
    prediction_value = model.predict([list])
    return prediction_value

# Route to render the form
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

# Route to handle the form submission
@app.route('/result', methods=['POST'])
def result():
    ram = request.form['ram']
    weight = request.form['weight']
    company = request.form['company']
    typename = request.form['type']
    opsystem = request.form['os']
    cpu = request.form['cpu']
    gpu = request.form['gpu']
    touchscreen = 'Yes' if request.form.get('touchscreen') else 'No'
    ips = 'Yes' if request.form.get('ips') else 'No'
    currency = request.form['currency']

    # Convert inputs to features for prediction
    featurelist = [
        int(ram),
        float(weight),
        touchscreen == 'Yes',
        ips == 'Yes'
    ]

    company_list = ['acer', 'apple', 'asus', 'dell', 'hp', 'lenovo', 'microsoft', 'msi', 'other', 'toshiba']
    type_list = ['2in1convertible', 'gaming', 'notebook', 'ultrabook', 'workstation']
    os_list = ['linux', 'mac', 'windows', 'other']
    cpu_list = ['amd', 'intelcorei3', 'intelcorei5', 'intelcorei7', 'other']
    gpu_list = ['amd', 'intel', 'other']

    def traverse_list(lst, value):
        for item in lst:
            if item == value.lower().replace(" ", "").replace("-", ""):
                featurelist.append(1)
            else:
                featurelist.append(0)

    traverse_list(company_list, company)
    traverse_list(type_list, typename)
    traverse_list(os_list, opsystem)
    traverse_list(cpu_list, cpu)
    traverse_list(gpu_list, gpu)

    # Predict
    conversion_rates = {'USD': 1, 'EUR': 0.92, 'LKR': 330, 'JPY': 155}
    symbols = {'USD': '$', 'EUR': '€', 'LKR': 'Rs', 'JPY': '¥'}

    pred = prediction(featurelist)
    pred = np.round(pred[0] * conversion_rates.get(currency, 1), 2)
    pred = f"{symbols.get(currency, '$')}{pred}"

    return render_template('result.html', pred=pred, ram=ram, weight=weight,
                           company=company, typename=typename, os=opsystem,
                           cpu=cpu, gpu=gpu, touchscreen=touchscreen, ips=ips,
                           currency=currency)

if __name__ == '__main__':
    app.run(debug=True)
