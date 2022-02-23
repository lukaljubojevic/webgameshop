from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from trgovina.models import Kupac
from django.views import View
  
  
class Login(View):
    return_url = None
  
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')
  
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('lozinka')
        kupac = Kupac.get_customer_by_email(email)
        error_message = None
        if kupac:
            flag = check_password(password, kupac.lozinka)
            if flag:
                request.session['kupac'] = kupac.id
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = 'Krivi podaci za prijavu'
        else:
            error_message = 'Krivi podaci za prijavu'
  
        print(email, password)
        return render(request, 'login.html', {'error': error_message})
  
  
def logout(request):
    request.session.clear()
    return redirect('login')