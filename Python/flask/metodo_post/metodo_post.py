from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def start():
	if request.method == "POST":
		user=request.form['usuario']
		return f"Hola como estas {user}, que es de tu vida ? "
	return '''
	<form method="post">
  <input type="text" name="usuario">
  <input type="submit" value="ENVIAR">
	</form>
	'''
if __name__ == '__main__':
	app.run(debug=True)


## si pones en el form david lo va enviar por method post y mostrara ##
## Hola como estas david, que es de tu vida ? ##

