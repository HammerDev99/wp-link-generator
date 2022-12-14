from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/concat', methods=['POST'])
def concat():
  val1 = request.form['val1']
  val2 = request.form['val2']
  result = 'https://api.whatsapp.com/send?phone=+57' + val1 + '&text=' + val2
  return render_template('index.html', result =result)

if __name__ == '__main__':
  app.run()
