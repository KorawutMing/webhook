from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary in-memory storage of events
EVENTS = []

@app.route("/webhook", methods=["POST"])
def webhook():
    """
    Receives LINE webhook events and stores them in memory.
    """
    body = request.get_json()
    if not body or "events" not in body:
        return jsonify({"status": "ignored"}), 400

    # Append all incoming events to EVENTS
    EVENTS.extend(body["events"])
    return jsonify({"status": "received", "count": len(body["events"])}), 200

@app.route("/poll", methods=["GET"])
def poll():
    """
    Local backend polls this endpoint to get LINE events.
    After returning events, clear the list to avoid duplicates.
    """
    global EVENTS
    events_to_return = EVENTS.copy()
    EVENTS = []  # clear after polling
    return jsonify(events_to_return)
