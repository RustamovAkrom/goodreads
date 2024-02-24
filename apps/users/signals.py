from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.users.models import User
from django.core.mail import send_mail
from config import settings

@receiver(post_save, sender=User)
def remove_from_inventory(sender, instance, created, **kwargs):
    if created:
        print("send email")
        send_mail(
            subject="welcome to goodreads clone site 👩‍🏫👨‍🏫🧑‍🏫🖐️🖐️🖐️",
            message="""Hi you Horse from Rustamov Akromjo's website royhat I hope you will make the most of this site""",
            from_email="akromjonrustamov56@gmail.com",
            recipient_list=[instance.email]
        )
