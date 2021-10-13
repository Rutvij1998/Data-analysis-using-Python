import pandas as pd
import numpy as np
from collections import Counter  #It is used to count the number of occurences in this case "?"
import matplotlib.pyplot as plt #It is used for plotting the data in graphical way
count = 0
out = open('clean_data.csv','w')
out1 = open('removed_clean_data.csv','w')
for line in open('data.csv','r'):
  if("?" in line):
    count +=1
    out1.write(line) 
  else:
    out.write(line)

print("The number of rows which has \'?\' mark :", count)
data1 = pd.read_csv("clean_data.csv", header = None)
data1.columns = ['Age','Workclass','fnlwgt','education','education-num','marital-status','Occupation',
                 'relationship','race','sex','capital-gain','capital-loss','hours-per-week',
                 'native-country','Salary']
data1.head(5)
part1 = 0
part1_private=0
part1_SelfEmp=0
part1_gov = 0
part1_withoutPay = 0
part1_doc_male = 0
part1_masters_male = 0
part1_12_male = 0
part1_hs_male = 0
part1_doc_female = 0
part1_masters_female = 0
part1_12_female = 0
part1_hs_female = 0
part2 = 0
part2_private = 0
part2_SelfEmp = 0
part2_gov=0
part2_withoutPay = 0
part2_doc_male = 0
part2_masters_male = 0
part2_12_male = 0
part2_hs_male = 0
part2_doc_female = 0
part2_masters_female = 0
part2_12_female = 0
part2_hs_female = 0
part3 = 0
part3_private=0
part3_SelfEmp=0
part3_gov = 0
part3_withoutPay = 0
part3_doc_male = 0
part3_masters_male = 0
part3_12_male = 0
part3_hs_male = 0
part3_doc_female = 0
part3_masters_female = 0
part3_12_female = 0
part3_hs_female = 0
part4 = 0
part4_private=0
part4_SelfEmp=0
part4_gov = 0
part4_withoutPay = 0
part4_doc_male = 0
part4_masters_male = 0
part4_12_male = 0
part4_hs_male = 0
part4_doc_female = 0
part4_masters_female = 0
part4_12_female = 0
part4_hs_female = 0
for index, row, in data1.iterrows():
  if(row[0]<21):
    part1 += 1
    if "Male" in row[9]:
      if "Doctorate" in row[3]:
        part1_doc_male += 1
      elif "Masters" in row[3]:
        part1_masters_male += 1
      elif "12" in row[3]:
        part1_12_male += 1
      elif "HS-grad" in row[3]:
        part1_hs_male += 1
    elif "Female" in row[9]:
      if "Doctorate" in row[3]:
        part1_doc_female += 1
      elif "Masters" in row[3]:
        part1_masters_female += 1
      elif "12" in row[3]:
        part1_12_female += 1
      elif "HS-grad" in row[3]:
        part1_hs_female += 1
    if "Private" in row[1]:
      part1_private += 1
    elif "gov" in row[1]:
      part1_gov += 1
    elif "Self-emp" in row[1]:
      part1_SelfEmp += 1
    elif "Without-pay" in row[1]:
      part1_withoutPay += 1
part1_emp_total = part1_private+part1_SelfEmp+part1_gov+part1_withoutPay
print("Employed : ",part1_emp_total)
print("Total population :",part1)
for index, row, in data1.iterrows():
  if row[0] > 20 and row[0] <= 40:
    part2 += 1
    if "Male" in row[9]:
      if "Doctorate" in row[3]:
        part2_doc_male += 1
      elif "Masters" in row[3]:
        part2_masters_male += 1
      elif "12" in row[3]:
        part2_12_male += 1
      elif "HS-grad" in row[3]:
        part2_hs_male += 1
    elif "Female" in row[9]:
      if "Doctorate" in row[3]:
        part2_doc_female += 1
      elif "Masters" in row[3]:
        part2_masters_female += 1
      elif "12" in row[3]:
        part2_12_female += 1
      elif "HS-grad" in row[3]:
        part2_hs_female += 1
    if "Private" in row[1]:
      part2_private +=1
    elif "Self-emp" in row[1]:
      part2_SelfEmp += 1
    elif "gov" in row[1]:
      part2_gov += 1
    elif "Without-pay" in row[1]:
      part2_withoutPay += 1
