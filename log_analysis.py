# -*- coding: utf-8 -*-

import pandas as pd
import os
import numpy as np
import sys

#import csv

import tkinter
import tkinter.filedialog


#from pathlib import Path
#import csv
#import io
#import scipy
#import matplotlib.pyplot as plt

tk = tkinter.Tk()

currentdirectory = os.getcwd()

def getNearestValue(df,num):
	df=df.astype(float)
	lst=list(df.values.flatten())
	idx = np.abs(np.asarray(lst) - num).argmin()
	return idx

def getNearestValueList(df,num):
	df=df.astype(float)
	lst=list(df.values.flatten())
	lst_diff =np.abs(np.asarray(lst)-num)
	idx_lst = np.where(lst_diff == lst_diff.min())
	return idx_lst
	

pd.set_option('display.max_rows' , 1000)

'''
SDM1 Ti   4.67801  - 3.15402
SDM2 SiAl 6.05401  - 4.53599
SSM1 Ag   7.25599  - 5.83900
SSM1 Ti   7.49401  - 6.08299
SSM1 Sn
SDM3 ZnAl 8.66102  - 10.1690
SDM4 ZnSn 10.02500 - 11.55390
'''

target_position_names = ['PM1','PM1 & PM2','PM2','PM3','PM3 & PM4','PM4','PM5','PM5 & PM6','PM6','PM7','PM7 & PM8','PM8','PM9','PM9 & PM10','PM11','PM11 & PM12','PM12']
target_center_position_values  = [3.87,3.96,4.05,5.24,5.33,5.42,6.61,6.70,6.79,7.98,8.07,8.16,9.35,9.44,9.53,10.73,10.82,10.91]
target_waiting_position_values = [4.678,4.678,4.678,6.054,6.054,6.054,7.256,7.256,7.494,8,8,8,8.661,8.661,8.661,10.025,10.025,10.025]
target_end_position_values     = [3.154,3.154,3.154,4.536,4.536,4.356,5.839,5.839,6.083,9,9,9,10.169,10.169,10.169,11.554,11.554,11.554]

target_center_position_dict = dict(zip(target_position_names , target_center_position_values))
target_waiting_position_dict = dict(zip(target_position_names , target_waiting_position_values))


logfile = tkinter.filedialog.askopenfilename(initialdir = 'D:\Wicon32\Run\Visualisation\Logfiles\Substrates',title='Choose the log file', filetypes=[('Log Files', '*.log')])

if os.path.exists(logfile):
	print('path.exists')
	print(logfile)
	
	filename_ext = os.path.basename(logfile)
	filename, ext = os.path.splitext(filename_ext)
	
	df = pd.read_table(logfile)
#	df = pd.read_csv(logfile)
	#['_01_SUBSTART_ID.INPUT']が空白である行を削除
	df = df.dropna(subset=['_01_SUBSTART_ID.INPUT'])

	
	#ログ途中に現れるヘッダー行を削除するため、['_02_LAYER_NUMBER.INPUT']列に['_02_LAYER_NUMBER.INPUT']と記載されている行を削除
	try:
		df = df[df['_02_LAYER_NUMBER.INPUT'] != '_02_LAYER_NUMBER.INPUT']
	except:
		print('except - single layer')

