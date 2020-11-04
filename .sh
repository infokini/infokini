#!/bin/bash

HIJAU='\033[0;32m'
MERAH='\033[01;31m'
NORMAL='\033[0m'
CYAN='\033[0;36m'
BIRU='\033[0;34m'
PUTIH='\033[1;37m'

main(){
	url="https://data.bmkg.go.id/lastgempadirasakan.xml";
	getData=$(curl -s "${url}" >> result.xml);
	if [[ -z $(cat result.xml) ]]; then
		echo "Error: Cannot create object";
	else
		echo " Tanggal    :" $(cat result.xml  | grep -Po '(?<=<Tanggal>).*?(?=<)')
		echo " Jam        :" $(cat result.xml  | grep -Po '(?<=<Jam>).*?(?=<)')
		echo ""
		printf "${NORMAL}"
		echo " Lintang    :" $(cat result.xml  | grep -Po '(?<=<Lintang>).*?(?=<)')
		echo " Bujur      :" $(cat result.xml  | grep -Po '(?<=<Bujur>).*?(?=<)')
		echo " Magnitude  :" $(cat result.xml  | grep -Po '(?<=<Magnitude>).*?(?=<)')
		echo " Kedalaman  :" $(cat result.xml  | grep -Po '(?<=<Kedalaman>).*?(?=<)')
		printf "${HIJAU}"
		echo ""
		echo " Keterangan  :" $(cat result.xml  | grep -Po '(?<=<Keterangan>).*?(?=<)')
		echo ""
		echo " Dirasakan   :" $(cat result.xml  | grep -Po '(?<=<Dirasakan>).*?(?=<)')
		echo ""
		echo " Linkdetail  :" $(cat result.xml  | grep -Po '(?<=<Linkdetail>).*?(?=<)')
		echo ""
		printf "${NORMAL}"
	fi
echo ""
read -p "==Enter untuk kembali== " user 
echo
echo "JANGAN LUPA BAHAGIA :D $user"
rm result.xml
python info.py
}
clear;
printf "${MERAH}"
cat << "banner"
===================================
   ____                            
  / ___| ___ _ __ ___  _ __   __ _ 
 | |  _ / _ \ '_ ` _ \| '_ \ / _` |
 | |_| |  __/ | | | | | |_) | (_| |
  \____|\___|_| |_| |_| .__/ \__,_|
                      |_|   TERKINI
===================================

banner
printf "${NORMAL}"
main $1
