import os
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from . import preprocessing

def home_page(request):
    return render(request, "search_handler_app/index.html")         


def view_documents(request):
    if request.method == 'POST':
        ranked = []
        try:
            files = preprocessing.PreProcessing()
            files.process()
            files.tokenize()
            files.stop_word_stem()
            files.vectorize()

            query = request.POST.get('query')
            print("query", query)

            ranked = files.rank_documents(query)
            ranked = [[rank[0], rank[1], os.path.join(settings.MEDIA_ROOT, rank[0])] for rank in ranked]
            print("ranked",ranked)
        except Exception as e:
            print(e)    

        return render(request, 'search_handler_app/result.html', {"ranked":ranked})
        
    else:
        return render(request, 'search_handler_app/index.html')

    