part2_emp_total = part2_private + part2_SelfEmp + part2_gov + part2_withoutPay
print("total population",part2,"Working :",part2_emp_total)
for index, row, in data1.iterrows():
  if row[0] >= 41 and row[0] <= 60:
      part3 += 1
      if "Male" in row[9]:
        if "Doctorate" in row[3]:
          part3_doc_male += 1
        elif "Masters" in row[3]:
          part3_masters_male += 1
        elif "12" in row[3]:
          part3_12_male += 1
        elif "HS-grad" in row[3]:
          part3_hs_male += 1
      elif "Female" in row[9]:
        if "Doctorate" in row[3]:
          part3_doc_female += 1
        elif "Masters" in row[3]:
          part3_masters_female += 1
        elif "12" in row[3]:
          part3_12_female += 1
        elif "HS-grad" in row[3]:
          part3_hs_female += 1
      if "Private" in row[1]:
        part3_private += 1
      elif "Self-emp" in row[1]:
        part3_SelfEmp += 1
      elif "gov" in row[1]:
        part3_gov += 1
      elif "Without-pay" in row[1]:
        part3_withoutPay +=1
      else:
        other3 +=1
part3_emp_total = part3_private+part3_SelfEmp+part3_gov+part3_withoutPay
print("total population",part3,"Working :",part3_emp_total)
for index, row, in data1.iterrows():
  if row[0] > 61:
      part4 += 1
      if "Male" in row[9]:
        if "Doctorate" in row[3]:
          part4_doc_male += 1
        elif "Masters" in row[3]:
          part4_masters_male += 1
        elif "12" in row[3]:
          part4_12_male += 1
        elif "HS-grad" in row[3]:
          part4_hs_male += 1
      elif "Female" in row[9]:
        if "Doctorate" in row[3]:
          part4_doc_female += 1
        elif "Masters" in row[3]:
          part4_masters_female += 1
        elif "12" in row[3]:
          part4_12_female += 1
        elif "HS-grad" in row[3]:
          part4_hs_female += 1
      if "Private" in row[1]:
        part4_private += 1
      elif "Self-emp" in row[1]:
        part4_SelfEmp += 1
      elif "gov" in row[1]:
        part4_gov += 1
      elif "Without-pay" in row[1]:
        part4_withoutPay += 1
      else:
        other1 += 1

