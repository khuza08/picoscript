nc tethys.picoctf.net 52981

ada 4 opsi yang relevan: 2 buat mengalokasi objek, 3 buat mencetak x, 4 buat win check, dan 5 buat free x.

Karena ini adalah "Use after free" seperti yang disebutkan dalam hint dan dapat dilihat di opsi sebelum melakukan apa pun,
pertama kamu free x nya dulu atau opsi 5.

Dari challenge sebelumnya diketahui bahwa 32 karakter 'A' perlu digunakan buat sampai ke X, namun dalam challenge ini ditemukan 30 karakter 
dengan test dengan perintah 3 untuk melihat mengapa tidak work.
Sekarang pilih opsi 2 dengan panjang 31 untuk 30 karakter 'A' dan value "pico" alih alih "bico". 
Perhatikan bahwa dapat dilihat di kode sumber bahwa nilainya harus "pico" untuk mendapatkan tandanya. 
Setelah memasukkan panjang yang benar, masukkin value ini:
```
AAAAAAAAAAAAAAAAAAAAAAAAAAAAApico
```
kemudian cek dengan opsi 3 kalo emang "pico". trus, 
opsi 4 buat nge-print flagnya.
```
flag: picoCTF{now_thats_free_real_estate_a11...}
```
