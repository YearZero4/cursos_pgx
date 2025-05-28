from flask import Flask

app = Flask(__name__)
@app.route('/calcular/<int:num1><string:operacion><int:num2>')

def calcular(num1, operacion, num2):
	if operacion == 'mas':
	 result=num1+num2
	elif operacion == 'menos':
	 result=num1-num2
	elif operacion == 'entre':
	 result=num1/num2
	elif operacion == 'por':
	 result=num1*num2

	return f"El resultado de {num1} {operacion} {num2} es = {result}"

if __name__ == '__main__':
	app.run(debug=True)

## http://localhost:5000/sumar/2+2 ##
## El resultado de 2 + 2 es = 4 ##
