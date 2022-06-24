from django.core.mail import send_mail

def send(user_email):
    send_mail(
        'Тема тестового сообщения',
        "Текст сообщения для тестирования отправки сообщений.",
        'admin@mytestproject.website',
        [user_email],
    )