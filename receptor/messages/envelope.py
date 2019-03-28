import logging
logger = logging.getLogger(__name__)

class OuterEnvelope:
    def __init__(self, frame_id, sender, recipient, route_list):
        self.frame_id = frame_id
        self.sender = sender
        self.recipient = recipient
        self.route_list = route_list

class InnerEnvelope:
    def __init__(self, message_id, sender, recipient, message_type, timestamp,
                 raw_payload, in_response_to=None, ttl=None):
        self.message_id = message_id
        self.sender = sender
        self.recipient = recipient
        self.message_type = message_type
        self.timestamp = timestamp
        self.raw_payload = raw_payload
        self.in_response_to = in_response_to
        self.ttl = ttl