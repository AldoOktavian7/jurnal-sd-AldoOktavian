from flask import Flask
import os

app = Flask(__name__)

user_name = os.getenv("APP_USER", "Developer Mahasiswa")
app_env = os.getenv("APP_ENV", "development")

@app.route("/")
def home():
    return f"""
    <html>
    <head>
        <title>Si Jayam</title>
    </head>
    <body>
        <h1>Halo {user_name}!</h1>
        <h2>Si Jayam</h2>
        <h3>Versi 2.0 - Stabil</h3>
        <p>Environment: {app_env}</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)