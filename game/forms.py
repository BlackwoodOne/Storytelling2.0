from django import forms
from .models import GameState, RoundState, Game, Player, WordCard, Sentence, PlayerName
import re

class GameStateForm(forms.ModelForm):

    class Meta:
        model = GameState
        fields = ['name']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(GameStateForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(GameStateForm, self).is_valid()

    def full_clean(self):
        return super(GameStateForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean(self):
        return super(GameStateForm, self).clean()

    def validate_unique(self):
        return super(GameStateForm, self).validate_unique()

    def save(self, commit=True):
        return super(GameStateForm, self).save(commit)


class RoundStateForm(forms.ModelForm):

    class Meta:
        model = RoundState
        fields = ['name']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(RoundStateForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(RoundStateForm, self).is_valid()

    def full_clean(self):
        return super(RoundStateForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean(self):
        return super(RoundStateForm, self).clean()

    def validate_unique(self):
        return super(RoundStateForm, self).validate_unique()

    def save(self, commit=True):
        return super(RoundStateForm, self).save(commit)


class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ['game_code', 'name', 'players', 'maxPlayers', 'round', 'maxRounds', 'waitSeconds', 'gameState', 'roundState']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(GameForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(GameForm, self).is_valid()

    def full_clean(self):
        return super(GameForm, self).full_clean()

    def clean_game_code(self):
        game_code = self.cleaned_data.get("game_code", None)
        return game_code

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_players(self):
        players = self.cleaned_data.get("players", None)
        return players

    def clean_maxPlayers(self):
        maxPlayers = self.cleaned_data.get("maxPlayers", None)
        return maxPlayers

    def clean_round(self):
        round = self.cleaned_data.get("round", None)
        return round

    def clean_maxRounds(self):
        maxRounds = self.cleaned_data.get("maxRounds", None)
        return maxRounds

    def clean_waitSeconds(self):
        waitSeconds = self.cleaned_data.get("waitSeconds", None)
        return waitSeconds

    def clean_gameState(self):
        gameState = self.cleaned_data.get("gameState", None)
        return gameState

    def clean_roundState(self):
        roundState = self.cleaned_data.get("roundState", None)
        return roundState

    def clean(self):
        return super(GameForm, self).clean()

    def validate_unique(self):
        return super(GameForm, self).validate_unique()

    def save(self, commit=True):
        return super(GameForm, self).save(commit)


class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ['name', 'playerPosition', 'playing', 'points', 'game', 'playerState']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(PlayerForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(PlayerForm, self).is_valid()

    def full_clean(self):
        return super(PlayerForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_playerPosition(self):
        playerPosition = self.cleaned_data.get("playerPosition", None)
        return playerPosition

    def clean_playing(self):
        playing = self.cleaned_data.get("playing", None)
        return playing

    def clean_points(self):
        points = self.cleaned_data.get("points", None)
        return points

    def clean_game(self):
        game = self.cleaned_data.get("game", None)
        return game

    def clean_playerState(self):
        playerState = self.cleaned_data.get("playerState", None)
        return playerState

    def clean(self):
        return super(PlayerForm, self).clean()

    def validate_unique(self):
        return super(PlayerForm, self).validate_unique()

    def save(self, commit=True):
        return super(PlayerForm, self).save(commit)


class WordCardForm(forms.ModelForm):

    class Meta:
        model = WordCard
        fields = ['content', 'deckNumber', 'used', 'game', 'createdBy', 'onPlayerHand']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(WordCardForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(WordCardForm, self).is_valid()

    def full_clean(self):
        return super(WordCardForm, self).full_clean()

    def clean_content(self):
        content = self.cleaned_data.get("content", None)
        return content

    def clean_deckNumber(self):
        deckNumber = self.cleaned_data.get("deckNumber", None)
        return deckNumber

    def clean_used(self):
        used = self.cleaned_data.get("used", None)
        return used

    def clean_game(self):
        game = self.cleaned_data.get("game", None)
        return game

    def clean_createdBy(self):
        createdBy = self.cleaned_data.get("createdBy", None)
        return createdBy

    def clean_onPlayerHand(self):
        onPlayerHand = self.cleaned_data.get("onPlayerHand", None)
        return onPlayerHand

    def clean(self):
        return super(WordCardForm, self).clean()

    def validate_unique(self):
        return super(WordCardForm, self).validate_unique()

    def save(self, commit=True):
        return super(WordCardForm, self).save(commit)


class SentenceForm(forms.ModelForm):

    class Meta:
        model = Sentence
        fields = ['content', 'valid', 'reject', 'game', 'createdBy']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(SentenceForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(SentenceForm, self).is_valid()

    def full_clean(self):
        return super(SentenceForm, self).full_clean()

    def clean_content(self):
        content = self.cleaned_data.get("content", None)
        return content

    def clean_valid(self):
        valid = self.cleaned_data.get("valid", None)
        return valid

    def clean_reject(self):
        reject = self.cleaned_data.get("reject", None)
        return reject

    def clean_game(self):
        game = self.cleaned_data.get("game", None)
        return game

    def clean_createdBy(self):
        createdBy = self.cleaned_data.get("createdBy", None)
        return createdBy

    def clean(self):
        return super(SentenceForm, self).clean()

    def validate_unique(self):
        return super(SentenceForm, self).validate_unique()

    def save(self, commit=True):
        return super(SentenceForm, self).save(commit)

class UserNameForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ['name',]
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        self.game_inst = kwargs.pop('game_inst', None)
        super(UserNameForm, self).__init__(*args, **kwargs)

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        print(Player.objects.filter(game=self.game_inst, name=name).count())
        if Player.objects.filter(game=self.game_inst, name=name).count() > 0:
            raise forms.ValidationError(
                'Name \'%(value)s\' is already in use by another player in this game. Please pick another name.',
                code='already-used',
                params={'value': name},
            )
        else:
            return name

class AddWordCardsForm(forms.Form):
    word_collection = forms.CharField(widget=forms.Textarea(attrs={'id': 'textArea', 'rows': 5, 'cols': 100}),help_text="Enter words that you want to use for the game")
    def clean_word_collection(self):
        return self.cleaned_data.get("word_collection", '')

class AddSentenceForm(forms.Form):
    sentence_proposal = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 2, 'cols': 100}),help_text="Enter the sentence that you want to commit")

    def clean_sentence_proposal(self):
        return self.cleaned_data.get("sentence_proposal", '')




