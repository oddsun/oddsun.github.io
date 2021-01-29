---
layout: post
title: "Raspberry Pi 4 Setup: Part 2"
date: 2021-01-29 04:03:23 -0000
tags: rpi4 i3wm ubuntu-server20.10 bluetooth keyboard keychron linux
categories:
description: "Bluetooth Keyboard"
image: ""
---
# My Setup:
<span style="color:hsl(0,80%,65%)">Raspberry Pi 4</span> + <span style="color:hsl(102,80%,65%)">Ubuntu Server 20.10</span> +  <span style="color:hsl(204,80%,65%)">i3wm</span>

# Summary
For those short on time, here is a quick summary:
1. install: `sudo apt install pi-bluetooth`
2. reboot
3. `bluetoothctl`
4. with in `bluetoothctl` shell:
	1. `power on`
	2. `agent on`
	3. `scan on` until you see your device (usually by device name)
	4. `scan off`
	5. `pair AA:BB:CC:DD:EE:FF` (replace the placeholder with actual device MAC address)
	6. `trust AA:BB:CC:DD:EE:FF`
	7. `connect AA:BB:CC:DD:EE:FF`

## Troubleshoot:
1. `No defaul controller available`: repeat step #1 and #2.
2. If encounter follow error, try removing device (`remove AA::BB:CC:DD:EE:FF`) and repeat step #4 in **Summary**.
```
[bluetooth]# connect AA:BB:CC:11:22:33
Attempting to connect to AA:BB:CC:11:22:33
[CHG] Device AA:BB:CC:11:22:33 Connected: yes
Failed to connect: org.bluez.Error.Failed
[CHG] Device AA:BB:CC:11:22:33 Connected: no
```



# The Cleanup
With my <span style="color:hsl(0,80%,65%)">Raspberry Pi 4</span> finally setup for good use. While the software setup is perfectly clean and lite, the hardware setup is horrendous. Why? Because of all the cables coming out of it, which reminded me a bit of Sadako (though I never watched it).

With i3wm + vim + qutebrowser, I no long need a mouse. So I threw it away (into some pile of spare parts). Now, I have to get a <span style="color:hsl(204,80%,75%)">bluetooth</span> keyboard. After reading reviews after reviews and watching reviews after reviews, I've finally settled on **Keychron K8**. What's attractive is that it can 
1. connect up to 3 devices via <span style="color:hsl(204,80%,75%)">bluetooth</span> simultaneously 
2. mechanical
3. compact (TKL, or ten-key-less) while still retaining the layout of regular keyboard (as oppose to the other siblings, i.e. K1,2,4,6).

The reason I still want the layout of regular keyboard is because I'm still using a full-size keyboard on my other system. So don't want to develop unnecessary habits of using weird compact placement of `right ctrl` or the arrow keys.

