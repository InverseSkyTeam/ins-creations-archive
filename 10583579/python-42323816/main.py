import requests
import json

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

json_data = {
    'query': '\n    query questionOfToday {\n  todayRecord {\n    date\n    userStatus\n    question {\n      questionId\n      frontendQuestionId: questionFrontendId\n      difficulty\n      title\n      titleCn: translatedTitle\n      titleSlug\n      paidOnly: isPaidOnly\n      freqBar\n      isFavor\n      acRate\n      status\n      solutionNum\n      hasVideoSolution\n      topicTags {\n        name\n        nameTranslated: translatedName\n        id\n      }\n      extra {\n        topCompanyTags {\n          imgUrl\n          slug\n          numSubscribed\n        }\n      }\n    }\n    lastSubmission {\n      id\n    }\n  }\n}\n    ',
    'variables': {},
}

response = requests.post('https://leetcode.cn/graphql/', headers=headers, json=json_data)

data = json.loads(response.text)['data']['todayRecord'][0]

difficulty = {"Easy":"简单", "Medium":"中等", "Hard":"困难"}
difficulty_color = {"Easy":"green", "Medium":"yellow", "Hard":"red"}

class Color:
    def __init__(self) -> None:
        self.colordict = {
            "red":"\033[91m",
            "yellow":"\033[93m",
            "green":"\033[92m",
            "blue":"\033[34m",
            "purple":"\033[95m",
            "white":"\033[0m",
            "cyan":"\033[96m"
        }

    def convert(self,string,color):
        return self.colordict[color]+string+self.colordict["white"]

color = Color()

# print(data)
print()
print(f"\t{color.colordict['purple']}日期\t{color.convert(data['date'], 'blue')}\n")
print(f"\t{color.colordict['purple']}题目\t{color.convert(data['question']['frontendQuestionId']+'.'+data['question']['titleCn'], 'cyan')}\n")
print(f"\t{color.colordict['purple']}难度\t{color.convert(difficulty[data['question']['difficulty']], difficulty_color[data['question']['difficulty']])}\n")
print(f"\t{color.colordict['purple']}通过率\t{color.convert(str(round(data['question']['acRate']*100,1))+'%', 'cyan')}\n")
print(f"\t{color.colordict['purple']}标签\t{color.convert(' '.join([i['nameTranslated'] for i in data['question']['topicTags']]), 'green')}\n")
print(f"\t{color.colordict['purple']}题解\t{color.convert(str(data['question']['solutionNum']), 'green')}")
print()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

json_data = {
    'query': '\n    query questionTranslations($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    translatedTitle\n    translatedContent\n  }\n}\n    ',
    'variables': {
        'titleSlug': "-".join(data["question"]["title"].split()),
    },
    'operationName': 'questionTranslations',
}

response = requests.post('https://leetcode.cn/graphql/', headers=headers, json=json_data)

with open("index.html","w") as f:
    f.write(response.json()['data']['question']['translatedContent'])
f.close()

import os
os.startfile("index.html")