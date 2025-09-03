from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Programmer',
    'location': 'Hyderabad, India',
    'salary': 'Rs. 20,00,000'
}, {
    'id': 3,
    'title': 'Associate',
    'location': 'Chennai, India',
}, {
    'id': 4,
    'title': 'Data scientist',
    'location': 'Remote',
    'salary': 'Rs. 30,00,000'
}]


@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)


def home():
    return render_template('home.html', jobs=JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
