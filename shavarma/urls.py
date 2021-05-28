from django.urls import path,include
from . import views
extra_urlpatterns = [
    path('',views.detailposition, name = 'detailposition'),
    path('comment/',views.addcomment, name = 'addcomment'),
]
urlpatterns = [
    path('',views.homepage, name = 'home'),
    path('allpoint/',views.alllist, name = 'alllist'),
    path('<int:id_point>/',views.detailShavarma, name = 'detailPoint'),

    path('<int:id_point>/<int:id_pos>/',include(extra_urlpatterns)),
]
