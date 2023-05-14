from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Folder(models.Model):
    name = models.CharField(max_length=256)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='child_folders')

    def __str__(self):
        name = self.name
        if not self.parent:
            return name

        parent = self.parent
        while parent:
            name = f'{parent.name}/{name}'
            parent = parent.parent
        return name


class Document(models.Model):
    name = models.CharField(max_length=256)
    file = models.FileField(upload_to='data/')
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='documents')
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, blank=True, null=True, related_name='documents')

    def __str__(self):
        return f"{self.folder}/{self.name}"
