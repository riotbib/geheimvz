from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth import views as auth_views

from .models import AppearanceSettings, NotificationSettings, PrivacySettings
from core.components.tabs.tabs import TabsMixin
from core.models import User

from .forms import (
    AppearanceForm,
    AuthenticationForm,
    DeleteForm,
    NotificationSettingsForm,
    PasswordChangeForm,
    PrivacyForm,
    UserForm,
)

tabs = {
    "account": {
        "href": reverse_lazy("account"),
        "label": _("Account settings"),
    },
    "appearance": {
        "href": reverse_lazy("account-appearance"),
        "label": _("Appearance"),
    },
    "notifications": {
        "href": reverse_lazy("account-notifications"),
        "label": _("Notifications"),
    },
    "privacy": {
        "href": reverse_lazy("account-privacy"),
        "label": _("Privacy"),
    },
}


class ProfileUpdateView(
    TabsMixin,
    LoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    form_class = UserForm
    model = User
    success_message = _("Profile successfully updated")
    template_name = "my_account/user_form.html"
    tabs = tabs
    tab_current = "account"

    def get_object(self):
        return self.request.user


class AppearanceUpdateView(
    TabsMixin,
    LoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    form_class = AppearanceForm
    model = AppearanceSettings
    success_message = _("Profile successfully updated")
    template_name = "my_account/appearance_form.html"
    success_url = reverse_lazy("account-appearance")
    tabs = tabs
    tab_current = "appearance"

    def get_object(self):
        return self.request.user.appearance_settings


class NotificationSettingsUpdateView(
    TabsMixin,
    LoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    form_class = NotificationSettingsForm
    model = NotificationSettings
    tabs = tabs
    tab_current = "notifications"
    success_message = _("Notification settings successfully updated")
    success_url = reverse_lazy("account-notifications")

    def get_object(self):
        return self.request.user.notification_settings


class PrivacyUpdateView(
    TabsMixin,
    LoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    form_class = PrivacyForm
    model = PrivacySettings
    success_message = _("Profile successfully updated")
    success_url = reverse_lazy("account-privacy")
    template_name = "my_account/privacy_form.html"
    tabs = tabs
    tab_current = "privacy"

    def get_object(self):
        return self.request.user.privacy_settings


class UserDeleteView(LoginRequiredMixin, DeleteView):
    form_class = DeleteForm
    model = User
    success_message = _("Account successfully deleted")
    success_url = reverse_lazy("index")
    template_name = "my_account/user_confirm_delete.html"

    def get_object(self):
        return self.request.user


class PasswordChangeView(SuccessMessageMixin, auth_views.PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "my_account/password_change_form.html"
    success_message = _("Password change successful")
    success_url = reverse_lazy("account")


class LoginView(auth_views.LoginView):
    form_class = AuthenticationForm
    template_name = "my_account/login.html"
