from django.db import models


def eng_to_persian(user_number):
    persian_numbers = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹']
    eng_number = str(user_number)
    persian_number = ''
    for i in range(len(eng_number)):
        num = eng_number[i]
        if num == ',':
            persian_number = f"{persian_number}٬"
        else:
            fa_num = persian_numbers[int(num)]
            persian_number = f"{persian_number}{fa_num}"

    return persian_number


class Account(models.Model):
    f_name = models.CharField(
        max_length=255,
        verbose_name='نام',
    )
    l_name = models.CharField(
        max_length=255,
        verbose_name='نام‌خانوادگی',
    )
    number = models.CharField(
        max_length=16,
        verbose_name='شماره',
        unique=True
    )

    class Meta:
        verbose_name = "حساب بانکی"
        verbose_name_plural = "حساب‌های بانکی"

    def __str__(self):
        return f"{self.f_name} {self.l_name}  |  {str(self.number)[12:16]}"

    def full_name(self):
        return f"{self.f_name} {self.l_name}"

    def fa_number(self):
        p1 = eng_to_persian(self.number)[0:4]
        p2 = eng_to_persian(self.number)[4:8]
        p3 = eng_to_persian(self.number)[8:12]
        p4 = eng_to_persian(self.number)[12:16]

        return f"{p1}-{p2}-{p3}-{p4}"

    def fa_number_p1(self):
        p1 = eng_to_persian(self.number)[0:4]

        return f"{p1}"

    def fa_number_p2(self):
        p2 = eng_to_persian(self.number)[4:8]

        return f"{p2}"

    def fa_number_p3(self):
        p3 = eng_to_persian(self.number)[8:12]

        return f"{p3}"

    def fa_number_p4(self):
        p4 = eng_to_persian(self.number)[12:16]

        return f"{p4}"

    def number_p1(self):
        p1 = self.number[0:4]

        return f"{p1}"

    def number_p2(self):
        p2 = self.number[4:8]

        return f"{p2}"

    def number_p3(self):
        p3 = self.number[8:12]

        return f"{p3}"

    def number_p4(self):
        p4 = self.number[12:16]

        return f"{p4}"

    def get_bank(self):
        banks = {
            'MELI': '603799',
            'SEPAH': '589210',
            'TOSE_SAD': '627648',
            'SANAT_MADAN': '627961',
            'KESHAVAR': '603770',
            'MASKAN': '628023',
            'POST_BAN': '627760',
            'TOSE_TAVON': '502908',
            'EQTESAT_NOVIN': '627412',
            'PARSIYAN': '622106',
            'PASARGAD': '502229',
            'CARAFARIN': '627488',
            'SAMAN': '621986',
            'SINA': '639346',
            'SARMAYE': '639607',
            'TAT': '636214',
            'SHAHR': '502806',
            'DAY': '502938',
            'SADERAT': '603769',
            'MELAT': '610433',
            'TEJARAT': '627353',
            'TEJARAT_JADID': '585983',
            'RAFAH': '589463',
            'ANSAR': '627381',
            'MEHR_AQTESAD': '639370',
        }
        keys = [k for k, v in banks.items() if v == self.number[:6]]
        if keys:
            return keys[0]

        return None

    def get_fa_bank(self):
        banks = {
            'MELI': '603799',
            'SEPAH': '589210',
            'TOSE_SAD': '627648',
            'SANAT_MADAN': '627961',
            'KESHAVAR': '603770',
            'MASKAN': '628023',
            'POST_BAN': '627760',
            'TOSE_TAVON': '502908',
            'EQTESAT_NOVIN': '627412',
            'PARSIYAN': '622106',
            'PASARGAD': '502229',
            'CARAFARIN': '627488',
            'SAMAN': '621986',
            'SINA': '639346',
            'SARMAYE': '639607',
            'TAT': '636214',
            'SHAHR': '502806',
            'DAY': '502938',
            'SADERAT': '603769',
            'MELAT': '610433',
            'TEJARAT': '627353',
            'TEJARAT_JADID': '585983',
            'RAFAH': '589463',
            'ANSAR': '627381',
            'MEHR_AQTESAD': '639370',
        }
        keys = [k for k, v in banks.items() if v == self.number[:6]]

        if keys:
            if keys[0] == 'MELI':
                return 'بانک ملی'
            elif keys[0] == 'SEPAH':
                return 'بانک سپه'

        return None
