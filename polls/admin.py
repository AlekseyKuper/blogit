from django.contrib import admin
from .models import Categories, Tests, Questions, Answers
# Register your models here.

admin.site.register(Categories)
admin.site.register(Tests)
admin.site.register(Questions)
admin.site.register(Answers)

