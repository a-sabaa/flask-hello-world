from flask import Flask,jsonify,request 
  
app =   Flask(__name__) 
  
@app.route('/hello-world', methods = ['GET']) 
def ReturnJSON(): 
    if(request.method == 'GET'): 
        data = { 
            "content" : 'hello-world', 
        } 
  
        return jsonify(data) 
  
if __name__=='__main__': 
    app.run(debug=True)
