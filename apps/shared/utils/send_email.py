from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

from root.settings_email import EMAIL_HOST_USER


def send_email_code(email: str, code: str):
    subject = 'Activate Email 😀'
    recipient = [email]
    # Define the HTML content
    html_content = """
           <html>
               <body>
                   <h1>Your verify code 👇</h1>
                   <p>Yur activate code: {value}</p>
               </body>
           </html>
           """.format(value=code)
    # Create the text content by stripping HTML tags
    text_content = strip_tags(html_content)

    # Send the email
    email = EmailMultiAlternatives(subject, text_content, EMAIL_HOST_USER, recipient)
    email.attach_alternative(html_content, "text/html")
    email.send()
    print('send email')
