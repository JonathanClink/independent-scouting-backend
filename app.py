from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Get the database URL from Render's environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Function to connect to the database
def get_db_connection():
    return psycopg2.connect(DATABASE_URL, sslmode="require")

@app.route("/")
def home():
    return "API is working!"

if __name__ == "__main__":
    app.run(debug=True)
