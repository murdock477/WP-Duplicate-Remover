# WP-Duplicate-Remover
Simple bot with selenium that logs into wordpress admin and deletes duplicate items (requires duplicate remover plugin for wordpress).
To make sure bot works fine, create a JSON file called 'info' inside your folder and fill this template:
{
    "email": "FILLME",
    "password": "FILLME",
    "url": "FILLME",
    "url2": "FILLME"
}

url being your WP admin login screen and url2 being your duplicate remover plugin url.