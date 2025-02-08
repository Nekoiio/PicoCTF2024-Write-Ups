The first 6 checks can be passed by changing the basic tags with exiftool, remmember to prefix all the fields with "SubSec" to the able to change the millisencond part.

For the last check exiftool doesn't have the capability of changing the Samsung:Timestamp tag.

Therefore, we have to get dirty with a hex editor. First, we want to know where the tag is so we can use the -v3 option for exiftool to get more detailed information.

We see that the date starts after UTC, therefore it will likely be in the format of seconds since epoch. we also see that the numbers for each place have to be over 30, so 31 == 1. With all of this in mind we just set every place to 30, except the last one to get the first date possible, one second after the epoch, and Boom we're done.