#	df['Date_time'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])

	# pandas DataFrameの型変換
	df['_02_LAYER_NUMBER.INPUT'] = df['_02_LAYER_NUMBER.INPUT'].astype(int)
	df['_4MI1.CURRENT'] = df['_4MI1.CURRENT'].astype(float)
	df['_41TP42.ROTSPD']= df['_41TP42.ROTSPD'].astype(str)

	df['_4MI1.PSETP']   = df['_4MI1.PSETP'].astype(float)	
	df['_4MI1.POWER']   = df['_4MI1.POWER'].astype(float)
	df['_4MI1.CURRENT'] = df['_4MI1.CURRENT'].astype(float)
	df['_4MI1.VOLTAGE'] = df['_4MI1.VOLTAGE'].astype(float)
	
	df['_4MI1.MODE'] = df['_4MI1.MODE'].astype(int)

	df['_4DI1.PSETP']   = df['_4DI1.PSETP'].astype(float)
	df['_4DI1.POWER']   = df['_4DI1.POWER'].astype(float)
	df['_4DI1.CURRENT'] = df['_4DI1.CURRENT'].astype(float)
	df['_4DI1.VOLTAGE'] = df['_4DI1.VOLTAGE'].astype(float)
	
	df['_411FC111.FLOW']   = df['_411FC111.FLOW'].astype(float)
	df['_411FC112.FLOW']   = df['_411FC112.FLOW'].astype(float)
	df['_411FC113.FLOW']   = df['_411FC113.FLOW'].astype(float)
	df['_411FC114.FLOW']   = df['_411FC114.FLOW'].astype(float)

	df['_413FC111.FLOW']   = df['_413FC111.FLOW'].astype(float)
	df['_413FC112.FLOW']   = df['_413FC112.FLOW'].astype(float)
	df['_413FC113.FLOW']   = df['_413FC113.FLOW'].astype(float)
	df['_413FC114.FLOW']   = df['_413FC114.FLOW'].astype(float)

	df['_421FC111.FLOW']   = df['_421FC111.FLOW'].astype(float)
	df['_421FC112.FLOW']   = df['_421FC112.FLOW'].astype(float)
	df['_421FC113.FLOW']   = df['_421FC113.FLOW'].astype(float)
	df['_421FC114.FLOW']   = df['_421FC114.FLOW'].astype(float)

	df['_422FC111.FLOW']   = df['_422FC111.FLOW'].astype(float)
	df['_422FC112.FLOW']   = df['_422FC112.FLOW'].astype(float)
	df['_422FC113.FLOW']   = df['_422FC113.FLOW'].astype(float)
	df['_422FC114.FLOW']   = df['_422FC114.FLOW'].astype(float)

	df['_423FC111.FLOW']   = df['_423FC111.FLOW'].astype(float)
	df['_423FC112.FLOW']   = df['_423FC112.FLOW'].astype(float)
	df['_423FC113.FLOW']   = df['_423FC113.FLOW'].astype(float)
	df['_423FC114.FLOW']   = df['_423FC114.FLOW'].astype(float)

	df['VAP_FC11.FLOW']    = df['VAP_FC11.FLOW'].astype(float)
	df['VAP_FC12.FLOW']    = df['VAP_FC12.FLOW'].astype(float)
	df['VAP_FC13.FLOW']    = df['VAP_FC13.FLOW'].astype(float)
	try:
		df['VAP_FC1.FLOW_ACT'] = df['VAP_FC1.FLOW_ACT'].astype(float)
	except:
		print('old lod - not exist VAP_FC1.FLOW_ACT in this log')
	
	

	#データベースの微修正（ノイズ除去、変換）
	
	try:
		df['POWER_SOURCE_4MI1'] = df['_4MI1'].apply( lambda x:'_4MI1' if (x =="RUN") else "")
		df['POWER_SOURCE_4DI1'] = df['_4DI1'].apply( lambda x:'_4DI1' if (x =="RUN") else "")
	except:
		print('POWER_SOURCE ERROR')
		
	df['POWER_SOURCE'] = df['POWER_SOURCE_4MI1'].str.cat(df['POWER_SOURCE_4DI1'])
	
	df['_4MI1.PSETP']   = df['_4MI1.PSETP'].apply( lambda x:0 if (x < 0.01) else x)
	df['_4MI1.POWER']   = df['_4MI1.POWER'].apply( lambda x:0 if (x < 0.01) else x)
	df['_4MI1.CURRENT'] = df['_4MI1.CURRENT'].apply( lambda x:0 if (x < 0.5) else x)
	df['_4MI1.VOLTAGE'] = df['_4MI1.VOLTAGE'].apply( lambda x:0 if (x < 1) else x)

	try:
		df['_4DI1.PSETP']   = df['_4DI1.PSETP'].apply( lambda x:0 if (x < 0.01) else x)
	except:
		print('Error df[_4DI1.PSETP] - because it may be old logs')
		
	df['_4DI1.POWER']   = df['_4DI1.POWER'].apply( lambda x:0 if (x < 0.01) else x)
	df['_4DI1.CURRENT'] = df['_4DI1.CURRENT'].apply( lambda x:0 if (x < 0.5) else x)
	df['_4DI1.VOLTAGE'] = df['_4DI1.VOLTAGE'].apply( lambda x:0 if (x < 1) else x)

	#DC電源の値とAC電源の値を統合した項目追加
	try:
		df['SETPOWER'] = df['_4MI1.PSETP']+df['_4DI1.PSETP']
	except:
		df['SETPOWER'] = df['_4MI1.PSETP']
		
	df['POWER'] = df['_4MI1.POWER']+df['_4DI1.POWER']
	df['CURRENT'] = df['_4MI1.CURRENT']+df['_4DI1.CURRENT']
	df['VOLTAGE'] = df['_4MI1.VOLTAGE']+df['_4DI1.VOLTAGE']
	
	
	def func_bpmode(x):
		if x == 0:
			return 'DC-A'
		elif x == 1:
			return 'DC-B'
		elif x == 2:
			return 'Full'
		elif x == 3:
			return 'Monopulse-A'
		elif x == 4:
			return 'Monopulse-B'
		elif x == 5:
			return 'Bipulse'
		elif x == 5:
			return 'Bipulse-Trapez'
		else :
			return ''
	
