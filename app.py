from flask import Flask,render_template,url_for,request
import pickle
import sklearn

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("base.html")

@app.route('/data',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        op=request.form['op']
        if op=="":
            raise ValueError("This field cant be empty")
        op=float(op)
        high=request.form['high']
        if high=="":
            raise ValueError("This field cant be empty")
        high=float(high)
        low=request.form['low']
        if low=="":
            raise ValueError("This field cant be empty")
        low=float(low)
        volume=request.form['volume']
        if volume=="":
            raise ValueError("This field cant be empty")
        volume=float(volume)
        with open("scalar.pkl",'rb')as file:
            scalar_model=pickle.load(file)
            
        arr=[[op,high,low,volume]]
        new=scalar_model.transform(arr)
        with open("stock.pkl",'rb') as file:
            model=pickle.load(file) 
        ans=model.predict(new)
        
            
    return render_template("index.html",ans=ans)



if __name__=="__main__":
    app.run(debug=True)