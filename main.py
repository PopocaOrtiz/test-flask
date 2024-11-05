from flask import Flask, url_for, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
	return "<h1>hello world!</h1>"


@app.route("/<name>")
def say_my_name(name: str):
	return f"<h1>Hello: {escape(name)}</h1>"

@app.route("/users/<int:user_id>")
def get_user(user_id: int):
	return f"User: {user_id}"


@app.route("/users/<int:user_id>/<path:attribute>")
def get_user_attributes(user_id: int, attribute):
	return f"User: {user_id}, Path: {attribute}"


@app.route("/projects/")
def list_projects():
	return f"Projects: "


@app.route("/login", methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return "<h1>Login:</h1>"
	else:
		return "<h1>You are loged</h1>"

@app.get("/products")
def get_products():
	return "List products"

@app.post("/products")
def create_product():
	return "Create product"

with app.test_request_context():
	print(url_for("hello_world"))
	print(url_for("say_my_name", name="fer"))
	print(url_for("get_user", user_id=10, user_name="the_other"))