#	df['_4MI1.MODE_NAME'] = df['_4MI1.MODE'].apply( lambda x:'Full' if (x == 2) else ('Monopulse-A' if (x == 3) else ('Monopulse-B' if (x == 4) else ('Bipulse' if (x == 5) else ('Bipulse-Trapez' if (x == 6) else "else mode")))))
	df['_4MI1.MODE_NAME'] = df['_4MI1.MODE'].apply(func_bpmode)


	df['_411FC111.FLOW']   = df['_411FC111.FLOW'].apply( lambda x:0 if (x < 0.1) else x)
	df['_411FC112.FLOW']   = df['_411FC112.FLOW'].apply( lambda x:0 if (x < 0.1) else x)
	df['_411FC113.FLOW']   = df['_411FC113.FLOW'].apply( lambda x:0 if (x < 0.1) else x)
	df['_411FC114.FLOW']   = df['_411FC114.FLOW'].apply( lambda x:0 if (x < 0.1) else x)

	df['_413FC111.FLOW']   = df['_413FC111.FLOW'].apply( lambda x:0 if (x < 0.1) else x)
	try:
		df['_413FC112.FLOW']   = df['_413FC112.FLOW'].apply( lambda x:0 if (x < 0.1) else x)
	except:
		print(' ')
		print('df[_413FC112.FLOW]   = df[_413FC112.FLOW].apply( lambda x:0 if (x < 0.1) else x) is error. Skip.')
		print('  CAUTION : The O2 Flow does not include SSM1')

		
	df['_413FC113.FLOW']   = df['_413FC113.FLOW'].apply( lambda x:0 if (x < 0.1) else x)
	df['_413FC114.FLOW']   = df['_413FC114.FLOW'].apply( lambda x:0 if (x < 0.1) else x)

	df['_421FC111.FLOW']   = df['_421FC111.FLOW'].apply( lambda x:0 if (x < 0.1) else x)
	df['_421FC112.FLOW']   = df['_421FC112.FLOW'].apply( lambda x:0 if (x < 0.1) else x)
	df['_421FC113.FLOW']   = df['_421FC113.FLOW'].apply( lambda x:0 if (x < 0.1) else x)
	df['_421FC114.FLOW']   = df['_421FC114.FLOW'].apply( lambda x:0 if (x < 0.1) else x)

	df['_422FC111.FLOW']   = df['_422FC111.FLOW'].apply( lambda x:0 if (x < 0.1) else x)
	df['_422FC112.FLOW']   = df['_422FC112.FLOW'].apply( lambda x:0 if (x < 0.1) else x)
	df['_422FC113.FLOW']   = df['_422FC113.FLOW'].apply( lambda x:0 if (x < 0.1) else x)
	df['_422FC114.FLOW']   = df['_422FC114.FLOW'].apply( lambda x:0 if (x < 0.1) else x)

	df['_423FC111.FLOW']   = df['_423FC111.FLOW'].apply( lambda x:0 if (x < 0.1) else x)
	df['_423FC112.FLOW']   = df['_423FC112.FLOW'].apply( lambda x:0 if (x < 0.1) else x)
	df['_423FC113.FLOW']   = df['_423FC113.FLOW'].apply( lambda x:0 if (x < 0.1) else x)
	df['_423FC114.FLOW']   = df['_423FC114.FLOW'].apply( lambda x:0 if (x < 0.1) else x)
	
	try:
		df['VAP_FC1.FLOW_ACT']   = df['VAP_FC1.FLOW_ACT'].apply( lambda x:0 if (x < 0.1) else x) 
	except:
		print(' ')
		print('df[VAP_FC1.FLOW_ACT] ERROR occured')
		print('  CAUTION : The O2 Flow does not include VAProcoss SDM2')
		
	df['VAP_FC11.FLOW']   = df['VAP_FC11.FLOW'].apply( lambda x:0 if (x < 0.1) else x)
	df['VAP_FC12.FLOW']   = df['VAP_FC12.FLOW'].apply( lambda x:0 if (x < 0.1) else x)
	df['VAP_FC13.FLOW']   = df['VAP_FC13.FLOW'].apply( lambda x:0 if (x < 0.1) else x)
	
	
	#要チェック_VAPFC11-13の対応
	df['ArFlow'] = df['_411FC111.FLOW'] +df['VAP_FC13.FLOW']+df['_413FC111.FLOW']+df['_421FC111.FLOW']+df['_422FC111.FLOW']+df['_423FC111.FLOW']
	
	# CAUTION #  old version log doesn't have df['_413FC112.FLOW']
	try:
		df['O2Flow'] = df['_411FC112.FLOW'] +df['VAP_FC1.FLOW_ACT']+df['_413FC112.FLOW']+df['_421FC112.FLOW']+df['_422FC112.FLOW']+df['_423FC112.FLOW']
	except:
		try:# log  df['VAP_FC1.FLOW_ACT'] has error
			df['O2Flow'] = df['_411FC112.FLOW'] +df['VAP_FC1.FLOW_ACT']+df['_421FC112.FLOW']+df['_422FC112.FLOW']+df['_423FC112.FLOW']
		except:
			df['O2Flow'] = df['_411FC112.FLOW'] +df['_421FC112.FLOW']+df['_422FC112.FLOW']+df['_423FC112.FLOW']
	df['N2Flow'] = df['_411FC113.FLOW'] +df['VAP_FC12.FLOW']+df['_413FC113.FLOW']+df['_421FC113.FLOW']+df['_422FC113.FLOW']+df['_423FC113.FLOW']
	#df['reserve'] = df['_411FC114.FLOW']+df['VAP_FC11.FLOW'] +df['_413FC114.FLOW']+df['_421FC114.FLOW']+df['_422FC114.FLOW']+df['_423FC114.FLOW']

	df['POWERSUPPLY_4MI1'] = df['_4MI1'].apply( lambda x:'4MI1' if (x =="RUN") else "")
	df['POWERSUPPLY_4DI1'] = df['_4DI1'].apply( lambda x:'4DI1' if (x =="RUN") else "")
	
	df['POWERSUPPLY'] = df['POWERSUPPLY_4MI1'].str.cat(df['POWERSUPPLY_4DI1'])

	def get_totalpower(df):
		if df['_05_CATHODE_USED.INPUT'] == 'PM1 & PM2' :
			return df['PM1KWH.KWH_OUT']
		elif df['_05_CATHODE_USED.INPUT'] == 'PM3 & PM4' :
			return df['PM3KWH.KWH_OUT']
		elif df['_05_CATHODE_USED.INPUT'] == 'PM5' :
			return df['PM5KWH.KWH_OUT']
		elif df['_05_CATHODE_USED.INPUT'] == 'PM6' :
			return df['PM6KWH.KWH_OUT']
		elif df['_05_CATHODE_USED.INPUT'] == 'PM5 & PM6' :
			return df['PM5KWH.KWH_OUT']
		elif df['_05_CATHODE_USED.INPUT'] == 'PM7' :
			return df['PM7KWH.KWH_OUT']
		elif df['_05_CATHODE_USED.INPUT'] == 'PM8' :
			return df['PM8KWH.KWH_OUT']
		elif df['_05_CATHODE_USED.INPUT'] == 'PM7 & PM8' :
			return df['PM7KWH.KWH_OUT']
		elif df['_05_CATHODE_USED.INPUT'] == 'PM9 & PM10' :
			return df['PM9KWH.KWH_OUT']
		elif df['_05_CATHODE_USED.INPUT'] == 'PM11 & PM12' :
			return df['PM11KWH.KWH_OUT']
		else :
			return np.nan


	df['TOTALPOWER'] = df.apply(get_totalpower, axis=1)
	

