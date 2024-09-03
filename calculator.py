from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression')
    try:
        result = eval(expression)
    except:
        result = 'Error'
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)