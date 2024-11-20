from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CodeFlow.accounts'

    def ready(self):
        import CodeFlow.accounts.signals