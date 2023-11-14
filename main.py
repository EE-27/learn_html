from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def get_assignment_page():
    # Replace 'REPLACE_WITH_RAW_GITHUB_CONTENT_URL' with the raw URL of your HTML file
    html_file_url = 'https://raw.githubusercontent.com/EE-27/learn_html/main/index.html'

    try:
        # Fetch the HTML content from the remote repository
        response = requests.get(html_file_url)
        response.raise_for_status()  # Raise an error for bad responses

        # Render the HTML content
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching HTML file: {e}")
        return "Internal Server Error", 500


if __name__ == '__main__':
    app.run(debug=True)