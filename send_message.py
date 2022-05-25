from twilio.rest import Client

account_sid = "ACcd49bca30e72044b6f40e0d5342f8fcb"

account_token = "1f905170a267192551bc4863099b2762"

my_cell = "+8801775482822"

my_twilio_cell = "+12058583048"

client = Client(account_sid, account_token)

my_msg = "Whats app"

message = client.messages.create(to=my_cell, from_=my_twilio_cell, body=my_msg)
