import ipapi

from flask import Flask
from flask import request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    search = request.form.get('search')
    ip = ipapi.location(ip=search, output='json')
    return render_template('index.html', ip=ip)

if __name__ == "__main__":
    app.run(debug=True)
