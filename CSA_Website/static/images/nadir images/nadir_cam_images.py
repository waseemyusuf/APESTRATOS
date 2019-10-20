#Script that downloads the images taken by nadir
import urllib.request

BASE_URL = "ftp://ftp.asc-csa.gc.ca/users/OpenData_DonneesOuvertes/pub/Space%20Apps%20Challenge%202019/STRATOS/Stratos_DataSet/TIMMINS2018/CDH/CAM1-NADIR/"

#Had to write a more brute-force like algorithm for downloading since the L images do not have timestamps that match up with the time stamps given
base = 103
for i in range(387):
    temp_guess = str(base + i) + ".jpg"
    temp_guess_L = str(base + i) + "L.jpg"
    print("%s downloading: ..."%temp_guess)
    try:
        urllib.request.urlretrieve(BASE_URL + temp_guess,temp_guess)
    except:
        print(temp_guess, " Not found on site checking next key!")
    try:
        urllib.request.urlretrieve(BASE_URL + temp_guess_L, temp_guess_L)
    except:
        print(temp_guess_L," Not found on site checking next key!")

