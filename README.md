# event_manager
: Event Manager

Overview

A FastAPI application deployed on EC2 using Docker. Deployment is automated using GitHub Actions.

Tech Stack

FastAPI

Docker

AWS EC2

GitHub Actions

Deployment Steps

Clone the repository:

git clone https://github.com/Yusufshaik19/event_manager.git

Create Docker image:

docker build -t event-manager-app .

Run Docker container:

docker run -d --name event-manager -p 5000:5000 event-manager-app

Automated Deployment:

GitHub Actions workflow automatically builds and deploys the latest version to the EC2 instance on every push.

Access:

Open EC2 security group for port 5000.

Access via: http://<EC2_PUBLIC_IP>:5000
