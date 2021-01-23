---
layout: post
title: "i3lock + xautolock + sleep"
date: 2021-01-22 00:40:53 -0000
tags: i3lock xautolock linux i3 rpi4
categories: 
description: "How to enable sleep with i3lock+xautolock setup"
image: ""
---
# HELL<span style="color:hsl(0,80%,75%)">O</span><span style="margin-left:-0em;color:hsl(51,80%,75%)">O</span><span style="margin-left:-0em;color:hsl(102,80%,75%)">O</span><span style="margin-left:-0em;color:hsl(153,80%,75%)">O</span><span style="margin-left:-0em;color:hsl(204,80%,75%)">O</span><span style="margin-left:-0em;color:hsl(255,80%,75%)">O</span><span style="margin-left:-0em;color:hsl(306,80%,75%)">O</span> WORLD~~~~

Very excited for the first blog ever! But enough about that. Let's talk linux.

# Linux on <span style="color:hsl(0,80%,65%)">Raspberry Pi 4</span>
Recently started working with linux, specifically **ubuntu**, and <span style="color:hsl(0,80%,65%)">raspberry pi 4</span>. Ubuntu desktop is now available on <span style="color:hsl(0,80%,65%)">raspberry pi 4</span>, but it's a little bit slooooow for me. Then, I tried **Lubuntu** and **Kubuntu**, both of which I didn't like much on <span style="color:hsl(0,80%,65%)">raspberry pi 4</span>. **Lubuntu** is fairly fast, but doesn't have toooooo many customizations. **Kubuntu** is very pretty, but imo it is soooo slooooow, much more than gnome **ubuntu** desktop. Solution: **ubuntu** server + **i3wm**.

"What's wrong with **raspbian**?" you may ask. Only 32-bit version is available at the time of writing. "What's wrong with 32-bit OS?" you may challenge. Well, **pycharm** doesn't have an up-to-date 32-bit version. Wait, **pycharm** doesn't support **ARM** architecture at all. Never mind. Guess we will just have to stick with **vscode** (which support **ARM** and **ARM64**) or **vim** (&#128561; why did I learn and forget **EMACS** all those years ago). "So why not **raspbian**?!" you may insist. I don't like the user `pi`. "But... and the story continues.

# **i3wm**
**i3wm** is very clean with the nice window layouts. And, when combined with **vim** (yuck, or so I thought a week ago) and **qutebrowser** (or **firefox** + vimium ff plugin) (is it just me or is **qutebrowser** slower than **firefox**...), noo mouse is needed! Moreover, there are tons of <span style="color:hsl(0,80%,75%)">cu</span><span style="color:hsl(51,80%,75%)">st</span><span style="color:hsl(102,80%,75%)">om</span><span style="color:hsl(153,80%,75%)">iz</span><span style="color:hsl(204,80%,75%)">at</span><span style="color:hsl(255,80%,75%)">io</span><span style="color:hsl(306,80%,75%)">ns</span>. Check out [my configs](https://github.com/oddsun/i2-starterpack), which is a fork of the coooool looking [i3-starterpack from addy-dclxvi](https://github.com/addy-dclxvi/i3-starterpack).

# My **wishes**
With the starterpack, it's pretty easy to get a decent looking i3 setup. However, what's troubling is the setup for `i3lock`. Coming from windows and mac, I have certain expectations and standards, or **wishes** in this case:
1. autolock with timer,
2. screen turns off/sleeps after some time (after autolock),
3. if wakes while locked but not signed in, screen goes back to sleep after some time,
4. ~~screensavers? (nah, who needs those.)~~

As you can see, I'm spoiled (by all those bloatware). And turns out it is not that easy to achieve all 3 **wishes** at the same time. That's the purpose of this post, acting as my personal <span style="color:hsl(153,80%,65%)">genie</span> and grant me 3 **wishes**, since I couldn't really find a good <span style="color:hsl(153,80%,65%)">genie</span> on the net.

With `i3lock` + `xautolock`, it's pretty easy to get **wish** #1 by adding the following line to `.config/i3/config`

```bash
exec --no-startup-id xautolock -time 10 -locker i3lcok
```

And if you want a wallpaper on the lock screen?
```bash
exec --no-startup-id xautolock -time 10 -locker "i3lcok -i ./wallpaper.png"
```
Note that quotes must be used for the `i3lock` commands for this to work. Moreover, `i3lock` only seems to take `png` files as input.

All done right? Ha. Soon you will realize, the default standby/suspend/off happens after 10 mintues, which coincides with the autolock delay. So the autolock will trigger while the sleep is happening and the screen doesn't shut off at all. Moreover, `xautolock` will keep trying to lock every 10 minutes even if it already locked. Again, this will reset the idle timer and prevent sleeping.

# The fix
After scouring the internet for 2 days and trying suggestions from various forums, my **wishes** are still left unfulfilled... BUT then I finally came across something useful. Guess where? The `man` pages for `i3lock` &#128514;. Under the section `DPMS`, there is some suggested code for getting exactly what I want. The code is pasted below (with my edits):
{% highlight bash %}
#!/bin/sh
revert() {
  xset dpms 600 600 600
}
trap revert HUP INT TERM
xset +dpms dpms 5 5 5
i3lock -n -i ./wallpaper.png
revert
{% endhighlight %}

To explain a bit: the script sets standby/suspend/off timer to 5 seconds and then locks with a blocking `i3lock` (`-n` stands for `--nofork`, which blocks the call); then system is unlocked, the settings are reverted to standby/suspend/off timer of 600 sections (or 10 minutes). So I saved this script under `~/i3lock.sh` and made it executable with
```bash
chmod u+x i3lock.sh
```
The blocking (`-n`) is important because it will help stopping `xautolock` keep locking every 10 minutes.

Finally, I updated `.config/i3/config` with the following line:
```bash
exec --no-startup-id xautolock -time 9 -locker ~/i3lcok.sh
```
And voila. My **wishes** have been granted (thank you, whichever heavenly being that wrote the `man` pages.):

&nbsp;&nbsp;&nbsp;&nbsp;<span style="margin-left:-0em;color:hsl(102,80%,50%)">&#10003;</span> autolocks after 9 minutes (10 minutes is just problematic with the default DPMS config &#128561;)  
&nbsp;&nbsp;&nbsp;&nbsp;<span style="margin-left:-0em;color:hsl(102,80%,50%)">&#10003;</span> screens turns off 5 secs after autolocking  
&nbsp;&nbsp;&nbsp;&nbsp;<span style="margin-left:-0em;color:hsl(102,80%,50%)">&#10003;</span> if wakes without signin, screen turns off after 5 secs again  
&nbsp;&nbsp;&nbsp;&nbsp;&#10799; screensavers? &#129318; maybe next time... 

So here you go, everyone and my future self. Enjoy!
