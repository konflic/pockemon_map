from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.TextField(verbose_name="Имя покемона на русском", max_length=200)
    title_en = models.TextField(
        verbose_name="Имя покемона на английском", max_length=200, blank=True
    )
    title_jp = models.TextField(
        verbose_name="Имя покемона на японском", max_length=200, blank=True
    )
    photo = models.ImageField(
        verbose_name="Изображение покемона", upload_to="pokemons", null=True
    )
    description = models.TextField(verbose_name="Описание покемона", null=True)
    previous_evolution = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="next_evolutions",
        verbose_name="Эволюционная ступень покемона",
    )

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    lat = models.FloatField(verbose_name="Широта")
    lon = models.FloatField(verbose_name="Долгота")
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    appeared_at = models.DateTimeField(verbose_name="Время появления покемона")
    disappeared_at = models.DateTimeField(verbose_name="Время исчезновения покемона")
    level = models.IntegerField(verbose_name="Уровень", default=1)
    health = models.IntegerField(verbose_name="Здоровье", default=1)
    strength = models.IntegerField(verbose_name="Сила", default=1)
    defence = models.IntegerField(verbose_name="Защита", default=1)
    stamina = models.IntegerField(verbose_name="Выносливость", default=1)
