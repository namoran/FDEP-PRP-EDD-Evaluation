import csv
import sys
from operator import itemgetter
import os
import fileinput

GCTLs = {'benzene':1,
         'acetone':6300,
         'acenaphthene':20,
         'acenaphthylene':210,
         'anthracene':2100,
         'benzo(a)anthracene':0.05,
         'benzo(a)pyrene':0.2,
         'benzo(b)fluoranthene':0.05,
         'benzo(g,h,i)perylene':210,
         'benzo(k)fluoranthene': 0.5,
         'chrysene':4.8,
         'dibenz(a,h)anthracene':0.005,
         'dibromochloromethane':0.4,
         'fluoranthene':280,
         'fluorene':280,
         'indeno(1,2,3-cd)pyrene':0.05,
         'isopropylbenzene':0.8,
         'cumene':0.8,
         '1-methylnaphthalene':28,
         '1-methylnaphthalene':28,
         '2-methylnaphthalene':28,
         'naphthalene':14,
         'phenanthrene':210,
         'pyrene':210,
         'ethylbenzene':30,
         'toluene':40,
         'xylenes, total':20,
         'xylenes- total':20,
         'dibromoethane, 1,2-':0.02,
         'edb':0.02,
         'dichloroethane, 1,2-':3,
         'mtbe':20,
         'methyl-t-butyl ether':20,
         'trphs':5000,
         'total recoverable pet. hydrocarbons':5000,
         'arsenic':10,
         'cadmium':5,
         'chromium (total)':100,
         'lead':15}

NADCs = {'benzene':100,
         'acenaphthene':200,
         'acenaphthylene':2100,
         'anthracene':21000,
         'benzo(a)anthracene':5, 
         'benzo(a)pyrene':20,
         'benzo(b)fluoranthene':5,
         'benzo(g,h,i)perylene':2100,
         'benzo(k)fluoranthene': 50, 
         'chrysene':480,
         'dibenz(a,h)anthracene':0.5,
         'fluoranthene':2800,
         'fluorene':2800,
         'indeno(1,2,3-cd)pyrene':5,
         'isopropylbenzene':8,
         'cumene':8,
         '1-methylnaphthalene':280,
         '1-methylnaphthalene':280,
         '2-methylnaphthalene':280,
         'naphthalene':140,
         'phenanthrene':2100,
         'pyrene':2100, 
         'ethylbenzene':300,
         'toluene':400,
         'xylenes, total':200,
         'xylenes- total':200,
         'dibromoethane, 1,2-':2,
         'edb':2,
         'dichloroethane, 1,2-':300, 
         'mtbe':200,
         'methyl-t-butyl ether':200,
         'trphs':50000,
         'total recoverable pet. hydrocarbons':50000,
         'arsenic':100,
         'cadmium':50,
         'chromium (total)':1000,
         'lead':150}

HitSummary = []
GCTLSummary = []
NADCSummary = []
DetectionSummary = []
EDD = []


def display_table(list):
        sortedlist = sorted(list,key=itemgetter('Parameter'))
        sortedlist = sorted(sortedlist,key=itemgetter('TestSite_Name'))
        for count, row in enumerate(sortedlist):
                if row['Parameter'] in ['Water Level (NGVD)', 'Dissolved Oxygen', 'Specific Conductance', 'Temperature, Water', 'Turbidity', 'pH']:
                        continue
                if row['Qualifier']!= 'U':
                        Detection = 'Detection'
                else:
                        Detection = ''

                        


                if GCTLs.get(row['Parameter']) != None:
                        GCTLno = GCTLs.get(row['Parameter'].lower())
                else:
                        GCTLno = ''
                        
                if NADCs.get(row['Parameter']) != None:
                        NADCno = NADCs.get(row['Parameter'].lower())
                else:
                        NADCno = ''
                        
                        
                if   GCTLs.get(row['Parameter'].lower()) != None and row['Units'] == 'ug/L' and float(row['Result']) > float(GCTLs.get(row['Parameter'].lower())):
                        GCTL_Exceedance = 'GCTL_Exceedance'
                      
                        
                elif GCTLs.get(row['Parameter'].lower()) != None and row['Units'] == 'mg/L' and float(row['Result'])*1000 > float(GCTLs.get(row['Parameter'].lower())):
                        GCTL_Exceedance = 'GCTL_Exceedance'
                       
                else:
                        GCTL_Exceedance = ''

                        

                if   NADCs.get(row['Parameter'].lower()) != None and row['Units'] == 'ug/L' and float(row['Result']) > float(NADCs.get(row['Parameter'].lower())):
                        NADC_Exceedance = 'NADC_Exceedance'
                       
                        
                elif NADCs.get(row['Parameter'].lower()) != None and row['Units'] == 'mg/L' and float(row['Result'])*1000 > float(NADCs.get(row['Parameter'].lower())):
                        NADC_Exceedance = 'NADC_Exceedance'
                        
                else:
                        NADC_Exceedance = ''
                                
                print("{:<17}{:<37}{:>6}{:^3}{:<10}{:>10}{:>10}{:^25}{:^25}{:^25}".format \
                      (row['TestSite_Name'], row['Parameter'], row['Result'], row['Qualifier'],\
                       row['Units'], GCTLno, NADCno, Detection, GCTL_Exceedance, NADC_Exceedance))

                




