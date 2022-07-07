import twilio
from twilio.rest import Client
import random
otp=''.join([str(random.randint(0,9)) for i in range(4)])
print(otp)
Clienmt=Client("AC892de81ef8f9dcf7f7ae04ac84dac799", "deb4540b03069adfe2385ea5418234ea" )
my_no="+917719818494"
my_twiliono="+19706590551"
messagesms=Clienmt.messages(f'Your otp is  {otp} Please verify it....')
Clienmt.messages.create(to=my_no, from_= my_twiliono, body=messagesms)
a=input("Enter the OTP here:")
a1=int(a)
b=int(otp)
if a1==b:
    print("entered otp is correct")
else:
    print("Entered OTP is not correct")
