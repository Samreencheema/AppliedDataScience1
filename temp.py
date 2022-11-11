# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#1st
#imporitng libraries
import pandas as pd
import matplotlib.pyplot as plt
#reading data from file
file = pd.read_excel(r'C:\Users\DELL\Desktop\ADS1 Assignment\Covid deaths recorded from march-September 2022.xlsx')
#sperating the exel data and saving it inside variables
months = file['Week ending']
months
# Plotting the Graph
plt.figure(figsize= (10,4))
plt.plot(months,file.loc[:,"Hospital"], color="blue", label="total deaths in hospital")
plt.plot(months,file.loc[:,"Care home"],color = "red" , label="total deaths in care home ")
plt.plot(months,file.loc[:,"Home"],color="green", label="total deaths in home")
plt.plot(months,file.loc[:,"Other"],color="brown", label="other deaths")
plt.grid(linewidth=1)
plt.legend()
plt.xlabel("months")
plt.ylabel("total_deaths")
plt.title("death occured in covid")
plt.show()
#2nd
#importing all libraries
import pandas as pd
import matplotlib.pyplot as plt
#reading data from an exel sheet
file = pd.read_csv(r'C:\Users\DELL\Desktop\ADS1 Assignment\2019-20-enforcement-data-sampling.csv')
# Separating data from excel sheet
microbiology = file['AnalysisType-Microbiologicalcontamination']
microbiology
other_contamination = file['AnalysisType-Othercontamination']
other_contamination
Analysis_type_composition = file['AnalysisType-Composition']
total_samples = file['Totalnumberofsamplestaken']
total_samples
# Plotting the Graph
plt.scatter(total_samples,microbiology,color='green',s=100,label='sampling',marker='*')
plt.scatter(other_contamination,Analysis_type_composition,color='yellow',s=100,label='composed samples',marker='*')
#labelling and giving title to the graph
plt.grid()
plt.xlabel('total_samples')
plt.ylabel('microbiology_samples')
plt.legend() 
plt.title('2019-20-enforcement-data-sampling')
#3rd
#importing all libraries
import pandas as pd
import matplotlib.pyplot as plt
#reading data from an exel sheet
file = pd.read_excel(r'C:\Users\DELL\Desktop\ADS1 Assignment\Ages.xlsx')
file.head()
# ploting the graph
file_1 = file.sort_values(by=['All ages'])
file_1
all_ages = file_1['All ages']
all_ages
age_04= file_1['Age 0 to 4']
age_04
age_57= file_1['Age 5 to 7']
age_above85 = file_1['Age 85 and over']
age_above85
plt.fill_between(file_1['All ages'],age_04,label=['Age 0 to 4'],color = 'red')
plt.fill_between(file_1['All ages'],age_57,label=['Age 5 to 7'],color = 'green')
plt.fill_between(file_1['All ages'],age_above85,label=['Age above 85'],color = 'blue')
plt.legend(loc = 'upper left')
plt.xlabel('Total ages')
plt.ylabel('analysis')
plt.title('comparison between ages')