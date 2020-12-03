class knn():
    # başlangıç fonksiyonumuz ve değişkenlerimiz. inp değişkenimiz sınıf niteliği
    # belli olmayan örneğimizdir. Siz isterseniz bu değeri dışardan da alabilirsiniz.
    # __init__ metodundaki dataset veri setimizi, k en yakın k komşuyu, nfrom veri
    # setini okumaya başlanacağı satır ve nto ise kaçıncı satıra kadar okuyacağını
    # belirtir. Son iki parametre çok büyük veri setlerini çözümlerken pc'ler yeter
    # siz kaldığından isteğe bağlı olarak sadece veri setinin belli bir kısmını
    # seçmek için ekledim. Ki bu örneğimizde öyle bir örnek.
    def __init__(self,dataset, k):
        self.a, self.b, self.c,self.d,self.tür = [], [], [], [],[]
        self.inp = [0.30081,0.17381,-1.7542,0.48921]
        self.k = k

        # Veri setimizi nfrom satırından nto satırına kadar okuyoruz.
        # Ayrıca veri setindeki her sutunu bir listeye atıyoruz. (r,g,b,class_attr)
        with open(dataset, "r") as f:
            for i in f.readlines():
                self.a.append(float(i.split(",")[0]))
                self.b.append(float(i.split(",")[1]))
                self.c.append(float(i.split(",")[2]))
                self.d.append(float(i.split(",")[3]))
                self.tür.append(i.split(",")[4])

    # Uzaklık hesaplamamızı yaptığımız metodumuz. dist parametresine göre
    # ilgili hesaplanma yapılmaktadır. Default oklid uzaklığı kullanılmaktadır.
    # Burda dikkat edilmesi gerekilen en önemli nokta; uzaklık değeri hesaplandıktan
    # sonra hangi uzaklığın başta hangi index numarasına sahip olduğunu bilmeyiz.
    # Çünkü bu indis numarasını kullanarak ilgili uzaklığın sınıf değerine ulaşacağız.
    # Bu sebeple uzaklığı ve uzaklığın indis değerini demet şeklinde
    # dist listemize ekliyoruz.Çünkü uzaklığı küçükten büyüğe sıraladığımızda
    # uzaklığa ait gerçek sınıf değerine ulaşamamaktayız.
    #
    # öklid = 2, manhattan=1
    def distance(self, dist=1):
        self.dist = []
        # for döngüsündeki karışık gibi gelen üs alma, mutlak değer gibi işlemler
        # minkowski formulunun karşılığından ibarettir.
        for i in range(len(self.tür)):
            self.dist.append((pow((pow((
                    abs(float(self.a[i]) - float(self.inp[0])) +
                    abs(float(self.b[i]) - float(self.inp[1])) +
                    abs(float(self.c[i]) - float(self.inp[2])) +
                    abs(float(self.d[i])- float(self.inp[3]))), dist)), 1 / dist), i))
        print(self.dist)
        return self.dist

    # uzaklık hesaplanması yapıldıktan sonra örneğimize en yakın olan k tane
    # elemanı buluyoruz ve bu elemanların sınıf değerlerini class_values
    # listemizde tutuyoruz. Ve döngünün sununda class_values listesindeki 1(cilt)
    # 2(cilt değil) sayılarını hesaplayıp, örneğin hangi sınıfa ait olduğunu
    # buluyoruz.
    def findClass(self):
        self.class_values = []
        self.result = ""
        sıralıliste=sorted(self.dist)

        for i in sıralıliste[:self.k]:
            self.class_values.append(self.tür[i[1]])
        print(sıralıliste)
        print(self.class_values)

        self.first = self.class_values.count("0\n")
        self.secnd = self.class_values.count("1\n")

        print("Birinci Sınıf:", self.first)
        print("İkinci Sınıf:", self.secnd)

        if self.first > self.secnd:
            self.result = "1. Sınıf(Kırmızı)"
        else:
            self.result = "2. Sınıf(Yeşil)"

        print("SONUÇ: " + self.result)
ins = knn("data_banknote_authentication.txt",60)
ins.distance(1)
ins.findClass()

