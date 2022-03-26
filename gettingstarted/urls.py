from django.urls import path, include

from django.contrib import admin

import fullstack_communication.views

admin.autodiscover()

# import fullstack_communication.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", fullstack_communication.views.index, name="index"),
    path("admin/", admin.site.urls),
    path("postCompany/", fullstack_communication.views.post_company),
    path("postUser/", fullstack_communication.views.post_user),
    path("postAnswers/", fullstack_communication.views.post_answers),
    path("getForm/", fullstack_communication.views.get_form),
    path("getRanking/", fullstack_communication.views.get_ranking),
    path("getStats/", fullstack_communication.views.get_stats),
]
