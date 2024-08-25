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


### 1. Clone the Repository


git clone https://github.com/shreyas7124/AccuKnox_Assignment.git
cd AccuKnox_Assignment

##create a virtual eniveronment
python -m venv myenv
## Activate it
myenv\Scripts\activate

## 2. Install Dependencies
pip install -r requirements.txt

##3.  Apply Migrations
python manage.py migrate

##4. Runserver
python manage.py runserver

##5. The API will be available at http://127.0.0.1:8000/

##6. 


### Prerequisites

1. **Docker**: Ensure Docker is installed on your system. You can download it from [Docker's official website](https://www.docker.com/products/docker-desktop).
2. **Docker Compose**: Docker Compose is included with Docker Desktop but ensure it is up-to-date.
3. **Git**: Make sure Git is installed to clone the repository.

### Clone the Repository

```bash
git clone https://github.com/your-username/AccuKnox_Assignment.git
cd AccuKnox_Assignment

docker-compose build
docker-compose up


