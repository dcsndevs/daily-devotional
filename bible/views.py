from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
def bible(request):
    return HttpResponse('Hello World!')




def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            verse = form.cleaned_data['verse']
            
            # Make request to Bible API
            api_url = f'https://bible-api.com/{verse}'
            response = requests.get(api_url)
            if response.status_code == 200:
                passage = response.json()['text']
                return render(request, 'devotional/post_created.html', {'title': title, 'verse': verse, 'passage': passage})
    else:
        form = PostForm()
    return render(request, 'devotional/create_post.html', {'form': form})
