from flask import Flask,render_template,jsonify,json,request
from utils import Medicalin
import config

app=Flask(__name__)
@app.route('/')
def hello_flask():
    print("welcome to my page")
    return jsonify({"result":"welcome to my page"})

@app.route("/prediction")
def predict():
     input_data=request.form
     print("input_data:",input_data)
     age=eval(input_data["age"] )
     sex=input_data["sex"]
     bmi=eval(input_data["bmi"])
     children=eval(input_data["children"])
     smoker=input_data["smoker"]
     region=input_data["region"] 
                              
     medin=Medicalin(age,sex,bmi,children,smoker,region)
     charges=medin.get_predictedcharges()
     return jsonify({"result":(f"(the predicted charge is {charges}")})
     
    
if __name__ == "__main__" :
    app.run(host="0.0.0.0",port=config.PORT_NUMBER,debug=False)

    
    