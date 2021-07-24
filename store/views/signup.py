from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('first_name')
        last_name = postData.get('last_name')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        confirm_password = postData.get('confirm_password')
        # validation
        value = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,

        }
        error_message = None
        customer = Customer(first_name=first_name,
        last_name=last_name,
        phone =phone,
        email =email,
        password =password,
        confirm_password =confirm_password)

        error_message = None
        if not customer.first_name:
            error_message = "First Name Required!!"
        elif len(customer.first_name) < 3:
            error_message = "First Name Must be 3  Character"
        elif not customer.last_name:
            error_message = "Last Name Required!!!"
        elif len(customer.last_name) < 4:
            error_message = "Last Name must be 4 Character!!"
        elif not customer.phone:
            error_message = "Phone Number Required"
        elif len(customer.phone) < 10:
            error_message = "Phone Number must be 10 Digits"
        elif not customer.password:
            error_message = "Password Required"
        elif len(customer.password) < 6:
            error_message = " Password must be 6 Character !!"
        elif not customer.confirm_password:
            error_message = "Password Required"
        elif not (customer.password == customer.confirm_password):
            error_message = "Passwords are not same.Please Re-enter Password!!"
        elif customer.isExits():
            error_message = " Email Address already Registered!!!"

        if not error_message:
            customer.password = make_password(customer.password)
            customer.confirm_password = make_password(customer.confirm_password)
            customer.register()
            return redirect('login_page')
        else:
            data = {'error': error_message,'values': value}

        return render(request, 'signup.html', data)