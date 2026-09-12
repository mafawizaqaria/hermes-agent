import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler


class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")

    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        pass


def run_health_server():
    port = int(os.environ.get("PORT", "10000"))

    server = HTTPServer(("0.0.0.0", port), HealthCheckHandler)

    print(f"🌐 Render health server listening on port {port}", flush=True)

    server.serve_forever()


if __name__ == "__main__":
    # تشغيل خادم Render في الخلفية
    threading.Thread(
        target=run_health_server,
        daemon=True
    ).start()

    print("🚀 Starting Hermes Gateway...", flush=True)

    # تشغيل Hermes Gateway
    from gateway.run import main

    main()
