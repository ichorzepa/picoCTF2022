
# Operation Orchid

Challenge from picoCTF 2022.



## Challenge description

Download this disk image and find the flag. Note: if you are using the webshell, download and extract the disk image into ```/tmp``` not your home directory.

[Download compressed disk image](https://artifacts.picoctf.net/c/142/disk.flag.img.gz)


## Explained

Download using ```wget```. Extract it using ```gunzip``` then create ```mkdir /tmp/foo```. Check partition using ```mmls disk.flag.img``` and mount last partition: ```sudo mount disk.flag.img /tmp/foo -o offset=$((411648*512)) ```. Run ```sudo find /tmp/foo -name flag* ``` and you will find encrypted password.

Check it using ```sudo file /tmp/foo/root/flag.txt.enc```. It is openssl encrypted data with salted password. We don't have any password. Let's check ```/tmp/foo/root/``` directory (to do that you have to login as root). If you check what is inside using ```ls -al``` you will find .ash_history file. Check it. There is:

```bash
penssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567
```

Now you know how it was encrypted. Decrypt it then:

```bash
openssl enc -aes-256-cbc -d -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567
```

```cat flag.txt``` to get the flag!


## 🔗 Links
[[https://play.picoctf.org/practice/challenge/285]](https://play.picoctf.org/practice/challenge/285)