else:
	#指定したファイルパスが見つからなかった場合
	print(' ')
	print('path does not exist! please check the file path')
	print('path : ', logfile)


layer_number=18
df_during_charging = [0] * layer_number
df_before_deposit = [0] * layer_number
df_during_deposit = [0] * layer_number

df_cathode_name =[0] * layer_number
cathode_name =[0] * layer_number

df_target_material =[0] * layer_number
target_material =[0] * layer_number

columns_list_ = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
rows_list_ = ['Purpose', 'SampleNo' , 'Composition', 'Thickness', 'Material', 'Position', 'PowerSource', 'TotalPower', 'SetPower', 'BeforePower','DuringPower', 'BeforeCurrent','DuringCurrent',  'BeforeVoltage',  'DuringVoltage', 'SetSpeed',
				'SetPass', 'Frequency', 'PulseValue', 'PulseMode', 'PressureMode', 'GasPressure', 'ArFlow', 'O2Flow', 'N2Flow', 'GlassType', 'Temperature', 'TrayNo', 'DynamicDepositionRate', 'RateMesDate', 'RateMeasurerMachine','RateMeasurerPerson',
				'ProcessRecipe', 'DepositionRecipe', 'TotalTime', 'IgnitionRamp', 'IgnitionRampTime', 'IgnitionPower', 'IgnitionWaitTime', 'IgnitionArFlow', 'IgnitionO2Flow', 'IgnitionN2Flow', 'ProcessRamptime', 'ProcessWaitTime']
