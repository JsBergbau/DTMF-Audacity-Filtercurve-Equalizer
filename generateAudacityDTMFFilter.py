####### Change here ##########
bandwith=15
baseline=-30
boost=5
####### End change here ######


#Source https://de.wikipedia.org/wiki/Mehrfrequenzwahlverfahren
dtmfFrequencies=[697 , 770, 852, 941, 1209, 1336, 1477, 1633]

res="FilterCurve:"
bandwithHalf = bandwith / 2
i=0
for frequency in dtmfFrequencies:
	lower = frequency - bandwithHalf
	upper = frequency + bandwithHalf
	res+=f'f{i}="{lower}" v{i}="{baseline}" '
	i+=1
	res+=f'f{i}="{frequency}" v{i}="{boost}" '
	i+=1
	res+=f'f{i}="{upper}" v{i}="{baseline}" '
	i+=1
	

res+='InterpolateLin="0" InterpolationMethod="B-spline"'

print(res)