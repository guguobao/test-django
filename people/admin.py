from django.contrib import admin
from .models import Person,Blog,Author

# Register your models here.
admin.site.register(Person)
admin.site.register(Blog)
admin.site.register(Author)