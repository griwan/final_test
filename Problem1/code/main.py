# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bhETvtW1fnU7hvw_N7ADlNdE8gOVWVP4
"""

import pandas as pd
df =pd.read_csv("intelligentGuessingDataSet.csv",encoding='latin-1')

df

import re

df2 = df.copy().fillna(0)

sample = df2.iloc[13,:]

array = df2['firstname'].tolist()+df2['lastname'].tolist()
for index, row in df2.iterrows():
    if row['firstname']==0 or row['lastname']==0:
     
      email = row['email'].split('@')[0]
     
      for i in array:
        if i==0:
          continue
        a = re.search(i,email)
        if a:
          break
      if a:
        if row['firstname'] ==0:
          df2.loc[index,'firstname'] = a.string
        else:
          df2.loc[index,'lastname'] = a.string
      else:
        if row['firstname'] ==0:
          df2.loc[index,'firstname'] = ''
        else:
          df2.loc[index,'lastname'] = ''

for index,r in df2.iterrows():
  p,p_n = get_pattern(r)
  df2.loc[index,'Email Pattern'] = p
  df2.loc[index,'Comments']=p_n

def get_pattern(data):
  email = data['email'].split('@')[0]
  lname = data['lastname'].lower()
  fname = data['firstname'].lower()
  dot = re.match(r'[\w\.-]+\.[\w\.-]+',email)
  under = re.match(r'[\w\.-]+\_[\w\.-]+',email)
  f_best = best_match(fname,email)
  record_f = ''
  record_f_n=''
  record_l_n=''
  record_l = ''
  l_names = lname.split(' ')
  l_best = []

  for ls in l_names:
    l_best.append(best_match(ls,email))

  
#For first name
  if fname!='':
    m = re.search(email[f_best[0]:f_best[1]],fname)
    if m.span()[1]==len(fname):
      record_f = '<11>'
      record_f_n = 'firstname'
    elif m.span()[1]-m.span()[0]>1:
      record_f ='<11-f{}l>'.format(m.span()[1]-m.span()[0])
      record_f_n = 'First {} letters of firstname'.format(m.span()[1]-m.span()[0])
    else:
      record_f ='<1>'.format(m.span()[1]-m.span()[0])
      record_f_n = 'first letter of firstname'

  # if record_f_n!='':
  #   record_f_n=record_f_n+' and '
#for last_name
  if l_names[0]!= '':
    for j,i in enumerate(l_best):
      # if record_f_n!='':
      #   record_l_n=record_l_n+' and '
      if(i == (0,0)):
        continue
      m = re.search(email[i[0]:i[1]],l_names[j])
      temp2=''
      temp= ''
      if record_l_n != '':
        record_l_n = record_l_n+' and '
      if m:
        if len(l_names)>1:
          record_l = record_l + ('<2{}>'.format(j))
          if j ==0:
            record_l_n = record_l_n+'First part of lastname'
            
          else:
             record_l_n = record_l_n+'Second part of lastname'
         
        else: 
          record_l = record_l+('<22>') 
          record_l_n = 'lastname' 
  if record_f_n=='' or record_l_n=='':
    conj=''
  else:
    if dot:
      conj = '.'
    elif under:
      conj='_'
    else:
      conj=' and '
  if conj==' and ':
    return record_f+record_l,record_f_n+conj+record_l_n
  else:
    return record_f+conj+record_l,record_f_n+conj+record_l_n

def best_match(s1,s2):
  a = (0,0)
  for i in range(len(s1)+1):
    if i ==0:
      continue
    m = re.search(s1[0:i],s2)
    if m:
      a = m.span()

  return a

df2.to_csv('problemset1_solution.csv', index=False,)

