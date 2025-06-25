from flask import Flask, request, render_template
import pyodbc
import hashlib

app = Flask(__name__)


# Database connection setup
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;' 
    'DATABASE=login;'  
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

# Route for Registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        password_hash = hashlib.sha256(password.encode()).hexdigest()

        cursor.execute(
            "INSERT INTO Users (Username, PasswordHash, Email) VALUES (?, ?, ?)",
            (username, password_hash, email)
        )
        conn.commit()

        return "Registration successful!"
    return render_template('chatgpt form.html')  # this will show the HTML form

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
