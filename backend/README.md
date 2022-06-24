
# Introduction 
Push insights is an application that presents information on key results to the relevant users in a timely manner. This information is presented to the user as dashboards/reports.

Beyond presenting the user with the information Push Insights also sends notifications to users based on either threshold or scheduled events. These notifications are sent either via:

    Push messages
    Email
    Other messaging platforms

Push Insights is also used to increase engagement. The application presents users with data capture forms for collection of:

    Survey information
    KPI tracking data

<!-- # Getting Started
1.	Clone Repository
2.	Create & Activate Python Virtual Environment 
    - [Python Virtual Environments](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)
3.	Install requirements ( run command - pip install -r requirements.txt in project in terminal)
4.	Run Migrations - python manage.py makemigrations - python manage.py migrate
5.  Run server - python manage.py runserver -->


# Getting Started With Docker
1. Recommended Python Development Environment includes
        OS: Linux (Ubuntu) or WSL2 with Ubuntu18.04 LTS (If on Windows)
        IDE: Visual Studio Code
        Python frameworks: Django

2. To set it up please follow the instructions in the link below
 - https://dev.azure.com/Scaleworks/Push%20Insights/_wiki/wikis/Push-Insights.wiki/14/Python-Development-Environment

3. To set up docker

    -Requirements:
        1. A linux/Mac-os/WSL environment
        2. A stable internet connection
        3. 450MB - 500MB of data(required only during first time)
    -For Linux users
        1. A working installation of Docker/Docker-engine
        2. A working installation of docker-compose
    -For Mac or Windows users
        1. A working installation of Docker Desktop(Docker Hub) or a working global installation of docker and docker-compose

    - Link for docker installation:
        https://docs.docker.com/get-docker/ 

    -  Link for docker-compose installation:
        https://docs.docker.com/compose/install/ 

    A development docker container config and yaml code has been written up for us to use during development.

        - Main feature:
        1. Hot Reload -on save
        - Requirements:
        1. Docker
        2. docker-compose
    - Setup Steps:
        1. Clone the the repo
        - git clone https://Scaleworks@dev.azure.com/Scaleworks/Push%20Insights/_git/Push%20Insights
        2. Move into the project root directory
        - cd Push%20Insights
        3. Ensure you have docker and docker-compose installed
        - docker --version
        - docker-compose --version
        4. Move to the back-end directory
        - cd backend
        PS: For those on WSL, run the command below before moving to step 5
        - sudo service docker start 
        5. Run the following command
        - docker-compose -f docker-compose-dev.yaml up --build
        6. Open another terminal, cd into backend and make migrations with the following command
        - docker-compose -f docker-compose-dev.yaml exec app python manage.py makemigrations

PS: You can use the command below to execute other things like migrate
docker-compose -f docker-compose-dev.yaml exec app YOUR_COMMAND
EG: docker-compose -f docker-compose-dev.yaml exec app python manage.py migrate
When done with development use the following command
docker-compose -f docker-compose-dev.yaml down -v

To access the development back-end API docker container instance please use the following url:
- http://localhost:8000 

