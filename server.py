from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Устанавливаем базовые директории
        base_dir = "templates"
        static_dir = "img"

        # Определяем маршрут
        if self.path == "/":
            file_path = os.path.join(base_dir, "index.html")
        elif self.path == "/katon-karagai":
            file_path = os.path.join(base_dir, "katon-karagai.html")
        elif self.path == "/tarbagatai":
            file_path = os.path.join(base_dir, "tarbagatai.html")
        elif self.path == "/altai-mountains":
            file_path = os.path.join(base_dir, "altai-mountains.html")
        elif self.path.startswith("/img/"):
            # Для статических файлов
            file_path = self.path.lstrip("/")
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write("<html><body><h1>404: Страница не найдена</h1></body></html>".encode("utf-8"))
            print(f"404: {self.path} не найден")
            return

        # Проверяем существование файла
        if os.path.exists(file_path):
            print(f"Файл найден: {file_path}")
            self.send_response(200)
            # Определяем Content-Type
            if file_path.endswith(".jpg") or file_path.endswith(".jpeg"):
                self.send_header("Content-type", "image/jpeg")
            elif file_path.endswith(".png"):
                self.send_header("Content-type", "image/png")
            elif file_path.endswith(".html"):
                self.send_header("Content-type", "text/html; charset=utf-8")
            else:
                self.send_header("Content-type", "application/octet-stream")
            self.end_headers()

            # Читаем и отправляем файл
            with open(file_path, "rb") as f:
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write("<html><body><h1>404: Файл не найден</h1></body></html>".encode("utf-8"))
            print(f"404: {file_path} не найден")

# Запуск сервера
def run(server_class=HTTPServer, handler_class=CustomHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Откройте в браузере: http://127.0.0.1:{port}/")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
