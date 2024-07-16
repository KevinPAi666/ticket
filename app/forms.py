from django import forms
from rest_framework import serializers

from .models import *


class order_Form(serializers.ModelSerializer):
    class Meta:
        model = order_model
        fields = '__all__'
