from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import JsonResponse, Http404
from .models import Menu, MenuPage, Home, About, Contact, ContactPage, Category, OpenHours
from .forms import ContactForm
from django.utils.translation import gettext_lazy as _


def home(request):
    # Getting Current Language Code
    lang_code = request.LANGUAGE_CODE

    # Getting the story from the database
    our_story = About.objects.translate(lang_code).first()
    our_story_is_2long = False

    # Check the our story length. we want make length displayed on home page to be 600 chars
    if our_story is not None:
        if len(our_story.about) > 600:
            our_story = our_story[:600]
            our_story_is_2long = True
        else:
            our_story = our_story.about

    # Context that is sent to the template
    context = {
        'menu': Menu.objects.exclude(feature=False)[0:3],
        'home': Home.objects.translate(lang=lang_code).first(),
        'open_hrs': OpenHours.objects.all(),
        'our_story': our_story,
        'our_story_2long': our_story_is_2long
    }
    return render(request, 'mySite/minHTML/home.html', context)


def menu(request):
    # Getting Current Language Code
    lang_code = request.LANGUAGE_CODE
    print(Category.objects.all())
    # Context that is sent to the template
    context = {
        'page': MenuPage.objects.translate(lang_code).first(),
        'menu': Menu.objects.translate(lang_code).all(),
        'categories': Category.objects.translate(lang_code).order_by('display_order').all()
    }
    return render(request, 'mySite/minHTML/menu.html', context)


def about(request):
    # Getting Current Language Code
    lang_code = request.LANGUAGE_CODE

    # Context that is sent to the template
    context = {
        'page': About.objects.translate(lang_code).first()
    }
    return render(request, 'mySite/minHTML/about.html', context)


def contact(request):
    # Getting Current Language Code
    lang_code = request.LANGUAGE_CODE
    # Initializing the form
    form = ContactForm()
    # Context that is sent to the template
    context = {
        'form': form,
        'page': ContactPage.objects.translate(lang_code).first(),
        'contact': Contact.objects.values_list('phone').first()[0]
    }
    return render(request, 'mySite/minHTML/contact.html', context)


def send_email(request):
    # Validating request type and form
    if request.is_ajax() and request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Getting form field inputs from the request
            name = request.POST.get('name')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            from_email = request.POST.get('email')
            # Getting the contact email from the database
            to_email = Contact.objects.values_list('email').first()[0]
            # Constructing the email body
            email_body = f"İsim: {name}\n" \
                         f"Gönderen İmeil: {from_email}\n" \
                         f"Mesaj: \n\n {message}"

            # Sending email + error handling
            try:
                send_mail(
                    subject,
                    email_body,
                    from_email,
                    [to_email],
                    fail_silently=False,
                )
            except BadHeaderError:
                return JsonResponse({'success': False,
                                     'message': _("Couldn't send message for the following error(s):"),
                                     'errors': _('Invalid header found.'),
                                     'msg_color': 'error'})
            except Exception as e:
                print(e)
                return JsonResponse({'success': False,
                                     'message': _("Couldn't send message for the following error(s):"),
                                     'errors': _('Email server down. Please try again later or give us a call.'),
                                     'msg_color': 'error'})

            response = {'success': True,
                        'message': _('Successfully Sent!'),
                        'msg_color': 'success'}
        else:
            print(form.errors)
            response = {'success': False,
                        'message': _("Couldn't send message for the following error(s):"),
                        'errors': str(form.errors),
                        'msg_color': 'error'}
        return JsonResponse(response)
    else:
        return Http404



