class Error(Exception):
    pass


class NumberMismatch(Error):
    pass


def not_hesapla(vize1, vize2, final):
    try:
        if isinstance(vize1, int) and isinstance(vize2, int) and isinstance(final, int):
            if vize1 >= 0 and vize1 <= 100 and vize2 >= 0 and vize2 <= 100 and final >= 0 and final <=100:
                vize1_effect = vize1 * 3 / 10
                vize2_effect = vize2 * 3 / 10
                final_effect = final * 4 / 10

                total_grade = vize1_effect + vize2_effect + final_effect

                if total_grade >= 90:
                    print("AA")

                elif total_grade >= 85:
                    print("BA")

                elif total_grade >= 80:
                    print("BB")

                elif total_grade >= 75:
                    print("CB")

                elif total_grade >= 70:
                    print("CC")

                elif total_grade >= 65:
                    print("DC")

                elif total_grade >= 60:
                    print("DD")

                elif total_grade >= 55:
                    print("FD")

                elif total_grade < 55:
                    print("FF")

            else:
                raise NumberMismatch

        else:
            raise TypeError

    except(NumberMismatch):
        print("Not 0'dan küçük veya 100'den büyük olamaz")

    except(TypeError):
        print("Lütfen parametreleri integer giriniz")


not_hesapla(100, 40, 65)
