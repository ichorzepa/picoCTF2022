
# Packets Primer

Challenge from picoCTF 2022.



## Challenge description

Download the packet capture file and use packet analysis software to find the flag.
 [[Download packet capture]](https://artifacts.picoctf.net/c/200/network-dump.flag.pcap)

## Explained

Download packet capture and open it in Wireshark. Press the right mouse button on one of the TCP packet, select Follow -> TCP Stream and get the flag. If you want remove spaces, type in command line ```echo <your_flag> | tr -d ' '```.


## 🔗 Links
[[https://play.picoctf.org/practice/challenge/286]](https://play.picoctf.org/practice/challenge/286)

