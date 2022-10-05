from django.contrib import admin
from django.urls import path
from accounts import views as accounts_views
from mugmaapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('normal/', views.normal, name='normal'),

    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    path('signup/', accounts_views.signup, name='signup'),

    path('create/', views.create, name='create'),
    path('detail/<int:recipe_id>', views.detail, name='detail'),
    path('new_comment/<int:recipe_id>', views.detail, name='new_comment'),
    path('detail/<int:recipe_id>/update',views.update, name="update"),
    path('detail/<int:recipe_id>/delete',views.delete, name="delete"),

    path('NVtrendy/', views.NVtrendy, name='NVtrendy'),
    path('Vtrendy/', views.Vtrendy, name='Vtrendy'),
    path('NVsteady/', views.NVsteady, name='NVsteady'),
    path('Vtsteady/', views.Vsteady, name='Vsteady'),

    path('like/<int:recipe_id>/', views.likes, name="likes"),

    path('mypage/', views.mypage, name='mypage'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('mugrap/', views.mugrap, name='mugrap'),
    path('mugup/', views.mugup, name='mugup'),
    path('mugchef/', views.mugchef, name='mugchef'),
    path('chefdetail/<int:chef_id>', views.chefdetail, name='chefdetail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)