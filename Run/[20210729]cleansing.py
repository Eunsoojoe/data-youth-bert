import pandas as pd 
import re
import pandas as pd
import os
from IPython import display

# 이모티콘 제거
emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002702-\U000027B0"
        u"\u2640-\u2642"
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
        u"\U00010000-\U0010ffff""]+", flags=re.UNICODE)


# html 태그 
cleanr1 = re.compile('</?br/?>')
cleanr2 = re.compile('/?&quot/?')
cleanr3 = re.compile('/?&lt/?')
cleanr4 = re.compile('</?a href.*/?>')
cleanr5 = re.compile('/?&gt/?')
cleanr6 = re.compile('</?i/?>')
cleanr7 = re.compile('/?j&amp;j/?')
cleanr8 = re.compile('/?&#39;/?')
cleanr9 = re.compile('https*')

import pandas as pd
from IPython import display

file_name = 'Output\comments_union\최종_웹사이트.xlsx'
df = pd.read_excel(file_name)
print(df)

comment_result = []

# 이모티콘, html 태그 삭제
for i in range(len(df)):
    tokens = re.sub(emoji_pattern,"",df['command'].iloc[i])
    tokens = re.sub(cleanr1,"",tokens)
    tokens = re.sub(cleanr2,"",tokens)
    tokens = re.sub(cleanr3,"",tokens)
    tokens = re.sub(cleanr4,"",tokens)
    tokens = re.sub(cleanr5,"",tokens)
    tokens = re.sub(cleanr6,"",tokens)
    tokens = re.sub(cleanr7,"",tokens)
    tokens = re.sub(cleanr8,"",tokens)
    tokens = re.sub(cleanr9,"",tokens)
   
    comment_result.append(tokens)

# 정제된 댓글 데이터 프레임 생성
comment_result = pd.DataFrame(comment_result, columns=["command"])
df['new_command'] = comment_result

print(df)
df.head()


# 엑셀로 저장
import pandas as pd
import openpyxl



df.to_excel("(정제)최종_웹사이트.xlsx")
df.head()