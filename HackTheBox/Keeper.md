# Keeper
Week 3 of trying to consistently solve a HTB. This one might have been too easy, but that's okay.

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

Fortunately, I'm actually familiar with KeePass from a previous job.

```bash
`ls -lah
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
`
```

With a quick Google search: `keepass dump file exploit`, you find this [PoC from github](https://github.com/vdohney/keepass-password-dumper?tab=readme-ov-file).

Special thanks to `vdohney` for their PoC and also mentioning a [python version](https://github.com/matro7sh/keepass-dump-masterkey) by `CMEPW`(unsure, if `matro7sh` is the same person. Shout out to them as well!)

```bash
git clone https://github.com/matro7sh/keepass-dump-masterkey.git
cd keepass-dump-masterkey/
```
