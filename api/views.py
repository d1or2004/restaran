from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class LandingAPIView(APIView):
    def get(self, request):
        return Response(data={"Landing Page, get request ": "Landing Page"})

    def post(self, request):
        return Response(data={"Landing Page, post request ": "Landing Page"})