Though this is not a product review, I'll just leave my comments here in case it's useful to anyone (since it's hard to find any real/useful review online).
1. The <span style="color:hsl(204,80%,75%)">bluetooth</span> works flawlessly (after it's properly setup on my rpi, which is a breeze if you know what you are doing, see below), 
2. The <span style="color:hsl(15,80%,40%)">brown</span> switch is like all the other <span style="color:hsl(15,80%,40%)">brown</span> switches: *soggy*. Good thing I got the **Hot-swappable** version. I may <span style="color:hsl(153,80%,75%)">blue-switch</span> them out later.  
>**Update/(Non)Pro-tip**: I realized typing with <span style="color:hsl(15,80%,40%)">brown</span> switches requires different technique from typing with <span style="color:hsl(153,80%,75%)">blue</span> switches. Typing with <span style="color:hsl(153,80%,75%)">blue</span> switches is like hit-and-run, because of the satisfying (or annoying) clicks. The same technique can't be used with <span style="color:hsl(15,80%,40%)">brown</span> switches, it will feel *soggy*. With <span style="color:hsl(15,80%,40%)">brown</span> switches, you really have to *lean* in. Then, it will feel just fine!
3. TKL is nice to carry around. Though, I keep hitting adjacent keys. Maybe it's because the keyboard is really tall compared to regular keyboards.

Now to the juicy &#127865; part.

# <span style="color:hsl(204,80%,75%)">Bluetooth</span>: install
If you know what you are doing, setting up <span style="color:hsl(204,80%,75%)">bluetooth</span> will be a breeze &#127811;~~~

Though, I definitely didn't know what I was doing and my setup is fairly non-standard. Typically, if you use a regular desktop environment/OS like **gnome** or **Raspbian**, the <span style="color:hsl(204,80%,75%)">bluetooth</span> is preconfigured and you just need to connect to the **K8** via some GUI. Moreover, I'm running a <span style="color:hsl(0,80%,65%)">Raspberry Pi 4</span>, which requires special driver. In the end, the main challenge is googling or duckduckgoing.

So this post saves you the trouble of sorting out the googles or ducks if you run a similar setup, i.e. minimal OS with no pre-installed <span style="color:hsl(204,80%,75%)">bluetooth</span> package and/or GUI on a <span style="color:hsl(0,80%,65%)">Raspberry Pi 4</span>.

To install the <span style="color:hsl(204,80%,75%)">bluetooth</span> stack:
```
sudo apt install pi-bluetooth
``` 

This will install the dependency `bluez`, the official Linux <span style="color:hsl(204,80%,75%)">bluetooth</span> stack, if given permission. The package `pi-bluetooth` works with <span style="color:hsl(0,80%,65%)">Raspberry Pi 4</span> even though it only mentions <span style="color:hsl(51,80%,65%)">Raspberry Pi 3</span> in the description from `apt show pi-bluetooth`. Now you will need to `reboot` so that the firmware for <span style="color:hsl(0,80%,65%)">Raspberry Pi 4</span> <span style="color:hsl(204,80%,75%)">bluetooth</span> module can be loaded on boot.

# <span style="color:hsl(204,80%,75%)">Bluetooth</span>: connecting
Now use command `bluetoothctl` to open shell for connecting to <span style="color:hsl(204,80%,75%)">bluetooth</span> device. Within the shell use the following command to connect to the desired device.
1. `power on`
2. `agent on`
3. `scan on` until you see your device (usually by device name)
4. `scan off`
5. `pair AA:BB:CC:DD:EE:FF` (replace the placeholder with actual device MAC address)
6. `trust AA:BB:CC:DD:EE:FF`
7. `connect AA:BB:CC:DD:EE:FF`

# Troubleshooting
Congrats on making it this far. As a reward, this is the real section of this post &#128539;.

The instruction in the previous section is everywhere. However, little useful information can be found about troubleshooting for specific errors I was encountering. Specifically, my <span style="color:hsl(0,80%,65%)">Raspberry Pi 4</span> can successfully pair with the **K8**, but when I try to connect, I got the following error:
```
[bluetooth]# connect AA:BB:CC:11:22:33
Attempting to connect to AA:BB:CC:11:22:33
[CHG] Device AA:BB:CC:11:22:33 Connected: yes
Failed to connect: org.bluez.Error.Failed
[CHG] Device AA:BB:CC:11:22:33 Connected: no
```
Upon further investigation with `btmon`, it seems after the initial successful connection, there is an authentication error. After chasing after rabbit holes after rabbit holes like Alice in borderland, the solution is surprisingly simple (and of course never suggested anywhere):
1. remove the pairing: `remove AA:BB:CC:DD:EE:FF` (`AA:BB:CC:DD:EE:FF` is dummy placeholder for actual device MAC address)
2. repeat steps #3--#7 from last section

Of course, you may encounter a genuine authentication error which requires another fix. But give this a try first and you maybe surprised &#127881;.

# <span style="color:hsl(0,80%,75%)">C</span><span style="margin-left:-0em;color:hsl(51,80%,75%)">i</span><span style="margin-left:-0em;color:hsl(102,80%,75%)">a</span><span style="margin-left:-0em;color:hsl(153,80%,75%)">o</span><span style="margin-left:-0em;color:hsl(204,80%,75%)">~</span><span style="margin-left:-0em;color:hsl(255,80%,75%)">~</span><span style="margin-left:-0em;color:hsl(306,80%,75%)">~</span>
