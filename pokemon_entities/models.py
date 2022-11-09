from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.TextField(max_length=200)
    title_en = models.TextField(max_length=200, blank=True)
    title_jp = models.TextField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='pokemons', null=True)
    description = models.TextField(null=True)
    previous_evolution = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name="next_evolutions")

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    appeared_at = models.DateTimeField()
    disappeared_at = models.DateTimeField()
    level = models.IntegerField(default=1)
    health = models.IntegerField(default=1)
    strength = models.IntegerField(default=1)
    defence = models.IntegerField(default=1)
    stamina = models.IntegerField(default=1)
