""" from faker import Faker as fk
import os

folder = "data/"
if not os.path.isdir(folder) :
    os.mkdir(folder)

temp = fk("ko-KR")
with open(folder + "fktemp.csv", "w", encoding='utf8') as f :
    f.write("name,address,postcode,company,job,phone,email,id,ip_prv,ip_pub,catch_parase,color\n")

with open(folder + "fktemp.csv", "a", newline='', encoding='utf8') as f :
    for i in range(30) :
        f.write(temp.name() + "," + 
            temp.address() + "," + 
            temp.postcode() + "," + 
            temp.company() + "," + 
            temp.job() + "," + 
            temp.phone_number() + "," + 
            temp.email() + "," + 
            temp.user_name() + "," + 
            temp.ipv4_private() + "," + 
            temp.ipv4_public() + "," + 
            temp.catch_phrase() + "," + 
            temp.color_name() + "\n") """

#Ranking

""" import pandas as pd

folder = "data/"
target = folder +"fktemp.csv"

df = pd.read_csv(target)
 """
# df["aver"] = df.postcode.rank(method="average")
# print(df[["postcode","aver"]])

# df["dense"] = df.postcode.rank(method="dense")
# print(df[["postcode","dense"]])

# df["first"] = df.postcode.rank(method="first")
# print(df[["postcode","first"]])

# df["min"] = df.postcode.rank(method="min")
# print(df[["postcode","min"]])

# df["max"] = df.postcode.rank(method="max")
# df["max"] = df.postcode.rank(method="max", ascending = False)
# print(df[["postcode","max"]])

# print(df[["postcode", "max", "min","first","aver", 'dense']])

# 컬럼-로우 변경
# print(df.transpose())

# ### 누적계산
# print(df["postcode"].expanding().sum())
# print(df["postcode"].expanding().max())

# 정렬 찾기
#smallest
# print(df.postcode.idxmax(axis=0))
#largest
# print(df.postcode.idxmin(axis=0))

# 빈 DataFrame  확인
# print(df.color.empty)

# print(df.isin([11559]))
# print(df.isin(["김은주"]))

# print(df.isin([17457,40556]))
# print(df.isin([11559,17457,"김은주"]))

# 기간 계산
# period = pd.period_range(start="2023-11-10 00:00:00", end="2023-11-10 02:30:00", freq="30T")
# dt = {"col1":[1,2,3,4,5,6],"col2":period}
# idx = ["row1","row2","row3","row4","row5","row6"]
# df=pd.DataFrame(data=dt,index=idx)
# print(df)


""" i = pd.date_range("2023-11-10", periods=10, freq="1H")
i = pd.date_range("2023-11-10", periods=10, freq="3H")
df = pd.DataFrame({"col1":[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df) """

""" period = pd.period_range(start="2023-11-10 00:00:00", end="2023-11-10 02:30:00", freq="30T")
dt = {"col1":[1,2,3,4,5,6],"col2":period}
idx = ["row1","row2","row3","row4","row5","row6"]

print(period)

i = pd.date_range("2023-11-10", periods=10, freq="3D")
df = pd.DataFrame({'col1':[1,2,3,4,5,6,7,8,9,10]}, index=i)

# print(df.first("3D"))

print(df.last("7D")) """


#kospi

#import FinanceDataReader as fdr

# ksp =fdr.DataReader("KS11", "2001")
# print(ksp)
#print("\n---------------------------\n")

# print(ksp["High"].max())
# print(ksp["High"].idxmax())

#최저가 확인
# res = ksp["Low"].min()
# res = ksp["Low"].idxmin()
# print(res)

# 최고가 값 찾기
""" res = ksp["Volume"].nlargest(n=5) """
# res = ksp["Volume"].nlargest(n=10)
# print(res)

# 최하위 값 찾기
# res = ksp["Volume"].nsmallest(n=5)
# res = ksp["Close"].nsmallest(n=5)
# print(res)

# kospi 3000 달성 최초일 찾기
# cond = ksp["Close"] >= 3000
# res = ksp[cond].index[0]
# print(res)

#위(shift) 값 참조, 처리
# ksp["Volume"] > ksp["Volume"].shift()
# print(ksp)

# ksp["up"] != ksp["up"].shift().cumsum()
# print(ksp)

# ksp["grp"] = (ksp["up"] != ksp["up"].shift.cumsum())
# print(ksp)

# 연속 증가값 확인
# ksp["grp"].groupby(ksp["grp"].values).cumcount() + 1
# print(ksp)

# print(ksp["up_cnt"].max())


#부동산 정보 처리
# import pandas as pd


""" target = "./data/apt.csv"

df = pd.read_csv(target, encoding = "CP949")

df.to_csv("./data/apttt.csv", encoding="utf8")

df.read_csv(target, encoding="CP949")
df.to_csv("./data/apttt.csv", encoding="utf8") """


""" target = "./data/apt.csv"

df = pd.read_csv(target, encoding = "CP949")

df.to_csv("./data/conv_apt.csv", encoding="utf8")
print(df.head()) """


