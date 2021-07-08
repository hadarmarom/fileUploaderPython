from django.db import models


class Files(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    fileSrc = models.CharField(blank=True, null=True)
    def swashbuckle(self) -> None:
        print("%s is swashbuckling!" % self["name"])

    class Meta:
        db_table = 'files'
