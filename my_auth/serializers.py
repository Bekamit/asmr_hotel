from rest_framework import serializers

from my_auth.utils import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'address', 'password', 'confirm_password']

    def validate_password(self, value):
        request = self.context.get('request')
        validate_password(value, request.user)
        return value

    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError('Password did not match')
        return data

    # def create(self, validated_data):
    #     user = User.objects.create(
    #         email=validated_data.get('email'),
    #         first_name=validated_data.get('first_name'),
    #         last_name=validated_data.get('last_name'),
    #         phone=validated_data.get('phone'),
    #         address=validated_data.get('address'),
    #     )
    #     user.password = make_password(validated_data.get('password'))
    #     user.save()
    #     return user
    def create(self, validated_data):
        return User.objects.create(
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            phone=validated_data.get('phone'),
            address=validated_data.get('address'),
            password=make_password(validated_data.get('password'))
        )


# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         exclude = ['password']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']


# class ProfileSerializer(UserSerializer):
#     pass
class ProfileSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        read_only_fields = [
            'last_login',
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',
            'groups',
            'user_permissions',
        ]


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_new_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'old_password',
            'new_password',
            'confirm_new_password'
        ]

    def validate_old_password(self, value):
        request = self.context.get('request')
        if not request.user.check_password(value):
            raise serializers.ValidationError('Old password is not correct ')
        return value

    def validate_new_password(self, value):
        request = self.context.get('request')
        validate_password(value, request.user)
        return value

    def validate(self, data):
        if data.get('new_password') != data.get('confirm_new_password'):
            raise serializers.ValidationError('Password did not match')
        return data

    def update(self, instance, validated_data):
        instance.password = make_password(validated_data.get('new_password'))
        instance.save()
        return instance

    # def update(self, instance, validated_data):
    #     instance.password = make_password(validated_data.get('new_password'))
    #     return User.objects.update(password=instance.password)
