This is a shock collar controller that runs on a raspberry pi and uses an arduino along with an FS1000a transmitter. This is the collar I used: https://www.amazon.ca/gp/product/B07CV5TZ9M
I imagine any other one that looks similar would work too. They're probably all made in the same factory.
The raspberry pi needs to be connected to the arduino by usb. There's also an optional switch indicating whether the collar is off. It says the collar is off when pin 23 on the rasberry pi is pulled low, so if you don't bother installing a switch it'll just say it's always on. 
For the arduino, connect the fs1000a's data line to pin 10 and make sure it has power.
This project is bad. Here are some problems:
- The UI is ugly and bad. This project is the most I've used CSS or Javascript in like 8 years so I'm pretty rusty.
- The security on this is bad. It's all over HTTP so anybody on the same network as either party or who can sniff your traffic as it travels the internet can see everything in plain text (I think). Also there's no authentication system so anyone with the link can send you a 99 power shock at any moment. Use this at your own risk.
- The shocks last for about a second longer than the duration value that's entered on the site, which I think is because of the little for loop I have in the arduino code.
- Various other bits and bobs, go poking around in the code and you'll find them
If anyone wants to put in the effort to improve this
project please do get in touch because I don't really have the time or mental bandwidth to work on it right now but I would love to see it get better.
Also it would be cool to integrate this with VRchat at some point, in the vein of https://github.com/markviews/VRChatVibratorController
I hereby release this project under the creative commons CC-BY-SA 4.0 license for the time being. If that doesn't meet your requirements for whatever reason just lemme know.