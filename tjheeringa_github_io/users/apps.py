from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = "tjheeringa_github_io.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import tjheeringa_github_io.users.signals  # noqa F401
        except ImportError:
            pass
