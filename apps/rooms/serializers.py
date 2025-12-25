from rest_framework import serializers

class RoomSerializer(serializers.Serializer):

    ROOM_TYPE = [("AC", "AC"), ("NON-AC", "NON-AC")]
    ROOM_STATUS = [("Available", "Available"), ("Reserved", "Reserved"), ("Maintenance", "Maintenance")]

    room_no = serializers.IntegerField(required=True)
    room_capacity = serializers.IntegerField(required=True)
    room_type = serializers.ChoiceField(required=True, choices= ROOM_TYPE)
    room_price = serializers.IntegerField(required=True)
    room_status = serializers.ChoiceField(required=True, choices= ROOM_STATUS)