""" df = pd.read_csv("./data/conv_apt.csv", index_col=0)

print(df.head()) """

# 컬럼명 바꾸기

#target = "./data/apt.csv"

# df = pd.read_csv("./data/conv_apt.csv", index_col=0)

# print(df.head())

# df = df.rename(columns={"분양가격(제곱미터)":"분양가"})
# print(df)
# print(df.dtypes)

# df["분양가"] = df["분양가"].convert_dtypes()
# print(df.dtypes)

#convert the array

# arr = df.to_numpy()
# print(arr)
# print(len(arr))

#요약정보
# print(df.describe())

""" print(df.transpose())
print("\n---------------------------\n")
print(df.T.head()) """


################################################################
################################################################

#11.27 lec

# 변환
# import pandas as pd

# target = "data/apt.csv"

# df = pd.read_csv(target, encoding="CP949")
# print(df.head())

# df.to_csv("data/apt.csv", encoding="utf8")

# df = pd.read_csv("data/apt.csv", index_col=0)

# 컬럼명 바꾸기

# df = df.rename(columns={"분양가격(제곱미터)":"분양가"})
# print(df)
# print(df.dtypes)

# df["분양가"] = df["분양가"].convert_dtypes()
# print(df.dtypes)
# print("\n--------------------------\n")

# 정렬
# res = df.sort_values(by="지역명")[:5]
# print(res)

# res = df.sort_values(by="지역명")
# res = df.sort_values(by="지역명")
# res = df.sort_values(by="지역명", ascending=False)
# res = df.sort_values(by="지역명", ascending=True) #디폴트
# print(res.head()) # n개 출력

# res = df.sort_values(by="연도")
# res = df.sort_values(by="분양가")
# res = df.sort_values(by="연도")[:5]
# print(res)
# print(res.head())

# 컬럼이름 출력
# res = df[["지역명"]][:5]
# res = df[["지역명"]]
# res = df[:, ["지역명", "연도","분양가"]] -> error
# res = df[:, ["지역명", "연도","분양가"]][:7]
# res = df[["지역명", "연도"]][:5]
# print(res)

# print("\n--------------------------\n")
# res = df.loc[:, ["지역명", "연도","분양가"]][:7]
# print(res)

# res = df.loc[:][:5]
# res = df.loc[:][:] -> 처음부터 끝까지 출력
# print(res)
# res = df.loc[:6, ["지역명", "연도"]] 6까지 출력
# res = df.loc[6:, ["지역명", "연도"]] 6부터 출력

# res = df.iloc[1] - > 행번호 1번 출력
# # print(res)

# res = df.loc[:3, ["지역명", "연도"]][:8]
# print(res)

# 필터 출력
# res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]]
# 전체 data 출력됨
# res = df.loc[df["지역명"]=="강원"]
# res = df.loc[df["연도"] > 2020]
# res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]][:16]
# res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]][-10:] -> 끝에서부터 출력
# print(res)

# 인덱스 지정 선택
# df0 = df.copy()
# print(df0) # 동일한 내용 copy

# print("\n--------------------------\n")
# res = df.iloc[2]
# res = df.iloc[2][2]
# print(res)

# 인덱스 필터
# res = df[df.index > 3560] # 3561번부터 출력
# print(res)

# 비트 연산 필터'
# res = df[df.연도 == 2023]
# res = df[df.월 == 3]
# res = df[(df.연도 == 2023) & (df.지역명 == "서울") & (df.월 == 6)]
# print(res)

# 컬럼 추가

# columns = list(df.columns)
# print(columns)

# df1 = df.reindex(index=df.index[:7], columns=list(df.columns) + ["extra"])
# df1 = df.reindex(columns=list(df.columns) + ["extra"])
# print(df)
# print("\n--------------------------\n")
# print(df1)

# print("\n--------------------------\n")
# df1.loc[:6, "extra"] = "0"
# df1.loc[:4, "extra"] = False
# print(df1)

# 복사
# df2 = df1.copy()

# Nan 제거
# res = df2.dropna(how="any")
# res = df2.fillna(value="text")
# print(res)
# res = df2.fillna(value="1234")
# print(df2)
# print("\n--------------------------\n")

# res = df2.dropna(how="any", inplace=True) -> 삭제한다는 뜻
# print(res)
# print("\n--------------------------\n")
# print(df2)

# Nan 데이터 출력
# res = pd.isna(df1)
# print(res)

###################################################################
###################################################################
### 23.12.01

# from faker import Faker as fk
# import os
import pandas as pd

tr = pd.read_csv("data/train.csv")

# print(tr)
# print("\n------------------------------\n")
# print(tr.head())



# res = tr.isnull().sum()
# print(res)

# # 승선지
print("\n------------------------------\n")
res = pd.crosstab(tr["Embarked"], tr["Survived"])
# print(res)
# print("\n------------------------------\n")
# 컬럼 매핑
res.columns = res.columns.map({0:"Dead", 1:"Alive"})
# print(res)

# # age
res = pd.crosstab(tr["Age"], tr["Survived"])
# print(res)

