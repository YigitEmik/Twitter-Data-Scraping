import snscrape.modules.twitter as sntwitter
import pandas as pd
userlist = ["haveibeenpwned","DataBreachToday","DS_Watch","ShieldSure","Experian_DBR",
            "S0ufi4n3","cyber_etc","ransomwaremap" ,"AcooEdi","DataConnectUK"]

for x in userlist:
    query ="(from:"+x+")"
    tweets= []
    limit= 500
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():

        #print(vars(tweet))
        #break
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.date, tweet.user.
                           username, tweet.content])

    df = pd.DataFrame(tweets, columns=['Data','User','Tweet'])
    df.to_csv('GFG.csv', mode='a', index=False, header=False)
# with open("tweets.csv", "w", encoding="utf-8") as f:
#     f.write(str(abc))



