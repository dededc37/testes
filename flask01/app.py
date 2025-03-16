from flask import Flask, render_template

app = Flask(__name__)

#criar a 1ª página do site
#route -> dede.com.br/alguma_página_com_sub_dominio
#função -> oque você quer exibir ná página
@app.route('/')
def home():
    return render_template('home/android.html')

#colocar o site no ar
if __name__== '__main__':
    #app.run(debug=True)