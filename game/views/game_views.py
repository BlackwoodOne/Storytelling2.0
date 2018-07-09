from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse , HttpResponseRedirect
from django.views import View
from ..models import Game , Player, PlayerName, RoundState, GameState, WordCard, Sentence
from ..forms import UserNameForm, AddWordCardsForm, AddSentenceForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404
from django.contrib import messages
from django.contrib.messages import get_messages
import random, json
from asgiref.sync import async_to_sync
import channels

def getGameObj(game_code):
    game_inst = get_object_or_404(Game, pk=game_code)
    return game_inst

def getPlayerObj(request):
    playerID = request.session.get('playerID')
    if(playerID != 0):
        player_inst = get_object_or_404(Player, pk=playerID)
        return player_inst
    else:
        return None

def checkPlayerInGame(request,pk):
    if(request.session.get('gameID') != pk):
        print('been here')
        return False
    return True

class GameListView(ListView):
    model = Game
    template_name = "game/game_list.html"
    paginate_by = 20
    context_object_name = "game_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(GameListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(GameListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(GameListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(GameListView, self).get_queryset()

    def get_allow_empty(self):
        return super(GameListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(GameListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(GameListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(GameListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(GameListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(GameListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(GameListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GameListView, self).get_template_names()


class GameDetailView(DetailView):
    model = Game
    template_name = "game/game_detail.html"
    context_object_name = "game"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(GameDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(GameDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(GameDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(GameDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(GameDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(GameDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(GameDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(GameDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(GameDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GameDetailView, self).get_template_names()


class GameLobbyView(View):
    model = Game
    template_name = "game/game_lobby.html"
    context_object_name = "game"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def get(self, request, pk):
        if not(checkPlayerInGame(request,pk)):
            return HttpResponse("You are not part of this game.")
        if(getPlayerObj(request) == None):
            return HttpResponse("You are not part of this game.")

        game_inst = getGameObj(pk)
        if(game_inst.players == game_inst.maxPlayers):
            gameState = get_object_or_404(GameState, name="collectingwords")
            game_inst.playerState = gameState
            game_inst.save()

        player_list = Player.objects.filter(game=game_inst)
        context = {'game': game_inst, 'player_list': player_list, 'playerNames': json.dumps([p.name for p in player_list])}
        # redirect to a new URL:
        return render(request, 'game/game_lobby.html', context)



class GamePlayCollectView(View):

    def get(self, request, pk):
        if not(checkPlayerInGame(request,pk)):
            return HttpResponse("You are not part of this game.")
        player_inst = getPlayerObj(request)
        if (player_inst == None):
            return HttpResponse("You are not part of this game.")

        game_inst = get_object_or_404(Game, pk=pk)
        player_list = Player.objects.filter(game=game_inst)
        form = AddWordCardsForm(initial={})
        context = {'game': game_inst, 'player_list': player_list,'form':form}

        word_cards = WordCard.objects.filter(game=game_inst)
        context['wordCards'] = [str(x) for x in word_cards]

        readyState = get_object_or_404(GameState, name="ready")
        if(player_inst.playerState != readyState):
            playerState = get_object_or_404(GameState, name="collectingwords")
            player_inst.playerState = playerState
            player_inst.save()
        else:
            context['proceed']=True

        return render(request, 'game/play_collect.html', context)

    def post(self,request, pk):
        game_inst =getGameObj(pk)
        player_inst = getPlayerObj(request)
        if (player_inst == None):
            return HttpResponse("You are not part of this game.")

        # Check if the form is valid:
        form = AddWordCardsForm(request.POST)
        if form.is_valid():
            gameReady = False
            words_arr = form.clean_word_collection().split()
            if(len(words_arr) < (game_inst.maxRounds/game_inst.maxPlayers)):
                # todo also check if already enough words present, not just this submit
                word_cards = WordCard.objects.filter(game=game_inst)
                error_message = "Not enough words entered, enter at least " + str(int((game_inst.maxRounds / game_inst.maxPlayers) + 0.5)) + " words."
                # print(word_cards)
                # print(list(word_cards))
                
                word_cards = [str(x) for x in word_cards]

                return render(request, 'game/play_collect.html',{'form': form, 'game': game_inst, 'error_message': error_message, 'wordCards': word_cards})
            else:
                for word in words_arr:
                    newWord = WordCard(content=word,deckNumber=0,game=game_inst,createdBy=player_inst)
                    newWord.save()

                # Send words to room group
                channel_layer = channels.layers.get_channel_layer()
                channel_name = 'game_collect_%s' % game_inst.game_code
                print(channel_name)
                async_to_sync(channel_layer.group_send)(
                    channel_name,
                    {
                        'type': 'game_newWords',
                        'new_words': words_arr
                    }
                )

                #Set Playerstate ready
                readyState = get_object_or_404(GameState, name="ready")

                player_inst.playerState = readyState
                player_inst.save()

                #Check Game State to be Ready
                player_list = Player.objects.filter(game=game_inst)
                readyPlayers = 0
                for player in player_list:
                     if(player.playerState == readyState):
                         readyPlayers = readyPlayers +1

                if(readyPlayers == game_inst.players):
                    game_inst.gameState = readyState
                    game_inst.save()
                    gameReady = True

                if(gameReady):
                    success_message = "All your words have been added. Please proceed to the game."
                else:
                    success_message = "All your words have been added. Please wait for the other players."

                word_cards = WordCard.objects.filter(game=game_inst)
                word_cards = [str(x) for x in word_cards]
                return render(request, 'game/play_collect.html', {'form': form, 'game': game_inst, 'word_list':words_arr, 'error_message':success_message, 'messagetype':1, 'proceed':True, 'gameReady':gameReady, 'wordCards': word_cards})
                #return HttpResponseRedirect(reverse("game:play_collect", args=[pk]))
        else:
            #how can this happen?
            word_cards = WordCard.objects.filter(game=game_inst)
            word_cards = [str(x) for x in word_cards]
            return render(request, 'game/play_collect.html', {'form': form, 'game': game_inst,'wordCards': word_cards})


class GamePlayWaitView(View):

    def get(self, request, pk):
        game_inst = getGameObj(pk)



        player_inst = getPlayerObj(request)
        if (player_inst == None):
            return HttpResponse("You are not part of this game.")



        form = AddWordCardsForm(initial={})
        player_list = Player.objects.filter(game=game_inst)

        context = {'game': game_inst, 'player_list': player_list, 'form': form}
        context['proceed'] = False


        player_list = Player.objects.filter(game=game_inst).all()
        foundWhoPlay = False
        for player in player_list:
            if (player.playing == 1) and (player_inst.id!=player.id):
                foundWhoPlay = True

        if (foundWhoPlay == False):
            player_inst.playing = 1
        else:
            player_inst.playing = 0
        player_inst.save()



        return render(request, 'game/play_wait.html',context)

    def post(self,request, pk):
        game_inst = getGameObj(pk)
        player_inst = getPlayerObj(request)
        if (player_inst == None):
            return HttpResponse("You are not part of this game.")
       # Sentence.objects.filter(game=game_inst).all().delete()


        player_list = Player.objects.filter(game=game_inst).all()
        foundWhoPlay = False
        for player in player_list:
            if (player.playing == 1) and (player_inst.id != player.id):
                foundWhoPlay = True

        if (foundWhoPlay == False):
            player_inst.playing = 1
        else:
            player_inst.playing = 0
        player_inst.save()


        allWords = list(WordCard.objects.filter(game=game_inst).all())
        for i in range(0, int(game_inst.maxRounds / game_inst.maxPlayers)):
            if (len(allWords) > 0):
                word = allWords.pop(random.randint(0, (len(allWords)-1) ))
                newWord = WordCard(content=word.content, deckNumber=0, game=game_inst,createdBy=word.createdBy, onPlayerHand=player_inst)
                newWord.save()
                WordCard.objects.filter(id=word.id).delete()

        form = AddWordCardsForm(initial={})
        player_list = Player.objects.filter(game=game_inst)

        context = {'game': game_inst, 'player_list': player_list, 'form': form}
        context['proceed'] = True
        return render(request, 'game/play_wait.html', context)


class GamePlayGroundView(View):

    def get(self, request, pk):
        game_inst = get_object_or_404(Game, pk=pk)
        context = {'game': game_inst}

        player_inst = getPlayerObj(request)
        if (player_inst == None):
            return HttpResponse("You are not part of this game.")

        player_list = Player.objects.filter(game=game_inst)
        context['player_list'] = player_list

        # 0- ready
        # 1- play
        # 2- nie ma
        # 3- pending
        # 4- play Done
        # 5 nie ma
        # 6 pending Done
        if (player_inst.playing == 0):
            State = "ready"

            foundWhoPost = False
            for player in player_list:
                if (player.playing == 4):
                    foundWhoPost = True

            if (foundWhoPost == True):
                player_inst.playing = 3
                player_inst.save()


        elif (player_inst.playing == 1):
            State = "play"
        elif (player_inst.playing == 3):
            State = "pending"
        elif (player_inst.playing == 4):
            State = "ready"
        elif (player_inst.playing == 6):
            State = "ready"
            foundAllReady = True
            countAll = 0
            countDone = 0

            for player in player_list:
                countAll=countAll+1
                if (player.playing == 6):
                    countDone=countDone+1

            if(countAll-countDone>2):
                    foundAllReady = False
            for player in player_list:
                if (player.playing != 6) and (player.playing != 4):
                    foundAllReady = False
            foundID = False
            if (foundAllReady == True):
                for player in player_list:
                    if (player.playing == 4):
                        player.playing = 0
                        lastPlayID = player.id
                        foundID=True
                        player.save()

                if foundID==True:
                    foundMax = False
                    for player in player_list:
                        if (lastPlayID < player.id):
                            foundMax=True
                            player.playing = 1
                            player.save()
                            break

                    if foundMax==False:
                        lastPlayID=100000000000
                        for player in player_list:
                            if (lastPlayID > player.id):
                                lastPlayID = player.id
                        for player in player_list:
                            if (player.id==lastPlayID):
                                player.playing = 1
                                player.save()
                                break
                else:
                    lastPlayID = 100000000000
                    for player in player_list:
                        if (lastPlayID > player.id):
                            lastPlayID = player.id
                    for player in player_list:
                        if (player.id == lastPlayID):
                            player.playing = 1
                            player.save()
                            break

        error_message = "0"
        context['State'] = State
        #context['error_message'] = error_message

        playerWords = []
        allWords = list(WordCard.objects.filter(game=game_inst, onPlayerHand=player_inst).all())
        for i in range(0, 4):
            if (len(allWords) > 0):
                playerWords.append(allWords.pop())

        word_cards = playerWords
        context['wordCards'] = word_cards

        form = AddSentenceForm(initial={})
        context['form'] = form



        sentence_list = Sentence.objects.filter(game=game_inst)
        context['sentence_list'] = sentence_list

        return render(request, 'game/play_ground.html', context)





    def post(self,request, pk):

        game_inst =getGameObj(pk)
        context = {'game': game_inst}
        player_inst = getPlayerObj(request)
        if (player_inst == None):
            return HttpResponse("You are not part of this game.")


        player_list = Player.objects.filter(game=game_inst)
        context['player_list'] = player_list

        form = AddSentenceForm(request.POST)
        context['form'] = form




        if (player_inst.playing == 0):
            State = "ready"
            context['State'] = State
        # Sentence.objects.filter(game=game_inst).all().delete()

            success_message = "Your ready now."
            context['error_message'] = success_message

            context['messagetype'] = 1

            sentence_list = Sentence.objects.filter(game=game_inst)
            context['sentence_list'] = sentence_list

            playerWords = []
            allWords = list(WordCard.objects.filter(game=game_inst, onPlayerHand=player_inst).all())
            for i in range(0, 4):
                if (len(allWords) > 0):
                    playerWords.append(allWords.pop())

            word_cards = playerWords
            context['wordCards'] = word_cards

            player_inst.playing = 0
            player_inst.save()

            return render(request, 'game/play_ground.html', context)



        elif (player_inst.playing == 1):
            State = "ready"
            context['State'] = State
            if form.is_valid() and (request.POST.get('Sentence')):
                sentence_str = form.clean_sentence_proposal()
                if len(sentence_str) < 10:
                    error_message = "Sentence to short!"
                    context['error_message'] = error_message

                    return render(request, 'game/play_ground.html', context)
                else:
                    if (sentence_str[len(sentence_str) - 1:len(sentence_str)] != "."):
                        error_message = "Add dot to end the Sentence!"
                        context['error_message'] = error_message

                        return render(request, 'game/play_ground.html', context)
                    elif (sentence_str.count(".") > 1):
                        error_message = "Too many Sentences!"
                        context['error_message'] = error_message

                        return render(request, 'game/play_ground.html', context)
                    else:

                        playerWords = []
                        allWords = list(WordCard.objects.filter(game=game_inst, onPlayerHand=player_inst).all())
                        for i in range(0, 4):
                            if (len(allWords) > 0):
                                word = allWords.pop()
                                playerWords.append(word)
                                if word.content in sentence_str:
                                    found = WordCard.objects.filter(content=word.content, game=game_inst, onPlayerHand=player_inst)
                                    WordCard.objects.filter(id=list(found).pop().id).delete()
                                    break

                        playerWords = []
                        allWords = list(WordCard.objects.filter(game=game_inst, onPlayerHand=player_inst).all())
                        for i in range(0, 4):
                            if (len(allWords) > 0):
                                word = allWords.pop()
                                playerWords.append(word)
                        word_cards = playerWords
                        context['wordCards'] = word_cards

                        newSentence = Sentence(content=sentence_str + " ", createdBy=player_inst, game=game_inst)
                        newSentence.save()

                        # Sentence.objects.filter(game=game_inst).all().delete()

                        success_message = "Your Sentence is pending."
                        context['error_message'] = success_message

                        context['messagetype'] = 1

                        sentence_list = Sentence.objects.filter(game=game_inst)
                        context['sentence_list'] = sentence_list

                        player_inst = getPlayerObj(request)

                        for player in player_list:
                            player.playing = 3
                            player.save()



                        player_inst.playing = 4
                        player_inst.save()





                        return render(request, 'game/play_ground.html', context)
            else:
                playerWords = []
                allWords = list(WordCard.objects.filter(game=game_inst, onPlayerHand=player_inst).all())
                for i in range(0, 4):
                    if (len(allWords) > 0):
                        playerWords.append(allWords.pop())

                word_cards = playerWords
                context['wordCards'] = word_cards

                return render(request, 'game/play_ground.html', context)


        elif (player_inst.playing == 3):
            State = "ready"
            context['State'] = State
            if form.is_valid() and (request.POST.get('Claim')):
                if (len(list(Sentence.objects.filter(game=game_inst).all())) > 0):
                    lastSentence = list(Sentence.objects.filter(game=game_inst).all()).pop()
                    allWords = list(WordCard.objects.filter(game=game_inst, onPlayerHand=player_inst).all())
                    for i in range(0, 4):
                        if (len(allWords) > 0):
                            word = allWords.pop()
                            if word.content in lastSentence.content:
                                #Sentence.objects.filter(id=lastSentence.id).delete()
                                WordCard.objects.filter(id=word.id , onPlayerHand=player_inst).delete()
                                break


                playerWords = []
                allWords = list(WordCard.objects.filter(game=game_inst, onPlayerHand=player_inst).all())
                for i in range(0, 4):
                    if (len(allWords) > 0):
                        playerWords.append(allWords.pop())

                word_cards = playerWords
                context['wordCards'] = word_cards


                player_inst.playing = 6
                player_inst.save()


                return render(request, 'game/play_ground.html', context)



            else:
                playerWords = []
                allWords = list(WordCard.objects.filter(game=game_inst,onPlayerHand=player_inst).all())
                for i in range(0, 4):
                    if(len(allWords)>0):
                         playerWords.append(allWords.pop())

                player_inst.playing = 6
                player_inst.save()

                word_cards = playerWords
                context['wordCards'] = word_cards

                return render(request, 'game/play_ground.html', context)





class GameJoinView(View):

    def post(self,request, pk):
        game_inst = get_object_or_404(Game, pk=pk)
        # Create a form instance and populate it with data from the request (binding):
        #//data = dict(request.POST)
        #//data['game_inst'] = game_inst
        form = UserNameForm(request.POST, game_inst=game_inst)

        # Check if the form is valid:
        if form.is_valid():
            #playerState = get_object_or_404(GameState, name="lobby")

            new_player= Player(name=form.cleaned_data['name'], playerPosition=0,game=game_inst,)
            new_player.save()

            playerCount = game_inst.players
            playerCount = playerCount +1
            game_inst.players = playerCount
            game_inst.save()

            request.session['playerID'] = new_player.id
            request.session['playerName'] = new_player.name
            request.session['gameID'] = game_inst.game_code

            pn = PlayerName.objects.filter(game=game_inst, name=new_player.name).first()
            if pn:
                pn.used = True
                pn.save()

            # redirect to a new URL:
            return HttpResponseRedirect('lobby')
        else:
            # return HttpResponseRedirect(
            #     reverse('game:game_join', kwargs={'pk': game_inst.game_code})
            # ) 
            return render(request, 'game/game_join.html', {'form': form, 'game': game_inst,})


    def get(self, request, pk):        
        game_inst = get_object_or_404(Game, pk=pk)        
        randomUnusedAnimal = PlayerName.randomUnusedNameForGame(game_inst)
        form = UserNameForm(initial={'name': randomUnusedAnimal, })
        return render(request, 'game/game_join.html', {'form': form, 'game': game_inst})



class GameCreateView(CreateView):
    model = Game
    #form_class = GameForm
    fields = ['name', 'maxPlayers', 'maxRounds', 'waitSeconds']
    template_name = "game/game_create.html"
    success_url = reverse_lazy("game_list")

    def __init__(self, **kwargs):
        return super(GameCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(GameCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(GameCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(GameCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(GameCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(GameCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(GameCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(GameCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(GameCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        #if game is successfully created, then add default player name suggestions
        animals = ['Hase', 'Fuchs', 'Dachs', 'Schildkröte', 'Flamingo', 'Pinguin', 'Schwein', 'Kuh', 'Storch', 'Katze', 'Hund', 'Elephant', 'Ente']
        for animal in animals:
            name = PlayerName(used=False, name=animal, game=obj)
            name.save()
        return super(GameCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(GameCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(GameCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GameCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("game:game_detail", args=(self.object.pk,))


class GameUpdateView(UpdateView):
    model = Game
    #form_class = GameForm
    fields = ['name', 'maxPlayers', 'maxRounds', 'waitSeconds']
    template_name = "game/game_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "game"

    def __init__(self, **kwargs):
        return super(GameUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(GameUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(GameUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(GameUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(GameUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(GameUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(GameUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(GameUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(GameUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(GameUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(GameUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(GameUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(GameUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(GameUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(GameUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(GameUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GameUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("game:game_detail", args=(self.object.pk,))


class GameDeleteView(DeleteView):
    model = Game
    template_name = "game/game_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "game"

    def __init__(self, **kwargs):
        return super(GameDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(GameDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(GameDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(GameDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(GameDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(GameDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(GameDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(GameDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(GameDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(GameDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GameDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("game:game_list")


