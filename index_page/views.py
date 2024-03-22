from django.shortcuts import render, redirect
from django.http import Http404
from django.template.loader import get_template
from .forms import ContactForm, SubscriptionForm
from django.core.mail import EmailMultiAlternatives
from .models import IndexContent, Comments, Events, Services, DopFieldsIndex


def feedback(name, mail, message):
    text = get_template('index_page/message.html')
    context = {'name': name, 'mail': mail, 'message': message}
    subject = "Форма зворотнтого зв'язку your-support.com.ua"
    from_email = 'admin@your-support.com.ua'
    text_content = text.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['dagilevsasa@gmail.com'])
    msg.send()


def index(request):
    success_post = False
    success_subscription = False
    index_content = IndexContent.objects.all()
    for index_con in index_content:
        index_con.dop_fields = index_con.dopfieldsindex_set.all()

    if request.method == 'POST':

        subscriptionform = SubscriptionForm(request.POST)
        feedbackform = ContactForm(request.POST)

        if feedbackform.is_valid():
            name = feedbackform.cleaned_data['name']
            sender = feedbackform.cleaned_data['sender']
            message = feedbackform.cleaned_data['message']
            feedback(name, sender, message)

            # Custom flag. The operation is successful
            success_post = True

        if subscriptionform.is_valid():
            subscriptionform.save()


            # Custom flag. The operation is successful
            success_subscription = True
    else:
        feedbackform = ContactForm()
        subscriptionform = SubscriptionForm()

    dopfieldsindex = DopFieldsIndex.objects.all()
    comments = Comments.objects.filter(status='PB')
    events = Events.objects.filter(status='PB')
    services = Services.objects.filter(status='PB')

    return render(request, 'index_page/index.html', {
        'index_content': index_content,
        'dopfields': dopfieldsindex,
        'comments': comments,
        'events': events,
        'services': services,
        'feedbackform': feedbackform,
        'success_post': success_post,
        'subscriptionform': subscriptionform,
        'success_subscription': success_subscription,
    })


def customPermissionDenied(request, exception):
    return render(request, 'index_page/403.html', status=403)


def pageNotFound(request, exception):
    return render(request, 'index_page/404.html', status=404)


def customError(request):
    return render(request, 'index_page/500.html', status=500)

