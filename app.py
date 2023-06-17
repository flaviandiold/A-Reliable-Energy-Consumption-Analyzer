from flask import Flask,request,render_template
import pickle

model = pickle.load(open('PCASSS_model.pkl','rb'))
app = Flask(__name__, template_folder='./templates', static_folder='./static')

#The home page is rendered
@app.route('/')
def hello():
    return render_template('index.html')

#The inspection page is rendered
@app.route('/inspect')
def inspect():
    return render_template("inspect.html")

#The output page is rendered
@app.route('/home', methods=['POST','GET'])
def home():
    GlobalReactivePower = float(request.form['GlobalReactivePower'])
    GlobalIntensity = float(request.form['GlobalIntensity'])
    Sub_metering_1 = float(request.form['Sub_Metering_1'])
    Sub_metering_2 = float(request.form['Sub_Metering_2'])
    Sub_metering_3 = float(request.form['Sub_Metering_3'])
    
    X = [[GlobalReactivePower,GlobalIntensity,Sub_metering_1,Sub_metering_2,Sub_metering_3]]
    
    output = round(model.predict(X)[0],3)
    if output < 0:
        return render_template("output.html", pred = 'Error calculating the amount')
    else:
        return render_template("output.html", pred = output)

if __name__ == '__main__':
    app.run(debug = True,port = 4500)