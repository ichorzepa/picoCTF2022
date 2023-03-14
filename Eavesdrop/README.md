
# Eavesdrop

Challenge from picoCTF 2022.



## Challenge description

Download this packet capture and find the flag.

[Download packet capture](https://artifacts.picoctf.net/c/66/capture.flag.pcap)


## Explained

Download using ```wget``` and open in Wireshark. Press right mouse click on packet and Follow TCP Stream. You can see how to decode flag:

```openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123```

and where flag was sent. Set filter for port 9002: tcp.port == 9002

We have to export raw packet bytes. Select the flag with "Salted__" inside Data, then File->Export Packet Bytes, Save it as file.des3

Run decode command and get flag inside file.txt



## 🔗 Links
[[https://play.picoctf.org/practice/challenge/264]](https://play.picoctf.org/practice/challenge/264)

