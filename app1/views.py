
from django.shortcuts import render, redirect
from .models import UserProfile  # Import your UserProfile model


def registration_success(request):
    return render(request, 'registration_success.html')



def register(request):
    if request.method == 'POST':
        # Check if the required keys exist in the POST data
        if 'username' in request.POST and 'email' in request.POST and 'password' in request.POST and 'confirmPassword' in request.POST:
            # Retrieve form data from the request
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            confirm_password = request.POST['confirmPassword']

            # Check if passwords match
            if password == confirm_password:
                # Create a new UserProfile object and save it to the database
                user_profile = UserProfile(username=username, email=email)
                user_profile.set_password(password)  # Use set_password to securely hash the password
                user_profile.save()

                # Redirect to a success page after successful registration
                return redirect('registration_success')
            else:
                # Passwords don't match, handle the error as needed
                return render(request, 'register.html', {'error_message': 'Passwords do not match'})

    # Return a response in case the request is not a POST request or if the form data is missing
    return render(request, 'register.html')



