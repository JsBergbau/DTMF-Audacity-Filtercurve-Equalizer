# DTMF Audacity Filtercurve Equalizer
With this filter curve or the filter curve generator the sound can be filtered in such a way that the DTMF tones are highlighted to be able to decode them more easily.

I use https://play.google.com/store/apps/details?id=com.audiocommunication 
This App gave the best DTMF tone decodings results compared with a few other free apps years ago. If you know better apps, please share, especially because this app is so ad-infested.
With this app it is possible to decode DTMF sequences when there is only few background noise. When there is background noise, then this project into play.

## Using DTMF Filter curve direclty

Use the `DTMF Filter Curve_2Hz.txt` directly and import it in Filter Curve EQ of Audacity. Paramters for generation were bandwidth 2 Hz, baseline -30 dB and boost 5 dB. With these settings I was sucessfully able to decode the dialed sequence at the jingle of "Bei Anruf Erfolg" from Umberto Saxer, it is 15097.

There is another `DTMF Filter Curve_5Hz.txt` with the same parameters, but 5 Hz bandwidth.

## Generating your own filter curve

A bandwidth of only 2 Hz and even 5 Hz is very small but was necessary to decode the DTMF sequence of "Bei Anruf Erfolg". There is music around the sequence and with a larger bandwidth the frequencies of the music are decoded as DTMF tones. So for decoding in your case a larger bandwidth might be needed. 

Relevant parts to change

```
####### Change here ##########
bandwith=15
baseline=-30
boost=5
####### End change here ######
```

baseline is the attenuation of none DTMF frequencies and boost the amplification of DTMF frequencies.

Copy the output of the script to a text file and import it in Audacity. For this project Audacity 3.1.3 was used.
