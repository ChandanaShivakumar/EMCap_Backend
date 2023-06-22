from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, emp_id, email, password,password2=None, **extra_fields):
        """
        Create and save a user with the given emp_id, email, and password.
        """
        if not emp_id:
            raise ValueError('The Employee ID must be set')
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(emp_id=emp_id, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, emp_id, email, password=None, **extra_fields):
        """
        Create and save a regular user with the given emp_id, email, and password.
        """
        extra_fields.setdefault('is_admin', False)
        extra_fields.setdefault('role_id', 1)
        return self._create_user(emp_id, email, password, **extra_fields)

    def create_superuser(self, emp_id, email, password=None, **extra_fields):
        """
        Create and save a superuser with the given emp_id, email, and password.
        """
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('role_id', 1)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin=True.')

        return self._create_user(emp_id, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    emp_id = models.CharField(max_length=10, primary_key=True)
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)
    role_id= models.IntegerField(default=1, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['emp_id', 'name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin