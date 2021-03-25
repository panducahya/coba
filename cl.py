#  EDIT SESUKA MU_____________
from linepy import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import ChatRoomAnnouncement
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib3, urllib.parse, html5lib, wikipedia, atexit, timeit, pafy, youtube_dl, traceback
from googletrans import Translator
from youtube_dl import YoutubeDL
import subprocess, youtube_dl, humanize, traceback
from threading import Thread,Event
import wikipedia as wiki
from subprocess import check_output
from Naked.toolshed.shell import execute_js
import sys,traceback
import requests, json
import requests, json, random
import youtube_dl
import json, requests, LineService
from thrift.transport import THttpClient
from zalgo_text import zalgo
requests.packages.urllib3.disable_warnings()

_session = requests.session()
botStart = time.time()
try:
    import urllib.request as urllib3
except ImportError:
    import urllib3

#______________________________________
cl = LINE("panducahya969@gmail.com","panducahya26")
cl.log("Auth Token : " + str(cl.authToken))
MySelf = cl.getProfile()
print("My MID : " + MySelf.mid)
#______________________________________
g1 = LINE("panducahya62@gmail.com","panducahya26")
g1.log("Auth Token : " + str(g1.authToken))
MySelf = g1.getProfile()
print("My MID : " + MySelf.mid)
#______________________________________
g2 = LINE("fahriwahyu25@gmail.com","panducahya26")
g2.log("Auth Token : " + str(g2.authToken))
MySelf = g2.getProfile()
print("My MID : " + MySelf.mid)
#______________________________________
g3 = LINE('ghost56@gmail.com','panducahya26')
g3.log("Auth Token : " + str(g3.authToken))
MySelf = g3.getProfile()
print("My MID : " + MySelf.mid)
#______________________________________
admin = ["u1e812bcfc29ed4d9eae95a64a59b9568"]
whiteListedMid = ["u1e812bcfc29ed4d9eae95a64a59b9568","uda6d0a9f5ea094c291a5df1987ae8af8","uf2d5b9d84cc7c573804c4869099cc807","ufb0c4197af6db4ecb275288ce8868018"]
print ('__________________________________')
oepoll = OEPoll(cl)
mid = cl.getProfile().mid
g1MID = g1.getProfile().mid
g2MID = g2.getProfile().mid
g3MID = g3.getProfile().mid
zxcv = mid
protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
ghost = []
welcome = []
msg_dict = {}
msg_dict1 = {}
offbot = []
kickjs = []
Kibar = []
NoteCreate = []
Foto = {"foto":{}}
settings = {
	"batasfast":0.007999,
    "welcome": True,
    "keyCommand": "",
    "postEndUrl": {},
    "postingan":{},
    "checkPost": True,
    "autoRead": False,
    "autoJoinTicket": True,
    "setKey": False,
    "STKVR": False,
    "restartPoint": False,
    "checkSticker": False,
    "userMentioned": False,
    "selfbot":True,
    "unsendMessage": True,
    "Picture":False,
    "group":{},
    "displayName": "",
    "MySelf": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "commentPost": "Ikutan Comment ya, \nbiar gx dibilang sombong",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.200.32.99 Safari/537.36"
    ]
}
status = 6
wait = {
    "limit": 1,
    "video":{},
    "Timeline": True,
    "likePost": True,
    "likeOn": True,
    "lang":True,
    "readPoint":{},
    "contact": False,
    "readMember":{},
    "Blacklist":{},
    "wBlacklist":False,
    "dBlacklist":False,
    "TalkBlacklist":{},
    "TalkwBlacklist":False,
    "TalkdBlacklist":False,
    "talkban":True,
    "autoRead": False,
    "autoBlock": False,
    "autoAdd":False,
    "autoLeave":False,
    "autojoin":True,
    "detectMention":False,
    "Mentionkick":False,
    "welcome":True,
    "DetectUnsend": True,
    "nSmule":True,
    "nCall":True,
    "selfbot":True,
    "mention":"door",
    "ttt": "line://app/1602687308-GXq4Vvk9?type=text&text=",
    "Respontag":"ga usah tag , Langsung transfer ajha",
    "welcome":"Selamat datang",
    "comment":"autoLike by : ~ afr1z4l",
    "message1":"Nah loh ketahuan !",
}
read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
MySelf = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
MySelf["displayName"] = MySelf
MySelf["statusMessage"] = MySelf
MySelf["pictureStatus"] = MySelf

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
           
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def speedtest(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d' % (secs)
    elif days > 0 and weaks == 0:
        return '%02d' %(secs)
    elif days > 0 and weaks > 0:
        return '%02d' %(secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
    
def autolike():
    for zx in range(0,500):
      hasil = cl.activity(limit=500)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == True:
        try:
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postid'],wait["comment"])
          print ("Like Success")
        except:
          pass
      else:
          print ("Already Liked")
    
def logError(text):
    cl.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items

def downloadImageWithURL (mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)
    
def tium2(grup, targets):
	gMembMids = targets
	matched_list = []
	if matched_list != []:
		pass
	for tag in wait["Blacklist"]:
		matched_list+=filter(lambda str: str == tag, gMembMids)
	if matched_list == []:
		pass
		return
	try:
		cl.inviteIntoGroup(grup, ["u1e812bcfc29ed4d9eae95a64a59b9568","uf2d5b9d84cc7c573804c4869099cc807","u4f97f7fee3126f6524013e40a1019628","u78a739fab94aef6094b2e1f9b4d85f87","u5add75c7cb29a76635dce138334e7475"])
		kickjs(grup,matched_list)
	except:cl.sendMessage(grup,'limit')
	print("sukses")

def kickjs(grup,blaklist):
	try:
		cmd = 'kickall.js gid={} token={}'.format(grup, cl.authToken)
		for t in blaklist:
			if t not in whiteListedMid:
				cmd += ' uid={}'.format(t)
		success = execute_js(cmd)
		squad = ["u4c80dab0a85206b0f7c4153e0cdb8a21","u2c77157695c61c4dcdda02b2d43b1414","u09de0e4f6b8ce8ad6bfa4a9c217ae8ae","uded7c60de500066647426d47f396f4f2"]
		cl.inviteIntoGroup(grup, squad)
		try:cl.acceptGroupInvitation(grup)
		except:cl.acceptGroupInvitation(grup)
	except:pass
	print ('success')

def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            cl.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)

def sendflex(to, data):
    n1 = LiffChatContext(to)
    n2 = LiffContext(chat=n1)
    view = LiffViewRequest('1602687308-GXq4Vvk9', n2)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def sendCarousel(to, data):
    data = json.dumps(data)
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return requests.post(url, data=data, headers=headers)
def sendCarousel(to,col):
    col = json.dumps(col)
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = cl.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return requests.post(url, data=col, headers=headers)
    
def changeProfileVideo(to):
    if settings['changevp']['picture'] == True:
        return cl.sendMessage(to, "Foto tidak ditemukan")
    elif settings['changevp']['video'] == True:
        return cl.sendMessage(to, "Video tidak ditemukan")
    else:
        path = settings['changevp']['video']
        files = {'file': open(path, 'rb')}
        obs_params = cl.genOBSParams({'oid': cl.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return cl.sendMessage(to, "Gagal update profile")
        path_p = settings['changevp']['picture']
        settings['changevp']['status'] = True
        cl.updateProfilePicture(path_p, 'vp')
                     
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = cl.genOBSParams({'oid': mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4', 'name': 'GEGE.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        cl.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile %s"%str(e))

def cloneProfile(mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        MySelf = cl.getProfile()
        MySelf.displayName, MySelf.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(MySelf)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)

def restoreProfile():
    MySelf = cl.getProfile()
    MySelf.displayName = settings['MySelf']['displayName']
    MySelf.statusMessage = settings['MySelf']['statusMessage']
    if settings['MySelf']['videoProfile'] == None:
        MySelf.pictureStatus = settings['MySelf']['pictureStatus']
        cl.updateProfileAttribute(8, MySelf.pictureStatus)
        cl.updateProfile(MySelf)
    else:
        cl.updateProfile(MySelf)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['MySelf']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['MySelf']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['MySelf']['coverId']
    cl.updateProfileCoverById(coverId)
    
def NoteCreate(to,cmd,msg):
	h = []
	s = []
	if cmd == 'tagnote':
		sakui = cl.getProfile()
		group = cl.getGroup(msg.to);nama = [contact.mid+'||//{}'.format(contact.displayName) for contact in group.members];nama.remove(sakui.mid+'||//{}'.format(sakui.displayName))
		data = nama
		k = len(data)//20
		for aa in range(k+1):
			nos = 0
			if aa == 0:dd = '╭─[ Mention Note ]';no=aa
			else:dd = '';no=aa*20
			msgas = dd
			for i in data[aa*20 : (aa+1)*20]:
				no+=1
				if no == len(data):msgas+='\n│{}. @  \n╰─[ Mention Note ]'.format(no)
				else:msgas+='\n│{}. @'.format(no)
			msgas = msgas
			for i in data[aa*20 : (aa+1)*20]:
				gg = []
				dd = ''
				for ss in msgas:
					if ss == '@':
						dd += str(ss)
						gg.append(dd.index('@'))
						dd = dd.replace('@',' ')
					else:
						dd += str(ss)
				s.append({'type': "RECALL", 'start': gg[nos], 'end': gg[nos]+1, 'mid': str(i.split('||//')[0])})
				nos +=1
			h = cl.createPostGroup(msgas,msg.to,holdingTime=None,textMeta=s)
			
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "     [ Total {} Remote Tv ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error) 
        
def mentionMembers(to, mid):
    try:
        arrData = ""
        ginfo = cl.getGroup(to)
        textx = "1. "
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "{}. ".format(str(no))
            else:
                textx += "  「 ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀ : {} 」\n".format(str(len(mid)))
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = (str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
       # cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
       # cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
    #    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error)) 

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" wib\nNama Group : "+str(len(gid))+"\nTeman : "+str(len(teman))+"\nExpired : In "+hari+"\n Version :「Gaje whiteListedMid」  \nTanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\nRuntime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)                     
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def sendMentionV2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    
def sendTemplate(group, data):
    xyz = LiffChatContext(group)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def sendFooter(to, isi):
    data = {
        "type": "text",
        "text": isi,
        "sentBy": {
            "label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ",
            "iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif",
            "linkUrl": "line://ti/p/~afr1z4l"
        }
    }
    sendTemplate(to, data)
def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def removeCmd(cmd, text):
	key = settings["keyCommand"]
	if settings["setKey"] == False: key = ''
	rmv = len(key + cmd) + 1
	return text[rmv:]
def command(text):
        pesan = text.lower()
        if pesan.startswith(settings["keyCommand"]):
        	cmd = pesan.replace(settings["keyCommand"],"")
        else:
        	cmd = "command"
        return cmd
        
def lineBot(op):
    global time
    global ast
    global groupParam
    global multiprocessing
    global subprocess
    global threading
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoBlock"] == True:
                cl.blockContact(op.param1)
                cl.sendMessage(op.param1,"ᴀᴜᴛᴏʙʟᴏᴄᴋ ᴏɴ \nᴄᴏᴍᴇɴ ᴅɪ ᴛʟ ᴋʟᴏ ᴀᴅᴀ ᴘᴇʀʟᴜ")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in whiteListedMid and op.param2 not in admin:
                    if (wait["message1"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, wait["message1"])
#_____________________________________         
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in whiteListedMid and op.param2 not in admin:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            wait["Blacklist"][op.param2] = True       
                            g3.acceptGroupInvitation(op.param1)
                            g3.kickoutFromGroup(op.param1,[op.param2])                            
                            g3.updateGroup(X)
                            g3.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            g3.sendMessage(op.param1,"Contact curut oplek2 QR")
                            g3.leaveGroup(op.param1)
                except:
                    pass
                              
#_____________________________________         
        if op.type == 13:
            if mid in op.param3:
                if wait["autojoin"] == True:
                    if op.param2 not in whiteListedMid and op.param2 not in admin:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in whiteListedMid and op.param2 not in admin:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            cl.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        pass
                return
                        
            if op.param2 in wait["Blacklist"]:
                cl.kickoutFromGroup(op.param1,[op.param2])
                cl.cancelGroupInvitation(op.param1, [op.param3])
                
            if op.param3 in wait["Blacklist"]:
                if op.param2 not in whiteListedMid and op.param2 not in admin:
                    cl.cancelGroupInvitation(op.param1,[op.param3])
                    wait["Blacklist"][op.param2] = True
                    cl.kickoutFromGroup(op.param1,[op.param2])

#_____________________________________
        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                leaveMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)

#_____________________________________
        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in whiteListedMid:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)
                return
                      
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in whiteListedMid and op.param2 not in admin:
                    wait["Blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["Blacklist"]:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                        
        if op.type == 17:
            if op.param2 in wait["Blacklist"]:
                cl.kickoutFromGroup(op.param1,[op.param2])
                
                return
#_____________________________________         
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in whiteListedMid and op.param2 not in admin:
                    g1.acceptGroupInvitation(op.param1)
                    g1.kickoutFromGroup(op.param1,[op.param2])	
                    g1.sendMessage(op.param1,"Do not kick Member !!!")
                    g1.inviteIntoGroup(op.param1,["u4c80dab0a85206b0f7c4153e0cdb8a21","u95335158e840a318d1e69d5e4cbb478c","uc8adec62e406dbb1f6aa8308f9670baf","uf2d5b9d84cc7c573804c4869099cc807","u1ec280791176afb8be161eb934f98d38","u432c4c07807c53bbe816dd4dff2a2cf7","u5add75c7cb29a76635dce138334e7475"])
                    G = g1.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    g1.updateGroup(G)
                    Ticket = g1.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)							
                    G.preventedJoinByTicket = True
                    g1.updateGroup(G)
                    wait["Blacklist"][op.param2] = True
                    g1.leaveGroup(op.param1)
                    cl.inviteIntoGroup(op.param1,[g1MID])
            else:
                pass
							
						
                if op.param3 in g1MID:
                    if op.param2 not in whiteListedMid and op.param2 not in admin:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.inviteIntoGroup(op.param1,["u4a13cbe7471c74870ac828ef50ef1f1a","ua1fab51153eb593a6c9b3496ba6c5e72"])
                        cl.sendMessage(op.param1,"Ada yg ke JS an")
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.inviteIntoGroup(op.param1,["u4a13cbe7471c74870ac828ef50ef1f1a","ua1fab51153eb593a6c9b3496ba6c5e72"])
                        cl.sendMessage(op.param1,"Ada yg bypass ya")
                        
                if op.param3 in g2MID:
                    if op.param2 not in whiteListedMid and op.param2 not in admin:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.inviteIntoGroup(op.param1,["u4a13cbe7471c74870ac828ef50ef1f1a","ua1fab51153eb593a6c9b3496ba6c5e72"])
                        cl.sendMessage(op.param1,"Ada yg ke JS an")
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.inviteIntoGroup(op.param1,["u4a13cbe7471c74870ac828ef50ef1f1a","ua1fab51153eb593a6c9b3496ba6c5e72"])
                        cl.sendMessage(op.param1,"Ada yg bypass ya")
                        
        if op.type == 19:
            if op.param1 in ghost:
                try:
                    if op.param2 not in whiteListedMid and op.param2 not in admin:
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(op.param1)
                        g3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        g3.kickoutFromGroup(op.param1,[op.param2])
                        wait["Blacklist"][op.param2] = True
                        g3.leaveGroup(op.param1)
                        X = cl.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
                except:
                    pass
                                    
        if op.type == 19:
            if op.param1 in protectantijs:
                if mid in op.param3:
                    if op.param2 not in whiteListedMid and op.param2 not in admin:
                        try:
                            g1.acceptGroupInvitation(op.param1)
                            g2.acceptGroupInvitation(op.param1)                        
                            g1.inviteIntoGroup(op.param1,['u4c80dab0a85206b0f7c4153e0cdb8a21'])
                            g2.inviteIntoGroup(op.param1,['u4c80dab0a85206b0f7c4153e0cdb8a21'])
                            g1.kickoutFromGroup(op.param1,[op.param2])
                            g2.kickoutFromGroup(op.param1,[op.param2])
                            cl.acceptGroupInvitation(op.param1)
                            wait["Blacklist"][op.param2] = True
                            g1.leaveGroup(op.param1)
                            g2.leaveGroup(op.param1)
                            cl.inviteIntoGroup(op.param1,[g1MID,g2MID])
                        except:
                            pass

            if op.param1 in protectantijs:
                if g1MID in op.param3:
                    if op.param2 not in whiteListedMid and op.param2 not in admin:
                        wait["Blacklist"][op.param2] = True
                        try:
                            g2.inviteIntoGroup(op.param1,[mid,g1MID])
                            g2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                cl.inviteIntoGroup(op.param1,[g1MID,g2MID])
                                cl.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass
                                
            if op.param1 in protectantijs:
                if g2MID in op.param3:
                    if op.param2 not in whiteListedMid and op.param2 not in admin:
                        wait["Blacklist"][op.param2] = True
                        try:
                            g1.inviteIntoGroup(op.param1,[mid,g2MID])
                            g1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                cl.inviteIntoGroup(op.param1,[g1MID,g2MID])
                                cl.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass
#_____________________________________         
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 in whiteListedMid and op.param2 in admin:
                    pass
                else:
                    try:
                        if op.param2 not in whiteListedMid and op.param2 not in admin:
                            wait["Blacklist"][op.param2] = True
                            user = cl.getContact(op.param2)
                            cl.sendMessage(op.param1,"Jangan di cancel GOBLOOK/ @" + str(user.displayName))
                            try:
                                if op.param3 not in wait["Blacklist"]:
                                    cl.inviteIntoGroup(op.param1,[g1MID,g2MID])
                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                    cl.sendMessage(msg.to, 'Jangan di Ancel GOBLOK !!')
                            except:
                            	pass
                        else:
                            pass
                    except:
                        pass
                        
#_____________________________________         
        if op.type == 55:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = cl.getContact(op.param2)
                        cover = cl.getProfileCoverURL(op.param2)
                        tz = pytz.timezone("Asia/Jakarta")
                        timeNow = datetime.now(tz=tz)
                        data = {
                                "type": "flex",
                                "altText": "Sider member",
                                "contents": {
  "type": "bubble",
  "size": "micro",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://i.ibb.co/d6WfLYL/IMG-20201207-131718.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:1",
        "gravity": "center"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{} ".format(cl.getContact(op.param2).displayName),
            "size": "xs",
            "color": "#ffffff",
            "weight": "bold",
            "style": "normal",
            "align": "center",
            "wrap": True,
            "offsetTop": "2px",
            "offsetStart": "15px"
          }
        ],
        "position": "absolute",
        "width": "140px",
        "height": "25px",
        "borderWidth": "2px",
        "cornerRadius": "10px",
        "offsetTop": "67px",
        "offsetStart": "14px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
            "size": "full",
            "aspectRatio": "1:1",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "50px",
        "height": "50px",
        "borderWidth": "3px",
        "borderColor": "#3300cc",
        "cornerRadius": "100px",
        "offsetTop": "42px",
        "offsetStart": "3px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": wait["mention"],
            "size": "xxs",
            "color": "#33cc00",
            "weight": "bold",
            "style": "normal",
            "align": "center",
            "wrap": True
          }
        ],
        "position": "absolute",
        "width": "84px",
        "height": "20px",
        "borderWidth": "2px",
        "cornerRadius": "5px",
        "offsetTop": "8px",
        "offsetStart": "65px"
      }
    ],
    "paddingAll": "0px",
    "width": "160px",
    "height": "100px",
    "borderWidth": "3px",
    "borderColor": "#3300cc",
    "cornerRadius": "15px",
    "action": {
      "type": "uri",
      "label": "action",
      "uri": "http://linecorp.com/"
    }
  },
  "styles": {
    "body": {
      "backgroundColor": "#0066FF"
    }
  }
}
}
                        cl.postTemplate(op.param1, data)
