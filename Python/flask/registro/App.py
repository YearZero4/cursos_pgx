from flask import Flask, request, render_template
app=Flask(__name__)




@app.route('/')
def index():
 return render_template('index.html')

@app.route('/procesar_formulario', methods=['POST'])
def procesar_formulario():
	name=request.form['name']

	print(name)
	ntfy="REGISTRO EXITOSO"
	return render_template('index.html', ntfy=ntfy)

if __name__ == '__main__':
	app.run(debug=True)