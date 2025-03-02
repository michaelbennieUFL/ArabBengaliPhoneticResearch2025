import requests


def getFrequency(word)->float:
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Referer': 'https://ngrams.dev/',
        'Origin': 'https://ngrams.dev',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Priority': 'u=0',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        'query': word,
        'flags': 'cs',
    }

    response = requests.get('https://api.ngrams.dev/eng/search', params=params, headers=headers)
    return float(response.json()["ngrams"][0]["relTotalMatchCount"])



def getFrequencyOfMostCommon(word)->float:
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Referer': 'https://ngrams.dev/',
        'Origin': 'https://ngrams.dev',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Priority': 'u=0',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        'query': word,
    }

    response = requests.get('https://api.ngrams.dev/eng/search', params=params, headers=headers)
    return response.json()["ngrams"][0]["tokens"][0]["text"],float(response.json()["ngrams"][0]["relTotalMatchCount"])



if __name__ == "__main__":
    print("fish",getFrequency("fish"))
    print("FISH",getFrequency("FISH"))
    print("FISH(most common)",getFrequencyOfMostCommon("FISH"))