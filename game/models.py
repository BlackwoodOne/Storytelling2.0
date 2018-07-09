import uuid
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

def createUUID():
    d = uuid.uuid4()
    number = d.int
    return int(str(number)[:16])


class GameState(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class RoundState(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    channel_name = models.CharField(max_length=255)

class Game(models.Model):
    game_code = models.CharField(primary_key=True, max_length=18, default=createUUID, unique=True)
    name = models.CharField(max_length=200)
    players = models.IntegerField(default=0)
    maxPlayers = models.IntegerField(validators=[MinValueValidator(3),MaxValueValidator(10)], default=3)
    round = models.IntegerField(default=0)
    maxRounds = models.IntegerField(validators=[MinValueValidator(4),MaxValueValidator(120)], default=9)
    waitSeconds = models.IntegerField(validators=[MinValueValidator(30),MaxValueValidator(600)], default=300)
    gameState = models.ForeignKey(GameState, on_delete=models.SET_NULL, blank=True, null=True, default=1)
    roundState = models.ForeignKey(RoundState, on_delete=models.SET_NULL, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def getGameById(req_game_code):
        g = Game(game_code=req_game_code)
        return g


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    playerPosition = models.IntegerField()
    playing = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    playerState = models.ForeignKey(GameState, on_delete=models.SET_NULL, blank=True, null=True, default=1)

    def __str__(self):
        return self.name


class WordCard(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=200)
    deckNumber = models.IntegerField()
    used = models.BooleanField(default=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    createdBy = models.ForeignKey(Player, related_name='createdBy', on_delete=models.CASCADE)
    onPlayerHand = models.ForeignKey(Player, related_name='onPlayerHand', on_delete=models.CASCADE, null=True, blank=True,)

    def __str__(self):
        return self.content

class PlayerName(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    used = models.BooleanField(default=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    
    @classmethod
    def randomUnusedNameForGame(cls, game_inst):
        randomUnusedName = cls.objects.filter(game=game_inst, used=False).order_by('?').first()    
        return randomUnusedName

    def __str__(self):
        return self.name


class Sentence(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=1024)
    valid = models.BooleanField(default=False)
    reject = models.BooleanField(default=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    createdBy = models.ForeignKey(Player, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content



