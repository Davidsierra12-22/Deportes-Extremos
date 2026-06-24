import http.server
import socketserver
import os

PORT = 8000

# Asegura que el servidor siempre sirva los archivos desde la carpeta correcta
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

print(f"🚀 Servidor extremo corriendo en: http://localhost:{PORT}")
print("Presiona Ctrl+C para detener.")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Servidor detenido.")
        httpd.server_close()