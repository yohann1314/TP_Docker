from flask import Flask, render_template, request

app = Flask(__name__)

# Fonction logique pour addition
def calculate_addition(a, b):
    return a + b

# Fonction logique pour soustraction
def calculate_subtraction(a, b):
    return a - b

# Route principale
@app.route("/", methods=["GET", "POST"])
def home():
    result = None  # Valeur par défaut pour le résultat
    error = None   # Gestion des erreurs

    if request.method == "POST":
        try:
            # Récupération des entrées utilisateur
            num1 = float(request.form.get("num1", 0))
            num2 = float(request.form.get("num2", 0))
            operation = request.form.get("operation", "add")

            # Calcul en fonction de l'opération choisie
            if operation == "add":
                result = calculate_addition(num1, num2)
            elif operation == "subtract":
                result = calculate_subtraction(num1, num2)
            else:
                error = "Opération invalide."
        except ValueError:
            error = "Veuillez entrer des nombres valides."

    return render_template("calculator.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
