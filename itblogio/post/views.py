from django.shortcuts import render


def post_index(request):
    return render(request, 'post/index.html')


def post_detail(request, post_id):
    context = {
        "post_id": post_id,
    }
    return render(request, 'post/post_detail.html', context)
