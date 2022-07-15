import csv
import json
from collections import OrderedDict
import operator
import sys
import time
import editdistance

file_path="/ssd/finalDump/Dump_temp_it_2018/"
PATH_INPUT=file_path+"src_dest_SN.csv"
redirect=file_path+"redirect.csv"

# for English
csv.field_size_limit(1000000000)
reader=csv.reader(open(redirect),delimiter=",")
count=0
count1=0
count3=0
count_dup=0
redirect_file={}
for line in reader:
    dest=line[1].strip()
    dest=dest.strip('"')
    dest=dest.replace("&amd","and")
    dest=dest.strip('"')
    if dest not in redirect_file: 
        redirect2=line[0].strip('"')
        redirect2=redirect2.replace('&#039;', "'")
        redirect2=redirect2.replace("&amd","and")
        redirect_file[dest]=redirect2
        count+=1
    else:
        count3+ 1
print(count)
print(count1) 
print(count3)
print(count_dup)


def firstl(file_cur,num_lines,skip,alternate,dict_pid,dict_title):
    count=0
    count2=0
    count_redirect=0
    for line in file_cur:
        count2+=1
        if line.find("id") ==-1:
            continue
        index=line.find('id=""')
        pid=line[index+5:line.find('""',index+5)]
        index=line.find('title=""')
        title=line[index+8:line.find('"">',index+8)]
        if title in redirect_file:
            count_redirect+=1
            title=redirect_file[title]
        count+=1
        if title not in Entity_Dict:
            title=title.replace('&quot;','"')
            title=title.replace('&amp;','and')
            title=title.replace('&#039;',"'")
            Entity_Dict[title]=pid
        loc=line[:line.find(',')]
        dict_title[title]=[pid,loc]
    print(count)
    print(count_redirect)
    
    
file_path="/ssd/finalDump/Dump_temp_it_2018/"
file_name="artictDetails.csv"
file_cur = open(file_path+file_name,"r")
Entity_Dict={}
dict_title={}
num_lines=0
skip=0
alternate = 0
firstl(file_cur,num_lines,skip,alternate,Entity_Dict,dict_title)

print('Entities',len(Entity_Dict))

csv.field_size_limit(1000000000)
reader1 = csv.reader (open (PATH_INPUT), delimiter=",")
count = 0
count1=0
count10=0
SN_Dict = {}
D_sn_ct = {}
SN_Dict2 = {}
start=time.time() 
unrecognised_pages=0
redirected_dest=0
temp_SN={}
for line in reader1 :
    count += 1
    SN=line[3]
    SN=SN.replace('&quot;','"')
    SN=SN.replace('&amp;','and')
    SN=SN.replace('&#039;',"'")
    SN=SN.strip()
    temp_SN_ex=SN
    SN=line[3].lower()
    SN=SN.strip()
    temp_SN[SN]=1
    if line[2] in redirect_file:
        line[2]=redirect_file[line[2]]
        redirected_dest+=1
    line[2]=line[2].strip()
    if line[2] not in Entity_Dict:
        continue
    if SN not in SN_Dict:
        SN_Dict[SN] = 1 
    SN_Dict[SN] += 1
    count1+=1
    
    if line[2] in D_sn_ct:
        if SN in D_sn_ct[line[2]]: 
            D_sn_ct[line[2]][SN] += 1
        else: 
            D_sn_ct[line[2]].update({SN:1}) 
    else:
        D_sn_ct[line[2]]={SN:1}
end=time.time()
print(end-start)
print('total mentions',count1)
print('total mentions',count)

print(unrecognised_pages)
print(redirected_dest)

count = 0
for x in SN_Dict:
    count+=1
    SN_Dict[x] = count
    
with open(file_path+ 'Anuj_Table1.demo(2022)2.txt', 'a', encoding='utf-8') as file: 
    file.write("Entity_Number, Entity_Name\n")
    for k, v in Entity_Dict.items(): 
        k='`'+k+'`'
        file.write("{},{}\n".format(v,k))
    file.close()
print("Done T1")

