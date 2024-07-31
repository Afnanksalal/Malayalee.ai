from flask import Flask, render_template, request
from utils.text_processing import process_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_text = request.form['input_text']
        english_text, generated_text, malayalam_response = process_text(original_text)
        return render_template('index.html', 
                               original_text=original_text,
                               english_text=english_text,
                               generated_text=generated_text,
                               malayalam_response=malayalam_response)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)