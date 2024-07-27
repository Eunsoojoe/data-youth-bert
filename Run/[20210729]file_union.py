# 엑셀파일 concat 하기
import pandas as pd
import numpy as np
import glob
import sys

"""
#파일Union
all_data = pd.DataFrame()
for f in glob.glob('Output/daum_comments_raw/백신_*xlsx'): # 예를들어 201901, 201902 로 된 파일이면 2019_*
    df = pd.read_excel(f)
    all_data = all_data.append(df, ignore_index=True)

#데이터갯수확인
print(all_data.shape)

#데이터 잘 들어오는지 확인
all_data.head()

#파일저장
all_data.to_excel("Output/daum_comments_union/백신접종_다음.xlsx", header=False, index=False)
"""



# 이름이 다른 파일들 concat 하기
import pandas as pd  
import sys


#엑셀 파일 이름 입력
excel_names = ['Output\comments_union\최종_네이버.xlsx', 'Output\comments_union\최종_다음.xlsx']  
excels = [pd.ExcelFile(name) for name in excel_names]  
frames = [x.parse(x.sheet_names[0], header=None,index_col=None) for x in excels]  
frames[1:] = [df[1:] for df in frames[1:]]  
combined = pd.concat(frames)

#파일저장

combined.to_excel("Output/comments_union/최종_웹사이트.xlsx", header=False, index=False)
