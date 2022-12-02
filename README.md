# Begginning-Django-Web-Application

## Set Up Content: Understand Urls, Templates, and Apps

apps are the middlewares between urls and templates
urls are the entry points to the content ,the url then connects to the view which is the business logic which then connects to a template to display data or the desired output

DJANGO WORKFLOW:

1. user request => url mapping  => view(business logic) => html templates
2. form data from templates => url mapping(post request to a specific url) => view(data processing and logic) => database(CRUD operations)

## Configure and Install the Django admin site docs App

To install the Django admin site documentation app, you first need to install the docutils Python package with the pip package manager executing the following command:
                 python3 -m pip install docutils
. Once you install the docutils package, you can proceed to install the Django admin site documentation app as any other Django app.
Add the url to access the Django admin site documentation app. If you open the project’s urls.py file, in the urlpatterns variable add the following line:
            1. path('admin/doc/', include('django.contrib.admindocs.urls'))
            2. in settings.py {installed apps add this}:
                    i. 'django.contrib.admindocs'
                    ii. 'docutils'

## Precedence Rule: Granular Urls First, Broad Urls Last

Django urls need to follow a certain order and syntax to work correctly. Broad url regular expressions should be declared last and only after more granular url regular expressions.This is because Django url regular expression matching doesn’t use short-circuiting behavior, like anested conditional statement (e.g., if/elif/elif/elif/else) where as soon as one condition is met, the remaining
options are ignored. In Django urls if there’s more than one matching regular expression for an incoming url request, it will be the top-most one’s action that gets triggered. Precedence for matching url regular expressions is given from top (i.e., first declared) to bottom (i.e., last declared).The more specific one should come first

Correct precedence for Django url regular expressions:
            urlpatterns = [
                url( r'^about/index/', TemplateView.as_view(template_name='index.html') ),
                url( r'^about/', TemplateView.as_view(template_name='about.html') ),
            ]

## REGULAR EXPRESSIONS

1. ^ (Start of url)
2. $ (End of url)
3. \ (Escape for interpreted values)
4. | (Or)
5. + (1 or more occurrences)
6. ? (0 or 1 occurrences)
7. {n} (n occurrences)
8. {n,m} (Between n and m occurrences)
9. [] (Character grouping)
10. (?P<name>___) (Capture occurrence that matches regexp___ and assign it to name
11. . (Any character)
12. \d+ (One or more digits). Note escape, without escape matches ‘d+’ literally.
13. \D+ (One or more non-digits).Note escape, without escape matches ‘D+’ literally]
14. [a-zA-Z0-9_]+ (One or more word characters,letter lower or uppercase,number, or underscore)
15. \w+ (One or more word characters, equivalent to [a-zA-Z0-9_]). Note escape, without escape matches ‘w+’ literally].
16. [-@\w]+ (One or more word character, dash. or at sign). Note no escape for \w since it’s enclosed in brackets (i.e., a grouping).

## REGULAR EXPRESSIONS DJANGO URLS EXAMPLES

1. url(r‘^$’,.....) => Empty string (Home Matches:page) => <http://127.0.0.1/>

2. url(r‘^stores/’,.....) => Any trailing characters Matches: =>
        i. <http://127.0.0.1/stores>
        ii. <http://127.0.0.1/stores>
        iii.<http://127.0.0.1/stores/long+string+with+anything+12345>

3. url(r‘^about/contact/$’,.....) => Exact, no trailing charaters Matches: => <http://127.0.0.1/about/contact/>

4. url(r‘^stores/\d+/’,..…) Number Matches:[ anything that start with store the a tailing number eg stores/1 ]
        i. <http://127.0.0.1/stores/2/>
        ii.<http://127.0.0.1/stores/34/>
        iii. Doesn’t match: <http://127.0.0.1/stores/downtown/>

5. url(r‘^drinks/\D+/’,.....) Non-digits Matches: <http://127.0.0.1/drinks/mocha>

6. url(r‘^drinks/mocha|espresso/’,.....) Word options,trailing characters . Matches:
        i. <http://127.0.0.1/drinks/mocha>
        ii. <http://127.0.0.1/drinks/mochaccino>
        iii. <http://127.0.0.1/drinks/expresso>

7. url(r‘^drinks/mocha$|espresso/$’,.....) Word options exact, no trailing characters Matches: <http://127.0.0.1/drinks/mocha> . Doesn’t match: <http://127.0.0.1/drinks/mochaccino>

