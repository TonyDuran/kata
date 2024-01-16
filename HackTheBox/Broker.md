# Broker
First write-up doing HTB after a long time. I already solved this, so the notes will be from memory.


Metadata:
- OS: Linux
- Difficulty: Easy
- target_ip: 10.10.11.243

## Recon

Started with running `nmap -sS 10.10.11.243` to get some information on the server. Learned that 22 & 80 were open. The fact it is using Nginx will be important later.

When you go to `http://10.10.11.243` you're prompted with a basic auth pop-up. And of course, `admin/admin` would work for the credentials.

After logging in, you're directed to the splash page of ActiveMQ with the version: `5.15.15`. This is important because it is vulnerable to RCE [CVE-2023-46604](https://nvd.nist.gov/vuln/detail/CVE-2023-46604)


