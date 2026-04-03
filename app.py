from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    stock_name = request.form['stock']

    # Dummy prediction logic (you can replace with ML model)
    prediction = "UP 📈" if len(stock_name) % 2 == 0 else "DOWN 📉"

    return render_template('index.html', stock=stock_name, result=prediction)

if __name__ == '__main__':
    app.run(debug=True)