from django.db import models
import uuid

class UserCustom(models.Model):
    """ID autoincrement, username, fullname."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(unique=True, max_length=100)
    fullname = models.CharField(max_length=200)

class Role(models.Model):
    """ Role : ID, Role"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    role = models.CharField(max_length=200)

class UserRole(models.Model):
    """ UserRole: ID,USer_ID,Role_ID"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_id = models.ForeignKey(UserCustom, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)

