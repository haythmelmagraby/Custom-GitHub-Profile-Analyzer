from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GITHUB_API_URL = "https://api.github.com/users/"

@app.route('/profile/<username>', methods=['GET'])
def get_profile(username):
    response = requests.get(f"{GITHUB_API_URL}{username}")
    if response.status_code == 200:
        profile_data = response.json()
        return jsonify(profile_data)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/profile/<username>/repos', methods=['GET'])
def get_repos(username):
    response = requests.get(f"{GITHUB_API_URL}{username}/repos")
    if response.status_code == 200:
        repos_data = response.json()
        repos_list = [{
            "name": repo["name"],
            "language": repo["language"],
            "stars": repo["stargazers_count"]
        } for repo in repos_data]
        return jsonify(repos_list)
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
