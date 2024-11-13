from flask import Flask, render_template, request

app = Flask(__name__)

# Exibir formulário
@app.route("/")
def index():
    return render_template('index.html')

# Receber dados do formulário
@app.route("/", methods=['POST'])
def form_submit():
    ask = request.form.get('ask')
    url_pdf = request.form.get('url-pdf')
    option = request.form.get('option')
    
    print(f"Texto: {ask}")
    print(f"URL ou PDF: {url_pdf}")
    print(f"Opção: {option}")

    return f'Você enviou: {ask}, {url_pdf}, {option}'

if __name__ == '__main__':
    app.run(debug=True)