from flask import Flask, request, jsonify,render_template
from flask_sqlalchemy import SQLAlchemy
from  flask_marshmallow import Marshmallow
import os

 # to initialize the app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
#database
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///'+os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#initialinsing the db
db = SQLAlchemy(app)

#init marshmallow
ma = Marshmallow(app)

#customer class/model
class Customer(db.Model):
    
    id =db.Column(db.Integer, primary_key=True)
    f_name =db.Column(db.String(50))
    l_name =db.Column(db.String(50))
    age =db.Column(db.Integer)
    marital_status=db.Column(db.String)
    income=db.Column(db.Float)
    have_kids=db.Column(db.String)#boolean type
    city=db.Column(db.String(30))
    religion=db.Column(db.String(30))

    def __init__(self,f_name,l_name,age,marital_status,income,have_kids,city,religion):# analogy for this in java
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.marital_status = marital_status
        self.income = income
        self.have_kids = have_kids
        self.city = city
        self.religion = religion

# Customer schema
class CustomerSchema(ma.Schema):
    class Meta:
        fields = ('id','f_name','l_name','age','marital_status','income','have_kids','city','religion')

#initializing the schema


Customer_schema =CustomerSchema()

#test endpoint
@app.route('/test', methods=['GET'])
def testHello():
   print("=================================")
   return "hello there !!"

#Adding a customer end point
@app.route('/AddCustomer', methods=['POST'])
def add_Customer():
 
    f_name = request.json['f_name']
    l_name = request.json['l_name']
    age = request.json['age']
    marital_status = request.json['marital_status']
    income = request.json['income']
    have_kids = request.json['have_kids'] 
    city = request.json['city']
    religion = request.json['religion']

    
    new_Customer = Customer(f_name,l_name,age,marital_status,income,have_kids,city,religion)
    
  
    db.session.add(new_Customer)
    db.session.commit()
    #return "success"
    return Customer_schema.jsonify(new_Customer) 

@app.route("/")
def front():
    return render_template("front.html")




#run the server
if __name__ =='__main__':
     app.run(debug=True)