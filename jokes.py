import requests

def get_jokes(srch_for):
    jokes = []
    hdr = {"Accept":"application/json"}
    if srch_for == "":
        url = "https://icanhazdadjoke.com"
        response = requests.get(url,headers=hdr)
        jokes.append(response.json()['joke'])
    else:
        url = "https://icanhazdadjoke.com/search"
        response = requests.get(url,params={"term":srch_for},headers=hdr)
        results = response.json()['results']
        cnt = 0
        for j in results:
            cnt += 1
            jokes.append(j['joke'])
            if cnt >= 10:
                break
    return jokes

msg = "Want to hear a joke?\n1)Just press enter to get a random joke or\n2)Enter a joke subject to search for\n>>>"    
user_input = input(msg)
jokes = get_jokes(user_input)
cnt = 1
for j in jokes:
    print(cnt,") ",j)
    cnt += 1
