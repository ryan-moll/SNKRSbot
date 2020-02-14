from twython import TwythonStreamer, TwythonError
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            print('@{} tweeted the keyword.'.format(username))
            from twitter import (
                message,
                twitter
            )
            finalPrint = '@'
            finalPrint += username
            finalPrint += '\n'
            finalPrint += message
            try:
                a = twitter.update_status(status=finalPrint, in_reply_to_status_id=data['id'])
                print('Tweet sent!')
            except TwythonError as e:
                print('ERROR: The tweet could not be sent.')

stream = MyStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
stream.statuses.filter(track="What's dropping on SNKRS?")