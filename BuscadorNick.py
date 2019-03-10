#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Copyright (c) 2019, QuantiKa14 Servicios Integrales S.L
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met: 
1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer. 
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution. 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
The views and conclusions contained in the software and documentation are those
of the authors and should not be interpreted as representing official policies, 
either expressed or implied, of the FreeBSD Project.
'''

#AUTHOR: JORGE WEBSEC
#Twitter: @JorgeWebsec
#WEB: www.quantika14.com

import requests
from bs4 import BeautifulSoup

urls={"Facebook":"https://www.facebook.com/data",
      "YouTube":"https://www.youtube.com/user/data",
      "Twitter":"https://twitter.com/data",
      "Instagram":"https://www.instagram.com/data/",
      "Blogger":"http://data.blogspot.com/",
      "GooglePlus":"http://plus.google.com/+data/",
      "Twitch":"https://www.twitch.tv/data",
      "Reddit":"http://www.reddit.com/user/data/",
      "WordPress":"https://data.wordpress.com/",
      "Ebay":"https://www.ebay.com/usr/data",
      "Pinterest":"https://www.pinterest.com/data/",
      "Yelp":"http://data.yelp.com",
      "Slack":"https://data.slack.com/",
      "GitHub":"https://github.com/data",
      "Tumblr":"https://data.tumblr.com/",
      "Flickr":"https://www.flickr.com/photos/data/",
      "ProductHunt":"https://www.producthunt.com/@data",
      "Steam":"https://steamcommunity.com/id/data",
      "Foursquare":"https://foursquare.com/data",
      "Vimeo":"https://vimeo.com/data",
      "Etsy":"https://www.etsy.com/people/data",
      "SoundCloud":"https://soundcloud.com/data",
      "BitBucket":"https://bitbucket.org/data/",
      "CashMe":"https://cash.me/$data/",
      "DailyMotion":"https://www.dailymotion.com/data",
      "Aboutme":"https://about.me/data",
      "Disqus":"https://disqus.com/by/data/",
      "Medium":"https://medium.com/@data/",
      "Behance":"https://www.behance.net/data",
      "Bitly":"https://bitly.com/u/data",
      "CafeMom":"http://cafemom.com/home/data",
      "Fanpop":"http://www.fanpop.com/fans/data",
      "deviantART":"https://data.deviantart.com/",
      "GoodReads":"https://www.goodreads.com/data",
      "Instructables":"http://www.instructables.com/member/data/",
      "Keybase":"https://keybase.io/data/",
      "Kongregate":"http://www.kongregate.com/accounts/data",
      "LiveJournal":"https://data.livejournal.com/",
      "AngelList":"https://angel.co/data",
      "LastFM":"https://www.last.fm/user/data",
      "Slideshare":"https://www.slideshare.net/data",
      "Tripit":"https://www.tripit.com/people/data#/profile/basic-info",
      "Fotolog":"https://fotolog.com/data/",
      "Dribbble":"https://dribbble.com/data",
      "Imgur":"https://imgur.com/user/data",
      "Tracky":"https://tracky.com/~data",
      "Flipboard":"https://flipboard.com/@data",
      "Codecademy":"https://www.codecademy.com/data",
      "Roblox":"http://www.roblox.com/user.aspx?username=data",
      "Gravatar":"https://en.gravatar.com/data",
      "Trip":"https://www.trip.skyscanner.com/user/data",
      "Pastebin":"https://pastebin.com/u/data",
      "BlipFM":"https://blip.fm/data",
      "StreamMe":"https://www.stream.me/data",
      "IFTTT":"https://ifttt.com/p/data",
      "CodeMentor":"https://www.codementor.io/data",
      "Soupio":"http://data.soup.io/",
      "Fiverr":"https://www.fiverr.com/data",
      "Trakt":"https://trakt.tv/users/data",
      "Hackernews":"https://news.ycombinator.com/user?id=data",
      "five00px":"https://500px.com/data",
      "Spotify":"https://open.spotify.com/user/data",
      "Houzz":"https://www.houzz.es/pro/data/artverlin?irs=US",
      "BuzzFeed":"https://www.buzzfeed.com/data",
      "TripAdvisor":"https://www.tripadvisor.com/members/data",
      "HubPages":"https://hubpages.com/@data",
      "Scribd":"https://www.scribd.com/data",
      "Venmo":"https://venmo.com/data",
      "Canva":"https://www.canva.com/data",
      "CreativeMarket":"https://creativemarket.com/data",
      "Bandcamp":"https://bandcamp.com/data",
      "ReverbNation":"https://www.reverbnation.com/data",
      "Designspiration":"https://www.designspiration.net/data/",
      "ColourLovers":"http://www.colourlovers.com/lover/data",
      "KanoWorld":"https://world.kano.me/profile/data",
      "Badoo":"https://badoo.com/en/profile/data",
      "Newgrounds":"https://data.newgrounds.com/",
      "Patreon":"https://www.patreon.com/data",
      "Mixcloud":"https://www.mixcloud.com/data/",
      "Gumroad":"https://gumroad.com/data",
      "Quora":"https://data.quora.com/",
      "Rankia":"https://www.rankia.com/usuarios/data",
      "El Mundo":"http://www.elmundo.es/social/usuarios/data",
      "Twicsy":"https://twicsy.com/u/data",
      "Gapyear":"http://es.gravatar.com/data.json",
      "Tradimo":"http://en.tradimo.com/profile/data",
      "Eyeem":"https://www.eyeem.com/u/data",
      "QQ":"http://bbs.map.qq.com/space-username-data.html",
      "Verbling":"https://www.verbling.com/profesores/data",
      "Pastebin":"http://pastebin.com/u/data"}

def clean_webs(response, name):
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    
    if name == "Ebay": 
        if "The User ID you entered was not found" in soup.text:
            return False
    elif name == "Hackernews":
        if "No such user" in soup.text:
            return False
    elif name == "Mixcloud":
        if "Page Not Found" == soup.text[0:15].strip():
            return False
    elif name == "Twitch":
        if "Lo sentimos" in soup.text:
            return False
    elif name == "Steam":
        if "The specified profile could not be found" in soup.text:
            return False
    elif name == "KanoWorld":
        if "Page could not be found" in soup.text:
            return False
    return True

def getnickWebs(nick):
    dictWebs=dict()
    for name,url in urls.items():
        try:
            url=url.replace("data",nick)
            response=requests.get(url)
            if str(response)[11]!="4" and str(response)[11]=="2":
                if name == "Pastebin" and response.url != "https://pastebin.com/index":
                    dictWebs[name]=response.url
                elif name == "Yelp" and response.url != "https://www.yelp.com/":
                    dictWebs[name]=response.url
                elif name == "GoodReads":
                    dictWebs[name]=response.url
                elif name == "Roblox":
                    dictWebs[name]=response.url
                elif url.lower() == str(response.url).lower():
                    val=clean_webs(response, name)
                    if val:
                        dictWebs[name]=response.url
                else:
                    pass
        except requests.exceptions.ConnectionError:
            continue
    return dictWebs


def banner():
    print ("""                               -                 
                                -                 
                     .-         .o:               
          .`      .+o-            /s-             
        `+s/:.  -ss-               -y+:/s+`       
        ++`   `+y:       `          .y+ `oo       
       `o    `ss`        +:          -y-  o.      
       +-    os`         so           oo  -+      
      `o    -d-          ys           -h` `s      
      `s`   +y          `ds           `h- `s      
      `y-   +s          .ds           -h. -s`     
      -sho` /y.         `hs           os`+hy-     
      `.hh  .ys`        .hs          /y/ +d-`     
       -yd-  +hs.  ./ ``+dd-   -   `odo` yh:`     
       `.hy  `ohh/../-syyddss+-o ./yds. -d+`      
         :d+  `oydhs/-shhddhy+-:ohdhs. `ys`       OSINT
          +h:-``ohdmmmmmmmmmmdddmmhs.`.+y.           PARA
           /hdhsyhdddmmNNmmmmmmhyyyyshhy.              TODOS
            -/oyhydmmmmmdmmdyyhyyhyyyo/.                 E
               `.yhddmmdymdhoyddhys`                       INVESTIGA
           `.:+sydyhddddhdddhhhdysyo+/.`                     CONMIGO
       `.:+o+:.:dmmdmmmmmmmmddmddddd:-+o+-` 
     -+oo:.`   +dmmmmdmmmmmmmmssdmhy/  `-/++:`    
   .+:.`.     `shmmNdo/ymmmmmy/+shsyo     .::/`   
  :+`         -sydmmhs-/mmhmy+/+sdhso`       -+`  
 .o           /syhmmdy:ommyms//+ymhoo.        -/  
 /-           oyyhmmmh+ommddo++oymyss-         o` 
 ++          `ohhdmmmy+-hddy+//+shhss:         :/ 
 `+:.       :shhyddNmyo:dddh+/++shyyhy+`      `o: 
   `       :y.:hyydNmdsymmmd++++sdsyo-/y`    `::` 
          `y/  /yyhmNmhmmmmmho+odyss.  y+         
          os    /yydmmmmmmmmmyohdyo.   -h-        
         :h-     -+sdmmmmmddmmyho:`     +s.       
        :y+        ./shhhyyhhho-`       `ss`      
        o-`           `...```            .o`      
       .s                                 :/      
       .o                                 ::      
        s`                                o`      
        .s`                              :/       
         :s-``                       `..o+        
           ..                         `-.         
 
 """)
    print( "-----------------------------------------------------------------------------------------------")
    print( "DANTE'S GATES MINIMAL v 1.0 | <<TIP-1337>> | Buscador De Nicks | QUANTIKA14 | @JORGEWEBSEC")
    print( "     VERSION: 1.0 | 19/02/2019 | INVESTIGA CONMIGO DESDE EL SU | WWW.QUANTIKA14.COM ")

def main():
    banner()
    print( "_______________________________________________________________________________________________")
    print( "| El buscador de nicks no es perfecto. Necesita la colaboración de todos para mejorar.        |")
    print( "| Si quieres ayudarnos con Dante's Gates Minimal Version solo tienes que compartirnos tu idea |")
    print( "| Si hay un fallo o mejoras puedes subirlo en issues aquí:                                    |")
    print( "| https://github.com/Quantika14/osint-suite-tools/issues                                      |")
    print( "|_____________________________________________________________________________________________|")

    print( "")
    nick = str(input("Indique el nick que quiere buscar:"))
    r_nicks = getnickWebs(nick)
    for n in r_nicks:
        print( "|----[INFO][" + n.upper() + "][>] " + r_nicks.get(n).replace("data", nick))

main()
