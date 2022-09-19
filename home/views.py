from django.shortcuts import render
from django.views import View
from .utils import send_email
import os
from django.contrib import messages


class ContactView(View):
    def post(self, request):
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["msg"]
        content = f"""
            Sender: {name}<br><br>
            Sender's email address: {email}<br><br>
            Message:<br><br>
            {message}
        """
        subject = f"New message from {name}"
        receiver = os.getenv("ADMIN_EMAIL")

        if not name or not email or not message:
            messages.error(request, "Couldn't send the email, please make sure you filled all the required inputs and try again...")

            return render(request, 'index.html')       
        
        try:

            send_email(
                receiver,
                subject,
                content
            )

            messages.success(request, "Your message has been sent successfully!")
            
            return render(request, 'index.html')
            
        except:
            messages.error(request, "Couldn't send the email, please make sure you filled all the required inputs and try again...")
