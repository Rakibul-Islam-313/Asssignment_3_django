from django.shortcuts import render

def home(request):
    pera = {
        'p' : 'The challenge that restaurants have is that people come in, eat, pay, and leave. There’s little opportunity to build relationships and invite diners back.That’s where texting comes in. When you collect phone numbers you have a connection to your customers that you can use to drive sales and increase customer lifetime value.The most common way restaurants drive repeat business using phone numbers is by sending time-sensitive promotions that often lead to immediate sales.'
    }
    return render(request,'home.html', context = pera)