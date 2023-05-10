import sqlite3
from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
	name = ''
	age = None
	photo = ''
	bio = ''

	if request.method == 'GET':
		
		conn = sqlite3.connect('main.db')
		c = conn.cursor()
		c.execute('''SELECT * FROM users''')
		row = c.fetchone()
		print (row)

		if row:
			name = row[0]
			age = row[1]
			photo = row[2]
			bio = row[3]

		conn.close()
	# return
	#return render_template('my_info.htm', name=name, age=age, photo=photo, bio=bio)
	if request.method == 'POST':

		name = request.form['name']
		age = request.form['age']
		photo = request.form['photo']
		bio = request.form['bio']

		conn = sqlite3.connect('main.db')
		c = conn.cursor()
		c.execute('''SELECT * FROM users''')		
		row = c.fetchone()
		if row:
			c.execute('''UPDATE users SET name = ?, age = ?, photo = ?, bio = ?''', 
				(name, age, photo, bio))
		else:
			c.execute('''INSERT INTO users VALUES (?, ?, ?, ?)''', 
				(name, age, photo, bio))
		conn.commit()
		conn.close()
	# return
	return render_template('my_info.htm', name=name, age=age, photo=photo, bio=bio)



def get(request):
	pass

def post(request):
	pass

@app.after_request
def add_header(response):
	"""
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
	response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
	response.headers['Cache-Control'] = 'public, max-age=0'
	return response


if __name__ == '__main__':
	app.run(debug=False)
