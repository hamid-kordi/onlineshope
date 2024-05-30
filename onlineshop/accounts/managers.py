from django.contrib.auth.models import BaseUserManager 


class UserMnagers(BaseUserManager):
    def create_user(self, email, full_name, phone_number,password):
        if not email:
            raise ValueError("Users must have an email address")
        if not phone_number:
            raise ValueError("Users must have an phone number")

        if not full_name:
            raise ValueError("Users must have an full name")

        user = self.model(phone_number=phone_number,email=self.normalize_email(email),full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,full_name,phone_number, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            full_name=full_name,
            phone_number=phone_number,
            password=password
        
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user