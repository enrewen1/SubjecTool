# -*- coding: utf-8 -*-
import FileControl 
import re
control = FileControl.inputMode("subjectFile.txt")

str1=re.split("\n|\t",str(control.getData()).replace("\r","").replace("\ufeff",""))



i=0
count=0
matrix=[["" for x in range(4)] for x in range(100)] 
notGood=[] 
while(count<len(str1)/5):
    if(i+4>len(str1)):
            break
    try:
        if(float(str1[i+4])<60):
            notGood.append(str1[i]+":"+str1[i+4]+"分")
            i+=5        
    except:
        if(i>len(str1)):
            break
        #print("ERROR score"+str1[i+4])
        
    j=0
    matrix[count][j]=str1[i]
    j+=1
    i+=1
    matrix[count][j]=str1[i]
    i+=2
    j+=1
    matrix[count][j]=str1[i]
    i+=1
    j+=1
    matrix[count][j]=str1[i]
    i+=1
    count+=1

for x in range(count):
    print("\t",x+1,end="")
    for y in matrix[x]:
        print(y,end="\t")
    print()
control.closeMode()
print("修得科目有: "+str(count)+" 門")


for x in range(len(notGood)):
    print("\t",str(x+1)+notGood[x])
print("未修得科目有: "+str(len(notGood))+" 門")

print("***************開始檢查應修學分***************".center(80))
#s1
s11=["科技與社會","歷史與文化","進階英文","學習與服務","民主與法治"]
s12=["國文","英文（"]
s13=["      "]
s14=["體育"]
s15=["通識"]
s1=[ s11
    ,s12
    ,s13
    ,s14]

print("校定必修:")

c=1
for i in s1:
    
    for j in i:
        cc=c
        print("\t",j)
        if(j)==s13[0]:
            continue
        for k in range(count):
            if(matrix[k][0].find(j)>=0):
                cc-=1
                print("\t\t"+matrix[k][0])
        if(cc>0):
            print("\t\t\t\t\t缺"+str(cc)+"門")
        
    c+=1
#s2
s21=["電路實驗","計算機概論","計算機實習","工程數學(一)","程式語言","電磁學","電磁波"
     ,"工程數學(二)","電子學(一)","電子實驗(一)","訊號與系統","電子學(二)"]
s22=["微積分","普通物理","電路學"]

s2=[ s21
    ,s22]

print("專業必修:")            
c=1
for i in s2:
    
    for j in i:
        cc=c
        print("\t",j)
        for k in range(count):
            if(matrix[k][0].find(j)>=0):
                cc-=1
                print("\t\t"+matrix[k][0])
        if(cc>0):
            print("\t\t\t\t\t缺"+str(cc)+"門")
        
    c+=1
#s3
s3={"控制程式","高階C語言","Matlab","軟體工程","資料結構","物件導向程式"}
print("專業選修:")
cc=2
print("\t","電腦:")
for j in range(count):
    for i in s3:
        if(matrix[j][0].find(i)>=0):
            cc-=1
            print("\t\t"+matrix[j][0])
            
if(cc>0):
        print("\t\t\t\t\t缺"+str(cc)+"門")
        
s3={"數位邏輯設計","微算機系統","半導體物理","通訊電子學","電子學(三)","光電半導體"}

cc=3
print("\t","電子:")
for j in range(count):
    for i in s3:
        if(matrix[j][0].find(i)>=0):
            cc-=1
            print("\t\t"+matrix[j][0])
            
if(cc>0):
        print("\t\t\t\t\t缺"+str(cc)+"門")
        
s3={"應用光學","通訊系統導論"}

cc=2
print("\t","光電通訊基礎核心課程:")
for j in range(count):
    for i in s3:
        if(matrix[j][0].find(i)>=0):
            if(matrix[j][0].find("實驗")>=0):
                break
            cc-=1
            print("\t\t"+matrix[j][0])
            
if(cc>0):
        print("\t\t\t\t\t缺"+str(cc)+"門")
        
s3={"複變函數","通訊原理(一)","數位訊號處理","無線電波與天線理論","射頻微波電路設計"
    ,"通訊網路","鎖相技術與頻率合成","展頻通訊原理","傅氏分析 ","錯誤更正碼概論"
    ,"網路安全導論","數位傳輸 ","微波工程","高頻電路設計 ","交換系統","通訊 VLSI 設計"
    ,"寬頻交換網路","電磁相容","天線工程","行動與室內無線通訊","數據通訊","影像處理"
    ,"窄頻通訊","無線通訊系統模擬","統計訊號處理","通訊原理(二)","天線理論"
    ,"數位通訊導論","數位通訊系統","隨機程序","區域網路","網路程式設計","遙感測原理"
    ,"機率","線性代數"}

cc=5
print("\t","通訊專業選修:")
for j in range(count):
    for i in s3:
        if(matrix[j][0].find(i)>=0):
            if(matrix[j][0].find("實驗")>=0):
                break
            cc-=1
            print("\t\t"+matrix[j][0])
            
if(cc>0):
        print("\t\t\t\t\t缺"+str(cc)+"門")
        
s3={"光電工程導論","近代物理","光通訊","光學設計","光資訊儲存"
    ,"雷射工程導論","顯示器導論","晶體光學","光感測系統","光通訊元件基本原理"
    ,"光電子學","光學模擬軟體應用設計","微光學元件","顯示器製作與量測實驗","顯示器色彩學"
    ,"光通訊系統","綠能科技","太陽能工程導論","薄膜蒸鍍技術","光檢測技術"
    ,"量子光學導論","液晶顯示元件","傅氏光學","非線性光學","半導體感測技術"
    ,"高密度分波多工通訊","顯示光學","光纖放大器","偏極光及其應用","全像術"
    ,"雷射技術及其應用"}

cc=5
print("\t","光電專業選修:")
for j in range(count):
    for i in s3:
        if(matrix[j][0].find(i)>=0):
            if(matrix[j][0].find("實驗")>=0):
                break
            cc-=1
            print("\t\t"+matrix[j][0])
            
if(cc>0):
        print("\t\t\t\t\t缺"+str(cc)+"門")

s3={"通訊系統實驗","電子實驗(二)","應用光學實驗"}

cc=2
print("\t","基礎選修實驗:")
for j in range(count):
    for i in s3:
        if(matrix[j][0].find(i)>=0):
            cc-=1
            print("\t\t"+matrix[j][0])
            
if(cc>0):
        print("\t\t\t\t\t缺"+str(cc)+"門")

s3={"微算機實驗","數位信號處理實驗","無線通訊電路實驗","射頻微波電路實驗"
    ,"類比電子實驗","通訊網路實驗","光通訊實驗","光感測系統實驗","顯示器製作與量測實驗"}

cc=4
print("\t","專業選修實驗:")
for j in range(count):
    for i in s3:
        if(matrix[j][0].find(i)>=0):
            cc-=1
            print("\t\t"+matrix[j][0])
            
if(cc>0):
        print("\t\t\t\t\t缺"+str(cc)+"門")
input("任意鍵離開")
