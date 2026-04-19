---
id: dds_master_manifesto
version: 2.0.0
tür: root_dispatcher
öncelik: absolute_override
son güncelleme tarihi: 2026-04-11
açıklama: Belgesel Tabanlı Sistem (DDS) için kök yönlendirme protokolü.
---

# SİSTEM YÖNERGESİ: DDS_MASTER_DISPATCHER

## [0] TANIM VE KAPSAM
Bu belge, Belge Tabanlı Sistemin (`.dds/`) Kök Dağıtıcısıdır. 
Biçimlendirme, güncelleme veya yazım kuralları İÇERMEZ. TEK amacı, kullanıcı niyetini değerlendirmek ve UYGULAYICIYI (Yapay Zeka Ajanı veya İnsan) doğru Alan Adı Kural Kümesine yönlendirmektir.

## [1] DOMAIN_ROUTING_MATRIX
EXECUTOR, dokümanları okuma, oluşturma veya güncelleme görevi aldığında, bağlamı değerlendirmeli ve aşağıdaki yönlendirme yollarından BİRİNİ izlemelidir. 

**IF context === "İş Mantığı, Pazar Hedefleri, Kullanıcı Profilleri veya Destanlar":**
- HEDEF_ALAN: `ürün`
- NEXT_ACTION: EXECUTOR, `.dds/meta/dds.product/rules.dds.md` dosyasını okumalıdır.
- *EXECUTOR, bu manifestoyu okumayı bırakmalı ve hedef dosyadaki talimatları izlemelidir.*

**IF context === "Küresel Teknoloji Yığını, Veritabanı Şemaları, Sistem Altyapısı veya Küresel API Sözleşmeleri":**
- TARGET_DOMAIN: `architecture`
- NEXT_ACTION: EXECUTOR, `.dds/meta/dds.architecture/rules.dds.md` dosyasını okumalıdır.
- *EXECUTOR, bu manifestoyu okumayı bırakmalı ve hedef dosyadaki talimatları izlemelidir.*

**IF context === "Belirli Uygulama Özellikleri, Kod Mantığı, Kullanıcı Arayüzü Bileşenleri veya İzole Modüller":**
- TARGET_DOMAIN: `modules`
- NEXT_ACTION: EXECUTOR, `.dds/meta/dds.modules/rules.dds.md` dosyasını okumalıdır.
- *EXECUTOR, bu manifestoyu okumayı bırakmalı ve hedef dosyadaki talimatları izlemelidir.*

## [2] CORE_CONSTITUTION (KÜRESEL YASALAR)
Alan adı ne olursa olsun, bu küresel yasalar evrensel olarak geçerlidir:

1. **TEK DOĞRU KAYNAK:**  Kod, iş mantığını BELİRLEMEMELİDİR. `.dds/` dizini mutlak otoritedir.
2. **GERÇEKLİK HİYERARŞİSİ:**  Çelişki varsa: `ürün` kuralları `mimari` kurallarını geçersiz kılar. `Mimari` kuralları `modül` kurallarını geçersiz kılar.
3. **EŞİK DEĞERİ SENKRONİZASYONU:** İlgili tüm `.dds/` dosyaları kod tabanı değişikliklerini yansıtacak şekilde güncellenmedikçe Git commit işlemleri gerçekleştirilmemelidir.

# END_OF_DIRECTIVE