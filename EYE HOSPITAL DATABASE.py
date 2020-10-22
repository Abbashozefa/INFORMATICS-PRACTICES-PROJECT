try:
    import pymysql
    import pandas as pd
    pd.set_option('display.max_columns', 11)


    conn=pymysql.connect(host='localhost',user='root',password='yellowyellow',database='EYEHOSPITAL')
    a=conn.cursor()
    while(True):
        print('1.RECEPTIONIST')
        print('2.OPTOMETRIST(GENERAL CHECKUP)')
        print('3.OPTHALMOLOGIST(DOCTOR)')
        ch1=int(input('SELECT YOUR FIELD:::'))

        def receptionist():
            
            
            conn=pymysql.connect(host='localhost',user='root',password='yellowyellow',database='EYEHOSPITAL')
            a=conn.cursor()

           
            print('1.NEW PATIENT')
            print('2.ROUTINE CHECKUP PATIENT DETAILS')
            print('3.VIEW PATIENT DETAILS')
            ch2=int(input('SELECT YOUR FIELD:::'))
           
            
            '''a.execute('CREATE TABLE PATIENT(PATIENT_ID INT ,PATIENT_NAME VARCHAR(20),AGE INT,DATE_OF_LAST_VISIT DATE,CONSULTING_DOCTOR VARCHAR(20),RIGHT_SPH DECIMAL(2,1),RIGHT_CYL DECIMAL(2,1),RIGHT_AXIS INT,LEFT_SPH DECIMAL(2,1),LEFT_CYL DECIMAL(2,1),LEFT_AXIS INT)')'''
                
           
            if (ch2==1) :
                
                

                user=int(input('Enter PATIENT ID:'))
                name=input('Enter PATIENT NAME:')
                age=int(input('Enter PATIENT AGE:'))
                date=input('Enter DATE:')
                doc=input('Enter CONSULTING DOCTOR:')
                 
                 

                a.execute("insert into PATIENT values("+str(user)+",'"+name+"',"+str(age)+",'"+date+"','"+doc+"',NULL,NULL,NULL,NULL,NULL,NULL)")
            elif(ch2==3):
                user=int(input('Enter PATIENT ID'))
                name=input('Enter PATIENT NAME')
                a.execute("select PATIENT_ID  ,PATIENT_NAME,AGE,DATE_OF_LAST_VISIT,CONSULTING_DOCTOR from PATIENT where PATIENT_ID="+str(user)+" and PATIENT_NAME='"+name+"'" )
                D=a.fetchall()
                data=pd.DataFrame(D,columns=['PATIENT_ID ' ,'PATIENT_NAME','AGE','DATE_OF_LAST_VISIT','CONSULTING_DOCTOR'])
                data.set_index('PATIENT_ID ',inplace=True)
                print(data.iloc[:,0:5])
                a.execute("select *from PATIENT")
                D=a.fetchall()
                data=pd.DataFrame(D,columns=['PATIENT_ID ' ,'PATIENT_NAME','AGE','DATE_OF_LAST_VISIT','CONSULTING_DOCTOR','RIGHT_SPH','RIGHT_CYL','RIGHT_AXIS','LEFT_SPH','LEFT_CYL','LEFT_AXIS'])
                
                print(data.iloc[:,0:5])
                
            elif(ch2==2):
                user=int(input('Enter PATIENT ID'))
                date=input('ENTER DATE :')
                age=int(input('Enter PATIENT AGE'))
                a.execute("select distinct* from PATIENT where PATIENT_ID="+str(user) )
                D=a.fetchall()
                print(D)
                
                a.execute("insert into PATIENT values("+str(user)+",'"+D[0][1]+"',"+str(age)+",'"+date+"','"+D[0][4]+"',NULL,NULL,NULL,NULL,NULL,NULL)")
                
                

                
                
            conn.commit()
        def general():
            
            conn=pymysql.connect(host='localhost',user='root',password='yellowyellow',database='EYEHOSPITAL')
            a=conn.cursor()

           
            print('1.UPDATE PATIENTS EYE POWER')
            print('2.MAKE EYEM POWER')
            print('3.')
            ch2=int(input('SELECT YOUR FIELD:::'))
           
            
            '''a.execute('CREATE TABLE PATIENT(PATIENT_ID INT PRIMARY KEY ,PATIENT_NAME VARCHAR(20),AGE INT,DATE_OF_LAST_VISIT DATE,CONSULTING_DOCTOR VARCHAR(20),RIGHT_SPH DECIMAL(2,1),RIGHT_CYL DECIMAL(2,1),RIGHT_AXIS INT,LEFT_SPH DECIMAL(2,1),LEFT_CYL DECIMAL(2,1),LEFT_AXIS INT)')'''
                
           
            if (ch2==1) :
                
                

                user=input('Enter PATIENT ID:')
                rsph=input('Enter RIGHT EYE AXIS:')
                rcyl=input('Enter RIGHT EYE CYLINDRICAL:')
                raxis=input('Enter RIGHT EYE AXIS')
                date=input('ENTER DATE :')
                lsph=input('Enter LEFT EYE AXIS:')
                lcyl=input('Enter LEFT EYE CYLINDRICAL:')
                laxis=input('Enter LEFT EYE AXIS') 
                 

                a.execute("update PATIENT set RIGHT_SPH ="+rsph+",RIGHT_CYL ="+rcyl+",RIGHT_AXIS ="+raxis+",LEFT_SPH ="+lsph+",LEFT_CYL ="+lcyl+",LEFT_AXIS="+laxis+"where PATIENT_ID="+user+" and DATE_OF_LAST_VISIT='"+date+"'")
            elif(ch2==3):
                user=int(input('Enter PATIENT ID'))
                name=input('Enter PATIENT NAME')
                a.execute("select PATIENT_ID  ,PATIENT_NAME,AGE,DATE_OF_LAST_VISIT,CONSULTING_DOCTOR from PATIENT where PATIENT_ID="+str(user)+" and PATIENT_NAME='"+name+"'" )
                D=a.fetchall()
                data=pd.DataFrame(D,columns=['PATIENT_ID ' ,'PATIENT_NAME','AGE','DATE_OF_LAST_VISIT','CONSULTING_DOCTOR'])
                data.set_index('PATIENT_ID ',inplace=True)
                print(data.iloc[:,0:5])
                a.execute("select *from PATIENT")
                D=a.fetchall()
                data=pd.DataFrame(D,columns=['PATIENT_ID ' ,'PATIENT_NAME','AGE','DATE_OF_LAST_VISIT','CONSULTING_DOCTOR','RIGHT_SPH','RIGHT_CYL','RIGHT_AXIS','LEFT_SPH','LEFT_CYL','LEFT_AXIS'])
                
                print(data.iloc[:,0:5])
                
            elif(ch2==2):
                
                user=input('Enter PATIENT ID:')
                rsph=input('Enter RIGHT EYE AXIS:')
                rcyl=input('Enter RIGHT EYE CYLINDRICAL:')
                raxis=input('Enter RIGHT EYE AXIS')
                date=input('ENTER DATE :')
                lsph=input('Enter LEFT EYE AXIS:')
                lcyl=input('Enter LEFT EYE CYLINDRICAL:')
                laxis=input('Enter LEFT EYE AXIS')
                a.execute("update PATIENT set RIGHT_SPH ="+rsph+",RIGHT_CYL ="+rcyl+",RIGHT_AXIS ="+raxis+",LEFT_SPH ="+lsph+",LEFT_CYL ="+lcyl+",LEFT_AXIS="+laxis+"where PATIENT_ID="+user+" and DATE_OF_LAST_VISIT='"+date+"'")
                
                
            conn.commit()
        def doctor():
            
            conn=pymysql.connect(host='localhost',user='root',password='yellowyellow',database='EYEHOSPITAL')
            a=conn.cursor()

           
            print('1.CHECK COMPLETE RECORD')
            print('2.ROUTINE CHECKUP PATIENT DETAILS')
            print('3.GIVE PRESCRIPTION')
            ch2=int(input('SELECT YOUR FIELD:::'))
           
            
            '''a.execute('CREATE TABLE PATIENT(PATIENT_ID INT PRIMARY KEY ,PATIENT_NAME VARCHAR(20),AGE INT,DATE_OF_LAST_VISIT DATE,CONSULTING_DOCTOR VARCHAR(20),RIGHT_SPH DECIMAL(2,1),RIGHT_CYL DECIMAL(2,1),RIGHT_AXIS INT,LEFT_SPH DECIMAL(2,1),LEFT_CYL DECIMAL(2,1),LEFT_AXIS INT)')'''
                
           
            if (ch2==1) :
                
                

                user=int(input('Enter PATIENT ID:'))
                a.execute("select *from PATIENT WHERE PATIENT_ID="+str(user))
                D=a.fetchall()
                data=pd.DataFrame(D,columns=['PATIENT_ID ' ,'PATIENT_NAME','AGE','DATE_OF_LAST_VISIT','CONSULTING_DOCTOR','RIGHT_SPH','RIGHT_CYL','RIGHT_AXIS','LEFT_SPH','LEFT_CYL','LEFT_AXIS'])
                data.set_index('PATIENT_ID ',inplace=True)
                print(data)
                
                 
                 

               
            elif(ch2==3):
                print('=================================================================================================================================================================================')
                print('====================================================================================================================PRESCRIPTION=================================================')
                
                user=int(input('                PATIENT ID: '))
                pass
                pass
                date=input('                    DATE:')
                pass
                pass
                med=input('                     MEDICATIONS::')
                a.execute("select *from PATIENT WHERE PATIENT_ID="+str(user)+" and DATE_OF_LAST_VISIT='"+date+"'")
                D=a.fetchall()
                print('                         AGE :: '+str(D[0][2]))
                print('                      CONSULTING DOCTOR'+D[0][4])      
                data=pd.DataFrame(D,columns=['PATIENT_ID ' ,'PATIENT_NAME','AGE','DATE_OF_LAST_VISIT','CONSULTING_DOCTOR','RIGHT_SPH','RIGHT_CYL','RIGHT_AXIS','LEFT_SPH','LEFT_CYL','LEFT_AXIS'])
                data.set_index('PATIENT_ID ',inplace=True)
                print(data.iloc[:,5:])
                print('=================================================================================================================================================================================')
            elif(ch2==2):
                user=int(input('Enter PATIENT ID'))
                name=input('Enter PATIENT NAME')
                a.execute("select PATIENT_ID  ,PATIENT_NAME,AGE,DATE_OF_LAST_VISIT,CONSULTING_DOCTOR from PATIENT where PATIENT_ID="+str(user)+" and PATIENT_NAME='"+name+"'" )
                D=a.fetchall()
                data=pd.DataFrame(D,columns=['PATIENT_ID ' ,'PATIENT_NAME','AGE','DATE_OF_LAST_VISIT','CONSULTING_DOCTOR'])
                data.set_index('PATIENT_ID ',inplace=True)
                print(data.iloc[:,0:5])
                a.execute("select *from PATIENT")
                D=a.fetchall()
                data=pd.DataFrame(D,columns=['PATIENT_ID ' ,'PATIENT_NAME','AGE','DATE_OF_LAST_VISIT','CONSULTING_DOCTOR','RIGHT_SPH','RIGHT_CYL','RIGHT_AXIS','LEFT_SPH','LEFT_CYL','LEFT_AXIS'])
                
                print(data.iloc[:,0:5])
                
            conn.commit()    
        if(ch1==1):
            receptionist()
            
        elif(ch1==2):
            general()
        else:
            doctor()
    conn.commit()
except:
    print('Something went wrong \n Requesting you to try again')
