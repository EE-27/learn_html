from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Replace 'REPLACE_WITH_RAW_GITHUB_CONTENT_URL' with the raw URL of your HTML file
        html_file_url = 'https://raw.githubusercontent.com/EE-27/learn_html/main/index.html'

        try:
            # Fetch the HTML content from the remote repository
            response = requests.get(html_file_url)
            response.raise_for_status()  # Raise an error for bad responses

            # Send response headers
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Send the HTML content
            self.wfile.write(response.content)
        except requests.RequestException as e:
            print(f"Error fetching HTML file: {e}")
            # Send an internal server error response
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b'Internal Server Error')

def run(server_class=HTTPServer, handler_class=MyRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on http://localhost:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()

