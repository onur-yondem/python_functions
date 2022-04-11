class Error(Exception):
    pass

class digitMismatch(Error):
    pass

def sayiAtama(number):
    try:
        if isinstance(number, int):
            if number / 10 >= 1 and number / 10 < 10 or number / 10 < -1 and number / 10 > -10:
                two_digit_number = number
                sayiOkunusu(two_digit_number)
            else:
                raise digitMismatch
        else:
            raise TypeError

    except digitMismatch:
        print("Sayı basamağı 2'den küçük veya 2'den büyük olamaz")

    except TypeError:
        print("Girilen sayı integer olmalı")

    except Exception as e:
        print("Birşeyler ters gitti..." + e.__class__)

def sayiOkunusu(number):
    second_digits_dict = {0:"",1:"bir",2:"iki",3:"üç",4:"dört",5:"beş",6:"altı",7:"yedi",8:"sekiz",9:"dokuz"}
    first_digits_dict = {1:"on",2:"yirmi",3:"otuz",4:"kırk",5:"elli",6:"altmış",7:"yetmiş",8:"seksen",9:"doksan"}

    first_digit = int(abs(number)/10)
    second_digit = abs(number)%10
    stringNumber = first_digits_dict[first_digit] + second_digits_dict[second_digit]
    print("eksi " + stringNumber if number < 0 else stringNumber)

sayiAtama(-99.5)