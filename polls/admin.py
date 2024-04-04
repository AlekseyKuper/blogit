from django.contrib import admin
from .models import Categories, Tests, Questions, Answers, Result
# Register your models here.

admin.site.register(Categories)
admin.site.register(Tests)
admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Result)