#_____________________________________                    
        if op.type == 55:            
            try:
                if op.param1 in read["readPoint"]:
                    if op.param2 in read["readMember"][op.param1]:
                        pass
                    else:
                        read["readMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass
        if op.type == 65:
            if wait["DetectUnsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'ɢᴀᴍʙᴀʀʏᴀ ɪʟᴀɴɢ':
                                ginfo = cl.getGroup(at)
                                ika = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "ᴘᴇsᴀɴ ᴅɪʜᴀᴘᴜs\nᴘᴇɴɢɪʀɪᴍ: "
                                ret_ = "ɴᴀᴍᴀ ɢʀᴜᴘ: {}".format(str(ginfo.name))
                                ret_ += "\nᴊᴀᴍ sʜᴀʀᴇ: {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ik = str(ika.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ika.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendReplyMessage(msg_id, to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                           else:
                                ginfo = cl.getGroup(at)
                                ika = cl.getContact(msg_dict[msg_id]["from"])
                                ika1 = "{}".format(str(ika.displayName))
                                ika2 = ":{}".format(str(ginfo.name))
                                ika3 = "{}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                seber = "═══「 ᴘᴇsᴀɴ ᴅɪʜᴀᴘᴜs 」═══\n{}".format(str(msg_dict[msg_id]["text"]))
                                cl.sendImage(msg.to, msg_dict[msg_id]["data"])
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["DetectUnsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "╭──「  Unsend Sticker  」"
                                ret_ += "\n├ {}".format(str(ryan.displayName))
                                ret_ += "\n├ {}".format(str(ginfo.name))
                                ret_ += "\n├ {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "\n├ {}".format(str(msg_dict1[msg_id]["text"]))
                                ret_ += "\n╰──「 Sticker dibawah 」"
                                cl.sendReplyMessage(msg_id, to, str(ret_))
                                cl.sendImage(msg.to, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)
#_____________________________________         
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 6:
                if settings["responGc"] == True and sender != clMID:
                    contact = cl.getContact(sender)
                    if msg.toType == 0:
                        if msg.contentMetadata["GC_EVT_TYPE"] == "I":
                            sendMention(to, sender, "Nah",", พ่องไตพ่องไตรันคลอทำควยอะไร กูร้องเพลง😂$")
                            arg = "   [ Notify ] SpamCall"
                            arg += "\n   UserSpam: {}".format(str(contact.displayName))
                            print (arg)
                    elif msg.toType == 2:
                        group = cl.getGroup(to)
                        if msg.contentMetadata["GC_EVT_TYPE"] == "S":
                            arg = "   [ Notify ] เริ่มการคลอ"
                            arg += "\n   Group: {}".format(str(group.name))
                            arg += "\n   User Started: {}".format(str(contact.displayName))
                            print (arg)
                            sendMention(to, sender, "คุณ ", " \nฮันแน่ เหงาสิถ้า รู้นะคิดอะไรอยู่55😜")
                        elif msg.contentMetadata["GC_EVT_TYPE"] == "E":
                            sendMention(to, sender, "คุณ ", " \nแหม๋แหม๋ลงไวจิงเชียว มีคนเรียกอะดี้😝")
                            arg = "   [ Notify ] สิ้นสุดการคลอ"
                            arg += "\n   Group: {}".format(str(group.name))
                            arg += "\n   User Ended: {}".format(str(contact.displayName))
                            print (arg)
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != cl.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'ɢᴀᴍʙᴀʀʏᴀ ᴅɪʙᴀᴡᴀʜ',"data":path,"from":msg._from,"createdTime":msg.createdTime}
                if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n      「✯sᴛɪᴄᴋᴇʀ ɪɴғᴏ✯]"
                   ret_ += "\nsᴛɪᴄᴋᴇʀ ɪᴅ: {}".format(stk_id)
                   ret_ += "\nsᴛɪᴄᴋᴇʀ ᴠᴇʀsɪᴏɴ: {}".format(stk_ver)
                   ret_ += "\nsᴛɪᴄᴋᴇʀ: {}".format(pkg_id)
                   ret_ += "\nᴜʀʟ:{}".format(pkg_id)
                   ret_ += "\n    「✯ᴜɴsᴇɴᴅ ғɪɴɪsʜ✯」"
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
             
#________________________________
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg._from in admin:
               if msg._from not in whiteListedMid:
                 if wait["talkban"] == True:
                   if msg._from in wait["TalkBlacklist"]:
                      try:
                          cl.kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              cl.kickoutFromGroup(msg.to, [msg._from])
                          except:
                              try:
                                  cl.kickoutFromGroup(msg.to, [msg._from])
                              except:
                                  try:
                                  	cl.kickoutFromGroup(msg.to, [msg._from])
                                  except:
                                      pass
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   contact = cl.getContact(msg._from)
                   tz = pytz.timezone("Asia/Jakarta")
                   timeNow = datetime.now(tz=tz)
                   cover = cl.getProfileCoverURL(sender)
                   name = re.findall(r'@(\w+)', msg.text)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in mid:
                           data = {
                                       "type": "flex",
                                       "altText": "Bagi Bagi Sembako",
                                       "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/2PBHBRY/Cropped-image-20201030-221042-3427731946386620016.png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "."
              }
            ],
            "position": "absolute",
            "width": "137px",
            "height": "25px",
            "backgroundColor": "#556788",
            "borderWidth": "2px",
            "offsetTop": "5px",
            "offsetStart": "8px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "."
              }
            ],
            "position": "absolute",
            "width": "137px",
            "height": "25px",
            "backgroundColor": "#566788",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "200px",
            "offsetStart": "8px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "."
              }
            ],
            "position": "absolute",
            "width": "137px",
            "height": "168px",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "31px",
            "offsetStart": "8px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": wait["ResponTag"],
                "size": "xxs",
                "color": "#ffffff",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "5px"
              }
            ],
            "position": "absolute",
            "width": "137px",
            "height": "30px",
            "backgroundColor": "#ff0000",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "32px",
            "offsetStart": "8px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": cover,
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://linecorp.com/"
                }
              }
            ],
            "position": "absolute",
            "width": "122px",
            "height": "122px",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "100px",
            "offsetTop": "69px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "TAG LAGI",
                "size": "xxs",
                "color": "#ffffff",
                "wrap": True,
                "offsetTop": "1px",
                "offsetStart": "26px"
              }
            ],
            "position": "absolute",
            "backgroundColor": "#000000",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "20px",
            "width": "95px",
            "offsetTop": "154px",
            "offsetStart": "55px",
            "height": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{} ".format(contact.displayName),
                "size": "xxs",
                "color": "#ffffff",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "25px"
              }
            ],
            "position": "absolute",
            "width": "100px",
            "height": "20px",
            "backgroundColor": "#000000",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "20px",
            "offsetTop": "132px",
            "offsetStart": "55px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://linecorp.com/"
                }
              }
            ],
            "position": "absolute",
            "width": "72px",
            "height": "72px",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "100px",
            "offsetTop": "101px",
            "offsetStart": "10px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/2PBHBRY/Cropped-image-20201030-221042-3427731946386620016.png",
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "25px",
            "height": "25px",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "5px",
            "offsetStart": "8px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": " RESPONTAG ",
                "size": "xs",
                "offsetTop": "3px",
                "offsetStart": "1px",
                "color": "#ffffff"
              }
            ],
            "width": "114px",
            "height": "25px",
            "backgroundColor": "#000000",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "5px",
            "offsetStart": "31px",
            "position": "absolute"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/2PBHBRY/Cropped-image-20201030-221042-3427731946386620016.png",
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "25px",
            "height": "25px",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "5px",
            "offsetStart": "119px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/2PBHBRY/Cropped-image-20201030-221042-3427731946386620016.png",
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "25px",
            "height": "25px",
            "backgroundColor": "#556788",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "200px",
            "offsetStart": "8px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/2PBHBRY/Cropped-image-20201030-221042-3427731946386620016.png",
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "25px",
            "height": "25px",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "200px",
            "offsetStart": "119px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "     NM BOTS",
                "size": "xs",
                "color": "#ffffff",
                "offsetTop": "1px",
                "offsetStart": "0px"
              }
            ],
            "width": "92px",
            "height": "25px",
            "backgroundColor": "#000000",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "200px",
            "offsetStart": "31px",
            "position": "absolute"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/2PBHBRY/Cropped-image-20201030-221042-3427731946386620016.png",
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://line.me/ti/p/~afr1z4l"
                }
              }
            ],
            "position": "absolute",
            "width": "20px",
            "height": "20px",
            "cornerRadius": "100px",
            "offsetTop": "64px",
            "offsetStart": "12px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/2PBHBRY/Cropped-image-20201030-221042-3427731946386620016.png",
                "aspectRatio": "1:1",
                "size": "full",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://linecorp.com/"
                }
              }
            ],
            "position": "absolute",
            "width": "20px",
            "height": "20px",
            "cornerRadius": "100px",
            "offsetTop": "64px",
            "offsetStart": "121px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/2PBHBRY/Cropped-image-20201030-221042-3427731946386620016.png",
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://linecorp.com/"
                }
              }
            ],
            "width": "20px",
            "cornerRadius": "100px",
            "offsetTop": "175px",
            "position": "absolute",
            "offsetStart": "13px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/2PBHBRY/Cropped-image-20201030-221042-3427731946386620016.png",
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://linecorp.com/"
                }
              }
            ],
            "position": "absolute",
            "width": "20px",
            "height": "20px",
            "cornerRadius": "100px",
            "offsetTop": "175px",
            "offsetStart": "121px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#330033",
        "cornerRadius": "10px"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        }
      }
    },
  ]
}
}
                           cl.postTemplate(to, data)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in whiteListedMid:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in whiteListedMid:
                           cl.sendReplyMessage(msg_id, to,"Notag mode On")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
