from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
from nike import (
	stack,
	size
)
message = ''
i = 0
while i < size:
    message += stack[i]
    if i < (size-1):
    	message += '\n'
    i += 1

length = 0
for char in message:
	length += 1

if length > 280:
	message = 'There are too many upcoming sneakers to fit in a tweet! \nCheck out the release calendar here: https://goo.gl/XreX7P'