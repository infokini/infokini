class bcolors:
    HIJAU='\033[0;32m'
    MERAH='\033[01;31m'
    NORMAL='\033[0m'
    CYAN='\033[0;36m'
    BIRU='\033[0;34m'
    PUTIH='\033[1;37m'
import os
try:
	import requests
except:
	os.system('pip install requests')
	import requests

rs = requests.Session()

def menu():
	os.system('clear')
	print('')
	os.system('toilet -f smblock --filter border:metal INFO TERKINI!') 
	print('    \033[0;37m[ INFO COVID DAN GEMPA INDONESIA ]')
	print('') 
	print('    [✓] Tunggu beberapa detik agar script bekerja dengan baik')
	print('    [•] Author  : Pandas ID') 
	print('    Data diambil dari situs kawalcorona.com & bmkg ')
	print('    ==================================')
	print('    [1] Covid Indonesia')
	print('    [2] Provinsi Di Indonesia')
	print('    [3] Covid Dunia') 
	print('    [4] Info Gempa')
	print('    [0] Exit')
	pil()

def pil():
	print('')
	pilih = input('    [•] Chose: ')
	if pilih == '1':
		indonesia()
	elif pilih == '2':
		prov()
	elif pilih == '3':
		dunia()
	elif pilih == '4':
		os.system('bash .sh') 
	elif pilih == '0':
		print('')
		print('    [•] Silahkan Share Script Ini ')
		exit()
	else:
		print('')
		print('    [!] Silahkan masukan angka pilihan 1 2 3 4 0')
		
def indonesia():
	indonesia = rs.get('https://api.kawalcorona.com/indonesia')
	data = indonesia.json()
	negara = data[0]['name']
	positif = data[0]['positif']
	sembuh = data[0]['sembuh']
	mati = data[0]['meninggal']
	print('')
	print('    \033[1;37m[ DATA KASUS CORONA DI INDONESIA ]')
	print('    ==================================')
	print('')
	print('    \033[01;31m[•] Negara :',negara)
	print('    [•] Positif Corona : ' + str(positif) + ' orang')
	print('    \033[1;37m[•] Sembuh : ' + str(sembuh) + ' orang')
	print('    [•] Meninggal : ' + str(mati) + ' orang')
	print('    [•] Link : https://kawalcorona.com')
	print('')
	input('    [ Kembali ]')
	menu()
	
def prov():
	url_prov = rs.get('https://api.kawalcorona.com/indonesia/provinsi')
	data_prov = url_prov.json()
	print('')
	print('    \033[1;37m[ DATA KASUS CORONA DI SETIAP PROVINSI DI INDONESIA ]')
	print('    =====================================================')
	print('')
	for x in data_prov:
		nama_prov = (x['attributes']['Provinsi'])
		positif = (x['attributes']['Kasus_Posi'])
		sembuh = (x['attributes']['Kasus_Semb'])
		mati = (x['attributes']['Kasus_Meni']) 
		print('    \033[93m[•] Provinsi :',nama_prov)
		print('    [•] Positif Corona : ' + str(positif) + ' orang')
		print('    [•] Sembuh : ' + str(sembuh) + ' orang')
		print('    [•] Meninggal : ' + str(mati) + ' orang')
		print('')
	print('    [•] Total Provinsi :',len(data_prov))
	print('')
	input('    [ Kembali ]')
	menu()

def dunia():
	positif = rs.get('https://api.kawalcorona.com/positif').json()
	sembuh = rs.get('https://api.kawalcorona.com/sembuh').json()
	mati = rs.get('https://api.kawalcorona.com/meninggal').json()
	ttl_positif = positif['value']
	ttl_sembuh = sembuh['value']
	ttl_mati = mati['value']
	print('')
	print('    \033[1;37m[ DATA KASUS CORONA DI SELURUH DUNIA ]')
	print('    ======================================')
	print('')
	print('    \033[1;37m[•] Total Positif : ' + str(ttl_positif) + ' orang')
	print('    [•] Total Sembuh : ' + str(ttl_sembuh) + ' orang')
	print('    [•] Total Meninggal : ' + str(ttl_mati) + ' orang')
	print('')
	print('    [✓] Link :https://kawalcorona.com')
	input('    [ Kembali ]')
	menu()
menu()
