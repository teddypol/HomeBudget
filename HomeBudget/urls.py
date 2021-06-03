from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from HomeBudget import settings
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls, name="administrator"),
    path('', include('dashboard.urls')),
    # path('password-reset/', auth_views.PasswordResetView.as_view(
    #     template_name='password/password_reset.html'), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
    #     template_name='password/password_reset_done.html'), name='password_reset_done'),
    # path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    #     template_name='password/password_reset_confirm.html'), name='password_reset_confirm'),
    # path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
    #     template_name='password/password_reset_complete.html'), name='password_reset_complete'),
    #
    # path("password_reset", views.password_reset_request, name="password_reset")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
