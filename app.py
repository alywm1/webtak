from flask import Flask, render_template, request
import webbrowser
import time
from threading import Timer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    url = request.form['url']
    views = int(request.form['views'])
    
    if 3 <= views <= 20:
        for i in range(views):
            Timer(i * 60, open_url, args=(url,)).start()
    return render_template('index.html')

def open_url(url):
    webbrowser.open_new(url)
    time.sleep(60)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
  
