from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

from root import settings


def send_email_code(email: str, code: str, first_name: str):
    subject = 'Activate Email 😀'
    recipient = [email]
    # Define the HTML content
    html_content = """
           <html>
               <body>
                   <h1>Hi {first_name} !</h1>
                   <h3>Yur activate code 👇 <h1>{value}</h1></h3>
               </body>
           </html>
           """.format(value=code, first_name=first_name.title())

    # Create the text content by stripping HTML tags
    text_content = strip_tags(html_content)

    # Send the email
    email = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, recipient)
    email.attach_alternative(html_content, "text/html")
    email.send()
    print('send email')
