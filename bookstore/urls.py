from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [

# Shared URL's
 path('', views.login_form.as_view(), name='home'),
 path('login/', views.loginView.as_view(), name='login'),
 path('logout/', views.logoutView.as_view(), name='logout'),
 path('regform/', views.register_form.as_view(), name='regform'),
 path('register/', views.registerView.as_view(), name='register'),



 # Librarian URL's
 path('librarian/', views.librarian.as_view(), name='librarian'),
 path('labook_form/', views.labook_form.as_view(), name='labook_form'),
 path('labook/', views.labook.as_view(), name='labook'),
 path('llbook/', views.LBookListView.as_view(), name='llbook'),
 path('ldrequest/', views.LDeleteRequest.as_view(), name='ldrequest'),
 path('lsearch/', views.lsearch.as_view(), name='lsearch'),
 path('ldbook/<int:pk>', views.LDeleteBook.as_view(), name='ldbook'),
 path('lmbook/', views.LManageBook.as_view(), name='lmbook'),
 path('ldbookk/<int:pk>', views.LDeleteView.as_view(), name='ldbookk'),
 path('lvbook/<int:pk>', views.LViewBook.as_view(), name='lvbook'),
 path('lebook/<int:pk>', views.LEditView.as_view(), name='lebook'),
 path('lcchat/', views.LCreateChat.as_view(), name='lcchat'),
 path('llchat/', views.LListChat.as_view(), name='llchat'),




 # Publisher URL's
 path('publisher/', views.UBookListView.as_view(), name='publisher'),
 path('uabook_form/', views.uabook_form.as_view(), name='uabook_form'),
 path('uabook/', views.uabook.as_view(), name='uabook'),
 path('ucchat/', views.UCreateChat.as_view(), name='ucchat'),
 path('ulchat/', views.UListChat.as_view(), name='ulchat'),
 path('request_form/', views.request_form.as_view(), name='request_form'),
 path('delete_request/', views.delete_request.as_view(), name='delete_request'),
 path('feedback_form/', views.feedback_form.as_view(), name='feedback_form'),
 path('send_feedback/', views.send_feedback.as_view(), name='send_feedback'),
 path('about/', views.about.as_view(), name='about'),
 path('usearch/', views.usearch.as_view(), name='usearch'),



 # Admin URL's
 path('dashboard/', views.dashboard.as_view(), name='dashboard'),
 path('acchat/', views.ACreateChat.as_view(), name='acchat'),
 path('alchat/', views.AListChat.as_view(), name='alchat'),
 path('aabook_form/', views.aabook_form.as_view(), name='aabook_form'),
 path('aabook/', views.aabook.as_view(), name='aabook'),
 path('albook/', views.ABookListView.as_view(), name='albook'),
 path('ambook/', views.AManageBook.as_view(), name='ambook'),
 path('adbook/<int:pk>', views.ADeleteBook.as_view(), name='adbook'),
 path('avbook/<int:pk>', views.AViewBook.as_view(), name='avbook'),
 path('aebook/<int:pk>', views.AEditView.as_view(), name='aebook'),
 path('adrequest/', views.ADeleteRequest.as_view(), name='adrequest'),
 path('afeedback/', views.AFeedback.as_view(), name='afeedback'),
 path('asearch/', views.asearch.as_view(), name='asearch'),
 path('adbookk/<int:pk>', views.ADeleteBookk.as_view(), name='adbookk'),
 path('create_user_form/', views.create_user_form.as_view(), name='create_user_form'),
 path('aluser/', views.ListUserView.as_view(), name='aluser'),
 path('create_use/', views.create_user.as_view(), name='create_user'),
 path('alvuser/<int:pk>', views.ALViewUser.as_view(), name='alvuser'),
 path('aeuser/<int:pk>', views.AEditUser.as_view(), name='aeuser'),
 path('aduser/<int:pk>', views.ADeleteUser.as_view(), name='aduser'),



















]
