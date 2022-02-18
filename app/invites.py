import requests
from starlette import status

from app.config import settings
from app.validator import is_valid_email

INVITES_URL = f'https://api.github.com/orgs/{settings.ORG_NAME}/invitations'


class GitHub:
    def __init__(self):
        self.emails = []
        self.headers = {'Authorization': 'token %s' % settings.GITHUB_TOKEN, 'Accept': 'application/vnd.github.v3+json'}

    def create_invite(self, email):
        if not is_valid_email(email) or email in self.emails:
            return False

        r = requests.post(INVITES_URL, headers=self.headers, data='{"email": "%s"}' % email)
        if r.status_code == status.HTTP_201_CREATED:
            self.emails.append(email)
        return r