df_tocsv = pd.DataFrame(np.zeros((44, 18)), columns = columns_list_ , index= rows_list_)
df_tocsv = pd.DataFrame( columns = columns_list_ , index= rows_list_)



target_center_position =[0] * layer_number
target_waiting_position =[0] * layer_number
nearestvalue = [0] * layer_number

for i in range(0,layer_number):
	#print('layer number = ',i)	
	
	df_during_charging[i] = df[(df['_02_LAYER_NUMBER.INPUT'] == i) & (df['CURRENT'] >= 0.3)]
	
	df_before_deposit[i] = df[(df['_02_LAYER_NUMBER.INPUT'] == i) & (df['CURRENT'] >= 0.5)]
	df_during_deposit[i] = df[(df['_02_LAYER_NUMBER.INPUT'] == i) & (df['CURRENT'] >= 0.5)]
		
	if df_during_charging[i].empty == False:
	
		df_cathode_name[i] = df_during_charging[i][['_05_CATHODE_USED.INPUT']][1:2]
		cathode_name[i]=df_cathode_name[i].iloc[0,0]
		
		df_target_material[i] = df_during_charging[i][['_03_TARGET_MATERIAL.INPUT']][1:2]
		target_material[i]=df_target_material[i].iloc[0,0]		
		
		target_waiting_position[i]=target_waiting_position_dict[cathode_name[i]]
		target_center_position[i]=target_center_position_dict[cathode_name[i]]
		
		#print('target waiting position is  ', target_waiting_position[i])
		#print('target center position is  ', target_center_position[i])
		
		row_before_deposit = getNearestValueList(df_during_charging[i]['_4TD.POS'], target_waiting_position[i])[0][-1]
		row_during_deposit = getNearestValue(df_during_charging[i]['_4TD.POS'], target_center_position[i])
		
		
		'''
		
		print('the row index of glass locates in waiting position = ', row_before_deposit)
		print('the row index of glass locates in front of target = ', row_during_deposit)
		
		if row_before_deposit >= row_during_deposit:
			print(' ')
			print('*************** Something wrong about row_before_deposit *************** ')
			print('*********** PAY ATTENTION to the value of before deposit! *********** ')
		
		print('*** before deposit -- before starting deposit ***')
		print(df_during_charging[i][row_before_deposit : row_before_deposit + 1])
		print('*** during deposit -- glass locates in front of the target ***')
		print(df_during_charging[i][row_during_deposit : row_during_deposit + 1])
		
		print('  ')

		
		print('layer ', i, '-', cathode_name[i] ,target_material[i], '  : POWER     before', '{0:8.0f}'.format(round(df_during_charging[i]['POWER'][row_before_deposit : row_before_deposit + 1].iloc[0] * 1000,0)), ' during ', '{0:8.0f}'.format(round(df_during_charging[i]['POWER'][row_during_deposit : row_during_deposit + 1].iloc[0] * 1000, 0)))
		print('layer ', i, '-', cathode_name[i] ,target_material[i], '  : CURRENT   before', '{0:8.2f}'.format(round(df_during_charging[i]['CURRENT'][row_before_deposit : row_before_deposit + 1].iloc[0],2)), ' during ', '{0:8.2f}'.format(round(df_during_charging[i]['CURRENT'][row_during_deposit : row_during_deposit + 1].iloc[0],2)))
		print('layer ', i, '-', cathode_name[i] ,target_material[i], '  : VOLTAGE   before', '{0:8.0f}'.format(round(df_during_charging[i]['VOLTAGE'][row_before_deposit : row_before_deposit + 1].iloc[0],0)), ' during ', '{0:8.0f}'.format(round(df_during_charging[i]['VOLTAGE'][row_during_deposit : row_during_deposit + 1].iloc[0],0)))

		print(' ')
		
		try:
			print('layer ', i, '-', cathode_name[i] ,target_material[i], '  : SETSPEED  ', '{0:8.4f}'.format(float(df_during_charging[i]['_4TD.SETSPEED'][row_during_deposit : row_during_deposit + 1].iloc[0])))
			print('layer ', i, '-', cathode_name[i] ,target_material[i], '  : SETPASS   ', '{0:8.2f}'.format(float(df_during_charging[i]['_4TD.SETOSZCOUNT'][row_during_deposit : row_during_deposit + 1].iloc[0])))
			print('  ')
		except:
			print('It seems old log. Then SETSPEED and PASSES cant show.')

		print('layer ', i, '-', cathode_name[i] ,target_material[i], '  : _4CG41    before', '{0:8.2f}'.format(float(df_during_charging[i]['_4CG41.VALUE'][row_before_deposit : row_before_deposit + 1].iloc[0])), ' during ', '{0:8.2f}'.format(float(df_during_charging[i]['_4CG41.VALUE'][row_during_deposit : row_during_deposit + 1].iloc[0])))

		
		print('layer ', i, '-', cathode_name[i] ,target_material[i], '  : Ar FLOW   before', '{0:8.1f}'.format(df_during_charging[i]['ArFlow'][row_before_deposit : row_before_deposit + 1].iloc[0]), 
			 ' during ', '{0:8.1f}'.format(df_during_charging[i]['ArFlow'][row_during_deposit : row_during_deposit + 1].iloc[0]))
		
		print('layer ', i, '-', cathode_name[i] ,target_material[i], '  : O2 FLOW   before', '{0:8.1f}'.format(df_during_charging[i]['O2Flow'][row_before_deposit : row_before_deposit + 1].iloc[0]), 
			' during ', '{0:8.1f}'.format(df_during_charging[i]['O2Flow'][row_during_deposit : row_during_deposit + 1].iloc[0]))
		
		print('layer ', i, '-', cathode_name[i] ,target_material[i], '  : N2 FLOW   before', '{0:8.1f}'.format(df_during_charging[i]['N2Flow'][row_before_deposit : row_before_deposit + 1].iloc[0]), 
			' during ', '{0:8.1f}'.format(df_during_charging[i]['N2Flow'][row_during_deposit : row_during_deposit + 1].iloc[0]))
		
		print('  ')
		
		''' #end
		
		df_tocsv.loc['SampleNo',1] = df_during_charging[i]['_01_SUBSTART_ID.INPUT'][row_during_deposit : row_during_deposit + 1].iloc[0]
		df_tocsv.loc['Material',i] = df_during_charging[i]['_03_TARGET_MATERIAL.INPUT'][row_during_deposit : row_during_deposit + 1].iloc[0]
		df_tocsv.loc['Position',i] = df_during_charging[i]['_05_CATHODE_USED.INPUT'][row_during_deposit : row_during_deposit + 1].iloc[0]
		df_tocsv.loc['PowerSource',i] = df_during_charging[i]['POWER_SOURCE'][row_during_deposit : row_during_deposit + 1].iloc[0]
		df_tocsv.loc['TotalPower',i] = df_during_charging[i]['TOTALPOWER'][row_during_deposit : row_during_deposit + 1].iloc[0]
		df_tocsv.loc['SetPower',i] = df_during_charging[i]['SETPOWER'][row_during_deposit : row_during_deposit + 1].iloc[0]
		
		df_tocsv.loc['BeforePower',i] = df_during_charging[i]['POWER'][row_before_deposit : row_before_deposit + 1].iloc[0] * 1000
		df_tocsv.loc['DuringPower',i] = df_during_charging[i]['POWER'][row_during_deposit : row_during_deposit + 1].iloc[0] * 1000
		df_tocsv.loc['BeforeCurrent',i] = df_during_charging[i]['CURRENT'][row_before_deposit : row_before_deposit + 1].iloc[0]
		df_tocsv.loc['DuringCurrent',i] = df_during_charging[i]['CURRENT'][row_during_deposit : row_during_deposit + 1].iloc[0] 
		df_tocsv.loc['BeforeVoltage',i] = df_during_charging[i]['VOLTAGE'][row_before_deposit : row_before_deposit + 1].iloc[0]
		df_tocsv.loc['DuringVoltage',i] = df_during_charging[i]['VOLTAGE'][row_during_deposit : row_during_deposit + 1].iloc[0]

		df_tocsv.loc['SetSpeed',i] = df_during_charging[i]['_4TD.SETSPEED'][row_during_deposit : row_during_deposit + 1].iloc[0]
		df_tocsv.loc['SetPass',i] = df_during_charging[i]['_4TD.SETOSZCOUNT'][row_during_deposit : row_during_deposit + 1].iloc[0]
		
		
		if df_during_charging[i]['POWER_SOURCE'][row_during_deposit : row_during_deposit + 1].iloc[0] == '_4MI1' :
			df_tocsv.loc['Frequency',i] = df_during_charging[i]['_4MI1.FREQ'][row_during_deposit : row_during_deposit + 1].iloc[0]
			df_tocsv.loc['PulseValue',i] = df_during_charging[i]['_4MI1.PULSE_DURATION_SHIFT'][row_during_deposit : row_during_deposit + 1].iloc[0]
			df_tocsv.loc['PulseMode',i] = df_during_charging[i]['_4MI1.MODE_NAME'][row_during_deposit : row_during_deposit + 1].iloc[0]
			
		elif df_during_charging[i]['POWER_SOURCE'][row_during_deposit : row_during_deposit + 1].iloc[0] == '_4DI1' :
			try:
				if df_during_charging[i]['_4DI1.PULSE_ENABLED'][row_during_deposit : row_during_deposit + 1].iloc[0] == 1 :
					df_tocsv.loc['Frequency',i] = df_during_charging[i]['_4DI1.FREQUENCY'][row_during_deposit : row_during_deposit + 1].iloc[0]
					df_tocsv.loc['PulseValue',i] = df_during_charging[i]['_4DI1.REVERSE_VOLTAGE'][row_during_deposit : row_during_deposit + 1].iloc[0]
					df_tocsv.loc['PulseMode',i] = df_during_charging[i]['_4DI1.PULSETIME'][row_during_deposit : row_during_deposit + 1].iloc[0]
				elif df_during_charging[i]['_4DI1.PULSE_ENABLED'][row_during_deposit : row_during_deposit + 1].iloc[0] == 0 :
					df_tocsv.loc['Frequency',i] = '-'
					df_tocsv.loc['PulseValue',i] = '-'
					df_tocsv.loc['PulseMode',i] = '-'
			except:
				print('old log -  DC pulse log dont exist')

		df_tocsv.loc['PressureMode',i] = df_during_charging[i]['_4PCU'][row_during_deposit : row_during_deposit + 1].iloc[0]		
		df_tocsv.loc['GasPressure',i] = df_during_charging[i]['_4CG41.VALUE'][row_during_deposit : row_during_deposit + 1].iloc[0]
		
		df_tocsv.loc['ArFlow',i] = df_during_charging[i]['ArFlow'][row_during_deposit : row_during_deposit + 1].iloc[0]
		df_tocsv.loc['O2Flow',i] = df_during_charging[i]['O2Flow'][row_during_deposit : row_during_deposit + 1].iloc[0]
		df_tocsv.loc['N2Flow',i] = df_during_charging[i]['N2Flow'][row_during_deposit : row_during_deposit + 1].iloc[0]
		
		df_tocsv.loc['TrayNo',i] = df_during_charging[i]['_00_SLOT_NUMBER.INPUT'][row_during_deposit : row_during_deposit + 1].iloc[0]
		df_tocsv.loc['ProcessRecipe',1] = filename
		
		df_tocsv.loc['TotalTime'] = df['Time'].values[-1]
		#print(df['Time'].values[-1] - df['Time'].values[0])
		

