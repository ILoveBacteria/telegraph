from django.shortcuts import render


def conversations(request):
    return render(request, 'chat/conversations.html', {'title': 'Chats'})