# res.columns = res.columns.map({0:"Dead", 1:"Alive"})
# print(res)

# # passenger class
res = pd.crosstab(tr["Pclass"], tr["Survived"])
# print(res)

# # 성별별
# print("\n------------------------------\n")
# res = pd.crosstab(tr["Sex"], tr["Survived"])
# print(res)

# # 호칭별 구분

tr["Title"] = tr.Name.str.extract(" ([A-Za-z]+)\.")
res = tr["Title"].value_counts()
# print(res)

tr["Title"] = tr["Title"].replace(["Capt", "Col", "Countess", "Don","Dona", "Dr", "Jonkheer", "Lady","Major", "Rev", "Sir"], "Other")
tr["Title"] = tr["Title"].replace("Mlle", "Miss")
tr["Title"] = tr["Title"].replace("Mme", "Mrs")
tr["Title"] = tr["Title"].replace("Ms", "Miss")
tr["Title"].value_counts()

# print(res)

# # age 별 Null 확인

# print(tr["Age"].isnull())
# print(tr["Age"].isnull().sum())

meanAge = tr[["Title", "Age"]].groupby(["Title"]).mean()
# print(meanAge)
# print(tr["Age"].head(20))

# # 빈 나이 평균값 채워넣기

# print("\n------------------------------\n")

for index, row in meanAge.iterrows():
    nullIndex = tr[(tr.Title == index) & (tr.Age.isnull())].index
    # print(nullIndex, index, row[0])
    tr.loc[nullIndex, "Age"] = row[0]

# print(tr)

# print(tr["Age"].head(20))
# print(tr["Age"].isnull().sum())

# 나이 구간 나누기
tr["AgeCate"] = pd.qcut(tr.Age, 8, labels=range(1, 9))
# print(tr.head())
# print(tr.dtypes)
# print("\n------------------------------\n")

tr.AgeCate = tr.AgeCate.astype(int)
# print(tr.head())
# print(tr.dtypes)

tr["CabinCate"] = tr["Cabin"].str.slice(start=0, stop=1)
# print(tr["CabinCate"].value_counts())
# print(tr)
# print("\n------------------------------\n")

# # 객실
tr["CabinCate"] = tr["CabinCate"].map({ "N": 0, "C": 1, "B": 2, "D": 3, "E": 4, "A": 5, "F": 6, "G": 7, "T": 8 })
tr.CabinCate = tr.CabinCate.astype
# print(tr.dtypes)
# print(tr)

res = pd.crosstab(tr["CabinCate"], tr["Survived"])
# print(res)

# # 요금
# print(tr.Fare)

# # 요금컬럼
tr["FareCate"] = pd.qcut(tr.Fare, 8, labels=range(1, 9))
tr["FareCate"] = pd.qcut(tr.Fare, 5, labels=range(1, 6))
tr.FareCate = tr.FareCate.astype(int)
#print(tr)
#print(tr["FareCate"].value_counts())

res = pd.crosstab(tr["FareCate"], tr["Survived"])
# print(res)

# # 아이리스 정보 처리

df = pd.read_csv("./data/Iris.csv", index_col="Id")
print(df.head())

""" ir = df.rename(columns={
    "SepalLengthCm": "꽃받침길이",
    "SepalWidthCm": "꽃받침너비",
    "PetalLengthCm": "꽃잎길이",
    "PetalWidthCm": "꽃잎너비", 
    "Species": "품종"},
    inplace=True
) """

ir = df.rename(columns={
    "SepalLengthCm": "꽃받침길이",
    "SepalWidthCm": "꽃받침너비",
    "PetalLengthCm": "꽃잎길이",
    "PetalWidthCm": "꽃잎너비", 
    "Species": "품종"},)

# print(ir.head())


# print("\n------------------------------\n")
res = ir.iloc[:, [0, 1, 4]]
# print(res)

ir["품종"] = ir["품종"].str[5:]
# print(ir)

res = ir.groupby("품종").mean()
# print(res)

res = ir["품종"].value_counts()
# print(res)


# # # 시각화 처리

import matplotlib.pyplot as plt

# # y축 데이터 지정 구성

# value = [1, 2, 3, 4]
""" value = [2,4,5,7,10]
res = plt.plot(value) """
# plt.show()

# # 두 축 지정 구성

""" x_value = [2, 3, 6, 7, 10 ]
y_value = [1, 4, 5, 8, 9]

plt.plot(x_value, y_value) """
# plt.plot([2, 3, 6, 7, 10 ], [1, 4, 5, 8, 9])
# plt.show()

# # 딕셔너리
""" dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)
plt.show() """

# # label setting

""" dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)

plt.xlabel("x_data", labelpad = 10, loc="right")
plt.ylabel("y_data",loc="top")
plt.show() """

# # 다중데이터 출력
""" dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y1_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val)
plt.plot("x1_data", "y1_data", data=dic1_val)
plt.show() """

# # 라벨 출력
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val, label="PData(km)")
plt.xlabel("x-data")
plt.ylabel("y_data")
plt.legend()