''' # comment out start
print('Integeral power before this coating program start ')
print(' PM01KWH.KWH_OUT ', '{0:8.1f}'.format(float(df['PM1KWH.KWH_OUT'][0])))
print(' PM02KWH.KWH_OUT ', '{0:8.1f}'.format(float(df['PM2KWH.KWH_OUT'][0])))
print('  ')
print(' PM03KWH.KWH_OUT ', '{0:8.1f}'.format(float(df['PM3KWH.KWH_OUT'][0])))
print(' PM04KWH.KWH_OUT ', '{0:8.1f}'.format(float(df['PM4KWH.KWH_OUT'][0])))
print('  ')
print(' PM05KWH.KWH_OUT ', '{0:8.1f}'.format(float(df['PM5KWH.KWH_OUT'][0])))
print(' PM06KWH.KWH_OUT ', '{0:8.1f}'.format(float(df['PM6KWH.KWH_OUT'][0])))
print('  ')
print(' PM07KWH.KWH_OUT ', '{0:8.1f}'.format(float(df['PM7KWH.KWH_OUT'][0])))
print(' PM08KWH.KWH_OUT ', '{0:8.1f}'.format(float(df['PM8KWH.KWH_OUT'][0])))
print('  ')
print(' PM09KWH.KWH_OUT ', '{0:8.1f}'.format(float(df['PM9KWH.KWH_OUT'][0])))
print(' PM10KWH.KWH_OUT ', '{0:8.1f}'.format(float(df['PM10KWH.KWH_OUT'][0])))
print('  ')
print(' PM11KWH.KWH_OUT ', '{0:8.1f}'.format(float(df['PM11KWH.KWH_OUT'][0])))
print(' PM12KWH.KWH_OUT ', '{0:8.1f}'.format(float(df['PM12KWH.KWH_OUT'][0])))
print(' The Log Data ')
''' #  comment out end

print(logfile)

df_tocsv.to_csv(str(filename) + ".csv", index = False, header = False, index_label =False)

print('')
print('finish!')
print(str(filename) + ".csv")

sys.exit()


idx= getNearestValue(df['_4TD.POS'],3.16)
print(df['_4TD.POS'].iat[idx])

