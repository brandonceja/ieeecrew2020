# IEEE CREW 2020
A small Python 3 script that takes viewers from the IEEE CREW 2020 Twitch stream every X minutes using its API which returns a JSON, and then matches them with the registered users to count its total watching time.

First with the script **getJSON.py** every X minutes during conference time (in the real scenario we decided to count them every 5 minutes) we pull the total viewers using the following URL from the API:

*URL->* https://tmi.twitch.tv/group/user/ieeeramaestudiantil_itm/chatters

This script will store every *.JSON file with the viewers deppending on the day and conference.

Then we fed the script **superCounter.py** with all the registered student's control number and for every saved file stored, on each occurence of the control number we add 5 minutes.

Finally we save the control number, total minutes and total hours (simply minutes/60) in a *.CSV* file.

Special thanks to IEEE CS, RAS, EMBS and WIE student chapters from Instituto Tecnológico de Morelia and to all our audience for participating in this wonderful event. I hope that this script can be useful in future projects. Fell free to use it, modify it, update it or do wathever you want with it I really don't care haha :satisfied:

By: Oraclox (Brandon Ceja)
