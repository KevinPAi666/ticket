from rest_framework.generics import GenericAPIView
from django.http import HttpResponse

from . import forms

import json, re


class order_page(GenericAPIView):
    def post(self, request):
        if request.method == "POST":
            form_get = False
            try:
                serializer_class = forms.order_Form
                data = request.data
                serializer = serializer_class(data=data)
                serializer.is_valid(raise_exception=True)

                id = serializer.validated_data['id']
                name = serializer.validated_data['name']
                address = serializer.validated_data['address']
                price = serializer.validated_data['price']
                currency = serializer.validated_data['currency']
                address_city = serializer.validated_data['address']['city']
                address_district = serializer.validated_data['address']['district']
                address_street = serializer.validated_data['address']['street']
                form_get = True

                error = stander(name, address, price, currency, serializer)

                if len(error) == 0:
                    serializer.save()
                    result = "PASS"
                    status_code = 200

                else:
                    result = ', '.join(error)
                    status_code = 400

            except Exception as e:
                if form_get:
                    result = str(e)
                else:
                    err = str(e).replace("\'", "")
                    result = f"Please check form {err} is exist."

                status_code = 400

            return HttpResponse(json.dumps(f"{status_code} - {result}"), content_type="application/json", status=status_code)


def stander(name, address, price, currency, serializer):
    error = []

    for text in name.split(" "):
        if not re.match("^[A-Za-z]*$", text):
            error.append("Name contains non-English characters")
            break
        if not text[0].isupper():
            error.append("Name is not capitalized")
            break

    if currency not in ["TWD", "USD"]:
        error.append("Currency format is wrong")

    if currency == "USD":
        price *= 31
        serializer.validated_data['currency'] = "TWD"

    if price > 2000:
        error.append("Price is over 2000")

    for i, j in address.items():
        if len(j) == 0:
            error.append(f"please enter address - {i}")

    return error

