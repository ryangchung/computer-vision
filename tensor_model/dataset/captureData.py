
'''
This is a script that was used to automate taking website screenshots for over 200 different websites


'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
from PIL import Image
import time

# Initialize ChromeDriver
def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

# Take screenshots
def capture_screenshots(websites, output_dir, label):
    os.makedirs(output_dir, exist_ok=True)
    driver = setup_driver()

    for i, url in enumerate(websites):
        try:
            driver.maximize_window()
            driver.get(url)
            time.sleep(3)  # Wait for page to load
            screenshot_path = os.path.join(output_dir, f"{label}_{i}.png")
            driver.save_screenshot(screenshot_path)
            print(f"Saved: {screenshot_path}")
        except Exception as e:
            print(f"Failed for {url}: {e}")
    driver.quit()



trainUnproductive = [
    "https://www.tiktok.com/tag/reels?lang=en", "https://about.instagram.com/features/reels", "https://www.facebook.com/gaming/play/",
    "https://www.youtube.com/results?search_query=call+of+duty+black+ops+6", "https://www.netflix.com", "https://www.hulu.com",
    "https://www.disneyplus.com", "https://www.crunchyroll.com", "https://www.funimation.com",
    "https://www.spotify.com", "https://www.pandora.com", "https://www.soundcloud.com",
    "https://www.reddit.com/search/?q=funnyt&cId=00622a9e-e240-48fa-8515-b9eb5771beb4&iId=36f86fa2-5cd9-4edc-a79d-0d0df49120b3", "https://www.minecraft.net",
    "https://www.fortnite.com", "https://www.epicgames.com", "https://www.steampowered.com",
    "https://www.battlenet.com", "https://www.riotgames.com", "https://www.leagueoflegends.com",
    "https://www.dota2.com", "https://www.callofduty.com", "https://www.genshin.hoyoverse.com",
    "https://www.anime-planet.com", "https://www.myanimelist.net", "https://www.foodnetwork.com",
    "https://www.allrecipes.com", "https://www.yelp.com", "https://www.doordash.com",
    "https://www.grubhub.com", "https://www.ubereats.com", "https://www.tastemade.com",
    "https://www.buzzfeed.com", "https://www.delish.com", "https://www.cookinglight.com",
    "https://www.food.com", "https://www.epicurious.com", "https://www.seriouseats.com",
    "https://www.chowhound.com", "https://www.animefreak.tv",  "https://www.tiktokreels.com", "https://www.memes.com",
    "https://www.giphy.com", 
    "https://www.lolcats.com", "https://www.gamespot.com", "https://www.ign.com",
    "https://www.pcgamer.com", "https://www.anime.newsnetwork.com", "https://www.animenewsnetwork.com",
    "https://www.chess.com", "https://www.pogo.com", "https://www.popcap.com",
    "https://www.zombiegames.com", "https://www.addictinggames.com", "https://www.miniclip.com",
"https://www.boredpanda.com",
    "https://www.funnyjunk.com",
    "https://www.humoropedia.com", "https://www.iwastesomuchtime.com", "https://www.stumbleupon.com",
    
    "https://www.tumblr.com", "https://www.weheartit.com", "https://www.dailymotion.com", 'https://www.slither.io'
     "https://www.metacafe.com", "https://www.animejoy.net",
    "https://www.watchcartoononline.com", "https://www.espn.com",
    "https://www.sporcle.com", "https://www.crazygames.com",
    "https://www.funnyordie.com", "https://www.y8.com", "https://www.animelab.com", 'https://agargame.io/', 'https://www.netflix.com/ca/', 'https://www.youtube.com/results?search_query=try+not+to+laugh', 'https://www.youtube.com/@MrBeast', 'https://www.fortnite.com/?lang=en-US', 'https://open.spotify.com/', 'https://www.ticketmaster.ca/?landing=c&awtrc=true&c=SEM_TMBRAND_ggl_6619616063_137379093082_ticketmaster&GCID=0&&gad_source=1&gclid=Cj0KCQiA6Ou5BhCrARIsAPoTxrCoYBrYheY-9nLDjatcv2X7ZPs9OElo6JUrjJ4TpusjxnYaYcesXCEaAvM0EALw_wcB&gclsrc=aw.ds', 'https://poki.com/?campaign=14724960448&adgroup=127692045099&extensionid=&targetid=kwd-11771561&location=9000679&matchtype=e&network=g&device=c&devicemodel=&creative=594129712022&keyword=games&placement=&target=&gad_source=1&gclid=Cj0KCQiA6Ou5BhCrARIsAPoTxrD1wosmmafsVPnyMXG3tJDp0MIlsylvagevkwKDVOMz111nql5i1r0aAvLOEALw_wcB'
]

testUnproductive = [   "https://www.snapchat.com/discover", "https://x.com/x", "https://www.twitch.tv", 'https://thejigsawpuzzles.com/', "https://www.livescore.com",  "https://www.toonami.com", "https://alternativeto.net/software/cartoon-crazy/about/", "https://www.dorkly.com", "https://www.icanhas.cheezburger.com", "https://www.cheezburger.com",'https://www.ebaumsworld.com/',"https://www.coolmathgames.com", "https://www.agame.com", "https://tenor.com/search/funny-gifs", "https://www.cheezburger.com",
    "https://www.animeheaven.ru", "https://www.9gag.com", "https://www.pinterest.com",
    "https://www.imgur.com", "https://www.roblox.com" ]

print(len(testUnproductive))
print(len(trainUnproductive))

capture_screenshots(trainUnproductive, "./data/train/unproductive", "unproductive")
capture_screenshots(testUnproductive, "./data/test/unproductive", "unproductive")

trainProductive = [
    "https://www.khanacademy.org", "https://www.coursera.org", "https://www.edx.org",
    "https://www.udemy.com", "https://www.codecademy.com", "https://www.freecodecamp.org",
    "https://www.leetcode.com", "https://www.codewars.com", "https://www.codechef.com",
    "https://www.datacamp.com", "https://www.w3schools.com", "https://www.mathway.com",
    "https://www.symbolab.com", "https://www.desmos.com", "https://www.geogebra.org",
    "https://www.wolframalpha.com", "https://www.kaggle.com", "https://www.github.com",
    "https://www.stackoverflow.com", "https://www.replit.com", "https://www.coursetro.com",
    "https://www.medium.com", "https://www.pluralsight.com",
    "https://www.udacity.com", "https://www.futurelearn.com", "https://www.skillshare.com",
    "https://www.brilliant.org", "https://www.hyperskill.org",
    "https://www.mathsisfun.com", "https://www.algebra.com", "https://www.projecteuler.net",
    "https://www.topcoder.com", 
    "https://www.toptal.com", "https://www.tinkercad.com", "https://www.scratch.mit.edu",
    "https://www.classdojo.com", "https://www.tynker.com",
    "https://www.babbel.com", "https://www.duolingo.com", "https://www.memrise.com",
     "https://www.brainly.com", "https://www.bigideasmath.com",
    "https://www.ck12.org", "https://www.readtheory.org", "https://www.vocabulary.com",
    "https://www.prezi.com", 
    "https://www.jupyter.org", "https://www.google.com/docs/about", "https://www.slideshare.net",
    "https://www.ted.com", "https://www.h5p.org",
    "https://www.lumosity.com", "https://www.tradingeconomics.com", "https://www.visualizing.org",
    "https://www.chartgo.com", 
    "https://www.zoho.com/learn", "https://www.bitdegree.org", "https://www.python.org", "https://www.r-project.org",
    "https://www.tableau.com", "https://www.powerbi.microsoft.com", 
    "https://www.graphpad.com", "https://www.teachstarter.com", "https://www.classcentral.com",
    "https://www.academia.edu", "https://www.researchgate.net", "https://www.doceri.com",
    "https://www.figma.com", "https://www.microsoft.com/en-us/microsoft-teams",
    "https://www.asana.com", "https://www.trello.com", "https://www.notion.so",
   "https://www.wolfram.com", "https://www.refseek.com",
    "https://www.britannica.com" , 'https://workspace.google.com/intl/en_ca/products/slides/', 'https://www.youtube.com/@TheOrganicChemistryTutor', 'https://en.wikipedia.org/wiki/Google_Docs', 'https://en.wikipedia.org/wiki/Graph', 'https://workspace.google.com/intl/en_ca/products/sheets/'

    
]

testProductive = ["https://www.simplilearn.com",
    "https://www.learncpp.com", "https://www.gograph.com", "https://www.growingwithgoogle.com","https://www.theodinproject.com", "https://www.geeksforgeeks.org", "https://www.tutorialspoint.com",
    "https://www.hackerrank.com","https://www.sitepoint.com", 'https://stackoverflow.com/questions/73356104/how-to-prevent-page-reload-on-form-input-with-fastapi', "https://www.zoom.us","https://www.d3js.org", "https://www.nationalgeographic.com", 'https://about.zearn.org/how-zearn-math-works', 'https://quizlet.com/latest', "https://www.canva.com", "https://www.whiteboard.fi", 'https://www.youtube.com/@ProfessorDaveExplains', 'https://www.codecademy.com/catalog/subject/web-development?g_network=g&g_productchannel=&g_adid=704109648940&g_locinterest=&g_keyword=learn%20web%20development&g_acctid=243-039-7011&g_adtype=&g_keywordid=aud-2014586126760:kwd-18700310&g_ifcreative=&g_campaign=account&g_locphysical=9000679&g_adgroupid=165596036324&g_productid=&g_source={sourceid}&g_merchantid=&g_placement=&g_partition=&g_campaignid=21420007862&g_ifproduct=&utm_id=t_aud-2014586126760:kwd-18700310:ag_165596036324:cp_21420007862:n_g:d_c&utm_source=google&utm_medium=paid-search&utm_term=learn%20web%20development&utm_campaign=ESC_Language:_Basic_-_Broad&utm_content=704109648940&g_adtype=search&g_acctid=243-039-7011&gad_source=1&gclid=Cj0KCQiA6Ou5BhCrARIsAPoTxrBDa7bNEt_JUdh_9ayCNEN41gv7NUvW4qI1MIQQvoL-HKyz1wdIcEQaAk3VEALw_wcB', 'https://www.google.com/search?q=graphs&sca_esv=eabdc2486f328348&sxsrf=ADLYWILWf_htX7ouI9QI3afDrZ_w_eyzlQ%3A1731945633878&ei=oWQ7Z96gNaGo5NoPvKG0gAg&ved=0ahUKEwie9ZuioOaJAxUhFFkFHbwQDYAQ4dUDCA8&uact=5&oq=graphs&gs_lp=Egxnd3Mtd2l6LXNlcnAiBmdyYXBoczIOEAAYgAQYkQIYsQMYigUyCxAAGIAEGJECGIoFMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgARIwQpQjQRY9QhwAXgBkAEAmAF8oAH6BKoBAzEuNbgBA8gBAPgBAZgCB6AClQWoAhLCAgcQIxgnGOoCwgIUEAAYgAQYkQIYtAIYigUY6gLYAQHCAh0QLhiABBjRAxjjBBi0AhjHARjIAxjpBBjqAtgBAcICChAjGIAEGCcYigXCAgQQIxgnwgIWEC4YgAQYsQMY0QMYQxiDARjHARiKBcICEBAAGIAEGLEDGEMYgwEYigXCAgoQABiABBhDGIoFwgILEAAYgAQYsQMYgwHCAg4QABiABBixAxiDARiKBcICDRAAGIAEGLEDGEMYigXCAg4QABiABBiRAhjJAxiKBcICCxAAGIAEGJIDGIoFwgIREAAYgAQYkQIYsQMYyQMYigWYAwi6BgYIARABGAGSBwMyLjWgB9Qo&sclient=gws-wiz-serp' ]

 


# print(len(testProductive))
# print(len(trainProductive))

# capture_screenshots(trainProductive, "./data/train/productive", "productive")
# capture_screenshots(testProductive, "./data/test/productive", "productive")
