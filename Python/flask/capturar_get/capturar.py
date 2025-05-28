from flask import Flask


app=Flask(__name__)

@app.route('/name/<name>')
def saludar(name):
	return f"Hello {name}, como estas?"

if __name__ == '__main__':
	app.run(debug=True)

## http://localhost:5000/name/PGX ##
## Hello PGX, como estas? ##