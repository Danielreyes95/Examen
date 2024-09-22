from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        try:
            nombre = request.form['ingresatunombre']
            edad = int(request.form['ingresatuedad'])
            tarrospintura = int(request.form['tarrospintura'])
            precionormal = tarrospintura * 9000


            if 18 <= edad <= 30:
                descuento = 0.15
            elif edad > 30:
                descuento = 0.25
            else:
                descuento = 0

            preciocon_descuento = round(precionormal * (1 - descuento))
            descuentototal = round(precionormal - preciocon_descuento)

            return render_template('ejercicio1.html', nombre=nombre, precionormal=precionormal,
                                   preciocon_descuento=preciocon_descuento, descuentototal=descuentototal, error="")
        except ValueError:
            error = "Por favor ingresa valores numéricos válidos para la edad y la cantidad de tarros de pintura."
            return render_template('ejercicio1.html', error=error)
    else:

        return render_template('ejercicio1.html', nombre="", precionormal=0, preciocon_descuento=0, descuentototal=0, error="")

usuarios = {
    "juan": "admin",
    "pepe": "user"
}

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = ""
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contraseña']

        if usuario in usuarios and usuarios[usuario] == contrasena:
            if usuario == "juan":
                mensaje = f"Bienvenido administrador {usuario}"
            elif usuario == "pepe":
                mensaje = f"Bienvenido usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"
        return render_template('ejercicio2.html',mensaje=mensaje)
    return render_template('ejercicio2.html', mensaje="")


if __name__ == '__main__':
    app.run(debug=True)
