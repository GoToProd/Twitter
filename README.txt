For start project, you must doing this:

    python3 -m venv venv
    source venv/bin/activate

its code creating your virtual environment and activate him.
Then you must doing:

    pip3 install -r requirements.txt
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py createsuperuser 

(at now you will see text message "create user with name of your computer or any name:". Write in console "root", skip email, 
set any password (in develope i set password "1". Enter your password second time and after your must choice as "y" for accept easy
password and finish to create superuser))

After this command you can start project. For this you must use in terminal command:

    python3 manage.py runserver

Go to link in terminal (127.0.0.1:8000) and visite (127.0.0.1:8000/admin). After login you must create some posts(tweets),
and back to main page. 

Congratulation, you start my project!!! 