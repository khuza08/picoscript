nc ke instancenya dulu wak

Penjelasannya
```
Dari tantangan sebelumnya (heap0) bahwa untuk menuju safe_var membutuhkan 32 karakter. 
pas liat kode sumber terlihat bahwa safe_var harus disetel ke pico untuk mendapatkan flag. 
Jadi dengan menulis ke buffer 32 karakter dan kemudian pico safe_var akan ditulis ke pico. 
trus run opsi 4, the flag is yours
```
Contoh:
```
kita pertama write safe_var ke buffer: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAApico
trus print heap, lalu tinggal print flagnya.
```
