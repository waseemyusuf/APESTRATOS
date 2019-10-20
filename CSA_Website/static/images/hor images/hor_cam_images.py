#script that downloads all the images taken by hor cam
import urllib.request


BASE_URL = "ftp://ftp.asc-csa.gc.ca/users/OpenData_DonneesOuvertes/pub/Space%20Apps%20Challenge%202019/STRATOS/Stratos_DataSet/TIMMINS2018/CDH/CAM2-HOR/"


#Had to write a more brute-force like algorithm for downloading since the L images do not have timestamps that match up with the time stamps given
for i in range(100, 488, 2):
    temp_guess = str(i) + ".jpg"
    print("%s downloading: ..."%temp_guess)
    try:
        urllib.request.urlretrieve(BASE_URL + temp_guess,temp_guess)
    except:
        print(temp_guess, " Not found on site checking next file name!")

