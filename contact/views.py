from asgiref.sync import async_to_sync
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from bot.data.config import CHANNELS
from bot.loader import bot
from .serializers import ContactSerializer



class ContactCreateApiView(APIView):
    serializer_class = ContactSerializer

    @swagger_auto_schema(
        request_body=ContactSerializer,
        responses={
            201: 'Contact successfully saved',
            400: 'Validation error',
        },
        operation_description="Create a new contact and send notification message"
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            async_to_sync(self.send_message)(request.data)
            return Response(data={
                'message': 'Contact successfully saved',
                'status': 201
            })
        return Response(data=serializer.errors, status=400)

    async def send_message(self, data):
        name = data.get('name')
        phone_number = data.get('phone_number')
        message = data.get('message')
        info = "🛒 New order:\n"
        info += f"👤 Name: {name}\n"
        info += f"📞 Phone number: {phone_number}\n"
        info += f"✍️ Message: {message}\n"
        await bot.send_message(chat_id=CHANNELS[0], text=info)
        await bot.session.close()

