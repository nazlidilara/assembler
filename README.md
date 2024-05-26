# SIC/XE Assembler Design
Bu projede sic/xe icin olusturulmus pass1 ve pass2 adimlarini isleyen assembler mevcuttur.Geçiş 1 ve Geçiş 2. Uyguladığımız assembler, tüm SIC/XE talimatlarını içerir ve tüm dört formatı (1, 2, 3, 4), adresleme modlarını ve program taşınabilirliğini destekler. Ayrıca makineden bağımsız özellikleri de destekler:
->Literaller
->Sembol Tanımlama Bildirimleri
->Program Blokları

## Assembler'a giriş: SIC/XE komut setini kullanan assembler kaynak programı (.txt formatinda olmalidir). Çıkış: Assemble edilmis program.

## **Proje yapisi**
Projede bulunan dosyalar şunlardır:
assembler.py: Assembler işlevlerini içeren Python betiği.
gui.py: Tkinter kullanılarak oluşturulan kullanıcı arayüzünü içeren dosya.
opcode.txt: SIC/XE opcode'larını içeren dosya.
input.txt: Assembler'ın işleyeceği kaynak kodun bulunduğu dosya.
Symtab.txt: Assembler tarafindan sembollerin listelendigi dosya 
littab.txt :Assembler tarafindan literallerin listelendigi dosya
input1.txt ve input2.txt : Assemblerin assemble edebilecegi ornek dosyalar.


# *Baslarken*
Bu rehber, projenin nasıl kurulacağı ve çalıştırılacağı hakkında adım adım bilgi vermektedir. Assembler'ı başarıyla kurmak ve kullanmak için aşağıdaki adımları takip edin.
### On Kosullar 
Projeyi kullanabilmek için sisteminizde Python'un yüklü olması gerekmektedir. Python'ı Python resmi web sitesi üzerinden indirip yükleyebilirsiniz.

### Gerensinimler 
Bu projeyi çalıştırmak için aşağıdaki yazılımlara ve dosyalara ihtiyacınız var:
Python 3.6+
Tkinter (Python'un standart GUI kütüphanesi)
opcode.txt dosyası (Bu dosya, assembler'ın çalışması için gerekli opcode'ları içerir) ve indirdiginiz projenin tum icerigi.

#### Kurulum 
Adım 1: Gerekli Paketleri Yükleyin
Gerekli Python paketlerini yüklemek için aşağıdaki komutu çalıştırın:
`pip install -r requirements.txt`

### Calistirma 
Assembler'ı Komut Satırından Çalıştırma
Assembler'ı çalıştırmak için, projenin bulunduğu dizinde terminal veya komut istemcisini açın ve aşağıdaki komutu girin:

`python assembler.py input.txt`
Bu komut, assembler betiğini başlatır ve işlem sonuçlarını terminalde görüntüler.

Assembler'ı GUI ile Çalıştırma
GUI'yi çalıştırmak için aşağıdaki komutu kullanın:
`python gui.py'
Bu komut, Tkinter tabanlı grafiksel kullanıcı arayüzünü başlatır. GUI'yi kullanarak bir kaynak dosya seçebilir ve assembler işlemini başlatabilirsiniz.

## *Proje Calisma Sekli*
#### Giriş Dosyası Okuma ve İşleme
-Dosya Okuma: read_file fonksiyonu, belirtilen kaynak kod dosyasını (örneğin, input.txt) satır satır okur. Bu sırada, boş satırlar ve yorumlar (. ile başlayan) dikkate alınmaz.
-Talimat Ayrıştırma: Her satır ayrıştırılarak talimatlar (instruction_arr) elde edilir. Her talimat için mnemonik, operandlar ve varsa semboller ayrıştırılır.
-Mnemonik Kontrolü: Mnemonikler, __check_mnemonic fonksiyonu ile opcode listesinde veya direktif listesinde olup olmadığı kontrol edilir.
-Hata Kontrolü: Yanlış mnemonik veya formata uygun olmayan girdiler söz konusu olduğunda SyntaxError ile hatalar işlenir.

#### Pass1 - Sembol ve Adres Tablolarını Oluşturma
-Başlangıç Ayarları: 'START' direktifi ile başlayan her bölüm için lokasyon sayacı (LOCCTR) sıfırlanır ve gerekli tablolar temizlenir.
-Sembol Tablosu Yapılandırma: Semboller, ilgili mnemonikler ve adreslerle __symbol_table içerisinde saklanır.
-Literaller ve Harici Referanslar: Literaller ve harici referanslar (EXTDEF ve EXTREF) işlenir.
-Adres ve Lokasyon Hesaplama: 'RESW', 'RESB', 'BYTE', 'WORD' gibi direktifler için gerekli byte hesaplamaları yapılır ve LOCCTR güncellenir.

#### Pass 2 - Nesne Kodu Üretimi ve Modifikasyon Kayıtları
-Nesne Kodu Oluşturma: Her talimat için uygun format ve adreslemeye göre nesne kodları __gen_code_list fonksiyonu ile oluşturulur.
-Modifikasyon Kayıtları: Belirli adresleme türlerinde gerekli olduğunda modifikasyon kayıtları oluşturulur.
-Bağımsız Değişkenler ve Hesaplamalar: İfadelerde kullanılan bağımsız değişkenler için gerekli hesaplamalar yapılır ve sonuçlar nesne koduna dönüştürülür.

#### Çıktı Dosyaları Yazma
-Nesne Kodu Dosyası: Oluşturulan nesne kodları ve diğer bilgiler write_file fonksiyonu kullanılarak belirtilen çıktı dosyasına yazılır (örneğin, output.txt).
-Sembol Tablosu: write_symbol_table fonksiyonu ile sembol tablosu, symtab.txt dosyasına yazılır.
-Literal Tablosu: write_literal_table fonksiyonu ile literal tablosu, littab.txt dosyasına yazılır.

##### Hata Ayıklama
Karşılaşabileceğiniz olası hatalar ve çözümleri:

*Input file not found:* Seçtiğiniz giriş dosyasının mevcut olduğundan emin olun.
*Opcode not found:* opcode.txt dosyasının doğru dizinde olduğundan emin olun.
*Assembly failed:* Kaynak kodun doğru formatta olduğundan ve desteklenen opcode'ları içerdiğinden emin olun.


