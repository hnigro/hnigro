"""
este programa crea una html

también voy a hacer un scrap de una html para usarla


"""

from flask import Flask, render_template, request

app = Flask(__name__)
x = 1000000001
bw_srt_abc_01 = "20/08/24"
bw_srt_abc_02 = 22222222
bw_srt_abc_03 = 33333333
bw_srt_abc_04 = 44444444
bw = [bw_srt_abc_01,bw_srt_abc_02,bw_srt_abc_03,bw_srt_abc_04]


@app.route("/")
def home():
    xx2 =["q","w","e"]

    return render_template("index.html",
                           contenido= f"Testing {x}",
                           x1= f"valor de x1 = {bw_srt_abc_01}",
                           x2= f"valor de x2 = {bw_srt_abc_02}",
                           x3= f"valor de x3 = {bw_srt_abc_03}",
                           x4= f"valor de x4 = {bw_srt_abc_04}",
                           xx= bw,
                           xx2 = xx2
                           )


@app.route("/hhh1/")
def hh1():
    return render_template("index1.html",
                           contenido=f"Testing {x}",
                           x1=f"hhhhhxxxxxxxxxxxxxxxxx x1 = {bw_srt_abc_01}",
                           x2=f"xxxxxxxxxxxxxxxxxx = {bw_srt_abc_02}",
                           x3=f"valor de x3 = {bw_srt_abc_03}",
                           x4=f"valor de x4 = {bw_srt_abc_04}",
                           xx=[0,1,2]
                           )


if __name__ == "__main__":

    #app.run(debug= True)
    app.run(debug = True, host="0.0.0.0", port=16000)