part4_emp_total = part4_private + part4_SelfEmp + part4_gov + part4_withoutPay
print("total ",part4,"Working : ",part4_emp_total)
plt.hist(data1['Age'],bins = [0,20] ,color = 'red', edgecolor = 'black')
plt.hist(data1['Age'],bins = [21,40] ,color = 'skyblue', edgecolor = 'black')
plt.hist(data1['Age'],bins = [41,60] ,color = 'blue', edgecolor = 'black')
plt.hist(data1['Age'],bins = [61,90] ,color = 'orange', edgecolor = 'black')
plt.xlabel('Ages')
plt.ylabel('Poplulation')
print("----------- For age <21 --------- \nTotal:",part1_emp_total ,"\nPrivate:",part1_private,"\nSelf employed:",part1_SelfEmp,"\nGovernment:",part1_gov,"\n& Without Pay:",part1_withoutPay,"\n")
print("----------- For age 21 - 40 ----------\nTotal:",part2_emp_total,"\nPrivate:",part2_private,"\nSelf employed:",part2_SelfEmp,"\nGovernment:",part2_gov,"\n& Without Pay:",part2_withoutPay,"\n")
print("--------- For age 41-60 --------- \nTotal:",part3_emp_total,"\nPrivate:",part3_private,"\nSelf employed:",part3_SelfEmp,"\nGovernment:",part3_gov,"\n& Without Pay:",part3_withoutPay,"\n")
print("---------- For age >60 ------------- \nTotal:",part4_emp_total,"\nPrivate:",part4_private,"\nSelf employed:",part4_SelfEmp,"\nGovernment:",part4_gov,"\n& Without Pay:",part4_withoutPay,"\n")
labels = ['Private', 'Self Employed', 'Government', 'Without-Pay']
sizes = [part1_private,part1_SelfEmp,part1_gov,part1_withoutPay]
colors = ['gold','yellowgreen','lightcoral','lightskyblue']
plt.pie(sizes, labels=labels, colors=colors, radius = 7, explode=[0.3,0.2,0.5,0.1],
autopct = '%0.1f%%', shadow = True, startangle = 140)
plt.axis('equal')
plt.title("Age < 21\n")
plt.show()
labels = ['Private', 'Self Employed', 'Government', 'Without-Pay']
sizes = [part2_private,part2_SelfEmp,part2_gov,part2_withoutPay]
colors = ['gold','yellowgreen','lightcoral','lightskyblue']
plt.pie(sizes, labels=labels, colors=colors,
autopct = '%1.1f%%', shadow = True, startangle = 140)
plt.axis('equal')
plt.title("Age 21 - 40\n")
plt.show()
print("\n")
labels = ['Private','Self-Employed','Government','Without-Pay']
sizes = [part3_private,part3_SelfEmp,part3_gov,part3_withoutPay]
colors = ['gold','yellowgreen','lightcoral','lightskyblue']
plt.pie(sizes, labels=labels, colors=colors,
autopct = '%1.1f%%', shadow = True, startangle = 140)
plt.axis('equal')
plt.title("Age 41 - 60\n")
plt.show()
print("\n")
labels = ['Private','Self-Employed','Government','Without-Pay']
sizes = [part4_private,part4_SelfEmp,part4_gov,part4_withoutPay]
colors = ['gold','yellowgreen','lightcoral','lightskyblue']
plt.pie(sizes, labels=labels, colors=colors,
autopct = '%1.1f%%', shadow = True, startangle = 140)
plt.axis('equal')
plt.title("Age > 60\n")
plt.show()
print("\n")
print("For age < 21 [Male] :- PostDoctrate: ",part1_doc_male,"Masters:- ",part1_masters_male,"12th: ",part1_12_male,"High School: ",part1_hs_male,"\n")
print("Total :- ",part1_doc_male+part1_masters_male+part1_12_male+part1_hs_male)
p1total = part1_doc_male+part1_masters_male+part1_12_male+part1_hs_male
print("For age 21 - 40 [Male] :- PostDoctrate: ",part2_doc_male,"Masters:- ",part2_masters_male,"12th: ",part2_12_male,"High School: ",part2_hs_male,"\n")
print("Total :- ",part2_doc_male+part2_masters_male+part2_12_male+part2_hs_male)
p2total = part2_doc_male+part2_masters_male+part2_12_male+part2_hs_male
print("For age 41 - 60 [Male] :- PostDoctrate: ",part3_doc_male,"Masters:- ",part3_masters_male,"12th: ",part3_12_male,"High School: ",part3_hs_male,"\n")
print("Total :- ",part3_doc_male+part3_masters_male+part3_12_male+part3_hs_male)
ptotal3 = part3_doc_male+part3_masters_male+part3_12_male+part3_hs_male
print("For age > 60 [Male] :- PostDoctrate: ",part4_doc_male,"Masters:- ",part4_masters_male,"12th: ",part4_12_male,"High School: ",part4_hs_male,"\n")
print("Total :- ",part4_doc_male+part4_masters_male+part4_12_male+part4_hs_male)
ptotal4 = part4_doc_male+part4_masters_male+part4_12_male+part4_hs_male
print("\n\n")
print("Total male students :- ",p1total+p2total+ptotal3+ptotal4)
print("For age < 21 [Female] :- PostDoctrate: ",part1_doc_female,"Masters:- ",part1_masters_female,"12th: ",part1_12_female,"High School: ",part1_hs_female,"\n")
print("For age 21 - 40 [Female] :- PostDoctrate: ",part2_doc_female,"Masters:- ",part2_masters_female,"12th: ",part2_12_female,"High School: ",part2_hs_female,"\n")
print("For age 41 - 60 [Female] :- PostDoctrate: ",part3_doc_female,"Masters:- ",part3_masters_female,"12th: ",part3_12_female,"High School: ",part3_hs_female,"\n")
print("For age > 60 [Female] :- PostDoctrate: ",part4_doc_female,"Masters:- ",part4_masters_female,"12th: ",part4_12_female,"High School: ",part4_hs_female,"\n")
X = ['Doctorate','Masters','12th','Hs-Grad']
Ygirls = [part1_doc_female,part1_masters_female,part1_12_female,part1_hs_female]
Zboys = [part1_doc_male,part1_masters_male,part1_12_male,part1_hs_male]
  
X_axis = np.arange(len(X))
  
plt.bar(X_axis - 0.2, Ygirls, 0.4, label = 'Girls')
plt.bar(X_axis + 0.2, Zboys, 0.4, label = 'Boys')
  
