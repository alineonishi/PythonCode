# -*- coding: utf-8 -*-
from twilio import rest

account_sid = 'AC9d9222be8cd3e02e66633c8297aef1dc' # Your Account SID from www.twilio.com/console
auth_token  = '256da40d6fda7c9c6f7a7825989fdf6b'  # Your Auth Token from www.twilio.com/console

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body='Teste2',
    to='+5511993425021',    # Replace with your phone number
    from_='+19145065905') # Replace with your Twilio number

print message.sid