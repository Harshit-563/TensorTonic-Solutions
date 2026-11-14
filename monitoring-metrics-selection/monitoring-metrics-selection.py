def compute_monitoring_metrics(system_type: str, y_true: list, y_pred: list) -> dict:
    if(system_type=='classification'):
        tp,fp,tn,fn=0,0,0,0
        for i,j in zip(y_true,y_pred):
            if(i==1 and j==1):
                tp=tp+1
            elif(i==1 and j==0):
                fp=fp+1
            elif(i==0 and j==1):
                fn=fn+1
            else:
                tn=tn+1
        acc = (tp+tn)/len(y_true)   
        pre =  tp/(tp+fp) if (tp + fp) > 0 else 0.0
        rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = 2 * pre * rec/ (pre+rec) if(pre + rec) > 0 else 0.0 
        return {"accuracy":acc , "precision":pre, "recall": rec , "f1": f1}        
    elif(system_type=='regression'):
        tsum,ssum=0.0,0.0
        for i,j in zip(y_true,y_pred):
            tsum+=abs(i-j)
            ssum+=(i-j)**2        
        mae=tsum/len(y_pred)
        rmse=(ssum/len(y_pred))**0.5
        return {"mae": mae, "rmse": rmse}
    else:
        order = sorted(range(len(y_pred)), key=lambda i: y_pred[i], reverse=True)
        count = 0.0
        for i in order[:3]:
            count+=y_true[i]
        a = sum(y_true)    
        p3 = count/3
        r3 = count/a if a > 0 else 0.0
        return{"precision_at_3": p3, "recall_at_3":r3}    
        
        