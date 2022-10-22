import numpy as np 
import pickle
import config 
import json

class Medicalin():
    def __init__(self,age,sex,bmi,children,smoker,region):
        self.age=age   
        self.sex=sex 
        self.bmi=bmi 
        self.children=children 
        self.smoker=smoker 
        self.region="region_"+region
    
    def load_model(self):
        with open(config.MODEL_PATH,"rb")as f:
            self.model=pickle.load(f)
            
        with open(config.JSON_FILE_PATH,"r")as f:
            self.json_data=json.load(f)
            
    def get_predictedcharges(self):
        self.load_model()
        
        region_index=self.json_data["columns"].index(self.region)
        test_array=np.zeros(len(self.json_data["columns"]))
        test_array[0]=self.age 
        test_array[1]=self.json_data["sex"][self.sex]
        test_array[2]=self.bmi 
        test_array[3]=self.children 
        test_array[4]=self.json_data["smoker"][self.smoker]
        test_array[region_index]=1
        
        
        print("test_array",test_array)
        predicted_charge=self.model.predict([test_array])
        print("predicted charge",predicted_charge)
        return predicted_charge
        
        
if __name__ == "__main__" :
    age=34
    sex="female"
    bmi=27.9
    children=4
    smoker="no"
    region="northeast"
    
    med=Medicalin(age,sex,bmi,children,smoker,region)
    print("predicted charge:",med.get_predictedcharges())
    
        
    
    
