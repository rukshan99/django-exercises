from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

articles = {
    'sports': "Sports Page",
    'finance': 'Finance Page',
    'politics': 'Politics page'
}

def news_view(request, topic):
    try:
        article = articles[topic]
        return HttpResponse(article)
    except:
        message = 'GENERIC 404'
        raise Http404(message)


def num_page_view(request, num_page):
    topic_list = list(articles.keys())
    try:
        topic = topic_list[num_page]
        return HttpResponseRedirect(reverse('news_view', args=[topic]))
    except:
        message = 'GENERIC 404'
        raise Http404(message)


def add_view(request, num1, num2):
    result = f'{num1} + {num2} = {num1+num2}'
    return HttpResponse(result)


def simple_template_view(request):
    return render(request=request, template_name='first_app/example.html')
