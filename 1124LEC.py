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

import FinanceDataReader as fdr

# ksp =fdr.DataReader("KS11", "2001")
# print(ksp)
print("\n---------------------------\n")

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
import pandas as pd


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

target = "./data/apt.csv"

df = pd.read_csv("./data/conv_apt.csv", index_col=0)

# print(df.head())

df = df.rename(columns={"분양가격(제곱미터)":"분양가"})
# print(df)
# print(df.dtypes)

df["분양가"] = df["분양가"].convert_dtypes()
# print(df.dtypes)

#convert the array

arr = df.to_numpy()
# print(arr)
# print(len(arr))

#요약정보
# print(df.describe())

print(df.transpose())
print("\n---------------------------\n")
print(df.T.head())