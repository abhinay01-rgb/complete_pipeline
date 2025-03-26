from flask import Flask, request, render_template
import joblib
import pandas as pd

app=Flask(__name__)

model=joblib.load("models/model.pkl")


@app.route("/")
def home():
    return render_template("index.html",prediction=None)

@app.route("/predict",methods=["POST"])
def predict():
    try:
        age=float(request.form["age"])
        salary=float(request.form["salary"])


        df=pd.DataFrame([[age,salary]],columns=["age","salary"])

        prediction=model.predict(df)[0]

        return render_template("index.html",prediction=int(prediction),age=age,salary=salary)
    except Exception as e:
        return render_template("index.html",prediction="Error"+str(e))
    
if __name__ == '__main__':

    # app.run(host="0.0.0.0", port=5000) #for deployment run
    app.run(host="0.0.0.0", port=5000,debug=True) # for local run