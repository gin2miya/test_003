from django.shortcuts import render

# Create your views here.

##################
###make Heatmap###
##################

import sys
import folium
from folium.plugins import HeatMap
import csv
import pandas as pd



from django.views.decorators.clickjacking import xframe_options_exempt

#@xframe_options_exempt
##@xframe_options_exempted

def index(request):



    return render(request, 'index.html')


def calc(request):

    val1 = int(request.POST['val1'])
#    val2 = int(request.POST['val2'])
#    answer = val1 + val2
#    context = {
#        'answer': answer,
#    }

    #print('answer=' + str(val1))





    #ここから


    csvfile = 'data/気象データ_20200603.csv'

    #csvfile = args[1]
    #map_data = pd.read_csv(csvfile, header=0)
    map_data = pd.read_csv(csvfile, header=1)


    # プロットするデータのリスト
    lon_data = map_data.iloc[:,0]
    lat_data = map_data.iloc[:,1]
    #PV_data = map_data.iloc[:,2]

    R_data_1 = map_data.iloc[:,2]
    R_data_2 = map_data.iloc[:,3]
    R_data_3 = map_data.iloc[:,4]
    R_data_4 = map_data.iloc[:,5]
    R_data_5 = map_data.iloc[:,6]
    R_data_6 = map_data.iloc[:,7]
    R_data_7 = map_data.iloc[:,8]
    R_data_8 = map_data.iloc[:,9]
    R_data_9 = map_data.iloc[:,10]
    R_data_10 = map_data.iloc[:,11]
    R_data_11 = map_data.iloc[:,12]
    R_data_12 = map_data.iloc[:,13]

    T_data_1 = map_data.iloc[:,15]#1月
    T_data_2 = map_data.iloc[:,16]#2月
    T_data_3 = map_data.iloc[:,17]#3月
    T_data_4 = map_data.iloc[:,18]#4月
    T_data_5 = map_data.iloc[:,19]#5月
    T_data_6 = map_data.iloc[:,20]#6月
    T_data_7 = map_data.iloc[:,21]#7月
    T_data_8 = map_data.iloc[:,22]#8月
    T_data_9 = map_data.iloc[:,23]#9月
    T_data_10 = map_data.iloc[:,24]#10月
    T_data_11 = map_data.iloc[:,25]#11月
    T_data_12 = map_data.iloc[:,26]#12月

    X1 = val1

    map_data_index = 0

    E_data_1 = (R_data_1 * 31) + (X1 * T_data_1)
    E_data_2 = (R_data_2 * 29) + (X1 * T_data_2)
    E_data_3 = (R_data_3 * 31) + (X1 * T_data_3)
    E_data_4 = (R_data_4 * 30) + (X1 * T_data_4)
    E_data_5 = (R_data_5 * 31) + (X1 * T_data_5)
    E_data_6 = (R_data_6 * 30) + (X1 * T_data_6)
    E_data_7 = (R_data_7 * 31) + (X1 * T_data_7)
    E_data_8 = (R_data_8 * 31) + (X1 * T_data_8)
    E_data_9 = (R_data_9 * 30) + (X1 * T_data_9)
    E_data_10 = (R_data_10 * 31) + (X1 * T_data_10)
    E_data_11 = (R_data_11 * 30) + (X1 * T_data_11)
    E_data_12 = (R_data_12 * 31) + (X1 * T_data_12)

    E_data = E_data_1 + E_data_2 + E_data_3 + E_data_4 + E_data_5 + E_data_6 + E_data_7 + E_data_8 + E_data_9 + E_data_10 + E_data_11 + E_data_12

    E_data_max = max(E_data)
    E_data_min = min(E_data)

    #print(E_data[0])
    #print(E_data[64799])
    #print(E_data_max)
    #print(E_data_min)

    E_data_step = (E_data_max - E_data_min) / 7

    iE_data_step = int(E_data_step)

    iE_data_max = int(E_data_max)
    iE_data_min = int(E_data_min)

    iE_data_step1 = iE_data_min + iE_data_step
    iE_data_step2 = iE_data_step1 + iE_data_step
    iE_data_step3 = iE_data_step2 + iE_data_step
    iE_data_step4 = iE_data_step3 + iE_data_step
    iE_data_step5 = iE_data_step4 + iE_data_step
    iE_data_step6 = iE_data_step5 + iE_data_step


    #print(iE_data_step1)
    #print(iE_data_step2)
    #print(iE_data_step3)
    #print(iE_data_step4)
    #print(iE_data_step5)
    #print(iE_data_step6)

    ############
    # 7 colors
    ############
    map_data549 = []#350~549
    map_data550 = []#550~699
    map_data700 = []#700~849
    map_data850 = []#850~1000
    map_data1000 = []#1000~1150
    map_data1150 = []#1150~1300
    map_data1300 = []#1300~1500

    for w in E_data:

	    if w < iE_data_step1:
		    PV_temp = (w - iE_data_min) / iE_data_step
		    map_data549.append([lon_data[map_data_index],lat_data[map_data_index], PV_temp ])
    	
	    elif w >= iE_data_step1 and w < iE_data_step2:
		    PV_temp = (w - iE_data_step1) / iE_data_step
		    map_data550.append([lon_data[map_data_index],lat_data[map_data_index], PV_temp ])
    	
	    elif w >= iE_data_step2 and w < iE_data_step3:
		    PV_temp = (w - iE_data_step2) / iE_data_step
		    map_data700.append([lon_data[map_data_index],lat_data[map_data_index], PV_temp ])
    	
	    elif w >= iE_data_step3 and w < iE_data_step4:
		    PV_temp = (w - iE_data_step3) / iE_data_step
		    map_data850.append([lon_data[map_data_index],lat_data[map_data_index], PV_temp ])
    	
	    elif w >= iE_data_step4 and w < iE_data_step5:
		    PV_temp = (w - iE_data_step4) / iE_data_step
		    map_data1000.append([lon_data[map_data_index],lat_data[map_data_index], PV_temp ])
    	
	    elif w >= iE_data_step5 and w < iE_data_step6:
		    PV_temp = (w - iE_data_step5) / iE_data_step
		    map_data1150.append([lon_data[map_data_index],lat_data[map_data_index], PV_temp ])
    	
	    elif w >= iE_data_step6:
		    PV_temp = (w - iE_data_step6) / iE_data_step
		    map_data1300.append([lon_data[map_data_index],lat_data[map_data_index], PV_temp ])

	    else:
		    print ('???')

	    map_data_index = map_data_index + 1

    #print(map_data)  test print,,,,,

    #緯度・経度
    # 地図の中心をセット
    #world_map = folium.Map(location=[36, 140],zoom_start=1)
    #world_map = folium.Map(location=[0, 0],zoom_start=1)
    #world_map = folium.Map([48, 5], tiles='stamentoner', zoom_start=6)

    #world_map = folium.Map(location=[0, 0],zoom_start = 1,max_zoom = 5,width = 500, height = 500)

    world_map = folium.Map(location=[0, 0],tiles = "OpenStreetMap",zoom_start = 1,max_zoom = 5,width = 500, height = 500)

    #world_map = folium.Map(location=[0, 0],attr=copyright_st,tiles="http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",zoom_start = 1,max_zoom = 5,width = 500, height = 500)


    # データをヒートマップとしてプロット
    Radius_temp = 7
    Blur_temp = 20

    #グレイgray
    #青blue
    #黄緑色yellowgreen
    #緑green
    #黄色yellow
    #オレンジorange
    #赤red

    HeatMap(map_data549, name = '549PVポテンシャル_20200508',gradient={1:'gray'},radius=Radius_temp, blur=Blur_temp,max_val=1, max_zoom=18).add_to(world_map)
    HeatMap(map_data550, name = '550PVポテンシャル_20200508',gradient={1:'blue'},radius=Radius_temp, blur=Blur_temp,max_val=1, max_zoom=18).add_to(world_map)
    HeatMap(map_data700, name = '700PVポテンシャル_20200508',gradient={1:'yellowgreen'},radius=Radius_temp, blur=Blur_temp,max_val=1, max_zoom=18).add_to(world_map)
    HeatMap(map_data850, name = '850PVポテンシャル_20200508',gradient={1:'green'},radius=Radius_temp, blur=Blur_temp,max_val=1, max_zoom=18).add_to(world_map)
    HeatMap(map_data1000, name = '1000PVポテンシャル_20200508',gradient={1:'yellow'},radius=Radius_temp, blur=Blur_temp,max_val=1, max_zoom=18).add_to(world_map)
    HeatMap(map_data1150, name = '1150PVポテンシャル_20200508',gradient={1:'orange'},radius=Radius_temp, blur=Blur_temp,max_val=1, max_zoom=18).add_to(world_map)
    HeatMap(map_data1300, name = '1300PVポテンシャル_20200508',gradient={1:'red'},radius=Radius_temp, blur=Blur_temp,max_val=1, max_zoom=18).add_to(world_map)

    # HTMLを出力
    world_map.save('templates/PV_heatmap.html')

    #ここまで



    context = {"variable" : "hello world!"}


    #return render(request, 'index.html', context)
    return render(request, 'index.html')
