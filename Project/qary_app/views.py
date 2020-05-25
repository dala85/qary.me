
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from . import models
from . models import Chat, Document
from qary_app import models
from rest_framework import generics
from qary_app.serializers import ChatSerializer
import sys
sys.path.append("..")
from qary.qary.skills import parul_bots, basebots, pattern_bots, search_fuzzy_bots, eliza_bots


# import sys
# sys.path.append("..")
# from qary.clibot import CLIBot
# from qary.skills import qa_bots, faq_bots, eliza_bots, pattern_bots, glossary_bots

# bot = CLIBot(bots=('glossary',))

# qa_bot = qa_bots.Bot()
# faq_bot = faq_bots.Bot()
# glossary_bot = glossary_bots.Bot()
# pattern_bot = pattern_bots.Bot()
# eliza_bot = eliza_bots.Bot()


parul_bot = parul_bots.Bot()
basebot = basebots.HiBot()
glossary_bot = parul_bots.Bot()
pattern_bot = pattern_bots.Bot()
search_fuzzy_bot = search_fuzzy_bots.Bot()
eliza_bot = eliza_bots.Bot()
qa_bot = parul_bots.Bot()

# rest_api


class API_objects(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


def team(request):

    return render(request, "team.html")


def nlpia(request):
    return render(request, "nlpia.html")


def home_view(request):

    obj = Chat.objects.all().order_by('-create_date')

    dict_1 = {'c': obj}

    return render(request, "bot.html", context=dict_1)


def reply(request):

    my_question = request.POST.get('question_req')
    # radio button logic
    if request.POST.get('parul_bot'):
        bot_reply = parul_bot.reply(request.POST.get('question_req'))
        # bot_reply = [('hi', 'how are you')]

    elif request.POST.get('basebot'):
        bot_reply = basebot.reply(request.POST.get('question_req'))

    elif request.POST.get('glossary_bot'):
        bot_reply = glossary_bot.reply(request.POST.get('question_req'))

    elif request.POST.get('pattern_bot'):
        bot_reply = pattern_bot.reply(request.POST.get('question_req'))

    elif request.POST.get('search_fuzzy_bot'):
        bot_reply = search_fuzzy_bot.reply(
            request.POST.get('question_req'))

    elif request.POST.get('eliza_bot'):
        bot_reply = eliza_bot.reply(request.POST.get('question_req'))

    elif request.POST.get('qa_bot'):
        bot_reply = qa_bot.reply(request.POST.get('question_req'))
    else:
        bot_reply = parul_bot.reply(request.POST.get('question_req'))

        # chat history
        #
    obj = Chat.objects.all().order_by('-create_date')
    document_obj = Document.objects.all()

    dict_1 = {'insert': bot_reply, 'Question': my_question,
              'c': obj, 'document_obj': document_obj}

    # Save data in the database
    if my_question and bot_reply:
        Chat.objects.create(question=my_question,
                            answer=bot_reply)

    return render(request, "bot.html", context=dict_1)


if __name__ == '__main__':
    main()
