from rest_framework import serializers
from .models import User


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        except_fields = "followings"

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            # provide django, password will be hashing!
            instance.set_password(password)
        instance.save()
        return instance

class AccountDetailSerializer(AccountSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "nickname",
            "name",
            "email",
            "birthday",
            "gender",
            "produce_me"
        )