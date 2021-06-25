from flask import Flask, request
from ie_utils import tokenize

#Creating a variable which will be an instance from flask
#Double underscore will take a diff value weehter you import or run the code
app = Flask(__name__)
 
    
#We need to decorate this function with app.route:
@app.route("/")
def home(): #Taking no params
    return { 
        "message": "Hello World!",
        "version": "0.1"}  

#Adding this ({message and version}) to return Json data instead of string data GROUPWORK! So anybody consuming data from this app, can easily transform this into a python dictionary and consume this data easily
    
#This up here is a web API

#Now in terminal:
 #If i run $ flask run (We are alll in the same server using the same port, so we need to avoid this)
# To access the URL, we need to access from the server not from the outside, so we Open IFRAME, and we type the server, we can access that web API

#Ctrl + c to stop the API, we will see error 500 in the http screen

#If we don't get a port, we run $ random-port (e.g = 53707) let's stick to this port for the rest of the class, to go to the port we run $ flask run --port 53707
# ctr + c to cancel the API

#$ export FLASK_DEBUG=1
# now we run flask run and we will see that debug mode is on with flask $ run --port 53707
# http://127.0.0.1:53707


#Now let's add an endpoint (similar to a tokenizer) do_tokenize to avoid repeating the name of the importe function

@app.route("/tokenize") #decorating the function
def do_tokenize():
    print(request.args)
    sentence = request.args["sentence"] #this gives me the sentence that the user passes, so now we can tokenize my sentence
    lower = bool(request.args.get("lower",False)) #if we wanna make a parameter optional in our function we will use the get+False
    return str(tokenize(sentence, lower=lower)) #str to avoid getting a list of tokens
#Adding this to return Json data instead of string data GROUPWORK! So anybody consuming data from this app, can easily transform this into a python dictionary and consume this data easily


# now if we run http://127.0.0.1:53707/tokenize we will see tha API tokenize from the function

# curl is the command line to making request to URLs, a browser from the command line, we will run:
    # $ curl "http://127.0.0.1:53707/tokenize?sentence=python+tutorial"

#IF WE HAVE ISSUES WITH THE PORT
# ps -ef
# lsof -i :53703 to see who is binding in that port
# kill +PID(Port) you will see after running to lsof (e.g 892022)
    # kill :892022
# then lsof -i :53703 won't display anything



    