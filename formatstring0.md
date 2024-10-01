```
Use, nc mimas.picoctf.net 55122, to connect. Once connected it gives three options to choose from:

Breakf@st_Burger, Gr%114d_Cheese, Bac0n_D3luxe

This is a format string challenge, Gr%114d_Cheese, is the only thing that has a format string (%11) in it. Next, these are the choices:

Pe%to_Portobello, $outhwest_Burger, Cla%sic_Che%s%steak

Cla%sic_Che%s%steak has %s in it so by choosing that it gives the flag.

Helpful resources: Specifier table and manual page

Flag: picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_dc...}
