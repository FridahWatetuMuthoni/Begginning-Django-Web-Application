from django.shortcuts import render

# Create your views here.


def home(request):
    print(request.method)  # request method
    print(request.META['REMOTE_ADDR'])  # the address
    print(request.META['HTTP_COOKIE'])  # session id and csrf token
    # current user {it can either be current user or anonymousUser}
    print(request.user.username)
    print(request.user.email)
    # get values of a post request
    if request.method == 'POST':
        # gets the value of name and returns None is the value is not found
        name = request.POST.get('name', default=None)
    # getting parameters passed to the url using the get request
    name_parameter = request.GET.get('name', None)
    email_parameter = request.GET.get('email', None)
    print(name_parameter, email_parameter)
    # The render arguements:
    #  required=> request, template
    # optional=> context, Content-Type,status,template engine
    return render(request, 'home.html')
