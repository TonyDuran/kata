# Bizness
Attempting another easy retired box to get familiar/practice.

Metadata:
- OS: Linux
- Difficulty: Easy
- Status: Retired
- TARGET=10.10.11.252
- HOST=my IP

## Recon
Start off with an nmap scan.
`sudo nmap -p- -sC -sV $TARGET --open`

Results from initial nmap scan:
```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-01-20 15:37 CST
Nmap scan report for bizness.htb (10.10.11.252)
Host is up (0.061s latency).
Not shown: 65531 closed tcp ports (reset)
PORT      STATE SERVICE    VERSION
22/tcp    open  ssh        OpenSSH 8.4p1 Debian 5+deb11u3 (protocol 2.0)
| ssh-hostkey:
|   3072 3e:21:d5:dc:2e:61:eb:8f:a6:3b:24:2a:b7:1c:05:d3 (RSA)
|   256 39:11:42:3f:0c:25:00:08:d7:2f:1b:51:e0:43:9d:85 (ECDSA)
|_  256 b0:6f:a0:0a:9e:df:b1:7a:49:78:86:b2:35:40:ec:95 (ED25519)
80/tcp    open  http       nginx 1.18.0
|_http-server-header: nginx/1.18.0
|_http-title: Did not follow redirect to https://bizness.htb/
443/tcp   open  ssl/http   nginx 1.18.0
|_http-server-header: nginx/1.18.0
|_http-trane-info: Problem with XML parsing of /evox/about
|_http-title: BizNess Incorporated
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: organizationName=Internet Widgits Pty Ltd/stateOrProvinceName=Some-State/countryName=UK
| Not valid before: 2023-12-14T20:03:40
|_Not valid after:  2328-11-10T20:03:40
| tls-alpn:
|_  http/1.1
| tls-nextprotoneg:
|_  http/1.1
46103/tcp open  tcpwrapped
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 41.89 seconds
```

when I navigate to the site, I notice the request is rejected due to lack of domain name.
So I go to my `/etc/hosts` and add an entry for the target.
```

10.10.11.252 bizness.htb
```
