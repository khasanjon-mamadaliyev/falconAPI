from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

from root import settings


@shared_task
def send_email_code(email: str, code: int):
    subject = 'Activate Email 😀'
    recipient = [email]
    # Define the HTML content
    html_content = """
           <html>
               <body>
                   <h1>Hi !</h1>
                   <h3>Yur activate code 👇 <h1>{value}</h1></h3>
               </body>
           </html>
           """.format(value=code)

    # Create the text content by stripping HTML tags
    text_content = strip_tags(html_content)

    # Send the email
    email = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, recipient)
    email.attach_alternative(html_content, "text/html")
    email.send()
    print('send email')
