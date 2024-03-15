from flask import Flask
import mysql.connector

app = Flask(__name__)


@app.route("/")
def index():
    # Connexion à la base de données MySQL
    connection = mysql.connector.connect(
        host="mysql", user="root", password="root_password", database="mysql"
    )

    cursor = connection.cursor()

    # Exemple de requête à la base de données
    cursor.execute("SELECT * FROM example_table")
    data = cursor.fetchall()

    # Affichage des données dans la page web
    result = "<h1>Données de la base de données MySQL :</h1>"
    for row in data:
        result += "<p>" + str(row) + "</p>"

    connection.close()

    return result


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
