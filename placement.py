import streamlit as st
import pandas as pd
st.set_page_config("Placement Checker Project")
st.markdown("""
<style>
.css-d1b1ld.edgvbvh6
{
  visibility:hidden;
}
.css-1v8iw7l.eknhn3m4
{
  visibility:hidden;
}
#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.stForm.st-emotion-cache-4uzi61.e10yg2by1 > div > div > div > div:nth-child(2) > div > div > div > div > svg
{
  visibility:hidden;
}
#root > div:nth-child(1) > div.withScreencast > div > header
{
  visibility:hidden;
}
</style>
""",unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center;'>Placement Checker</h1>",unsafe_allow_html=True)
form1=st.form("Collection")
uploaded = form1.file_uploader("Upload Total Students List",type='xlsx')
uploaded1 = form1.file_uploader("Upload Job Qualified Students List",type='xlsx')
submit = form1.form_submit_button("Submit")
name=[]
mail=[]
# name=form1.text_input("Names: ").lower().strip().split(",")
# mail=form1.text_input("Mails:").lower().strip().split(",")
db = pd.read_excel(uploaded)
db1 = pd.read_excel(uploaded1)
l=[] #Unique Departments
l1=[] #Emails
l2=[] #Departments
l3=[] #Name
total_d1={} #For Percentage
d={} #For details
for i in db["Email"]:
  l1.append(str(i).lower().strip())
for j in db["Department"]:
  l2.append(j)
for k in db["Name"]:
  l3.append(str(k).lower().strip())
l=set(l2)
for i in l:
  d[i]={}
for i in range(len(l1)):
  d[l2[i]][l1[i]]=l3[i]
d1={}
d2={}
for i in l:
  d1[i]=0
  d2[i]=[]
for i in l:
  total_d1[i]=len(d[i].keys())
for i in db1['Name']:
    name.append(str(i).lower().strip())
for i in db1['Email']:
    mail.append(str(i).lower().strip())
final_k=[] #Relative Departments
km=[] #Unknown Mails
kn=[] #Corresponding Unknown Names
for i in set(mail):
  c=0
  for j in d.keys():
    if(i in d[j].keys()):
      d1[j]+=1
      k=mail.index(i)
      d2[j].append(name[k])
      c=1
  if(c==0):
    km.append(i)
    kn.append(name[mail.index(i)])
# print(km)
for i in kn:
  c=0
  l4=[]
  for j in d.keys():
    if(i in d[j].values()):
      l4.append(j)
  if(len(l4)==1):
    d1[l4[0]]+=1
    d2[l4[0]].append(i)
  else:
    d1["Undefined"]+=1
    final_k.append(i)
#d1["Undefined"]-=1
columns=['Department','Count','Percentage']
final_count = []
# print("--------------------------------")
# print("{:<12}| {:<6}|{:<11}".format("Department".center(12),"Count".center(6),"Percentage".center(11)))
for i in sorted(d1.keys()):
    final_count.append([i,str(d1[i]),str(round((d1[i]/total_d1[i])*100,2))+"%"])
#   print("--------------------------------")
#   print("{:<12}|{:<6} |  {:<6}".format(i.center(12),str(d1[i]).center(6),str(round((d1[i]/total_d1[i])*100,2))+"%"))
# print("--------------------------------")
# final_k
# d2["CSE(AIML)"]
final_df = pd.DataFrame(final_count,columns=columns)
final_df.index+=1
st.write(final_df)
for i in sorted(d1.keys()):
    if st.button(i):
        f_names=pd.DataFrame(sorted(d2[i]),columns=['Name'])
        f_names.index+=1
        st.write(f_names)
# final_df = pd.DataFrame(final_count,columns=columns)
# final_df.index+=1
# st.table(final_df)
