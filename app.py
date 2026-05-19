from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>CI/CD Python App</title>
            <style>
                body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f0f2f5; text-align: center; padding: 50px; }
                .card { background: white; padding: 40px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); display: inline-block; max-width: 500px; }
                h1 { color: #1e3d59; margin-bottom: 10px; }
                p { color: #17b978; font-size: 18px; font-weight: 500; }
                .track { color: #ff6f3c; font-weight: bold; }
                .footer { margin-top: 20px; font-size: 12px; color: #aaa; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>CI/CD Pipeline Task 🚀</h1>
                <p>Status: Application Deployed Successfully!</p>
                <div class="track">Track: Data Engineering / Python</div>
                <div class="footer">Jenkins Automation Cycle Completed</div>
            </div>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)