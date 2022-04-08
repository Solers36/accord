from django.db import models


class Artist(models.Model):
    artist_name = models.CharField("Исполнитель", max_length=50)
    url_name = models.CharField("Адрес", max_length=50)

    class Meta:
        verbose_name = "Артист"
        verbose_name_plural = "Артисты"

    def __str__(self):
        return self.artist_name


class Accord(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song_title = models.CharField("Название произведения", max_length=150)
    song_text = models.TextField("Аккорды и текст")
    сhords_used =models.CharField("Используемые аккорды", max_length=250)
    link_to_the_video = models.CharField("Ссылка на видео", max_length=250)

    class Meta:
        verbose_name = "Подбор аккордов"
        verbose_name_plural = "Подборы аккордов"

    def __str__(self):
        return str(self.artist) + ' - ' + self.song_title