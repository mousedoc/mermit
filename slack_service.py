# -*- coding: utf-8 -*-

import os
from slackclient import SlackClient
from util.singleton import Singleton

class SlackService(Singleton):


    client = None
    bot_token = None
    channel_id = None


    def initialize(self, bot_token, channel_id):
        self.bot_token = bot_token
        self.channel_id = channel_id

        self.client = SlackClient(
            # if public app use right side code ---> os.environ["SLACK_BOT_TOKEN"]
            token = self.bot_token,
            token_update_callback = self.updated_token_callback
        )
    

    def updated_token_callback(self, updated_data):
        print("Enterprise ID: {}".format(updated_data["enterprise_id"]))
        print("Workspace ID: {}".format(updated_data["team_id"]))
        print("Access Token: {}".format(updated_data["access_token"]))
        print("Access Token expires in (ms): {}".format(updated_data["expires_in"]))
        self.send_message("Access token updated")


    def get_channel_id(self):
        return self.channel_id


    def send_message(self, message):
        self.client.api_call(
            "chat.postMessage",
            channel = self.get_channel_id(),
            text = message
        )


    def reply_message(self, message, thread_ts):
        self.client.api_call(
            "chat.postMessage",
            channel = self.get_channel_id(),
            text = message,
            thread_ts = thread_ts
        )


    def add_reaction(self, reaction, timestamp):
        self.client.api_call(
            "reactions.add" ,
            channel = self.get_channel_id(),
            name = reaction,
            timestamp = timestamp
        )


    def remove_reaction(self, reaction, timestamp):
        self.client.api_call(
            "reactions.remove" ,
            channel = self.get_channel_id(),
            name = reaction,
            timestamp = timestamp
        )
