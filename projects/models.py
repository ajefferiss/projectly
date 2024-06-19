from django.db import models


TRUNCATE_TEXT_LEN = 50


class Project(models.Model):
    name_text = models.TextField()
    pub_date = models.DateField("date published")

    def __str__(self) -> str:
        return f"{self.name_text} created {self.pub_date}"


class Note(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    note_text = models.TextField()

    def __str__(self) -> str:
        note: str = self.note_text
        if len(self.note_text) > TRUNCATE_TEXT_LEN:
            note = self.note_text[:TRUNCATE_TEXT_LEN] + "..."

        return f"{note} created for {self.project.name_text}"


class Script(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    script_text = models.TextField()

    def __str__(self) -> str:
        script: str = self.script_text
        if len(self.script_text) > TRUNCATE_TEXT_LEN:
            script = self.script_text[:TRUNCATE_TEXT_LEN] + "..."

        return f"{script} created for {self.project.name_text}"
