import requests
from openai import OpenAI
import os
import sys

client = OpenAI()
GITLAB_URL = os.getenv("GITLAB_URL")
GITLAB_PRIVATE_TOKEN = os.getenv("GITLAB_PRIVATE_TOKEN")
GITLAB_PROXY = os.getenv("GITLAB_PROXY")

proxies = {"http": GITLAB_PROXY, "https": GITLAB_PROXY}


def get_merge_request_changes(project_id, merge_request_id):
    api_endpoint = f"{GITLAB_URL}/api/v4/projects/{project_id}/merge_requests/{merge_request_id}/changes"

    headers = {"Authorization": f"Bearer {GITLAB_PRIVATE_TOKEN}"}

    response = requests.get(api_endpoint, headers=headers, proxies=proxies)

    if response.status_code == 200:
        changes = response.json()["changes"]
        changes_text = "\n\n".join([change["diff"] for change in changes])
        return changes_text
    else:
        print(f"Failed to fetch merge request changes: {response.status_code}")
        return ""


def review_code(prompt, code_snippet):
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[{"role": "user", "content": f"{prompt}\n\n{code_snippet}"}],
        temperature=1,
        max_tokens=3000,
    )
    return response.choices[0].message.content


def post_merge_request_comment(project_id, merge_request_id, comment):
    api_endpoint = f"{GITLAB_URL}/api/v4/projects/{project_id}/merge_requests/{merge_request_id}/notes"

    headers = {"PRIVATE-TOKEN": GITLAB_PRIVATE_TOKEN}
    data = {"body": comment}

    response = requests.post(api_endpoint, headers=headers, json=data, proxies=proxies)
    if response.status_code == 201:
        print("Comment posted successfully.")
    else:
        print(f"Failed to post comment: {response.status_code}")


def main(prompt):
    if len(sys.argv) != 3:
        print("Usage: review_script.py <project_id> <merge_request_id>")
        sys.exit(1)

    project_id = sys.argv[1]
    merge_request_id = sys.argv[2]
    changes = get_merge_request_changes(project_id, merge_request_id)
    if changes:
        if len(changes) > 3000:
            review = "changes too long, please invite your teammates to review."
        else:
            review = review_code(prompt, changes)
        print("Review Results:")
        print(review)
        post_merge_request_comment(project_id, merge_request_id, review)
    else:
        print("No changes to review.")
