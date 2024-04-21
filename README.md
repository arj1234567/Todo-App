#Todo App


This is a simple Todo application built using Django framework. It allows users to register, log in, add projects, add tasks to projects, mark tasks as completed, and view project details.


##Features


   User authentication: Users can register an account and log in securely.
   
   Project management: Users can add projects with titles and descriptions.
   
   Task management: Users can add tasks to projects, mark tasks as completed, and view project details.
   
   Session management: User sessions are maintained securely throughout the application.
  
##Installation
  Navigate into the project directory:
  Install dependencies using pip:pip install django
  Apply database migrations:python manage.py makemigrations and then python manage.py migrate
  Run the development server:python manage.py runserver
  Access the application at http://localhost:8000/ in your web browser.
Usage
  Register an account or log in if you already have one.
  Once logged in, you will be directed to the homepage where you can view your existing projects or add new ones.
  Click on a project to view its details, add tasks, mark tasks as completed, etc.
  Log out when you're done.