with open(file_path+ 'Anuj_Table2.demo(2022)2.txt', 'a', encoding='utf-8') as file: 
    file.write("SN_Number, SN_Name\n")
    for x, count in SN_Dict.items():
        x=x.capitalize()
        x='`'+x+'`'
        file.write("{},{}\n".format (count, x))
    file.close()
print("Done T2")


def editDistDP(str1, str2):     
    m = len(str1)
    n = len(str2)
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)] 
    for i in range(m + 1): 
        for j in range(n + 1): 
            if i == 0: 
                dp[i][j] = j    # Min. operations = j 
            elif j == 0: 
                dp[i][j] = i    # Min. operations = i 
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
    return(dp[m][n])
   
 
count1=0
count2=0
selected_sn=0
total_sn=0
correct_men=0
incorrect_men=0
total_mentions=0
sno=0
total_mentions1=0
total_mentions2=0
total_mentions3=0
total_sn1_entity=0
total_sn2_entity=0
total_sn3_entity=0
Correct_Surface_Names = {}
Wrong_Surface_Names = {}
Substrings = {}
Superstrings={}
Edit_Distances = {}
start= time.time()
with open(file_path+ 'Anuj_Table5.demo(2022)2.txt', 'a', encoding='utf-8') as file:
    file.write("Sno, Entity_ID, Surface_ID, Frequency, Correct/Wrong\n") 
    for key,val in D_sn_ct.items():
        total_sn+=1
        if key in Entity_Dict:
            for k,v in val.items():
                total_mentions+=v
            if(len(val)==1):
                total_sn1_entity+=1
                for k,v in val.items():
                    total_mentions1+=v
                    file.write("{},{},{},{},1\n".format(sno, Entity_Dict[key], SN_Dict[k], D_sn_ct[key][k]))
            if(len(val)==2):
                total_sn2_entity+=1
                for k,v in val.items():
                    total_mentions2+=v
                    file.write("{},{},{},{},1\n".format(sno, Entity_Dict[key], SN_Dict[k], D_sn_ct[key][k]))
            if(len(val)>=3):
                total_sn3_entity+=1
                Correct_Surface_Names[key] = {} 
                Wrong_Surface_Names[key] = {}
                count = 0
                for k,v in val.items():
                    count+=v
                for k,v in val.items():
                    try:
                        sno+=1
                        if(v/count>=0.05 or v>10):
                            Correct_Surface_Names[key][k] = (v,v/count)
                            count1+=1;
                            correct_men+=v
                            file.write("{},{},{},{},1\n".format(sno, Entity_Dict[key], SN_Dict[k], D_sn_ct[key][k]))
                        else:
                            Substrings[key] = {} 
                            Superstrings[key] = {} 
                            Edit_Distances[key] = {}
                            count2+=1;
                            incorrect_men+=v
                            file.write("{},{},{},{},0\n".format(sno, Entity_Dict[key], SN_Dict[k], D_sn_ct[key][k]))
                    except:
                        do_nothing = 1
                correct_list = list(Correct_Surface_Names[key].keys())
                for k,v in val.items(): 
                    if (v/count<0.05 and v<=10):
                        temp_list_sub=[]
                        temp_list_super=[]
                        min_dist = 10**10
                        for name in correct_list:
                            if name in k:
                                temp_list_sub.append(name)
                                #count sub=1
                            if k in name:
                                temp_list_super.append(name)
                                #count sub+=1
                            if editDistDP (name, k)<min_dist: 
                                min_dist=min (min_dist, editDistDP (name, k))
                                correct= name
                        if temp_list_sub:
                            Substrings[key][k] = max(temp_list_sub,key=len)
                        if temp_list_super:
                            Superstrings[key][k] = min(temp_list_super,key=len)
                        Edit_Distances[key][k]=(correct,min_dist)
            else:
                selected_sn+=1
                #print(key)
    file.close()
