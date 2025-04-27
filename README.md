# 🏖 kumCTF

**kumCTF**, başlangıç seviyesindeki kullanıcılar için geliştirilen terminal tabanlı bir CTF çözüm asistanıdır. Nmap, netdiscover ve hashcat gibi sık kullanılan araçları tek bir arayüzde birleştirerek hızlı, pratik ve rehberli bir deneyim sunar.

## 🎯 Özellikler

- Komut satırı (CLI) tabanlı etkileşimli arayüz
- Sık kullanılan CTF araçlarına kolay erişim
- Kullanıcı dostu ve öğretici yapı
- Python ile subprocess üzerinden dış araç çalıştırma

## 🛠 Kullanılan Teknolojiler

- Python 3
- Terminal / Shell ortamı
- subprocess modülü
- `rich` kütüphanesi (CLI için zengin görsel arayüz)

## ⚠ Yasal Uyarı (Disclaimer)

Bu araç yalnızca **eğitim amaçlıdır** ve sadece **izinli ortamlarda** (örneğin CTF platformları, lab ortamları) kullanılmalıdır. Geliştirici, bu aracın yasa dışı kullanımından **sorumlu tutulamaz**.

---

## 📦 Kurulum

```bash
git clone https://github.com/tunakum/kumCTF.git
cd kumCTF
python3 kumCTF.py
