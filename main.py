from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def root():
    return "Home"

# GET -> Obtener datos
# POST -> Crear datos
# PUT -> Actualizar dato
# DELETE -> Borrar dato

@app.route("/users/<user_id>")
def get_user(user_id):
    user = {"id":user_id, "name":"test", "telefono": "351 102 1415"}
# /users/12345?query=query_test
    query = request.args.get('query')
    if query:
        user["query"] = query
    return jsonify(user), 200

if __name__ == "__main__":
    app.run(debug=True)