end=time.time() 
print(end-start)
print("now dump marathi")
print("correct SN", count1)
print("correct mention", correct_men) 
print("INcorrect SN", count2)
print("incorrect mention", incorrect_men) 
print("Entities with (whose ID is known) more then 0 SN",selected_sn)
print("total_destination_entity",total_sn)
print("total_mention",total_mentions)
print("total_destination_entity with_sn_1",total_sn1_entity)
print("total_destination_entity with_sn_2",total_sn2_entity)
print("total_destination_entity with_sn_3",total_sn3_entity)
print("total_mention",total_mentions1)
print("total_mention",total_mentions2)
print("total_mention",total_mentions3)

reader = csv.reader (open(file_path+"src_dest_SN.csv", encoding='utf-8'), delimiter=",") 
def gen_reader():
    for row in reader: 
        yield row
        
mid = 1
edit_distance1_mentions=0
edit_distance2_mentions=0
superstring_mention=0
substring_mention=0
start=time.time()
csv.field_size_limit(1000000000)
other_SN=0
reader1 = csv.reader (open (PATH_INPUT), delimiter=",")
with open(file_path+ 'Anuj_Table6.demo(2022)2.txt', 'a', encoding='utf-8') as file: 
    file.write("Entity_Mention_index, Dest_Entity_Index, Surface_Name_Entity_Index, Source_Entity_Index, Edit_Distance_val, Edit_Distance_SN, yes/no superstring, superstring, yes/no substring, substring,context \n") 
    for row in gen_reader():
        try:
            sid = row[0]
        except IndexError: 
            continue
        try:
            Source = row[1] 
        except IndexError: 
            continue
        try:
            Dest = row[2]
            if Dest in redirect_file: 
                Dest=redirect_file[Dest] 
            Dest=Dest.strip()
        except IndexError: 
            continue
        try:
            SN=row[3]
            SN=SN.replace('&quot;','"')
            SN=SN.replace('&amp;','and')
            SN=SN.replace('&#039;',"'")
            SN=SN.strip()
            SN_ex=SN
            SN=row[3].lower()
            SN=SN.strip()
        except IndexError: 
            continue
        if Source not in Entity_Dict or Dest not in Entity_Dict: 
            continue
        if len(D_sn_ct[Dest].items())<3: 
            continue
        count = 0
        for k,v in D_sn_ct[Dest].items(): 
            count+=v
        v=D_sn_ct[Dest][SN]
        if (v/count>=0.05 or v>10):
            continue
        else:
            mid+=1
            line="{},{},{},{},".format(mid, Entity_Dict[Dest], SN_Dict[SN], Entity_Dict[Source])
            line+="{},{},".format(Edit_Distances[Dest][SN][1],SN_Dict[Edit_Distances[Dest][SN][0]]) 
            flag=0
            if Edit_Distances[Dest][SN][1]==1:
                edit_distance1_mentions+=1
                flag=1
            if Edit_Distances[Dest][SN][1]==2:
                edit_distance2_mentions+=1
                flag=1
            if SN in Superstrings[Dest]: 
                superstring_mention+=1
                flag=1
                line+= "1,{},".format(SN_Dict[Superstrings[Dest][SN]])
            else:
                line += "0,0,"
            if SN in Substrings[Dest]:
                flag=1
                substring_mention+=1
                line += "1,{},".format(SN_Dict[Substrings[Dest][SN]])
            else:
                line += "0,0,"
            if flag==0:
                other_SN+=1
            context=row[4].strip()
            x11='`'+context+'`'
            x11=x11.replace('\n','') 
            x11=x11.replace('&quot;','"')
            x11=x11.replace('&amp;','and')
            x11=x11.replace('&#039;',"'")
            x11=x11.replace('&gt;',"")
            x11=x11.replace('&lt;',"")
            x11=x11.replace('====',"")
            x11=x11.replace('===',"")
            x11=x11.replace("ref/ref","")
            x11=x11.replace('\n','') 
            line+="{}\n".format(x11)
            file.write("{}".format(line))
    file.close()
end=time.time()
print (end-start)
print(mid)
print(edit_distance1_mentions)
print(edit_distance2_mentions)
print(superstring_mention)
print(substring_mention)
print(other_SN)
