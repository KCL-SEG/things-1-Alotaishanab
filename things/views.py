from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("""
    <!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Things</title>
</head>
<body>
<h1>Things</h1>
</body>
</html>
    """)
