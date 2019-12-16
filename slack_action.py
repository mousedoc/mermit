# -*- coding: utf-8 -*-

import html.parser

html_parser = html.parser.HTMLParser()

class SlackAction:

    # Default fileds
    action_type = None
    sub_type = None
    channel_id = None
    user_id = None
    text = None
    client_msg_id = None
    team = None
    event_timestamp = None
    timestamp = None
    reaction = None

    # Converted fields
    shortcut = None
    parameters = None

    # Raw
    raw_action = None

    def __init__(self, action):

        self.raw_action = action

        if "type" in action:
            self.action_type = action["type"]
        
        if "subtype" in action:
            self.sub_type = action["subtype"]

        if "channel" in action:
            self.channel_id = action["channel"]

        if "user" in action:
            self.user_id = action["user"]

        if "text" in action:
            self.text = html_parser.unescape(action["text"])

        if "client_msg_id" in action:
            self.type = action["client_msg_id"]

        if "team" in action:
            self.team = action["team"]

        if "event_ts" in action:
            self.event_timestamp = action["event_ts"]

        if "ts" in action:
            self.timestamp = action["ts"]

        if "reaction" in action:
            self.reaction = action["reaction"]

        self.convert()

    def convert(self):
        
        if self.text is None:
            return

        elements = self.text.split()

        if len(elements) is 0:
            return

        self.shortcut = elements[0]
        self.parameters = elements[1:]
        
            

            

