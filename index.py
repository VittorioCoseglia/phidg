from flask import Flask, render_template, request

app = Flask(__name__)
# Routes to Render Something


@app.route('/')
def phs():
    return render_template("home.html")


@app.route('/', methods=['POST'])
def phsp():
    text = request.form['text']
    print(text)
    return render_template(
		'home.html',
		info=text  
	)



if __name__ == '__main__':
	app.run(debug=True)
