# Importing flask module in the project is mandatory 
# An object of Flask class is our WSGI application. 
from flask import Flask, request
import json 
from flask_cors import CORS
from input import Input
  
# Flask constructor takes the name of  
# current module (__name__) as argument. 
app = Flask(__name__) 
CORS(app)
ip = Input()

  
# The route() function of the Flask class is a decorator,  
# which tells the application which URL should call  
# the associated function. 
@app.route('/', methods = ['GET','POST']) 
# ‘/’ URL is bound with hello_world() function. 
def hello_world():
    print(request)
    print(request.get_json())
    data = request.get_json()
    #print('data[text]',data['text'] )
    op = ip.search(data['text'])
    #print(op)
    json = {'data' : op}
    print(json)
    return json
  
# main driver function 
if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server. 
    app.run()