8. url(r‘^stores/\w+/’,.....) Word characters (Any letter lower or uppercase,number or underscore) Matches: Doesn’t match: <http://127.0.0.1/san-diego/>
        i. <http://127.0.0.1/stores/sandiego>
        ii. <http://127.0.0.1/stores/1/>
        iii.<http://127.0.0.1/stores/LA/>

9. url(r‘^stores/[-\w]+/’,.....) Word characters or dash Matches: <http://127.0.0.1/san-diego/>
10. url(r‘^state/[A-Z]{2}/’,.....) Two uppercase letters Matches:<http://127.0.0.1/CA/> does not match <http://127.0.0.1/Ca/>

## Namespaces and names

<a href="{% url 'coffee-banners:index' %}">Coffee banners</a>
coffee-banners=> namespace (at the root in include('app.urls'))
index => name(at the url (name=index))

## View Method Requests

View Method Responses

The render() method to generate view method responses you’ve used up to this point is actually a shortcut. You can see toward the top of Listing 2-21, the render() method is part of the django.shortcuts package.

This means there are other alternatives to the render() method to generate a view response, albeit the render() method is the most common technique. For starters, there are three similar variations to generate view method responses with data backed by a template, as illustrated in Listing 2-22.

Django view method response alternatives

1. Option 1) from django.shortcuts import render
from django.shortcuts import render

def detail(request,store_id='1',location=None):
        return render(request,'stores/detail.html', values_for_template)
2. Option 2) from django.template.response import TemplateResponse
from django.template.response import TemplateResponse

def detail(request,store_id='1',location=None):
        return TemplateResponse(request, 'stores/detail.html', values_for_template)
3. Option 3) from django.http import HttpResponse from django.template import loader, Context
from django.http import HttpResponse
from django.template import loader, Context

def detail(request,store_id='1',location=None):
        response = HttpResponse()
        t = loader.get_template('stores/detail.html')
        c = Context(values_for_template) return response.write(t.render(c))

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

The request parameter is an instance of django.http.requet.HttpRequest class
The request object has information set by entities present before a view method:

## ALTERING HTTP RESPONSE

return render(request,'stores/menu.csv', values_for_template, content_type='text/plain')

return render(request,'custom/notfound.html',status=404)

return render(request,'custom/internalerror.html',status=500)

return render(request,'stores/menu.json', values_for_template, content_type='application/json')

## STATUS CODES

404 = not found ::when a page is not found
500 = internal server error ::when an error is thrown in the view
400 = bad request ::unknown operations
403 = forbidden ::permissions

1. 404 (Not Found)
        from django.http import Http404
        raise Http404
2. 500 (Internal Server Error)
        raise Exception
3. 400 (Bad Request)
        from django.core.exceptions import SuspiciousOperation
        raise SuspiciousOperation
4. 403 (Forbidden)
        from django.core.exceptions import PermissionDenied
        raise PermissionDenied

## PAGES FOR STATUS CODES
403.html
500.html
this templates shoul be at the base template folder
this status code templates only work if DEBUG = False

Override built-in Django HTTP Status view methods in urls.py

## Overrides the default 400 handler django.views.defaults.bad_request

handler400 = 'coffeehouse.utils.views.bad_request'

## Overrides the default 403 handler django.views.defaults.permission_denied

handler403 = 'coffeehouse.utils.views.permission_denied'

## Overrides the default 404 handler django.views.defaults.page_not_found

handler404 = 'coffeehouse.utils.views.page_not_found'

## Overrides the default 500 handler django.views.defaults.server_error

handler500 = 'coffeehouse.utils.views.server_error'

## Custom views to override built-in Django HTTP view methods

from django.shortcuts import render

def page_not_found(request):
        // Dict to pass to template, data could come from DB query values_for_template = {} return render(request,'404.html',values_for_template,status=404)

def server_error(request):
        // Dict to pass to template, data could come from DB query values_for_template = {} return render(request,'500.html',values_for_template,status=500)

def bad_request(request):
        // Dict to pass to template, data could come from DB query values_for_template = {} return render(request,'400.html',values_for_template,status=400)

def permission_denied(request):
        // Dict to pass to template, data could come from DB query values_for_template = {} return render(request,'403.html',values_for_template,status=403)
