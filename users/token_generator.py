from django.contrib.auth.tokens import PasswordResetTokenGenerator
#from django.utils import six


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        # return (
        #     six.text_type(user.pk) + six.text_type(timestamp)# + six.text_type(user.is_active)
        # )
        login_timestamp = (
            ""
            if user.last_login is None
            else user.last_login.replace(microsecond=0, tzinfo=None)
        )
        email_field = user.get_email_field_name()
        email = getattr(user, email_field, "") or ""
        return f"{user.pk}{user.password}{login_timestamp}{timestamp}{email}"


account_activation_token = TokenGenerator()