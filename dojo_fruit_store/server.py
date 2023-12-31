from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    strawberry = int(request.form['strawberry'])
    raspberry = int(request.form['raspberry'])
    apple = int(request.form['apple'])
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']

    # Realizar el cálculo del total
    totalfruits = strawberry + raspberry + apple
    
    # Imprimir la información del pago en la terminal
    print(f"Cobrando a {first_name} {last_name} por {totalfruits} frutas")
    print(request.form)
    return render_template("checkout.html", strawberry=strawberry, raspberry=raspberry, apple=apple, first_name=first_name,last_name=last_name,student_id=student_id)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")


if __name__=="__main__":   
    app.run(debug=True)    