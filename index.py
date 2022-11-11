from flask import Flask, render_template
import os

#render_template es para renderizar vistas html

#confirmamos que este será el archivo de arranque
# guardamos el objeto en la variable app que utilizaremos para crear las rutas del servidor
app = Flask(__name__)

#creamos la ruta y definimos lo que hace la pág a través de una función
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')



#creamos el método de escucha de la web
if __name__ =='__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
    # debug=true es para decir q estamos en modo desarrollo y no tener que ir recargando el python todo el tiempo