#os.system("mode con: cols=180")
with open(sys.argv[1],newline='') as file:
	reader = csv.reader(file)
	for count, row in enumerate(reader):
		if count < 1:
			continue
		elif count == 1:
			fieldnames = row
			print(fieldnames)
			break
print(fieldnames)		
fileset = fileinput.input(sys.argv[1:])
reader = csv.DictReader(fileset,fieldnames=fieldnames)
for count, row in enumerate(reader):
                EDD.append(row)

                if row['Qualifier']!= 'U':
                        Detection = 'Detection'
                        DetectionSummary.append(row)
                else:
                        Detection = ''

                        


                if GCTLs.get(row['Parameter']) != None:
                        GCTLno = GCTLs.get(row['Parameter'].lower())
                else:
                        GCTLno = ''
                        
                if NADCs.get(row['Parameter']) != None:
                        NADCno = NADCs.get(row['Parameter'].lower())
                else:
                        NADCno = ''
                        
                        
                if   GCTLs.get(row['Parameter']) != None and row['Units'] == 'ug/L' and float(row['Result']) > float(GCTLs.get(row['Parameter'].lower())):
                        GCTL_Exceedance = 'GCTL_Exceedance'
                        HitSummary.append(row)
                        GCTLSummary.append(row)
                        
                elif GCTLs.get(row['Parameter']) != None and row['Units'] == 'mg/L' and float(row['Result'])*1000 > float(GCTLs.get(row['Parameter'].lower())):
                        GCTL_Exceedance = 'GCTL_Exceedance'
                        HitSummary.append(row)
                        GCTLSummary.append(row)
                else:
                        GCTL_Exceedance = ''

                        

                if   NADCs.get(row['Parameter']) != None and row['Units'] == 'ug/L' and float(row['Result']) > float(NADCs.get(row['Parameter'].lower())):
                        NADC_Exceedance = 'NADC_Exceedance'
                        #HitSummary.append(row)
                        NADCSummary.append(row)
                        GCTLSummary.pop()
                        
                elif NADCs.get(row['Parameter']) != None and row['Units'] == 'mg/L' and float(row['Result'])*1000 > float(NADCs.get(row['Parameter'].lower())):
                        NADC_Exceedance = 'NADC_Exceedance'
                        #HitSummary.append(row)
                        NADCSummary.append(row)
                        GCTLSummary.pop()
                else:
                        NADC_Exceedance = ''
                                
##                print("{:<7}{:<37}{:>6}{:^3}{:<10}{:>10}{:>10}{:^25}{:^25}{:^25}".format \
##                      (row['TestSite_Name'], row['Parameter'], row['Result'], row['Qualifier'],\
##                       row['Units'], GCTLno, NADCno, Detection, GCTL_Exceedance, NADC_Exceedance))


        


print(" HitSummary ".center(158,"*"))
print('')
display_table(HitSummary)
print('')
print('')
print(' GCTL_Exceedances '.center(158,'*'))
print('')
display_table(GCTLSummary)
print('')
print('')
print(' NADC_Exceedance '.center(158,'*'))
print('')
display_table(NADCSummary)
print('')
print('')
print(' DetectionSummary '.center(158,'*'))
print('')
display_table(DetectionSummary)
print('')
print('')

input('Press Enter to close')

	
