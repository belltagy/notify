import notify_me
from django import forms
from firebase_admin.messaging import Message, Notification
from fcm_django.models import FCMDevice

class MessageForm(forms.Form):
    title = forms.CharField(label="Message Title", max_length=255)
    body =  forms.CharField(widget=forms.Textarea)

    def send_message(self):
        notification_message = Message(
            notification=Notification(title=self.cleaned_data['title'], body=self.cleaned_data['body']),
            #topic="Optional topic parameter:Whatever you want",
        )
        data_message = Message(
                        data={
                            "Nick" : "Mario",
                            "body" : "great match!",
                            "Room" : "PortugalVSDenmark"
                    },
                    topic="first_topic",
                    )
        device = FCMDevice.objects.last()
        device.send_message(notification_message)
