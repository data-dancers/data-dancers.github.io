**How to Serve a Hugo Site Over Local Network**

Hey everyone! Here’s how to make a local development Hugo site accessible to anyone on the same Wi-Fi network :smiley_cat:  Follow these steps if you’re using Ubuntu or Arch Linux and you want to view a local development site from your phone:

**1. Make sure all devices are using the same WiFi network!**

**2. Open Terminal and Find Your Local IP Address:**

```
ip addr show | grep 192
```

Look for the line with your local IP address. It will look something like `inet 192.168.x.x/24`.

**3. Run the Hugo Server:**
Navigate to your Hugo project directory and run:

```
hugo server --bind 0.0.0.0 --baseURL http://0.0.0.0:1313
```

**4. Allow Firewall Access**
Ensure your firewall allows incoming connections on port 1313.

*For Ubuntu*:

```
sudo ufw allow 1313/tcp
```

*For Arch Linux*
```
# install firewalld
sudo pacman -S firewalld

# enable and start firewalld
sudo systemctl enable firewalld
sudo systemctl start firewalld

# open hugo's default port for TCP connections
sudo firewall-cmd --add-port=1313/tcp --permanent
sudo firewall-cmd --reload
```

5. Share the Access URL
Tell everyone and their web browsers about:

http://YOUR_LOCAL_IP:1313

(Replace YOUR_LOCAL_IP with the IP address you found in step 2.)

That’s it! Everyone on the same Wi-Fi network should now be able to access the Hugo site served from your computer. Happy hacking!