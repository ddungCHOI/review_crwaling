import tweepy

consumer_key = ""
consumer_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

access_token = ""
access_token_secret = ""
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

keyword = "토토디비"; #해시태그 키워드

search = []

cnt = 4
while(cnt <= 10):
    tweets = api.search(keyword)
    for tweet in tweets:
        search.append(tweet)
    cnt += 1

data = {}   # 전체 문서
i = 0       # 문서 번호

for tweet in search:
    data['text'] = tweet.text # text키에 text문서 저장
    print(i, "=", data)   # 파일 출력
    i += 1