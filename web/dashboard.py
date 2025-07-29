from flask import Flask, render_template_string
from shared.alert_store import get_alerts

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Syslog Alert Dashboard</title>
    <meta http-equiv="refresh" content="5">
    <style>
        body { font-family: monospace; background: #1e1e1e; color: #dcdcdc; padding: 2rem; }
        h1 { color: #4ec9b0; }
        .alert { border-bottom: 1px solid #333; padding: 0.5rem 0; }
    </style>
</head>
<body>
    <h1>🔍 Live Syslog Alerts</h1>
    {% for alert in alerts %}
        <div class="alert">{{ alert }}</div>
    {% endfor %}
</body>
</html>
"""

@app.route("/alerts")
def alerts():
    return render_template_string(TEMPLATE, alerts=get_alerts())

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
