# from django.db import models
# from django.contrib.auth.validators import UnicodeUsernameValidator
# from django.contrib.auth.models import (
#     PermissionsMixin,
#     UserManager,
#     AbstractBaseUser
# )
# from django.contrib.auth.models import UserManager
# from django.utils.translation import gettext_lazy as _
# from django.utils import timezone
# import jwt
# from django.conf import settings 
# from datetime import datetime, timedelta




# # # Create your models here.

# # # User = get_user_model()

# # class MyUserManager(UserManager):
# #     def _create_user(self, username, email, password, **extra_fields):

# #         if not username:
# #             raise ValueError('The username must be p ovided')
        
# #         if not email:
# #             raise ValueError('The email must be provided')
        

# #         email = self.normalize_email(email)
# #         username = self.model.normalize_username(username)
# #         user = self.mode(username=username, email=email, **extra_fields)
# #         user.set_password(password)
# #         user.save(using=self._db)
# #         return user
    
# #     def create_user(self, username, email, password, **extra_fields):
# #         extra_fields.setdefault('is_staff', False)
# #         extra_fields.setdefault('is_superuser', False)
# #         return self._create_user(username, email, password, **extra_fields)
    

# #     def create_superuser(self, username, email, password, **extra_fields):
# #         """
# #         Create and save a SuperUser with the given email and password.
# #         """
# #         extra_fields.setdefault("is_staff", True)
# #         extra_fields.setdefault("is_superuser", True)
    

# #         if extra_fields.get("is_staff") is not True:
# #             raise ValueError(_("Superuser must have is_staff=True."))
# #         if extra_fields.get("is_superuser") is not True:
# #             raise ValueError(_("Superuser must have is_superuser=True."))
# #         return self.create_user(username, email, password, **extra_fields)
    
# # class CustomUser(AbstractBaseUser, PermissionsMixin):
# #     username_validator = UnicodeUsernameValidator()
# #     username = models.CharField(
# #         _('username'),
# #         max_length=150,
# #         unique=True,
# #         help_text=_('Required. 150 characters or fewer'),
# #         validators=[username_validator],
# #         error_messages={'unique': _("A user with that username already exists.")},
# #     )
# #     email = models.EmailField(_("email address"), blank=False, unique=True)
# #     is_staff = models.BooleanField(default=False)
# #     is_active = models.BooleanField(default=True)
# #     date_joined = models.DateTimeField(default=timezone.now)
# #     email_verified = models.BooleanField(default=False)

# #     USERNAME_FIELD = "email"
# #     REQUIRED_FIELDS = []
 
# #     objects = MyUserManager()

# #     EMAIL_FIELD = 'email'
# #     USERNAME_FIELD = 'email'
# #     REQUIRED_FIELDS = ['username']

# #     @property
# #     def token(self):
# #         token = jwt.encode(
# #             {'username': self.username, 'email': self.email,
# #                 'exp': datetime.utcnow() + timedelta(hours=24)},
# #             settings.SECRET_KEY, algorithm='HS256')

# #         return token



# # # from django.db import models
# # # from django.contrib.auth.validators import UnicodeUsernameValidator
# # # from django.contrib.auth.models import (
# # #     PermissionsMixin, UserManager, AbstractBaseUser)
# # # from django.utils.translation import gettext_lazy as _
# # # from django.utils import timezone
# # # import jwt
# # # from datetime import datetime, timedelta


# # # from django.conf import settings



# # # class MyUserManager(UserManager):

# # #     def _create_user(self, username, email, password, **extra_fields):
# # #         """
# # #         Create and save a user with the given username, email, and password.
# # #         """
# # #         if not username:
# # #             raise ValueError('The given username must be set')

# # #         if not email:
# # #             raise ValueError('The given email must be set')

# # #         email = self.normalize_email(email)
# # #         username = self.model.normalize_username(username)
# # #         user = self.model(username=username, email=email, **extra_fields)
# # #         user.set_password(password)
# # #         user.save(using=self._db)
# # #         return user

# # #     def create_user(self, username, email, password=None, **extra_fields):
# # #         extra_fields.setdefault('is_staff', False)
# # #         extra_fields.setdefault('is_superuser', False)
# # #         return self._create_user(username, email, password, **extra_fields)

# # #     def create_superuser(self, username, email, password=None, **extra_fields):
# # #         extra_fields.setdefault('is_staff', True)
# # #         extra_fields.setdefault('is_superuser', True)

# # #         if extra_fields.get('is_staff') is not True:
# # #             raise ValueError('Superuser must have is_staff=True.')
# # #         if extra_fields.get('is_superuser') is not True:
# # #             raise ValueError('Superuser must have is_superuser=True.')

# # #         return self._create_user(username, email, password, **extra_fields)


# # # class CustomUser(AbstractBaseUser, PermissionsMixin):
# # #     """
# # #     An abstract base class implementing a fully featured User model with
# # #     admin-compliant permissions.

# # #     Username and password are required. Other fields are optional.
# # #     """
# # #     username_validator = UnicodeUsernameValidator()

# # #     username = models.CharField(
# # #         _('username'),
# # #         max_length=150,
# # #         unique=True,
# # #         help_text=_(
# # #             'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
# # #         validators=[username_validator],
# # #         error_messages={
# # #             'unique': _("A user with that username already exists."),
# # #         },
# # #     )
# # #     email = models.EmailField(_('email address'), blank=False, unique=True)
# # #     is_staff = models.BooleanField(
# # #         _('staff status'),
# # #         default=False,
# # #         help_text=_(
# # #             'Designates whether the user can log into this admin site.'),
# # #     )
# # #     is_active = models.BooleanField(
# # #         _('active'),
# # #         default=True,
# # #         help_text=_(
# # #             'Designates whether this user should be treated as active. '
# # #             'Unselect this instead of deleting accounts.'
# # #         ),
# # #     )
# # #     date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
# # #     email_verified = models.BooleanField(
# # #         _('email_verified'),
# # #         default=False,
# # #         help_text=_(
# # #             'Designates whether this users email is verified. '

# # #         ),
# # #     )
# # #     objects = MyUserManager()

# # #     EMAIL_FIELD = 'email'
# # #     USERNAME_FIELD = 'email'
# # #     REQUIRED_FIELDS = ['username']

# # #     @property
# # #     def token(self):
# # #         token = jwt.encode(
# # #             {'username': self.username, 'email': self.email,
# # #                 'exp': datetime.utcnow() + timedelta(hours=24)},
# # #             settings.SECRET_KEY, algorithm='HS256')

# # #         return token

         

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from rest_framework_simplejwt.tokens import RefreshToken




class UserManager(BaseUserManager):

    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)


class UserData(AbstractUser):


    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username