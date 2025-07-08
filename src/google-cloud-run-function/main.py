import flask
import functions_framework
import os
import redis


def resp(message, status=200):
    return message, status, {"Access-Control-Allow-Origin": "*"}


@functions_framework.http
def play(request: flask.Request) -> flask.typing.ResponseReturnValue:
    request_args = request.args
    if "station" in request_args:
        try:
            r = redis.from_url(os.getenv("REDIS_URL"), decode_responses=True)
            r.publish("now-playing", request_args["station"])
            return resp(
                f"Published station: {request_args['station']} to 'now-playing' channel"
            )
        except redis.ConnectionError as e:
            print(f"Error connecting to redis: {e}")
        except Exception as e:
            print(f"Error updating redis: {e}")

        return resp("an error occurred, check function logs.", 500)
    else:
        return resp("No station provided in request arguments.", 400)
