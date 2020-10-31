import pandas as pd
import numpy as np
#from datetime import datetime as dt
import datetime
import locale

pd.set_option("display.max_rows", 50)
data= pd.read_csv('data.csv')
df  = data.copy()
name_file = ["WEB-developer","tester","marketing","support","programmer","sisadmin","analytics","engineer","specialist","manager"]
#######################Разделение по группам#############################
group_v=[]

WEB= ['web','веб','full stack','fullstack','front-end','frontend','backend','back-end','верстальщик']
web_d=df.loc[df.name.map(lambda x: any([True for i in WEB if i in x.lower()]))]
df=df[df.index.map(lambda x: x not in web_d.index)]
group_v.append(web_d)

TEST = ['тестировщик','qa','тестированию','тестирование']
teste=df.loc[df.name.map(lambda x: any([True for i in TEST if i in x.lower()]))]
df=df[df.index.map(lambda x: x not in teste.index)]
group_v.append(teste)

MARK= ['маркетолог','таргетолог']
market=df.loc[df.name.map(lambda x: any([True for i in MARK if i in x.lower()]))]
group_v.append(market)

SUP=['техподдержки','службы поддержки']
support = df.loc[df.name.map(lambda x: any([True for i in SUP if i in x.lower()]))]
group_v.append(support)

PROG= ['программист','разработчик','developer','programmer']
programmer = df.loc[df.name.map(lambda x: any([True for i in PROG if i in x.lower()]))]
group_v.append(programmer)

SIS = ['системный администратор']
sisadmin = df.loc[df.name.map(lambda x: any([True for i in SIS if i in x.lower()]))]
group_v.append(sisadmin)

analysis= ['аналитик','анализ']
analytics = df.loc[df.name.map(lambda x: any([True for i in analysis if i in x.lower()]))]
group_v.append(analytics)

ENJ=['инженер','engineer']
engineer=df.loc[df.name.map(lambda x: any([True for i in ENJ if i in x.lower()]))]
group_v.append(engineer)

SPEC = ['специалист','specialist']
specialist= df.loc[df.name.map(lambda x: any([True for i in SPEC if i in x.lower()]))]
group_v.append(specialist)

MAN=['менеджер']
manager=df.loc[df.name.map(lambda x: any([True for i in MAN if i in x.lower()]))]
group_v.append(manager)

#########################################################################
count=0
for group in group_v:
#    -	заполнить пропуски по зарплате средним значением по городу
    group.salaryMAX = group.salaryMAX.fillna(round(group.groupby('address')['salaryMAX'].transform('mean'),1))
    group.salaryMIN = group.salaryMIN.fillna(round(group.groupby('address')['salaryMIN'].transform('mean'),1))
#    group.salaryMAX = group.salaryMAX.fillna(round(group.salaryMAX.mean(),1))
#    group.salaryMIN = group.salaryMIN.fillna(round(group.salaryMIN.mean(),1))
#количество дней с момента размещения;    
    count_day= []
    date_column =group['date'].copy()
    for dat in date_column:
        date_str = str(dat).replace("\xa0"," ").split()
        date_piblication_month = date_str[1]
        for new, old in [('января', '1'), ('февраля', '2'), ('марта', '3'), ('апреля', '4'), ('мая', '5'), ('июня', '6'), ('июля', '7'), ('августа', '8'), ('сентября', '9'), ('октября', '10'), ('ноября', '11'), ('декабря', '12')]:
            date_piblication_month = date_piblication_month.replace(new, old)
        difference = datetime.date(2020,10,29) - datetime.date(int(date_str[2]),int(date_piblication_month),int(date_str[0]))
        count_day.append(difference.days)
    se = pd.Series(count_day)
    group['count_day'] = se.values
#заполнить пропуски в признаке “требуемый опыт работы” 
    group.experience=group.experience.fillna('не требуется')
#-	заполнить пропуски в признаке “тип занятости” 
    group.type_of_employment=group.type_of_employment.fillna('любой тип')
#-	при наличии пропусков в остальных признаках заполнить их
    group.duty = group.duty.fillna('не указано')
    group.conditions = group.conditions.fillna('не указаны')
    name_f = name_file[count]+".csv"
    group.to_csv(name_f)
    count+=1
        