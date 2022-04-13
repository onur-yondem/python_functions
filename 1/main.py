class Error(Exception):
    pass

class SortError(Error):
    pass

def bolunen_sayi_bulma(min_sayi, max_sayi, bolunecek_sayi):
    try:
        number_list = []
        if isinstance(min_sayi, int) and isinstance(max_sayi, int) and isinstance(bolunecek_sayi, int):
            if min_sayi < max_sayi:
                for number in range(min_sayi, max_sayi):
                    if number % bolunecek_sayi == 0:
                        number_list.append(number)

                print(number_list)
                toplam_sayi = len(number_list)

                return toplam_sayi

            else:
                raise SortError

        else:
            raise TypeError

    except(TypeError):
        print("Lütfen sadece integer sayı girişi yapın")

    except SortError:
        print("minimum sayı maksimum sayıdan büyük olamaz")

    except Exception as error:
        print("Birşeyler ters gitti..." + error.__class__)



bolunen_sayi_bulma(-25, 50, 5)