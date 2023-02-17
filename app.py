from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS =[
{
  'id':1,
  'location': 'Nairobi',
  'title': 'Software developer',
  'salary': '40,000ksh'
},
{
  'id':2,
  'location': 'Eldoret',
  'title': 'Data Scientist',
  'salary': '80,000ksh'
},
{
  'id':1,
  'location': 'Mombasa',
  'title': 'Software developer',
  'salary': '40,000ksh'
},
{
  'id':1,
  'location': 'Nairobi',
   'title': 'Frontend developer',
  'salary': '30,000ksh'
},
]

@app.route("/")

def sayHello():
  return render_template('home.html',jobs=JOBS)


@app.route("/api/jobs")
def listJobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)

