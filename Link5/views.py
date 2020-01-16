from django.shortcuts import render
from django.shortcuts import HttpResponse
import numpy as np
import pandas as pd
import pickle
import os
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder
num=0
lstt=[]
data = [['tom', 10], ['nick', 15], ['juli', 14]] 
df = pd.DataFrame(data, columns = ['Name', 'Age'])
indexes1=[]
def Link5(request):
    return render(request, 'Link5.html', {})

def rowcol(request):
    if request.method == 'POST':
        try:
            global lstt
            global df
            file = request.FILES['file']
            dataset=pd.read_csv(file)
            count_row, count_col = dataset.shape
            df=dataset
            lst=list(dataset)
            lstt=lst
            lst1=lst[:-1]
            df1=df[:15]
            #dictionary = { lst[i] : i for i in range(0, len(lst) ) }
            return render(request, 'Link5_rc.html', {'arr':lst,'arr1':lst1,'cols':count_col,'rows':count_row,'data1':df1.to_html()})
        except:
            return HttpResponse('ERROR: No file uploaded')
    
def prec(request):
    if request.method == 'POST':
        global lstt
        global indexes1
        var = request.POST.getlist('checks[]')
        if len(var)==0:
            return HttpResponse('Error: No column selected')
        indexes=[]
        for i in range(0,len(var)):
            for j in range(i,len(lstt)):
                           if var[i]==lstt[j]:
                               indexes.append(j)
        indexes1=indexes
        return render(request, 'Link5_prec.html', {'checks':var,'arr':lstt})
    return HttpResponse('Nothin')

