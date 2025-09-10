from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406348540',
        'name': 'Rasyad Zulham Rabani',
        'app': 'Luluorange',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