#___________________________________
        if op.type == 25:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                terminal = command(text)
                for terminal in terminal.split(" & "):
                    setKey = settings["keyCommand"].title()
                    if settings["setKey"] == False:
                        setKey = ''
                    if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                        if msg.toType == 0:
                            if sender != cl.profile.mid:
                                to = sender
                            else:
                                to = receiver
                        elif msg.toType == 1:
                            to = receiver
                        elif msg.toType == 2:
                            to = receiver
                        if msg.contentType == 0:
                            if to in offbot:
                                return
                        elif msg.contentType == 16:
                            if settings["checkPost"] == True:
                                try:
                                    ret_ = "╔══[ Details Post ]"
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        contact = cl.getContact(sender)
                                        auth = "\n╠❂➢ Penulis : {}".format(str(contact.displayName))
                                    else:
                                        auth = "\n╠❂➢ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                    purl = "\n╠❂➢ URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                    ret_ += auth
                                    ret_ += purl
                                    if "mediaOid" in msg.contentMetadata:
                                        object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                        if msg.contentMetadata["mediaType"] == "V":
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\n╠❂➢ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                                murl = "\n╠❂➢ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\n╠❂➢ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                                murl = "\n╠❂➢ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                            ret_ += murl
                                        else:
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\n╠❂➢ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\n╠❂➢ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        ret_ += ourl
                                    if "stickerId" in msg.contentMetadata:
                                        stck = "\n╠❂➢ Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                        ret_ += stck
                                    if "text" in msg.contentMetadata:
                                        text = "\n╠❂➢ Tulisan :\n╠❂➢ {}".format(str(msg.contentMetadata["text"]))
                                        ret_ += text
                                    ret_ += "\n╚══[ Finish ]"
                                    sendpostTemplate(to, data)
                                except:
                               #     cl.sendReplyMessage(msg_id, to, "➢   Done Like")
                                    data = {"type": "text","text": "Done autoLike & Comment","sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                                    cl.postTemplate(to, data)
                            if msg.toType in (2,1,0):
                                purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                                adw = cl.likePost(purl[0], purl[1], random.choice([1001,1002,1003,1004,1005]))
                                adws = cl.createComment(purl[0], purl[1], settings["commentPost"])
                                data = {"type": "text","text": "  ➢   Done autoLike & comment","sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                                cl.postTemplate(to, data)
            except Exception as error:
                logError(error)   

            if msg.contentType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendReplyMessage(msg_id, to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendReplyMessage(msg_id, to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
               if msg.contentType == 13:
                if msg._from in admin:
                  if wait["invite"] == True:
                    msg.contentType = 0
                    contact = cl.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in wait["Blacklist"]:
                            cl.sendReplyMessage(msg_id, to, "ʟɪsᴛ ʙʟ")
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                             try:
                                  cl.findAndAddContactsByMid(target)
                                  cl.inviteIntoGroup(msg.to,[target])
                                  ryan = cl.getContact(target)
                                  zx = ""
                                  zxc = ""
                                  zx2 = []
                                  xpesan =  "「 sᴜᴋsᴇs ɪɴᴠɪᴛᴇ 」\nɴᴀᴍᴀ"
                                  ret_ = "ᴋᴇᴛɪᴋ ɪɴᴠɪᴛᴇ ᴏғғ ᴊɪᴋᴀ sᴜᴅᴀʜ ᴅᴏɴᴇ"
                                  ry = str(ryan.displayName)
                                  pesan = ''
                                  pesan2 = pesan+"@x\n"
                                  xlen = str(len(zxc)+len(xpesan))
                                  xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                  zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                  zx2.append(zx)
                                  zxc += pesan2
                                  text = xpesan + zxc + ret_ + ""
                                  cl.sendReplyMessage(msg_id, to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                  wait["invite"] = False
                                  break
                             except:
                                  cl.sendReplyMessage(msg_id, to,"ᴀɴᴅᴀ ᴛᴇʀᴋᴇɴᴀ sᴛʀᴜᴋ")
                                  wait["invite"] = False
                                  break
                                  
               if msg.contentType == 13:
                 if wait["Invi"] == True:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = cl.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                cl.sendReplyMessage(msg_id, to,"-> " + _name + " was here")
                                wait["Invi"] = False
                                break         
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                cl.findAndAddContactsByMid(target)
                                cl.inviteIntoGroup(msg.to,[target])
                                cl.sendReplyMessage(msg_id, to,"Success inv\n" + _name)
                                wait["Invi"] = False
                                break
#ADD Blacklist
                 if msg._from in admin:
                  if wait["wBlacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Blacklist"]:
                        cl.sendReplyMessage(msg_id, to,"Contact itu sudah ada di Blacklist")
                        wait["wBlacklist"] = True
                    else:
                        wait["Blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wBlacklist"] = True
                        cl.sendReplyMessage(msg_id, to,"Berhasil menambahkan ke Blacklist user")
                  if wait["dBlacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Blacklist"]:
                        del wait["Blacklist"][msg.contentMetadata["mid"]]
                        cl.sendReplyMessage(msg_id, to,"Berhasil menghapus dari Blacklist user")
                    else:
                        wait["dBlacklist"] = True
                        cl.sendReplyMessage(msg_id, to,"Contact itu tidak ada di Blacklist")
#TALKBAN
                 if msg._from in admin:
                  if wait["TalkwBlacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["TalkBlacklist"]:
                        cl.sendReplyMessage(msg_id, to,"Contact itu sudah ada di Talkban")
                        wait["TalkwBlacklist"] = True
                    else:
                        wait["TalkBlacklist"][msg.contentMetadata["mid"]] = True
                        wait["TalkwBlacklist"] = True
                        cl.sendReplyMessage(msg_id, to,"Berhasil menambahkan ke Talkban user")
                  if wait["TalkdBlacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["TalkBlacklist"]:
                        del wait["TalkBlacklist"][msg.contentMetadata["mid"]]
                        cl.sendReplyMessage(msg_id, to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["TalkdBlacklist"] = True
                        cl.sendReplyMessage(msg_id, to,"Contact itu tidak ada di Talkban")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                        if MySelf.mid in Foto["foto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Foto["foto"][MySelf.mid]
                            cl.updateProfilePicture(path)
                            cl.sendReplyMessage(msg_id, to,"Success update foto")
               if msg.contentType == 0:
                    if settings["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                            data = {"type": "text","text": "            ᴍᴇɴᴜ ʜᴇʟᴘ\n___________________________\n◯ ʜᴇʟᴘ\n◯ ʜᴇʟᴘ ꜱᴇʟꜰʙᴏᴛ\n◯ ʜᴇʟᴘ ꜱᴇʟꜰʙᴏᴛ2\n◯ ʜᴇʟᴘ ʙᴏᴛᴄʟ\n◯ ʜᴇʟᴘ ᴀɴᴛɪᴊꜱ\n◯ ʟɪꜱᴛᴛᴏᴋᴇɴ\n◯ ᴛᴀɢᴀʟʟ/ᴛᴀɢ ʀᴇᴍᴏᴛᴇ\n◯ ɴᴏᴛɪꜰ ꜱᴍᴜʟᴇ/ᴄᴀʟʟ\n◯ ᴠɪᴅᴇᴏ  [ ᴊᴜᴅᴜʟɴʏᴀ ]\n◯ ᴊᴏᴏx  [ ᴊᴜᴅᴜʟɴʏᴀ ]","sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                            cl.postTemplate(to, data)
                            
                        elif cmd == "help selfbot":
                            data = {"type": "text","text": "            ʜᴇʟᴘ ꜱᴇʟꜰʙᴏᴛ\n___________________________\n◯ ᴍᴇ\n◯ ᴍɪᴅ\n◯ ᴍɪᴅ @\n◯ ɪɴᴠɪᴛᴇ [ ᴄᴏɴᴛᴀᴄᴛ ]\n◯ ꜱɪᴅᴇʀ [ ᴏɴ/ᴏꜰꜰ ]\n◯ ᴡᴇʟᴄᴏᴍᴇ  [ ᴏɴ/ᴏꜰꜰ ]\n◯ ʀᴇꜱᴘᴏɴ  [ ᴏɴ/ᴏꜰꜰ ]\n◯ ɴᴏᴛᴀɢ  [ ᴏɴ/ᴏꜰꜰ ]\n◯ ʟɪꜱᴛᴘᴇɴᴅɪɴɢ","sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                            cl.postTemplate(to, data)
                            data = {"type": "text","text": "            ʜᴇʟᴘ ꜱᴇʟꜰʙᴏᴛ\n___________________________\n◯ ꜱᴘ - ꜱᴘᴇᴇᴅ\n◯ ᴜɴꜱᴇɴᴅ  [ ᴏɴ/ᴏꜰꜰ ]\n◯ ᴊᴏɪɴᴛɪᴄᴋᴇᴛ  [ ᴏɴ/ᴏꜰꜰ ]\n◯ ᴀᴜᴛᴏʙʟᴏᴄᴋ  [ ᴏɴ/ᴏꜰꜰ ]\n◯ ᴘᴏꜱᴛ  [ ᴏɴ/ᴏꜰꜰ ]\n◯ ʟɪᴋᴇ  [ ᴏɴ/ᴏꜰꜰ ]\n◯ ᴘɪᴄᴛᴍᴇᴍʙᴇʀ","sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                            cl.postTemplate(to, data)
                            data = {"type": "text","text": "            ʜᴇʟᴘ ꜱᴇʟꜰʙᴏᴛ\n___________________________\n◯ ᴛᴀɢɴᴏᴛᴇ\n◯ ʙʟᴏᴄᴋ @\n◯ ʀᴇᴄʜᴀᴛ\n◯ ᴀʙᴏᴜᴛ\n◯ ᴏʀᴅᴇʀ\n◯ ʟɪꜱᴛᴍᴇᴍʙᴇʀ\n◯ ᴅᴇʟʟꜰʀɪᴇɴᴅ @\n◯ ɪɴꜰᴏɢʀᴏᴜᴘ\n◯ ꜰʀɪᴇɴᴅʟɪꜱᴛ\n◯ ʙʀᴏᴀᴅᴄᴀꜱᴛ  [ ᴛᴇxᴛ ]","sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                            cl.postTemplate(to, data)
                            
                        elif cmd == "help selfbot2":
                            data = {"type": "text","text": "            ʜᴇʟᴘ ꜱᴇʟꜰʙᴏᴛ\n___________________________\n◯ ʟɪꜱᴛᴀᴅᴍɪɴ\n◯ ʟɪꜱᴛᴘʀᴏᴛᴇᴄᴛ\n◯ ꜱᴇᴛᴛɪɴɢ\n◯ ᴀᴜᴛᴏᴊᴏɪɴ  [ ᴏɴ/ᴏꜰꜰ ]\n◯ ᴀᴜᴛᴏʟᴇᴀᴠᴇ  [ ᴏɴ/ᴏꜰꜰ ]\n◯ ʀᴇꜰʀᴇꜱʜ\n◯ ꜰᴏᴏᴛᴇʀ  [ ᴛᴇxᴛ ]\n◯ ʟɪꜱᴛᴛᴏᴋᴇɴ\n◯ ʟɪꜱᴛʙʟᴏᴄᴋ\n◯ /ʀᴇꜱᴛᴀʀᴛ","sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                            cl.postTemplate(to, data)
                            
                        elif cmd == "help botcl":
                            data = {"type": "text","text": "            ʜᴇʟᴘ ʙᴏᴛᴄʟ\n___________________________\n◯ ᴊᴏɪɴ\n◯ ᴏᴜᴛ\n◯ ʀᴇꜱᴘᴏɴ\n◯ ɢʟɪꜱᴛ\n◯ ʙʟ\n◯ ᴄʙ\n◯ ᴋɪᴄᴋ @\n◯ ꜱᴘᴀᴍɪɴᴠ @\n◯ ᴋɪᴋᴇʟ  [ ᴏɴ/ᴏꜰꜰ ]\n◯ ᴋɪᴋᴇʟᴏɴᴛᴏ\n◯ ᴏᴜᴛᴀʟʟɢʀᴏᴜᴘ\n◯ ᴊᴏɪɴᴀʟʟɢʀᴏᴜᴘ","sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                            cl.postTemplate(to, data)
                            
                        elif cmd == "help antijs":
                            data = {"type": "text","text": "            ʜᴇʟᴘ ᴀɴᴛɪᴊꜱ\n___________________________\n◯ ᴀɴᴛɪᴊꜱ ꜱᴛᴀʏ\n◯ ᴀɴᴛɪᴊꜱ ᴊᴏɪɴ\n◯ ᴀɴᴛɪᴊꜱ ᴏᴜᴛ\n◯ ᴀʟʟᴘʀᴏᴛᴇᴄᴛ  [ ᴏɴ/ᴏꜰꜰ ]\n◯ ɢʜᴏꜱᴛ  [ ᴏɴ/ᴏꜰꜰ ]\n◯ ᴀɴᴛɪᴊꜱ/ʙʏᴘᴀꜱꜱ  [ ᴏɴ/ᴏꜰꜰ ]\n◯ ᴘʀᴏᴛᴇᴄᴛᴋɪᴄᴋ  [ ᴏɴ/ᴏꜰꜰ ]\n◯ ᴘʀᴏᴛᴇᴄᴛQʀ  [ ᴏɴ/ᴏꜰꜰ ]\n◯ ᴘʀᴏᴛᴇᴄᴛᴊᴏɪɴ  [ ᴏɴ/ᴏꜰꜰ ]\n◯ ᴘʀᴏᴛᴇᴄᴛɪɴᴠɪᴛᴇ  [ ᴏɴ/ᴏꜰꜰ ]\n◯ ᴘʀᴏᴛᴇᴄᴛᴄᴀɴᴄᴇʟ  [ ᴏɴ/ᴏꜰꜰ ]","sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                            cl.postTemplate(to, data)
                            
                        elif cmd == "listtoken":
                            data = {"type": "text","text": "            ʟɪꜱᴛᴛᴏᴋᴇɴ\n__________________________\n◯ ɪᴏꜱɪᴘᴀᴅ\n◯ ᴄʜʀᴏᴍᴇ\n◯ ᴅᴇꜱᴋᴛᴏᴘᴡɪɴ\n◯ ᴅᴇꜱᴋᴛᴏᴘᴍᴀᴄ","sentBy": {"label": "ɴʙ : ᴋᴇᴛɪᴋ ʟᴏɢɪɴ []","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                            cl.postTemplate(to, data)
                            
                        elif cmd.startswith("js1name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = g1.getProfile()
                                profile.displayName = string
                                g1.updateProfile(profile)
                                g1.sendMessage(msg.to,"done " + string + "")
                                
                        elif cmd.startswith("js2name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = g2.getProfile()
                                profile.displayName = string
                                g2.updateProfile(profile)
                                g2.sendMessage(msg.to,"done " + string + "")

                        elif cmd.startswith("ghostname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = g3.getProfile()
                                profile.displayName = string
                                g3.updateProfile(profile)
                                g3.sendMessage(msg.to,"done " + string + "")

                        elif cmd.startswith("footer "):
                            khie = text.split(" ")
                            hey = text.replace(khie[0] + " ", "")
                            text = "{}".format(hey)
                            data = {
                                "type": "text",
                                "text": "{}".format(text),
                                "sentBy": {
                                    "label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ",
                                    "iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif",
                                    "linkUrl": "https://line.me/ti/p/~afr1z4l",
                                }
                            }
                            sendTemplate(to, data)
                            
                        elif cmd.startswith("apikey"):
                           if msg._from in admin:
                                apiKey = "f6Ai8rmEJOEB"
                                headers = {"apiKey": apiKey}
                                main = json.loads(requests.get("https://api.be-team.me/apikey",headers=headers).text)
                                ret_="╭「 apiKey Status 」"
                                ret_ = "\n├ Expired: "+main["result"]["expired"]
                                ret_ += "\n├ Usage: "+main["result"]["usage"]
                                ret_ += "\n├ IsActive: "+str(main["result"]["isActive"])
                                ret_ += "\n├ IsLimit: "+str(main["result"]["isLimit"])
                                ret_ += "\n├ IsVIP: "+str(main["result"]["isVIP"])
                                ret_ += "\n├ UsageRestartDate: "+main["result"]["restartTime"]
                                ret_+="\n╰「 Wkwkwk 」"
                                cl.sendMessage(to, ret_)
                                
#_________________________________________________     
                        elif cmd.startswith("login iosipad"):
                           if msg._from in admin:
                                apiKey = "f6Ai8rmEJOEB"
                                headers = {
                                    "apiKey":apiKey, 
                                    "appName": "IOSIPAD\t10.10.0\tiPhone 8\t11.2.5",
                                    "cert" : None, 
                                    "server": random.choice(["pool-1","pool-2"]), 
                                    "sysname": "NIGHT MASTER BOTS"
                                    }
                                main = json.loads(requests.get("https://api.be-team.me/qrv2",headers=headers).text)
                                cl.sendReplyMessage(msg_id, to, "QR Link / IOSIPAD [ t10.5.2/tiPhone 8/t11.2.5 ] " + main["result"]["qr_link"])
                                if not headers["cert"]:
                                    result = json.loads(requests.get(main["result"]["cb_pincode"],headers=headers).text)
                                    print("Your Pincode: " + result["result"])
                                    cl.sendReplyMessage(msg_id, to, "Your Pincode: " + result["result"])
                                result = json.loads(requests.get(main["result"]["cb_token"],headers=headers).text)
                                if result["status"] != 200:
                                	cl.sendReplyMessage(msg_id, to, "[ Error ] "+ result["reason"])
                                else:
                                    cl.sendReplyMessage(msg_id, to, LINE(result["result"]["token"]))
                                    print('success')
                                
#_________________________________________________     
                        elif cmd.startswith("login chrome"):
                           if msg._from in admin:
                                apiKey = "f6Ai8rmEJOEB"
                                headers = {
                                    "apiKey":apiKey, 
                                    "appName": "CHROMEOS\t2.3.8\tChrome OS\t1",
                                    "cert" : None, 
                                    "server": random.choice(["pool-1","pool-2"]), 
                                    "sysname": "NIGHT MASTER BOTS"
                                    }
                                main = json.loads(requests.get("https://api.be-team.me/qrv2",headers=headers).text)
                                cl.sendReplyMessage(msg_id, to, "QR Link / CHROMEOS [ t2.3.8/tChrome OS/t1 ] " + main["result"]["qr_link"])
                                if not headers["cert"]:
                                    result = json.loads(requests.get(main["result"]["cb_pincode"],headers=headers).text)
                                    print("Your Pincode: " + result["result"])
                                    cl.sendReplyMessage(msg_id, to, "Your Pincode: " + result["result"])
                                result = json.loads(requests.get(main["result"]["cb_token"],headers=headers).text)
                                if result["status"] != 200:
                                	cl.sendReplyMessage(msg_id, to, "[ Error ] "+ result["reason"])
                                else:
                                    cl.sendReplyMessage(msg_id, to, LINE(result["result"]["token"]))
                                    print('success')
                                    
#_________________________________________________     
                        elif cmd.startswith("login dekstopwin"):
                           if msg._from in admin:
                                apiKey = "f6Ai8rmEJOEB"
                                headers = {
                                    "apiKey":apiKey, 
                                    "appName": "DESKTOPWIN\t6.0.3\tWindows\t10",
                                    "cert" : None, 
                                    "server": random.choice(["pool-1","pool-2"]), 
                                    "sysname": "NIGHT MASTER BOTS"
                                    }
                                main = json.loads(requests.get("https://api.be-team.me/qrv2",headers=headers).text)
                                cl.sendReplyMessage(msg_id, to, "QR Link / DESKTOPWIN [ t6.0.3/tWindows/t10 ]" + main["result"]["qr_link"])
                                if not headers["cert"]:
                                    result = json.loads(requests.get(main["result"]["cb_pincode"],headers=headers).text)
                                    print("Your Pincode: " + result["result"])
                                    cl.sendReplyMessage(msg_id, to, "Your Pincode: " + result["result"])
                                result = json.loads(requests.get(main["result"]["cb_token"],headers=headers).text)
                                if result["status"] != 200:
                                	cl.sendReplyMessage(msg_id, to, "[ Error ] "+ result["reason"])
                                else:
                                    cl.sendReplyMessage(msg_id, to, LINE(result["result"]["token"]))
                                    print('success')
                                
#_________________________________________________     
                        elif cmd.startswith("login dekstopmac"):
                           if msg._from in admin:
                                apiKey = "f6Ai8rmEJOEB"
                                headers = {
                                    "apiKey":apiKey, 
                                    "appName": "DESKTOPMAC\t6.0.3\tMAC\t10.15",
                                    "cert" : None, 
                                    "server": random.choice(["pool-1","pool-2"]), 
                                    "sysname": "NIGHT MASTER BOTS"
                                    }
                                main = json.loads(requests.get("https://api.be-team.me/qrv2",headers=headers).text)
                                cl.sendReplyMessage(msg_id, to, "QR Link / DESKTOPMAC [ t6.0.3/tMAC/t10.15 ]" + main["result"]["qr_link"])
                                if not headers["cert"]:
                                    result = json.loads(requests.get(main["result"]["cb_pincode"],headers=headers).text)
                                    print("Your Pincode: " + result["result"])
                                    cl.sendReplyMessage(msg_id, to, "Your Pincode: " + result["result"])
                                result = json.loads(requests.get(main["result"]["cb_token"],headers=headers).text)
                                if result["status"] != 200:
                                	cl.sendReplyMessage(msg_id, to, "[ Error ] "+ result["reason"])
                                else:
                                    cl.sendReplyMessage(msg_id, to, LINE(result["result"]["token"]))
                                    print('success')
                                    
#_________________________________________________     
                        elif cmd.startswith("image "):
                            name = removeCmd("image",text)
                            headers = {"apiKey": "f6Ai8rmEJOEB"}
                            main = json.loads(requests.get("https://api.be-team.me/googleimg?search="+name,headers=headers).text)
                            data = main
                            for a in data["result"]:
                                print(a)
                                cl.sendImageWithURL(to, str(a))
                                   
                        elif cmd.startswith("lagu "):
                            name = removeCmd("lagu",text)
                            headers = {"apiKey": "f6Ai8rmEJOEB"}
                            main = json.loads(requests.get("https://api.be-team.me/joox?search="+name,headers=headers).text)
                            data = main
                            for music in data["result"]:
                                print(music)
                                cl.sendAudioWithURL(to, str(music["m4aUrl"]))
                                   
                        elif cmd.startswith("videos "):
                            name = removeCmd("videos",text)
                            apiKey = "f6Ai8rmEJOEB"
                            headers = {"apiKey": apiKey}
                            main = json.loads(requests.get("https://api.be-team.me/ytdl?search="+name,headers=headers).text)
                            master = main
                            ret="╭「 youtube 」"
                            ret+="\n├ Artis : " +str(master["result"]["artist"])
                            ret+="\n├ Judul : " +str(master["result"]["title"])
                            ret+="\n├ Link : https://www.youtube.com/watch?v=" +master["result"]["display_id"]
                            ret+="\n╰「 klick videonya 」"
                            cl.sendMessage(to, ret)
#_________________________________________________     /vidio
                        elif cmd.startswith("joox"):
                            try:
                                x = text.split(" ")
                                y = text.replace(x[0] + " ","")
                                headers = {"apiKey": "f6Ai8rmEJOEB"}
                                main = json.loads(requests.get("https://api.be-team.me/joox?search="+y,headers=headers).text)
                                master=main["result"][0]
                                data = {
  "type": "bubble",
  "size": "micro",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "{}".format(master["imgSrc"]),
        "size": "full",
        "align": "center",
        "aspectMode": "cover",
        "offsetTop": "xs",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "https://line.me/ti/p~afr1z4l"
        }
      },
      {
        "type": "text",
        "text": "{}".format(master["artist"]),
        "size": "xxs",
        "color": "#ffffff"
      },
      {
        "type": "text",
        "text": "{}".format(master["title"]),
        "size": "xxs",
        "color": "#ffffff"
      }
    ],
    "backgroundColor": "#000000",
    "spacing": "sm"
  }
}
                                cl.postFlex(to, data)
                                cl.sendAudioWithURL(to,master["m4aUrl"])
                            except Exception as error:
                                cl.sendReplyMessage(msg.id, to, str(error))
#_________________________________________________         
                        elif cmd == "setting":
                          # if wait["selfbot"] == True:
                            if msg._from in admin:
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                cover = cl.getProfileCoverURL(sender)
                                listTimeLiking = time.time()
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = ""
                                if settings["checkPost"] == True: md+="├ Post : ✅\n"
                                else: md+="├ Post : ❌\n"
                                if wait["likeOn"] == True: md+="├ Like : ✅\n"
                                else: md+="├ Like ❌\n"
                                if wait["Mentionkick"] == True: md+="├ Notag : ✅\n"
                                else: md+="├ Notag : ❌\n"
                                if wait["detectMention"] == True: md+="├ Respontag : ✅\n"
                                else: md+="├ Respontag : ❌\n"
                                if wait["DetectUnsend"] == True: md+="├ Unsend : ✅\n"
                                else: md+="├ Unsend : ❌\n"
                                if wait["autoAdd"] == True: md+="├ Aut lt56oadd : ✅\n"
                                else: md+="├ Autoadd : ❌\n"
                                if wait["autoLeave"] == True: md+="├ Autoleave : ✅\n"-r3
                                else: md+="├ Autoleave : ❌\n"
                                if wait["autojoin"] == True: md+="├ Autojoin : ✅\n"
                                else: md+="├ Autojoin : ❌\n"
                                if settings["autoJoinTicket"] == True: md+="├ Jointicket : ✅\n"
                                else: md+="├ Jointicket : v❌\n"
                                if wait["autoBlock"] == True: md+="├ Autoblock : ✅\n"
                                else: md+="├ Autoblock : ❌\n"
                                if settings["welcome"] == True: md+="├ Welcome : ✅\n"
                                else: md+="├ Welcome : ❌\n"
                                cl.sendReplyMessage(msg_id, to, "╭──「 Setting 」\n"+ md +"╰──「 Mode On/Off 」")

                        elif text.lower() == "assalamualaikum" or text.lower() == "aslkm":
                              data = {"type": "text","text": "Waalaikumsalam wr.wb","sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                              cl.postTemplate(to, data)
                            
                        elif text.lower() == "mid":
                               middd = "Name : " +cl.getContact(msg._from).displayName + "\nMid : " +msg._from
                               data = {"type": "text","text": "{}".format(middd),"sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                               cl.postTemplate(to, data)
                               
                        elif ("Gname " in msg.text):
                          if msg._from in admin:
                              X = cl.getGroup(msg.to)
                              X.name = msg.text.replace("Gname ","")
                              cl.updateGroup(X)

                        elif cmd == 'listblock':
                          if msg._from in admin:
                            blockedlist = cl.getBlockedContactIds()
                            kontak = cl.getContacts(blockedlist)
                            num=1
                            msgs="List Blocked"
                            for ids in kontak:
                                msgs+="\n[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n\nTotal Blocked : %i" % len(kontak)
                            cl.sendReplyMessage(msg_id, to, msgs)
#_________________________________________
                        elif cmd == "join":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, ["uda6d0a9f5ea094c291a5df1987ae8af8","u1e812bcfc29ed4d9eae95a64a59b9568","uf2d5b9d84cc7c573804c4869099cc807","u4f97f7fee3126f6524013e40a1019628","u78a739fab94aef6094b2e1f9b4d85f87","u5add75c7cb29a76635dce138334e7475"])
                                except:
                                    pass
                                    
                        elif cmd == "antijs join":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, ["u4a13cbe7471c74870ac828ef50ef1f1a","ua1fab51153eb593a6c9b3496ba6c5e72"])
                                    g1.acceptGroupInvitation(msg.to)
                                    g2.acceptGroupInvitation(msg.to)
                                except:
                                    pass
                                    
                        elif cmd == "antijs out":
                            if msg._from in admin:
                                g1.leaveGroup(msg.to)
                                g2.leaveGroup(msg.to)
								
                        elif cmd == "antijs stay":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, ["u4a13cbe7471c74870ac828ef50ef1f1a","ua1fab51153eb593a6c9b3496ba6c5e72"])
                                    data = {"type": "text","text": "Group 「"+str(ginfo.name)+"」 \n\nAman dari Bypass \napalagi JS murahan","sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                                    cl.postTemplate(to, data)
                                except:
                                    pass
                                    
                        elif cmd == "ghost join":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, ["u0f13117cf1e1444cd8cdc2ae87d9f050"])
                                    g3.acceptGroupInvitation(msg.to)
                                except:
                                    pass
                                    
                        elif cmd == "ghost out":
                            if msg._from in admin:
                                g3.leaveGroup(msg.to)
								
#_________________________________________________     
    
                        elif cmd.startswith("broadcast: "):
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group," " + str(pesan))
                                   
                        elif cmd.startswith("block"):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.blockContact(ls)
                                cl.generateReplyMessage(msg.id)
                                cl.sendReplyMessage(msg_id, to, "sᴜᴋsᴇs ʙʟᴏᴄᴋ ᴋᴏɴᴛᴀᴋ" + str(contact.displayName) + "ᴍᴀsᴜᴋ ᴅᴀғᴛᴀʀ ʙʟᴏᴄᴋʟɪsᴛ")

                        elif "Mid " in msg.text:
                            if 'MENTION' in msg.contentMetadata.keys() != None:
                                names = re.findall(r'@(\w+)', msg.text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    try:
                                        cl.sendReplyMessage(msg_id, to,str(mention['M']))
                                    except Exception as e:
                                        pass

                        elif cmd == "rechat":
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   cl.sendReplyMessage(msg_id, to,"Sampah group hilang")
                               except:
                                   pass

                        elif cmd == "/restart":
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendReplyMessage(msg_id, to, "ʀᴇsᴛᴀʀᴛ ʙᴏᴛ")
                               wait["restartPoint"] = msg.to
                               restartBot()
                               cl.sendReplyMessage(msg_id, to, "Success")
                               
                        elif cmd == "ginfo":
                            group = cl.getGroup(to)
                            try:
                                gCreator = group.creator.displayName
                            except:
                                gCreator = "Tidak ditemukan"
                            if group.invitee is None:
                                gPending = "0"
                            else:
                                gPending = str(len(group.invitee))
                            if group.preventedJoinByTicket == True:
                                gQr = "Tertutup"
                                gTicket = "Tidak ada"
                            else:
                                gQr = "Terbuka"
                                gTicket = "https://cl.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                            path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            ret_ = "╔═════[ Group Info ]═══════"
                            ret_ += "\n╠ ☛ Nama Group : {}".format(str(group.name))
                            ret_ += "\n╠ ☛ ID Group : {}".format(group.id)
                            ret_ += "\n╠ ☛ Pembuat : {}".format(str(gCreator))
                            ret_ += "\n╠ ☛ Jumlah Member : {}".format(str(len(group.members)))
                            ret_ += "\n╠ ☛ Jumlah Pending : {}".format(gPending)
                            ret_ += "\n╠ ☛ Group Qr : {}".format(gQr)
                            ret_ += "\n╠ ☛ Group Ticket : {}".format(gTicket)
                            ret_ += "\n╚══════════════════════════"
                            cl.sendMessage(to, str(ret_))
                            cl.sendImageWithURL(to, path)

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +cl.getGroup(group).name + "\n"      
                                cl.sendReplyMessage(msg_id,to,"• PROTECTION •\n\n• PROTECT QR :\n"+ma+"\n• PROTECT KICK :\n"+mb+"\n• PROTECT JOIN :\n"+md+"\n• PROTECT CANCEL:\n"+mc+"\n• PROTECT INVITE :\n"+me+"\nTotal「%s」Protect" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectinvite))))

                        elif cmd == "listpending":
                            if msg.toType == 2:
                                group = cl.getGroup(to)
                                ret_ = "╭───「 Pending List 」"
                                no = 0
                                if group.invitee is None or group.invitee == []:
                                    return cl.sendReplyMessage(msg_id, to, "Tidak ada pendingan")
                                else:
                                    for pending in group.invitee:
                                        no += 1
                                        ret_ += "\n├≽ {}. {}".format(str(no), str(pending.displayName))
                                    ret_ += "\n╰───「 Total {} Pending 」".format(str(len(group.invitee)))
                                    data = {"type": "text","text": "{}".format(str(ret_)),"sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                                    cl.postTemplate(to, data)

                        elif cmd.startswith("dellfriend "):
                              if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        cl.deleteContact(ls)
                                        cl.sendReplyMessage(msg_id, to, "Success")

                        elif cmd == "listmember":
                          if msg._from in admin:
                            if msg.toType == 2:
                                group = cl.getGroup(to)
                                num = 0
                                ret_ = "╭──「 List member 」"
                                for contact in group.members:
                                    num += 1
                                    ret_ += "\n├ {}. {}".format(num, contact.displayName)
                                ret_ += "\n╰──「 Total {} member 」".format(len(group.members))
                                cl.sendReplyMessage(msg_id, to, str(ret_))

                        elif cmd == "friendlist":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.displayName+ "\n"
                               cl.sendReplyMessage(msg_id, to,"    [ FRIEND LIST ]\n\n"+ma+"\n    [ Total「"+str(len(gid))+"」Friends ]")
                               

                        elif cmd == "gruplist":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "●" + str(a) + ". " +G.name+ "\n"
                               cl.sendReplyMessage(msg_id, to,"    ● GROUP LIST ●\n●\n"+ma+"\n    ●Total "+str(len(gid))+" Groups ●")

                        elif cmd == "gurl":
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                gurl = cl.reissueGroupTicket(msg.to)
                                cl.sendReplyMessage(msg_id, to,"line://ti/g/" + gurl)

                        elif cmd == "open qr":
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   if X.preventedJoinByTicket == True:
                                       X.preventedJoinByTicket = False
                                       cl.updateGroup(X)
                                gurl = cl.reissueGroupTicket(msg.to)
                                cl.sendReplyMessage(msg_id, to, "Nama : "+str(X.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

                        elif cmd == "close qr":
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendReplyMessage(msg_id, to, "Url Closed")

                        elif cmd == "reject":
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      cl.rejectGroupInvitation(gid)
                                  cl.sendReplyMessage(msg_id, to, "ᴛᴏᴛᴀʟ {} ɢʀᴏᴜᴘ".format(str(len(ginvited))))
                              else:
                                  cl.sendReplyMessage(msg_id, to, "Success")
#______________________________________________
                        elif cmd == "updategrup":
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendReplyMessage(msg_id, to,"Send gambarnya")

                        elif cmd == "updatefoto":
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                                Foto["foto"][MySelf.mid] = True
                                cl.sendReplyMessage(msg_id, to,"Kirim fhotomu yg kece")
                        elif cmd.startswith("updatename: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendReplyMessage(msg_id, to,"Nama diganti jadi " + string + "")
                         
                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  data = {"type": "text","text": "sIder ᴍᴏᴅᴇ ᴏɴ ʙᴏs","sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                                  cl.postTemplate(to, data)
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendReplyMessage(msg_id, to, "sIder ᴍᴏᴅᴇ ᴏғғ ʙᴏs")
                              else:
                                  cl.sendReplyMessage(msg_id, to, "sIder ᴍᴏᴅᴇ ᴏғғ ʙᴏs")
#____________________________________________
                        if text.lower() == "tagnote":
                            if msg._from in admin:
                                NoteCreate(to,cmd,msg)
                        elif msg.text.lower().startswith("tagremot: "):
                            	separate = msg.text.split(":")
                            	number = msg.text.replace(separate[0] + ":"," ")
                            	groups = cl.getGroupIdsJoined()
                            	gid = groups[int(number)-1]                                                            
                            	group = cl.getGroup(gid)                                                            
                            	nama = [contact.mid for contact in group.members]
                            	k = len(nama)//19
                    	        for a in range(k+1):
                            		txt = u''
                    		        s=0
                            		b=[]
                            		for i in group.members[a*19 : (a+1)*19]:
                            			b.append(i.mid)
                            		mentionMembers(gid, b)                            
                    		        cl.sendReplyMessage(msg_id, to, "Berhasil Mention Member di Group: \n " + str(group.name))
                        elif cmd == "tagall":
                               if msg._from in admin:
                                try:group = cl.getGroup(to);midMembers = [contact.mid for contact in group.members]
                                except:group = cl.getRoom(to);midMembers = [contact.mid for contact in group.contacts]
                                midSelect = len(midMembers)//20
                                for mentionMembers in range(midSelect+1):
                                    no = 0
                                    ret_ = "╭Mention member"
                                    dataMid = []
                                    if msg.toType == 2:
                                        for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                            dataMid.append(dataMention.mid)
                                            no += 1
                                            ret_ += "\n"+"├ {}. @!".format(str(no))
                                        ret_ += "\n╰ᴛᴏᴛᴀʟ: {} \n".format(str(len(dataMid)))
                                        cl.sendReplyMention(msg_id, to, ret_, dataMid)
                                    else:
                                        for dataMention in group.contacts[mentionMembers*20 : (mentionMembers+1)*20]:
                                            dataMid.append(dataMention.mid)
                                            no += 1
                                            ret_ += "\n"+"{}. @!".format(str(no))
                                        ret_ += "\n➢ᴛᴏᴛᴀʟ: {}\n".format(str(len(dataMid)))
                                        cl.sendReplyMention(msg_id, to, ret_, dataMid)
                              
                        elif cmd == "sp" or cmd == "speed":
                          if wait["selfbot"] == True:
                            if msg._from in admin:                              
                               start = time.time()
                               time.sleep(0.001)
                               get_profile_time_start = time.time()
                               get_profile = cl.getProfile()
                               get_profile_time = time.time() - get_profile_time_start
                               cl.sendMessage(msg.to, "ᴛɪᴍᴇ :\n「%.5f」sᴇᴄᴏɴᴅs" % (get_profile_time/3))                   
                               start = time.time()
                               time.sleep(0.001)
                               get_profile_time_start = time.time()
                               get_profile = g1.getProfile()
                               get_profile_time = time.time() - get_profile_time_start
                               g1.sendMessage(msg.to, "ᴛɪᴍᴇ :\n「%.5f」sᴇᴄᴏɴᴅs" % (get_profile_time/3))                  
                               start = time.time()
                               time.sleep(0.001)
                               get_profile_time_start = time.time()
                               get_profile = g2.getProfile()
                               get_profile_time = time.time() - get_profile_time_start
                               g2.sendMessage(msg.to, "ᴛɪᴍᴇ :\n「%.5f」sᴇᴄᴏɴᴅs" % (get_profile_time/3))                  
                               start = time.time()
                               time.sleep(0.001)
                               get_profile_time_start = time.time()
                               get_profile = g3.getProfile()
                               get_profile_time = time.time() - get_profile_time_start
                               g3.sendMessage(msg.to, "ᴛɪᴍᴇ :\n「%.5f」sᴇᴄᴏɴᴅs" % (get_profile_time/3))
                        
                        elif cmd == "unsend ":
                          if msg._from in admin:
                            sep = text.split(" ")
                            args = text.replace(sep[0] + " ","")
                            ttl = "「UNSEND」"
                            mes = int(sep[1])
                            M = cl.getRecentMessageV2(to, 1001)
                            MId = []
                            for ind,i in enumerate(M):
                                if ind == 0:
                                    pass
                                else:
                                    if i._from == cl.profile.mid:
                                        MId.append(i.id)
                                        if len(MId) == mes:
                                            break
                            def unsMes(id):
                                cl.unsendMessage(id)
                            for i in MId:
                                thread1 = threading.Thread(target=unsMes, args=(i,))
                                thread1.daemon = True
                                thread1.start()
                                thread1.join()
                                
                        elif cmd == "call on" or text.lower() == 'notifcall on':
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["nCall"] = True                          
                                cl.sendReplyMessage(msg_id, to, "Detectcall on")

                        elif cmd == "call off" or text.lower() == 'notifcall off':
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["nCall"] = False
                                cl.sendReplyMessage(msg_id, to,"Detectcall off")
                                
#_______________________[   COMMAND PROTECT   ]
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendReplyMessage(msg_id, to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    cl.sendReplyMessage(msg_id, to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectqr ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectqr ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "ᴘʀᴏᴛᴇᴄᴛ Qʀ ʜᴀꜱ ʙᴇɴ ᴀᴄᴛɪᴠᴇ"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "ᴘʀᴏᴛᴇᴄᴛ Qʀ ʜᴀꜱ ʙᴇɴ ᴀᴄᴛɪᴠᴇ\n\nɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  data = {"type": "text","text": "{}".format(str(msgs)),"sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                                  cl.postTemplate(to, data)
                             #     cl.sendMessage(msg.to, "「STATUS PROTECT URL」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ᴘʀᴏᴛᴇᴄᴛ Qʀ ʜᴀꜱ ʙᴇɴ ᴏꜰꜰ\n\nɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = "ᴘʀᴏᴛᴇᴄᴛ Qʀ ʜᴀꜱ ʙᴇɴ ᴏꜰꜰ"
                                    data = {"type": "text","text": "{}".format(str(msgs)),"sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                                    cl.postTemplate(to, data)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "ᴘʀᴏᴛᴇᴄᴛ ᴋɪᴄᴋ ʜᴀꜱ ʙᴇᴇɴ ᴀᴄᴛɪᴠᴇ  : " +str(ginfo.name)
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "ᴘʀᴏᴛᴇᴄᴛ ᴋɪᴄᴋ ʜᴀꜱ ʙᴇᴇɴ ᴀᴄᴛɪᴠᴇ \n\nɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  data = {"type": "text","text": "{}".format(str(msgs)),"sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                                  cl.postTemplate(to, data)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ᴘʀᴏᴛᴇᴄᴛ ᴋɪᴄᴋ ʜᴀꜱ ʙᴇᴇɴ ᴏꜰꜰ \n\nɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = "ᴘʀᴏᴛᴇᴄᴛ ᴋɪᴄᴋ ʜᴀꜱ ʙᴇᴇɴ ᴏꜰꜰ "
                                    data = {"type": "text","text": "{}".format(str(msgs)),"sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                                    cl.postTemplate(to, data)

                        elif 'Protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "ᴘʀᴏᴛᴇᴄᴛ ᴊᴏɪɴ ʜᴀꜱ ʙᴇᴇɴ ᴀᴄᴛɪᴠᴇ"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "ᴘʀᴏᴛᴇᴄᴛ ᴊᴏɪɴ ʜᴀꜱ ʙᴇᴇɴ ᴀᴄᴛɪᴠᴇ \n\nɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  data = {"type": "text","text": "{}".format(str(msgs)),"sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                                  cl.postTemplate(to, data)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ᴘʀᴏᴛᴇᴄᴛ ᴊᴏɪɴ ʜᴀꜱ ʙᴇᴇɴ ᴏꜰꜰ \n\nɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = "ᴘʀᴏᴛᴇᴄᴛ ᴊᴏɪɴ ʜᴀꜱ ʙᴇᴇɴ ᴏꜰꜰ "
                                    data = {"type": "text","text": "{}".format(str(msgs)),"sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                                    cl.postTemplate(to, data)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ ʜᴀꜱ ʙᴇᴇɴ ᴀᴄᴛɪᴠᴇ"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ ʜᴀꜱ ʙᴇᴇɴ ᴀᴄᴛɪᴠᴇ\n\nɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  data = {"type": "text","text": "{}".format(str(msgs)),"sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                                  cl.postTemplate(to, data)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ ʜᴀꜱ ʙᴇᴇɴ ᴏꜰꜰ\n\nɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = "ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ ʜᴀꜱ ʙᴇᴇɴ ᴏꜰꜰ"
                                    data = {"type": "text","text": "{}".format(str(msgs)),"sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                                    cl.postTemplate(to, data)
                                    
                        elif 'Protectinvite ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectinvite ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ ʜᴀꜱ ʙᴇᴇɴ ᴀᴄᴛɪᴠᴇ"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ ʜᴀꜱ ʙᴇᴇɴ ᴀᴄᴛɪᴠᴇ\n\nɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  data = {"type": "text","text": "{}".format(str(msgs)),"sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                                  cl.postTemplate(to, data)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ ʜᴀꜱ ʙᴇᴇɴ ᴏꜰꜰ\n\nɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = "ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ ʜᴀꜱ ʙᴇᴇɴ ᴏꜰꜰ"
                                    data = {"type": "text","text": "{}".format(str(msgs)),"sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                                    cl.postTemplate(to, data)

                        elif 'Antijs/bypass ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Antijs/bypass ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "ᴘʀᴏᴛᴇᴄᴛ ᴀɴᴛɪᴊꜱ ʜᴀꜱ ʙᴇᴇɴ ᴀᴄᴛɪᴠᴇ"
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "ᴘʀᴏᴛᴇᴄᴛ ᴀɴᴛɪᴊꜱ ʜᴀꜱ ʙᴇᴇɴ ᴀᴄᴛɪᴠᴇ\n\nɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  data = {"type": "text","text": "{}".format(str(msgs)),"sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                                  cl.postTemplate(to, data)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ᴘʀᴏᴛᴇᴄᴛ ᴀɴᴛɪᴊꜱ ʜᴀꜱ ʙᴇᴇɴ ᴏꜰꜰ\n\nɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = "ᴘʀᴏᴛᴇᴄᴛ ᴀɴᴛɪᴊꜱ ʜᴀꜱ ʙᴇᴇɴ ᴏꜰꜰ"
                                    data = {"type": "text","text": "{}".format(str(msgs)),"sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                                    cl.postTemplate(to, data)
                                    
                        elif 'Ghost ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ghost ','')
                              if spl == 'on':
                                  if msg.to in ghost:
                                       msgs = "ᴘʀᴏᴛᴇᴄᴛ ɢʜᴏꜱᴛ ʜᴀꜱ ʙᴇᴇɴ ᴀᴄᴛɪᴠᴇ"
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "ᴘʀᴏᴛᴇᴄᴛ ɢʜᴏꜱᴛ ʜᴀꜱ ʙᴇᴇɴ ᴀᴄᴛɪᴠᴇ\n\nɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  data = {"type": "text","text": "{}".format(str(msgs)),"sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                                  cl.postTemplate(to, data)
                              elif spl == 'off':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ᴘʀᴏᴛᴇᴄᴛ ɢʜᴏꜱᴛ ʜᴀꜱ ʙᴇᴇɴ ᴏꜰꜰ\n\nɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = "ᴘʀᴏᴛᴇᴄᴛ ɢʜᴏꜱᴛ ʜᴀꜱ ʙᴇᴇɴ ᴏꜰꜰ"
                                    data = {"type": "text","text": "{}".format(str(msgs)),"sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                                    cl.postTemplate(to, data)

                        elif 'Allprotect ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Allprotect ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)                                      
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "ᴀʟʟᴘʀᴏᴛᴇᴄᴛɪᴏɴ ʜᴀꜱ ʙᴇᴇɴ ᴀᴄᴛɪᴠᴇ"
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "ᴀʟʟᴘʀᴏᴛᴇᴄᴛɪᴏɴ ʜᴀꜱ ʙᴇᴇɴ ᴀᴄᴛɪᴠᴇ\n\nɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  data = {"type": "text","text": "{}".format(str(msgs)),"sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                                  cl.postTemplate(to, data)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""                                         
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:		 
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ᴀʟʟᴘʀᴏᴛᴇᴄᴛɪᴏɴ ʜᴀꜱ ʙᴇᴇɴ ᴏꜰꜰ"
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ᴀʟʟᴘʀᴏᴛᴇᴄᴛɪᴏɴ ʜᴀꜱ ʙᴇᴇɴ ᴏꜰꜰ\n\nɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    data = {"type": "text","text": "{}".format(str(msgs)),"sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                                    cl.postTemplate(to, data)

#===========KICKOUT============#
                        elif ("Dor" in msg.text):
                          # if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in admin:
                                       try:
                                       	cl.kickoutFromGroup(msg.to,[target])
                                       except:
                                           cl.sendReplyMessage(msg_id, to,"Sorry kamu jelek !!!")
#=========COMEN RESPON======#
                        elif msg.text in ["invite"]:
                            if msg._from in admin:
                                wait["invite"] = True
                                cl.sendReplyMessage(msg_id, to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
                        elif cmd == "respon on" or text.lower() == 'respon on':
                          # if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                cl.sendReplyMessage(msg_id, to,"ᴀᴜᴛᴏʀᴇsᴘᴏɴ ᴏɴ")
                        elif cmd == "respon off" or text.lower() == 'respon off':
                          # if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                cl.sendReplyMessage(msg_id, to,"ᴀᴜᴛᴏʀᴇsᴘᴏɴ ᴏғғ")
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          # if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                cl.sendReplyMessage(msg_id, to,"ʀᴇsᴘᴏɴᴛᴀɢ ᴋɪᴄᴋ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "notag off" or text.lower() == 'notag off':
                          # if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = False
                                cl.sendReplyMessage(msg_id, to,"ʀᴇsᴘᴏɴᴛᴀɢ ᴋɪᴄᴋ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          # if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autojoin"] = True
                                cl.sendReplyMessage(msg_id, to,"ᴀᴜᴛᴏᴊᴏɪɴ ɢʀᴏᴜᴘ ᴏɴ")
                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          # if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autojoin"] = False
                                cl.sendReplyMessage(msg_id, to,"ᴀᴜᴛᴏᴊᴏɪɴ ɢʀᴏᴜᴘ ᴏғғ")
                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          # if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                cl.sendReplyMessage(msg_id, to,"ᴀᴜᴛᴏʟᴇᴀᴠᴇ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          # if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                cl.sendReplyMessage(msg_id, to,"ᴀᴜᴛᴏʟᴇᴀᴠᴇ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          # if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                cl.sendReplyMessage(msg_id, to,"ᴀᴜᴛᴏ ᴀᴅᴅ ᴏn")
                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          # if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                cl.sendReplyMessage(msg_id, to,"ᴀᴜᴛᴏ ᴀᴅᴅ ᴏғғ")
                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          # if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                cl.sendReplyMessage(msg_id, to,"ᴊᴏɪɴᴛɪᴄᴋᴇᴛ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          # if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = False
                                cl.sendReplyMessage(msg_id, to,"ᴊᴏɪɴᴛɪᴄᴋᴇᴛ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "autoblock on" or text.lower() == 'autoblock on':
                          # if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = True
                                cl.sendReplyMessage(msg_id, to,"ʙʟᴏᴄᴋ ᴄᴏɴᴛᴀᴄᴛ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "autoblock off" or text.lower() == 'autoblock off':
                          # if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = False
                                cl.sendReplyMessage(msg_id, to,"ʙʟᴏᴄᴋ ᴄᴏɴᴛᴀᴄᴛ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "post on" or text.lower() == 'post on':
                          # if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["checkPost"] = True
                                cl.sendReplyMessage(msg_id, to,"ᴀᴜᴛᴏ ᴘᴏsᴛ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "post off" or text.lower() == 'post off':
                          # if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["checkPost"] = False
                                cl.sendReplyMessage(msg_id, to,"ᴀᴜᴛᴏ ᴘᴏsᴛ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "like on" or text.lower() == 'like on':
                          # if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["likeon"] = True
                                cl.sendReplyMessage(msg_id, to,"ʟɪᴋᴇ ᴘᴏsᴛ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "like off" or text.lower() == 'like off':
                          # if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["likeon"] = False
                                cl.sendReplyMessage(msg_id, to,"ʟɪᴋᴇ ᴘᴏsᴛ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "invite on" or text.lower() == 'invite on':
                          # if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = True
                                cl.sendReplyMessage(msg_id, to, "ᴋɪʀɪᴍ ᴋᴏɴᴛᴀᴋ'ɴʏᴀ")
                        elif cmd == "invite off" or text.lower() == 'invite off':
                          # if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = False
                                cl.sendReplyMessage(msg_id, to,"ɪɴᴠɪᴛᴇ ᴠɪᴀ ᴄᴏɴᴛᴀᴄᴛ ᴏɴ")
                        if cmd == "unsend on":
                            if msg._from in admin:
                                wait["DetectUnsend"] = True
                                cl.sendReplyMessage(msg_id, to, "Unsend message mode on")
                        if cmd == "unsend off":
                            if msg._from in admin:
                                wait["DetectUnsend"] = False
                                cl.sendReplyMessage(msg_id, to, "Unsend message mode off")
                                
                        elif cmd == "screen vps":
                            if msg._from in admin:
                                proses = os.popen("screen -list")
                                a = proses.read()
                                cl.sendMessage(to, "{}".format(str(a)))
                                proses.close()
                                
                        elif "https://www.smule.com" in msg.text.lower():
                            if wait["nSmule"] == True:
                                nm = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
                                nm1 = re.findall(nm, text)
                                nm2 = []
                                for nm3 in nm1:
                                    if nm3 not in nm2:
                                        nm2.append(nm3)
                                for nm4 in nm2:
                                    nm5 = nm4
                                    nmBots = "f6Ai8rmEJOEB"
                                    headers = {
                                        "apiKey":nmBots,
                                        }
                                    master = json.loads(requests.get("https://api.be-team.me/smule?url="+nm5,headers=headers).text)
                                    ret="╭──「 NOTIF SMULE 」─────"
                                    ret+="\n├ Artis : " +master["result"]["artist"]
                                    ret+="\n├ Judul : " +master["result"]["title"]
                                    ret+="\n├ ID Smule : " +master["result"]["owner"]["handle"]
                                    ret+="\n├ Status :  " +master["result"]["message"]
                                    ret+="\n╰──「 Wait Video Nya 」─────"
                                    data = {"type": "text","text": "{}".format(ret),"sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                                    cl.postTemplate(to, data)
                              #      cl.sendReplyMessage(msg_id, to, ret)
                                    cl.sendAudioWithURL(msg.to, master["result"]["download_link"])
                                    cl.sendVideoWithURL(msg.to, master["result"]["download_link"])
                                
                        elif cmd == "autoread on":
                            if msg._from in admin:
                                if settings["autoRead"] == True:
                                    cl.sendReplyMessage(msg_id, to, "Auto read telah aktif")
                                else:
                                    settings["autoRead"] = True
                                    cl.sendReplyMessage(msg_id, to, "Berhasil mengaktifkan auto read")

                        elif cmd == "autoread off":
                            if msg._from in admin:
                                if settings["autoRead"] == False:
                                    cl.sendReplyMessage(msg_id, to, "Auto read telah nonaktif")
                                else:
                                    settings["autoRead"] = False
                                    cl.sendReplyMessage(msg_id, to, "Berhasil menonaktifkan auto read")
                        elif cmd.startswith("setcomment: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    wait["comment"] = txt
                                    cl.sendReplyMessage(msg_id, to, "Done Mengubah Pesan\n❂CommentTL:\n❂ {}".format(txt))
                                except:
                                    cl.sendReplyMessage(msg_id, to, "Failed")
                        elif cmd == "refresh":
                            if msg._from in admin:
                                wait["wBlacklist"] = False
                                wait["dBlacklist"] = False
                                wait["TalkwBlacklist"] = False
                                wait["TalkdBlacklist"] = False
                          #      cl.sendReplyMessage(msg_id, to,"Clean..")
                                cl.sendReplyMessage(msg_id, to,"Refresh done")
#===========ADMIN ADD============#
                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           #admin.append(target)
                                           admin[target] = True
                                           f=codecs.open('datamin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
                                           cl.sendMessage(msg.to,"Success Add admin")
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                  # if target not in admin:
                                       try:
                                           #admin.remove(target)
                                           del admin[target]
                                           f=codecs.open('datamin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
                                           cl.sendMessage(msg.to,"Success dell admin")
                                       except:
                                           pass

                        elif ("Ban " in msg.text):
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Blacklist"][target] = True
                                           cl.sendReplyMessage(msg_id, to,"✅Berhasil menambahkan Blacklist")
                                       except:
                                           pass
                        elif ("Unban " in msg.text):
                          # if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Blacklist"][target]
                                           cl.sendReplyMessage(msg_id, to,"✅Berhasil menghapus Blacklist")
                                       except:
                                           pass
                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wBlacklist"] = True
                                cl.sendReplyMessage(msg_id, to, "Kirim Contaknya...")
                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dBlacklist"] = True
                                cl.sendReplyMessage(msg_id, to, "Kirim Contaknya...")
                        elif cmd == "banlist" or text.lower() == 'banlist':
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Blacklist"] == {}:
                                cl.sendReplyMessage(msg_id, to,"Tak ada daftar buronan")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendReplyMessage(msg_id, to,"Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["Blacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Blacklist"] == {}:
                                    cl.sendMessage(msg.to,"⚪ ɴᴏ ᴜsᴇʀs ᴀʀᴇ ʙʟᴀᴄᴋʟɪsᴛ")
                              else:
                                    ma = ""
                                    for i in wait["Blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "cb" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["Blacklist"] = {}
                              ragets = cl.getContacts(wait["Blacklist"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              cl.sendMessage(msg.to,"⚪  Sampah Berhasil di Hapus ✅")
                              
#==========Setting bot========
                        elif 'Set hapus: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set hapus: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendReplyMessage(msg_id, to, "Gagal mengganti Pesan clear")
                              else:
                                  wait["clear"] = spl
                                  cl.sendReplyMessage(msg_id, to, "「clear」\clearl diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set tagall: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set tagall: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendReplyMessage(msg_id, to, "Gagal mengganti Pesan Tagall")
                              else:
                                  wait["tagall"] = spl
                                  cl.sendReplyMessage(msg_id, to, "「tagall」\nTagall diganti jadi :\n\n「{}」".format(str(spl))) 
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendReplyMessage(msg_id, to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  cl.sendReplyMessage(msg_id, to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendReplyMessage(msg_id, to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  cl.sendReplyMessage(msg_id, to, "「Welcome Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))
                                  
                        elif 'Set autoleave: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set autoleave: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendReplyMessage(msg_id, to, "Gagal mengganti Autoleave Msg")
                              else:
                                  wait["autoLave"] = spl
                                  cl.sendReplyMessage(msg_id, to, "「Autoleave Msg」\nAutoleave Msg diganti jadi :\n\n「{}」".format(str(spl)))
                                  
                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendReplyMessage(msg_id, to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  cl.sendReplyMessage(msg_id, to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendReplyMessage(msg_id, to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  cl.sendReplyMessage(msg_id, to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               cl.sendReplyMessage(msg_id, to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")
                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               cl.sendReplyMessage(msg_id, to, "「Welcome Msg」\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")
                        elif text.lower() == "cek leave":
                            if msg._from in admin:
                               cl.sendReplyMessage(msg_id, to, "「Autoleave Msg」\nAutoleave Msg mu :\n\n「 " + str(wait["autoleave"]) + " 」")
                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               cl.sendReplyMessage(msg_id, to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")
                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               cl.sendReplyMessage(msg_id, to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")
                        elif cmd == "me" or text.lower() == 'me':                            	
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                status = cl.getContact(sender)                   
                                cover = cl.getProfileCoverURL(sender)                             
                                data = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(msg._from).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(cl.getContact(sender).displayName),
                    "size": "xxs",
                    "color": "#ffffff",
                    "wrap": True,
                    "offsetStart": "10px"
                  }
                ],
                "height": "17px",
                "offsetTop": "-17px",
                "offsetStart": "18px"
              }
            ],
            "position": "absolute",
            "offsetStart": "2px",
            "offsetEnd": "0px",
            "paddingAll": "20px",
            "paddingTop": "18px",        
            "borderColor": "#ffffff",
            "cornerRadius": "10px",
            "width": "145px",
            "height": "25px",
            "offsetTop": "142px",        
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "PROFILE",
                "color": "#ffffff",
                "align": "center",
                "size": "xxs",
                "offsetTop": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "2px",      
            "offsetStart": "2px",
            "height": "25px",
            "width": "53px",
            "borderWidth": "3px",    
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "    NM BOTS",
                "size": "xxs",
                "color": "#ffffff",
                "style": "normal",
                "weight": "bold",
                "offsetTop": "3px",
                "offsetStart": "7px"
              }
            ],
            "position": "absolute",
            "width": "103px",
            "height": "27px",
            "backgroundColor": "#3366ff",
            "offsetTop": "160px",
            "offsetStart": "40px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/2PBHBRY/Cropped-image-20201030-221042-3427731946386620016.png",
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "45px",
            "height": "45px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "10px",
            "offsetTop": "143px",
            "offsetStart": "2px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "4px",
        "borderColor": "#3300cc",
        "cornerRadius": "10px",
        "height": "200px"      
      }
    },
    {      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": str(cl.getProfileCoverURL(sender)),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(cl.getContact(sender).displayName),
                    "size": "xxs",
                    "color": "#ffffff",
                    "wrap": True,
                    "offsetStart": "10px"
                  }
                ],
                "height": "17px",
                "offsetTop": "-17px",
                "offsetStart": "18px"
              }
            ],
            "position": "absolute",
            "offsetStart": "2px",
            "offsetEnd": "0px",
            "paddingAll": "20px",
            "paddingTop": "18px",        
            "borderColor": "#ffffff",
            "cornerRadius": "10px",
            "width": "145px",
            "height": "25px",
            "offsetTop": "142px",        
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "COVER",
                "color": "#ffffff",
                "align": "center",
                "size": "xxs",
                "offsetTop": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "2px",      
            "offsetStart": "2px",
            "height": "25px",
            "width": "53px",
            "borderWidth": "3px",    
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "    NM BOTS",
                "size": "xxs",
                "color": "#ffffff",
                "style": "normal",
                "weight": "bold",
                "offsetTop": "3px",
                "offsetStart": "7px"
              }
            ],
            "position": "absolute",
            "width": "103px",
            "height": "27px",
            "backgroundColor": "#3366ff",
            "offsetTop": "160px",
            "offsetStart": "40px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/2PBHBRY/Cropped-image-20201030-221042-3427731946386620016.png",
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "45px",
            "height": "45px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "10px",
            "offsetTop": "143px",
            "offsetStart": "2px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "4px",
        "borderColor": "#3300cc",
        "cornerRadius": "10px",
        "height": "200px"      
      }
    },
    {      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(cl.getContact(sender).displayName),
                    "size": "xxs",
                    "color": "#ffffff",
                    "wrap": True,
                    "offsetStart": "10px"
                  }
                ],
                "height": "17px",
                "offsetTop": "-17px",
                "offsetStart": "18px"
              }
            ],
            "position": "absolute",
            "offsetStart": "2px",
            "offsetEnd": "0px",
            "paddingAll": "20px",
            "paddingTop": "18px",        
            "borderColor": "#ffffff",
            "cornerRadius": "10px",
            "width": "145px",
            "height": "25px",
            "offsetTop": "142px",        
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "PROFILE",
                "color": "#ffffff",
                "align": "center",
                "size": "xxs",
                "offsetTop": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "2px",      
            "offsetStart": "2px",
            "height": "25px",
            "width": "53px",
            "borderWidth": "3px",    
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "    NM BOTS",
                "size": "xxs",
                "color": "#ffffff",
                "style": "normal",
                "weight": "bold",
                "offsetTop": "3px",
                "offsetStart": "7px"
              }
            ],
            "position": "absolute",
            "width": "103px",
            "height": "27px",
            "backgroundColor": "#3366ff",
            "offsetTop": "160px",
            "offsetStart": "40px",
            "borderWidth": "1px",
            "borderColor": "#3300cc",
            "cornerRadius": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/2PBHBRY/Cropped-image-20201030-221042-3427731946386620016.png",
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "45px",
            "height": "45px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "10px",
            "offsetTop": "143px",
            "offsetStart": "2px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "4px",
        "borderColor": "#3300cc",
        "cornerRadius": "10px",
        "height": "200px"      
      }
      }
  ]
}
                                cl.postFlex(to, data)

                        
                        elif cmd == "pictmember":
                              if msg._from in admin:
                                  kontak = cl.getGroup(to)
                                  group = kontak.members
                                  picall = []
                                  for ids in group:
                                    if len(picall) >= 400:
                                      pass
                                    else:
                                      picall.append({
                                        "imageUrl": "https://os.line.naver.jp/os/p/{}".format(ids.mid),
                                        "action": {
                                          "type": "uri",
                                          "uri": "http://line.me/ti/p/~afr1z4l"
                                          }
                                        }
                                      )
                                  k = len(picall)//10
                                  for aa in range(k+1):
                                    data = {
                                      "type": "template",
                                      "altText": "{} Bagi2 sembako".format(cl.getProfile().displayName),
                                      "template": {
                                        "type": "image_carousel",
                                        "columns": picall[aa*10 : (aa+1)*10]
                                      }
                                    }
                                    cl.postTemplate(to, data)

                        elif "Mid" in msg.text:
                	         if msg._from in admin:
                	             nk0 = msg.text.replace("aku dikick","")
                	             nk1 = nk0.lstrip()
                	             nk2 = nk1.replace("","")
                	             nk3 = nk2.rstrip()
                	             _name = nk3
                	             gs = cl.getGroup(msg.to)
                	             Bl = []
                	             for s in gs.members:
                	                 if _name in s.displayName:
                	              #      if s.mid not in whiteListedMid and s.mid not in whiteListedMid:
                	                        wait["Blacklist"].append(s.mid)
                	                        Bl.append(s.mid)
                	             wait["tempat"] = False
                	             Kibar.append(msg.to)
                	             sleding = Thread(target=tium2, args=(msg.to, wait["Blacklist"]))
                	             sleding.start()
                	             cl.sendMessage(msg.to,"knpa")
                
                        elif "/ti/g/" in msg.text.lower():
                           if wait["selfbot"] == True:
                            if msg._from in whiteListedMid or msg._from in admin:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     data = {"type": "text","text": "Masuk : {}".format(str(group.name)),"sentBy": {"label": "ɴɪɢʜᴛ ᴍᴀꜱᴛᴇʀ ʙᴏᴛꜱ","iconUrl": "https://i.ibb.co/0sQzJ0h/YOXO.gif","linkUrl": "line://nv/profilePopup/mid=u4c80dab0a85206b0f7c4153e0cdb8a21"}}
                                     cl.postTemplate(to, data)
                                   
    except Exception as error:
        print (error)
        
while True:
	try:
		ops = oepoll.singleTrace(count=50)
		if ops != None:
			for op in ops:
				oepoll.setRevision(op.revision)
				flashbot = threading.Thread(target=lineBot, args=(op,))
				flashbot.deamon = True
				flashbot.start()
				
	except Exception as e:
		print (e)
YoutubeSearch()
