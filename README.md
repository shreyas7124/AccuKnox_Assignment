# AccuKnox_Assignment
API for social networking application using Django REST Framework with Postman

# Social Network Project

## Overview

A Django-based social networking application featuring user registration, login, friend requests, and user search
- User registration and authentication
- Search users by email
- Send, accept, and reject friend requests
- List friends and pending friend requests
  
## Installation Steps

### Prerequisites

1. **Docker**: Ensure Docker is installed on your system. 
2. **Docker Compose**
3. **Git**


### 1. Clone the Repository


git clone https://github.com/shreyas7124/AccuKnox_Assignment.git
cd AccuKnox_Assignment

##create a virtual eniveronment
python -m venv myenv


## Activate the Virtual Environment
On Windows:
myenv\Scripts\activate

On macOS/Linux:
source myenv/bin/activate

## 2. Install Dependencies
pip install -r requirements.txt

##3.  Apply Migrations
python manage.py migrate

##4. Runserver
python manage.py runserver

##5. The API will be available at http://127.0.0.1:8000/

##6. Postman Collection

A Postman collection for testing the API endpoints is included in this repository.


### Importing the Collection

1. Open Postman.
2. Click on `Import`.
3. Select the `Choose Files` tab.
4. Upload the `Social Network API.postman_collection.json` file from this repository.
5. The collection will be available for use with pre-configured requests.
6. Thare various users created such as an example user:shreyas, email:shreyas@4.com, password:storm and other user is user:amar, email:amar@example.com, password:password123 (For testing purpose)

Endpoints
Signup: http://127.0.0.1:8000/api/signup/
Login: http://127.0.0.1:8000/api/login/
Profile: http://127.0.0.1:8000/api/profile/
Friend Request: http://127.0.0.1:8000/api/friend-request/
Search Users: http://127.0.0.1:8000/api/search/
Respond to Friend Request: http://127.0.0.1:8000/api/friend-respond/
Friend List: http://127.0.0.1:8000/api/friend-list/
Pending Requests: http://127.0.0.1:8000/api/pending-requests/

Feel free to adapt the provided information based on your specific project requirements and repository structure.



For questions, please contact Shreyas Shivakumar at shreyas.sys12@gmail.com




