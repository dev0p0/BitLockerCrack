# BitLockerCrack
A highly simplistic attempt to brute-force lost Bitlocker password!

It just happens, sometimes, out of bad luck, that one might forget the password for their Bitlocker encrypted volume or partition. While from a security perspective, if Bitlocker had any backdoors, or general keys, or a kind of algorithm built in that would generate close to actual keys, (like a filter or like if the number of possible keys for unlocking a Bitlocker drive are theoretically 10^48 possible keys, while the implementation of Bitlocker for the masses and general population only has actual 10^12 possible combinations that follow a secret formula or pattern that can be used to attack and unlock a (people version) Bitlocker drive), if any of these were implemented in a Bitlocker drive, then it wouldn't make any sense to encrypt a drive using Bitlocker and from a  security perspective it would be BAD!

So it is a good thing that it is hard to brute force a Bitlocker encrypted volume and that no one knows of a secret pattern. But not all attempts are bad, sometimes one might just forget the key inside the encrypted volume, should we format the whole partition?

Well, basically after a while and after trying this tools, or things like https://github.com/e-ago/bitcracker one might just give up and decide to format the whole partition eventually. But some might just want to take that one in a theoretical 10^48 chance. This tools, script rather, would help you with trying to crack open a Bitlocker encrypted volume using recovery password options.

## How to use

First, you need python 3.X, preferably the newest version, installed. Also this script only works on Windows machines, cause it calls 'manage-bde.exe'. For most machines there is no need to install any specific python libraries using pip, all the libraries come with default python installation.

You copy the "BitLockerCrack.py" from this repository to a folder of your choosing, open command prompt with admin privileges, and then run it like this: 'python BitLockerCrack.py D:' and hit enter, then it starts finding the password.
The sad part is that this is not a multithreaded or parallel brute forcer, not that it would make any difference as long as it would call 'manage-bde', and that it runs on only one core.

For faster options, you should look into https://github.com/e-ago/bitcracker, from a probabilistic view it would be throwing a coin with 10^48 much faster than this tool! :D

Good luck cracking!
