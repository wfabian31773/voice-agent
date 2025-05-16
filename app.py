from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/", methods=["POST"])
def voice_handler():
    """Basic call response"""
    response = """<?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Say voice="alice">Hello, this is Azul Vision. How can we help you?</Say>
    </Response>"""
    return Response(response, mimetype='text/xml')

if __name__ == "__main__":
    app.run(debug=True)