plt.xticks(X_axis, X)
plt.xlabel("Education")
plt.ylabel("Number of Students")
plt.title("For Age < 21")
plt.legend()
plt.show()
print("\n")
print("For Age < 21 : ")
print("Boys doing Doctorate : ",part1_doc_male)
print("Girls doing Doctorate :",part1_doc_female)
print("Boys doing Masters : ",part1_masters_male)
print("Girls doing Masters :",part1_masters_female)
print("Boys doing 12th : ",part1_12_male)
print("Girls doing 12th :",part1_12_female)
print("Boys doing HS-Grad : ",part1_hs_male)
print("Girls doing HS-grad :",part1_hs_female)
X = ['Doctorate','Masters','12th','Hs-Grad']
Ygirls = [part2_doc_female,part2_masters_female,part2_12_female,part2_hs_female]
Zboys = [part2_doc_male,part2_masters_male,part2_12_male,part2_hs_male]
  
X_axis = np.arange(len(X))
  
plt.bar(X_axis - 0.2, Ygirls, 0.4, label = 'Girls')
plt.bar(X_axis + 0.2, Zboys, 0.4, label = 'Boys')
  
plt.xticks(X_axis, X)
plt.xlabel("Education")
plt.ylabel("Number of Students")
plt.title("For Age 21 - 40 \n")
plt.legend()
plt.show()
print("\n")
print("For Age 21 - 40 \n ")
print("Boys doing Doctorate : ",part2_doc_male)
print("Girls doing Doctorate :",part2_doc_female)
print("Boys doing Masters : ",part2_masters_male)
print("Girls doing Masters :",part2_masters_female)
print("Boys doing 12th : ",part2_12_male)
print("Girls doing 12th :",part2_12_female)
print("Boys doing HS-Grad : ",part2_hs_male)
print("Girls doing HS-grad :",part2_hs_female)
X = ['Doctorate','Masters','12th','Hs-Grad']
Ygirls = [part3_doc_female,part3_masters_female,part3_12_female,part3_hs_female]
Zboys = [part3_doc_male,part3_masters_male,part3_12_male,part3_hs_male]
  
X_axis = np.arange(len(X))
  
plt.bar(X_axis - 0.2, Ygirls, 0.4, label = 'Girls')
plt.bar(X_axis + 0.2, Zboys, 0.4, label = 'Boys')
  
plt.xticks(X_axis, X)
plt.xlabel("Education")
plt.ylabel("Number of Students")
plt.title("For Age 41 - 60 \n")
plt.legend()
plt.show()
print("\n")
print("For Age 41 -60 \n ")
print("Boys doing Doctorate : ",part3_doc_male)
print("Girls doing Doctorate :",part3_doc_female)
print("Boys doing Masters : ",part3_masters_male)
print("Girls doing Masters :",part3_masters_female)
print("Boys doing 12th : ",part3_12_male)
print("Girls doing 12th :",part3_12_female)
print("Boys doing HS-Grad : ",part3_hs_male)
print("Girls doing HS-grad :",part3_hs_female)
X = ['Doctorate','Masters','12th','Hs-Grad']
Ygirls = [part4_doc_female,part4_masters_female,part4_12_female,part4_hs_female]
Zboys = [part4_doc_male,part4_masters_male,part4_12_male,part4_hs_male]
  
X_axis = np.arange(len(X))
  
plt.bar(X_axis - 0.2, Ygirls, 0.4, label = 'Girls')
plt.bar(X_axis + 0.2, Zboys, 0.4, label = 'Boys')
  
plt.xticks(X_axis, X)
plt.xlabel("Education")
plt.ylabel("Number of Students")
plt.title("For  Age >60  \n")
plt.legend()
plt.show()
print("\n")
print("For  Age >60  \n ")
print("Boys doing Doctorate : ",part4_doc_male)
print("Girls doing Doctorate :",part4_doc_female)
print("Boys doing Masters : ",part4_masters_male)
print("Girls doing Masters :",part4_masters_female)
print("Boys doing 12th : ",part4_12_male)
print("Girls doing 12th :",part4_12_female)
print("Boys doing HS-Grad : ",part4_hs_male)
print("Girls doing HS-grad :",part4_hs_female)
values = data1['Occupation'].value_counts().keys().tolist()
counts = data1['Occupation'].value_counts().tolist()
print("The top 5 Occupations and the number of poplulation :")
for i in range(0,5):
  print("For the Occupation",values[i]," The population is :",counts[i])
count_prof = 0
count_craft = 0
count_exec = 0
count_adm = 0
count_sales = 0
count_others = 0
for index, row, in data1.iterrows():
  if "Prof" in row[6]:
    count_prof += 1
  elif "Craft" in row[6]:
    count_craft += 1
  elif "Exec" in row[6]:
    count_exec += 1
  elif "Adm" in row[6]:
    count_adm += 1
  elif "Sales" in row [6]:
    count_sales += 1
  else:
    count_others += 1
