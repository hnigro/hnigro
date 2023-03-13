"""
este programa crea una html

también voy a hacer un scrap de una html para usarla


"""

from flask import Flask

app = Flask(__name__)
x = 1000000001
@app.route("/")
def hello_world():
    #return "<p>Hello, World!</p>"
    return(
        f"<h1>ancho de banda SRT1= {x}</h1>\n"
        f"<h1>ancho de banda SRT2= {x}</h1>\n"
        f"<h1>ancho de banda SRT3= {x}</h1>\n"
        f"<h1>ancho de banda SRT4= {x}</h1>\n"
    )






if __name__ == "__main__":

    app.run(debug= True)
