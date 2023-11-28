
from flask import Flask



app = Flask(__name__)


@app.route("/")
def hello():

    int a=13
    int b=14
    int c=a+b;
    return(c)



if __name__ == "__main__":
   
    app.run(host="127.0.0.1", port=8080, debug=True)