labels = ['Prof','Craft Repair','Exec-Managerial','Adm - Clericial', 'Sales','Others']
sizes = [count_prof,count_craft,count_exec,count_adm,count_sales,count_others]
colors = ['gold','yellowgreen','lightcoral','lightskyblue','blue','green']
plt.pie(sizes, labels=labels, colors=colors,
autopct = '%1.1f%%', shadow = True, startangle = 140)
plt.axis('equal')
plt.title("Different Professions \n")
plt.show()
print("\n")
X = ['Prof','Craft','Exec','Adm','Sales','Others']
Ygirls = [count_prof,count_craft,count_exec,count_adm,count_sales,count_others]
  
X_axis = np.arange(len(X))
  
plt.bar(X_axis - 0.0, Ygirls, 0.4, label = 'Occupations')
  
plt.xticks(X_axis, X)
plt.xlabel("Occupations")
plt.ylabel("Population")
plt.title("Top Occupations \n")
plt.legend()
plt.show()
print("\n")
count_cap_loss_20 = 0
count_cap_gain_20 = 0
count_cap_loss_40 = 0
count_cap_gain_40 = 0
count_cap_loss_60 = 0
count_cap_gain_60 = 0
count_cap_loss_61 = 0
count_cap_gain_61 = 0
cap_loss_20 = []
cap_gain_20 = []
cap_loss_40 = []
cap_gain_40 = []
cap_loss_60 = []
cap_gain_60 = []
cap_loss_61 = []
cap_gain_61 = []

for index, row, in data1.iterrows():
  if(row[0] < 21):
    if(row[10] == 0):
      cap_loss_20.append(row[11])
      count_cap_loss_20 += 1
    elif(row[11] == 0):
      cap_gain_20.append(row[10])
      count_cap_gain_20 += 1
  elif( 21 < row[0] < 41 ):
    if(row[10] == 0):
      cap_loss_40.append(row[11])
      count_cap_loss_40 += 1
    elif(row[11] == 0):
      cap_gain_40.append(row[10])
      count_cap_gain_40 += 1
  elif(41 < row[0] < 61):
    if(row[10] == 0):
      cap_loss_60.append(row[11])
      count_cap_loss_60 += 1
    elif(row[11] == 0):
      cap_gain_60.append(row[10])
      count_cap_gain_60 += 1  
  elif(row[0] > 60):
    if(row[10] == 0):
      cap_loss_61.append(row[11])
      count_cap_loss_61 += 1
    elif(row[11] == 0):
      cap_gain_61.append(row[10])
      count_cap_gain_61 += 1

X = ['Age < 21','Age 21 - 40','Age 41 - 60','Age > 60']
Ygirls = [count_cap_gain_20,count_cap_gain_40,count_cap_gain_60,count_cap_gain_61]
Zboys = [count_cap_loss_20,count_cap_loss_40,count_cap_loss_60,count_cap_loss_61]
  
X_axis = np.arange(len(X))
  
plt.bar(X_axis - 0.2, Ygirls, 0.4, label = 'Gain')
plt.bar(X_axis + 0.2, Zboys, 0.4, label = 'Loss')
  
plt.xticks(X_axis, X)
plt.xlabel("Age")
plt.ylabel("Value of Loss and Gain")
plt.title("Comparision of Different age groups for Capital Gain And Capital Losses \n")
plt.legend()
plt.show()
print("\n")
print("For age < 21 the total capital gain And capital loss is ",sum(cap_gain_20),sum(cap_loss_20))
print("For age 21 - 40 the total capital gain And capital loss is ",sum(cap_gain_40),sum(cap_loss_40))
print("For age 41 - 60 the total capital gain And capital loss is ",sum(cap_gain_20),sum(cap_loss_60))
print("For age 61 above the total capital gain And capital loss is ",sum(cap_gain_61),sum(cap_loss_61))
print("For age < 21 the total capital gain And capital loss is ",sum(cap_gain_20)/len(cap_gain_20),sum(cap_loss_20)/len(cap_loss_20))
print("For age 21 - 40 the total capital gain And capital loss is ",sum(cap_gain_40)/len(cap_gain_40),sum(cap_loss_40)/len(cap_loss_40))
print("For age 41 - 60 the total capital gain And capital loss is ",sum(cap_gain_60)/len(cap_gain_60),sum(cap_loss_60)/len(cap_loss_60))
print("For age 61 above  the total capital gain And capital loss is ",sum(cap_gain_61)/len(cap_loss_61),sum(cap_loss_61)/len(cap_loss_61))



