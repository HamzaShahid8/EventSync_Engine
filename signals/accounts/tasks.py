from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(email, username):
    subject = f'Welcome {username}! to our platform'
    message = f"Hi {username},\n\nThank you for registering on our platform. We're excited to have you on board!\n\nBest regards,\nThe Team"
    
    send_mail(
        subject,
        message,
        None,
        [email],
        fail_silently=False,
    )
    
    return f"Welcome email sent to {email}"