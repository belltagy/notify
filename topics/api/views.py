import re
from django.http.response import Http404
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_202_ACCEPTED
from firebase_admin import messaging
from firebase_admin.messaging import Message, Notification, subscribe_to_topic, unsubscribe_from_topic,send
from fcm_django.models import FCMDevice
from ..models import Topic
class CreateSubscriptionView(APIView):
    
    def post(self, request, pk=None):
        print(self.kwargs.get('pk'))
        return Response({}, status=HTTP_200_OK)
    
    def get(self, request, pk=None):
        
        topic = Topic.objects.get(id=pk)
        print(topic.name)
        user_devices =FCMDevice.objects.filter(user=request.user)
        # subscribe to topic
        user_devices.handle_topic_subscription(True, topic="hello")
        # See documentation on defining a message payload.
        print("before message creation")
        message = Message(
            data={
                'score': '850',
                'time': '2:45',
            },
            topic=topic.name
        )
        notification_message = Message(
            notification=Notification(title="Mohamed Beltagy", body="all days are you on"),
            topic=topic.name,
        )
        #FCMDevice.objects.send_message(message)

        response = messaging.send(notification_message)




        # Send a message to the devices subscribed to the provided topic.
        #response = messaging.send(message)
        return Response({"name":"hello"}, status=HTTP_200_OK)
