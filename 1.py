class uraiRajutKata:
    def urai(self, kata):
        str_tampung = ''
        b = len(kata)
        for i in range(b):
            a=0 
            for a in range(i+1): 
                str_tampung = str_tampung + kata[a]
        return str_tampung

    def rajut(self, kata_uraian):
        str_tampung = '' 
        panjangKata = len(kata_uraian)
        angkaTotal = 0
        pengulangan = 0
        penambah = 1
        while angkaTotal <= len(kata_uraian): 
            if angkaTotal != len(kata_uraian): 
                pengulangan += 1 
                angkaTotal = angkaTotal + penambah 
                penambah += 1
            else:
                angkaTotal = angkaTotal + penambah
        
        for i in range(panjangKata-1, panjangKata-pengulangan-1, -1): 
            str_tampung = kata_uraian[i] + str_tampung
        return str_tampung



x = uraiRajutKata() 

print(x.urai('Code'))
print(x.urai('Python'))
print(x.urai('Purwadhika'))

print(x.rajut('CCoCodCode'))
print(x.rajut('PPyPytPythPythoPython'))
print(x.rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))