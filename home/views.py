from django.shortcuts import render
from . forms import *
from django.contrib import messages
from django.views import generic
from youtubesearchpython import VideosSearch

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST)
        text = request.POST['text']
        video = VideosSearch(text, limit=10)
        result_list = []
        for i in video.result()['result']:
            result_dict = {
                'input': text,
                'title':i['title'],
                'duration':i['duration'],
                'thumbnail':i['thumbnails'][0]['url'],
                'channel':i['channel']['name'],
                'link':i['link'],
                'views':i['viewCount']['short'],
                'published':i['publishedTime'],
            }
            desc = ''
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc += j['text']
            result_dict['description'] = desc
            result_list.append(result_dict)
            context = {
                'form':form,
                'results':result_list
            }
        return render(request, 'index.html',context)
    else:
       form = DashboardForm()
    context = {'form':form}
    return render(request, 'index.html', context)
