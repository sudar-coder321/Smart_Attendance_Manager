import pandas as pd


def update(n,r):
    data = pd.read_csv("F:/voicerecog/attendance_database.csv") 

    names=data["NAMES"]
    names=list(names)

    usn=data["ROLL_NUMBER"]
    usn=list(usn)

    att=data["ATTENDANCE"]
    att=list(att)
    att1=list(att)

    #print(names)
    #print(usn)


    rows=len(names)


    #ASSUME NAME= RAJAT ROLL=127
    #n="nishant"
    #r=102

    for i in range(0,len(names)):
        #print(names[i])
        if names[i]==n:
            break

    #print(i)
    for j in range(0,len(usn)):
        #print(usn[j])
        if int(usn[j])==r:
            break

    if i==j:
        att[i]=1

    print(att)



    df = pd.read_csv("F:/voicerecog/attendance_database.csv") 

    #df = pd.DataFrame(data, columns = ['NAMES','ROLL_NUMBER','ATTENDANCE'])
    
    df = df[['NAMES','ROLL_NUMBER','ATTENDANCE']]

    #print(df)


    for i in range(0,len(names)):
        (df['ATTENDANCE'][i])=att[i]
    

    #print(df['ATTENDANCE'])
    print(df)

    df.to_csv("F:/voicerecog/attendance_database.csv")
n = 6
r = 5
update(n,r)
print("Database updated successfully")

