import markdown
import os
import shelve
from flask import Flask, g

#Create an instance of Flask
app = Flask(__name__)

#Handle connection to database
def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = shelve.open("employees.db")
	return db

@app.teardown_appcontext
def teardown_db(exception):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()

@app_route("/")
def index():
	"""Present some documentation"""

	# Open the README file
	with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

		#Read the content
		content = markdown_file.read()

		#Convert to HTML
		return markdown.markdown(content)

class DeviceList(Resource):
	def get(self):
		shelf = get_db()
		keys = list(shelf.keys())

		employees = []

		for key in keys:
			employees.append(shelf[key])

		return {'message': 'Success', 'data': employees}

	def post(self):
		parser = reqparse.RequestParser()

		parser.add_argument('identifier', required=True)
		parser.add_argument('title', required=True)
		parser.add_argument('name', required=True)
		parser.add_argument('age', required=True)
		parser.add_argument('address', required=True)

		#Parse the arguments into an object
		args = parser.parse_args()

		shelf = get_db()
		shelf[args['identifier']] = args

		return {'message': 'Employee registered', 'data': args}, 201

class Employee(Resource):
	def get(self, identifier):
		shelf = get_db()

		# if the key does not exist in the data store, return a 404 error.
		if not(identifier in shelf):
			return {'message': 'Employee not found', 'data': {}}, 404

		return {'message': 'Employee Found', 'data': shelf[identifier]}, 200

	def delete(self, identifier):
		shelf = get_db()

		# if the key does not exist, provide a message
		if not(identifier in shelf):
			return {'message': 'Employee not found', 'data': {}}, 404

		del shelf[identifier]
		return '', 204

api.add_resource(EmployeeList, '/employees')
api.add_resource(Employee, '/employee/<string:identifier>')