def classification(request):
    if request.method == 'POST':
        try:
            global lstt
            global df
            global indexes1
            count_row, count_col = df.shape
            target=request.POST.get("submit")
            colno=0
            for i in range(0,len(lstt)):
                if lstt[i]==target:
                    colno=i
                    break
            allcol=df.iloc[:,:].values
            labelencoder = LabelEncoder()
            allcol[:,1] = labelencoder.fit_transform(allcol[:,1])
            sc=StandardScaler()
            allcol[:,[0,2,3]]=sc.fit_transform(allcol[:,[0,2,3]])
            x=allcol[:,indexes1]
            y=allcol[:,colno].astype('int64')
            ''''''
            if len(indexes1)==4:
                decision_tree_model_pkl=open(os.path.dirname(os.path.realpath(__file__)) + '\classifiers\decision_tree_classifier_4col.pkl', "rb")
                decision_tree_model = pickle.load(decision_tree_model_pkl)
            elif len(indexes1)==3:
                if indexes1[0]==0 and indexes1[1]==1 and indexes1[2]==2:
                    decision_tree_model_pkl=open(os.path.dirname(os.path.realpath(__file__)) + '\classifiers\decision_tree_classifier_3col(userid,gender,age).pkl', "rb")
                    decision_tree_model = pickle.load(decision_tree_model_pkl)
                elif indexes1[0]==0 and indexes1[1]==1 and indexes1[2]==3:
                    decision_tree_model_pkl=open(os.path.dirname(os.path.realpath(__file__)) + '\classifiers\decision_tree_classifier_3col(userid,gender,sal).pkl', "rb")
                    decision_tree_model = pickle.load(decision_tree_model_pkl)
                elif indexes1[0]==0 and indexes1[1]==2 and indexes1[2]==3:
                    decision_tree_model_pkl=open(os.path.dirname(os.path.realpath(__file__)) + '\classifiers\decision_tree_classifier_3col(userid,age,sal).pkl', "rb")
                    decision_tree_model = pickle.load(decision_tree_model_pkl)
                elif indexes1[0]==1 and indexes1[1]==2 and indexes1[2]==3:
                    decision_tree_model_pkl=open(os.path.dirname(os.path.realpath(__file__)) + '\classifiers\decision_tree_classifier_3col(gender,age,salary).pkl', "rb")
                    decision_tree_model = pickle.load(decision_tree_model_pkl)                    
            elif len(indexes1)==2:
                if indexes1[0]==0 and indexes1[1]==1:
                    decision_tree_model_pkl=open(os.path.dirname(os.path.realpath(__file__)) + '\classifiers\decision_tree_classifier_2col(userid,gender).pkl', "rb")
                    decision_tree_model = pickle.load(decision_tree_model_pkl)
                elif indexes1[0]==0 and indexes1[1]==2:
                    decision_tree_model_pkl=open(os.path.dirname(os.path.realpath(__file__)) + '\classifiers\decision_tree_classifier_2col(userid,age).pkl', "rb")
                    decision_tree_model = pickle.load(decision_tree_model_pkl)
                elif indexes1[0]==0 and indexes1[1]==3:
                    decision_tree_model_pkl=open(os.path.dirname(os.path.realpath(__file__)) + '\classifiers\decision_tree_classifier_2col(userid,salary).pkl', "rb")
                    decision_tree_model = pickle.load(decision_tree_model_pkl)
                elif indexes1[0]==1 and indexes1[1]==2:
                    decision_tree_model_pkl=open(os.path.dirname(os.path.realpath(__file__)) + '\classifiers\decision_tree_classifier_2col(gender,age).pkl', "rb")
                    decision_tree_model = pickle.load(decision_tree_model_pkl)
                elif indexes1[0]==1 and indexes1[1]==3:
                    decision_tree_model_pkl=open(os.path.dirname(os.path.realpath(__file__)) + '\classifiers\decision_tree_classifier_2col(gender,sal).pkl', "rb")
                    decision_tree_model = pickle.load(decision_tree_model_pkl)
                elif indexes1[0]==2 and indexes1[1]==3:
                    decision_tree_model_pkl=open(os.path.dirname(os.path.realpath(__file__)) + '\classifiers\decision_tree_classifier.pkl', "rb")
                    decision_tree_model = pickle.load(decision_tree_model_pkl)
            elif len(indexes1)==1:
                if indexes1[0]==0:
                    decision_tree_model_pkl=open(os.path.dirname(os.path.realpath(__file__)) + '\classifiers\decision_tree_classifier_1col(userid).pkl', "rb")
                    decision_tree_model = pickle.load(decision_tree_model_pkl)
                elif indexes1[0]==1:
                    decision_tree_model_pkl=open(os.path.dirname(os.path.realpath(__file__)) + '\classifiers\decision_tree_classifier_1col(gender).pkl', "rb")
                    decision_tree_model = pickle.load(decision_tree_model_pkl)
                elif indexes1[0]==2:
                    decision_tree_model_pkl=open(os.path.dirname(os.path.realpath(__file__)) + '\classifiers\decision_tree_classifier_1col(age).pkl', "rb")
                    decision_tree_model = pickle.load(decision_tree_model_pkl)
                elif indexes1[0]==3:
                    decision_tree_model_pkl=open(os.path.dirname(os.path.realpath(__file__)) + '\classifiers\decision_tree_classifier_1col(salary).pkl', "rb")
                    decision_tree_model = pickle.load(decision_tree_model_pkl)
            else:
                return HttpResponse('ERROR: no column selected')
            y_pred = decision_tree_model.predict(x)
            cm=confusion_matrix(y,y_pred)
            accuracy = (cm[0][0]+cm[1][1])/(cm[0][0]+cm[1][0]+cm[0][1]+cm[1][1])
            recall=cm[0][0]/(cm[0][0]+cm[0][1])
            precision=cm[0][0]/(cm[0][0]+cm[1][0])
            f1= 2*(recall * precision) / (recall + precision)
            lst={'row':count_row,'col':count_col,'tp':cm[0][0],'tn':cm[1][1],'fn':cm[0][1],'fp':cm[1][0],'accuracy':accuracy,'recall':recall,'precision':precision,'f1':f1}
            return render(request, 'Link5_1.html', lst)
        except:
            return HttpResponse('ERROR: Irrelevent column selected for classification')            
