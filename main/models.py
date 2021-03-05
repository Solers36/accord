from django.db import models

class Accord(models.Model):
    artist = models.CharField("Исполнитель", max_length=50, default="Неизвестный исполнитель")
    song_title = models.CharField("Название произведения", max_length=150, default="Неизвестное название")
    song_text = models.TextField("Аккорды и текст")
    сhords_used =models.CharField("Используемые аккорды", max_length=250, default="Необязательное поле")
    link_to_the_video = models.CharField("Ссылка на видео", max_length=250)

    class Meta:
        verbose_name = "Подбор аккордов"
        verbose_name_plural = "Подборы аккордов"

    def __str__(self):
        return self.artist + ' - ' + self.song_title