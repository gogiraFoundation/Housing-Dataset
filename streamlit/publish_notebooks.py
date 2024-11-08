import streamlit as st
import requests
import base64
import os

# GitHub API URL
GITHUB_API_URL = "https://api.github.com"
REPO_OWNER = "your_github_username"  # Replace with your GitHub username or org name
REPO_NAME = "your_repository_name"  # Replace with your repository name
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Use your GitHub token here or set it as an environment variable

# Headers for GitHub API authentication
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

# Streamlit UI setup
st.title("Publish Notebooks to GitHub")

# File upload widget
uploaded_file = st.file_uploader("Choose a Jupyter Notebook file", type="ipynb")

# Input for commit message
commit_message = st.text_input("Commit Message", "Publish Jupyter notebook")

# Check if file is uploaded
if uploaded_file is not None:
    notebook_content = uploaded_file.read()
    notebook_base64 = base64.b64encode(notebook_content).decode("utf-8")

    # GitHub API endpoint for creating a new file or updating an existing one
    create_file_url = f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/contents/{uploaded_file.name}"

    # Define the payload for creating/updating the file
    payload = {
        "message": commit_message,
        "content": notebook_base64,  # The notebook content encoded in base64
        "branch": "main",  # Branch to commit to (adjust if needed)
    }

    if st.button("Publish Notebook"):
        response = requests.put(create_file_url, headers=headers, json=payload)

        if response.status_code == 201:
            st.success("Notebook successfully published!")
        elif response.status_code == 200:
            st.success("Notebook successfully updated!")
        else:
            st.error(f"Failed to publish notebook. Status Code: {response.status_code}")
            st.error(response.text)
