from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json
from unbabel.api import UnbabelApi
from models import db

with open('config.json') as f:
    config = json.load(f)

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = config["postgres_url"]
db = SQLAlchemy(app)
db.init_app(app)
api = UnbabelApi(username=config["unbabel_api_name"], api_key=config["unbabel_api_key"], sandbox=True)

from models import Job

@app.route('/', methods=["GET", "POST"])
def index():
    error = ""
    if request.method == 'POST':
        text = request.form['text']
        api.post_translations(text=text, target_language="es",
                              source_language="en",
                              callback_url="http://MISSING/translation/done")
        try:
            job = Job(text, "Requested")
            db.session.add(job)
            db.session.commit()
        except:
            error = "Unable to add item to database."
        render_template("index.html", error)

    #translations = api.get_translations()
    return render_template("index.html")

@app.route('/translation/done', methods=["POST"])
def translationDone():
    #TODO logic to receive translation state from unbabel

    Job.query.filter_by(unbabel_id="j")

    translations = api.get_translations()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", debug=True)
