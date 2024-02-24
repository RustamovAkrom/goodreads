from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.books.models import BookReview
from django.core.mail import send_mail

@receiver(post_save, sender=BookReview)
def remove_from_inventory(sender, instance, created, **kwargs):
    if created:
        emails = []
        for email in instance.book.authors.all():
            emails.append(email.email)
        print(instance.book.title)
        print(instance.user.username)
        print(instance.body)
        print(instance.user.email)
        print(instance.book.authors.all())
        print(emails)
        send_mail(
                subject=f"{instance.user.username} is writing is your book <{instance.book.title}> ",
                message=f"""
Message:{instance.body}\n\t
Book Reating : {instance.rating}
""",
                from_email=instance.user.email,
                recipient_list=emails
            )
        # except:
        #     print("SMTP error in send email !!!!!!!!!!!!")
