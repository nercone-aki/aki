from kaede import Server

from .app import Aki, Response
from .responses import PlainTextResponse

app = Aki()

@app.route("/")
def top(request, ws) -> Response:
    return PlainTextResponse("It works! This is Response from Aki.")

def main():
    print("Starting server... Try access it to http://localhost:80/")

    server = Server(app)
    server.run()

if __name__ == "__main__":
    main()
