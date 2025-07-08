import flask
import functions_framework
import os
import redis

def broadcast(message: str, channel: str):
    """Broadcast a message to the specified Redis channel."""
    try:
        r = redis.from_url(os.getenv("REDIS_URL"), decode_responses=True)
        r.publish(channel, message)
        return json_response(f"Published message: {message} to channel: {channel}")
    except redis.ConnectionError as e:
        return json_response(f"Error connecting to Redis: {e}", 500)
    except Exception as e:
        return json_response(f"Error publishing message: {e}", 500)

def json_response(message: str, status: int = 200):
    """Return a JSON response with CORS headers."""
    response = flask.make_response(flask.jsonify({"message": message}), status)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@functions_framework.http
def runfn(request: flask.Request) -> flask.typing.ResponseReturnValue:
    for channel in ["station-request", "station-playing"]:
        msg = request.args.get(channel)
        if msg:
            return broadcast(msg, channel)
    return json_response("No message provided.", 400)
