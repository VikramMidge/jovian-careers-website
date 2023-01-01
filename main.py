from flask import Flask,render_template,jsonify

app = Flask(__name__)

JOBS = [
      {
        'id': 1,
        'title' : 'Data Analyst',
        'location' : 'Bengaluru',
        'salary' : 'INR 10,00,000'
      },
      {
        'id': 2,
        'title' : 'Data Scientist',
        'location' : 'Bengaluru',
        'salary' : 'INR 10,00,000'
      },
      {
        'id': 3,
        'title' : 'Data Engineer',
        'location' : 'Bengaluru',
        'salary' : 'INR 10,00,000'
      },
  {
        'id': 4,
        'title' : 'FullStack Engineer',
        'location' : 'Bengaluru',
      }
]

@app.route('/')
def hello_world():
    return render_template('home.html',jobs=JOBS,company_name='Jovian')

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81, debug=True)
