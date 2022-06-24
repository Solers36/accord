from accord.celery import app
from .service import send
#from .models import Contact


@app.task
def send_register_email(user_email):
    send(user_email)
