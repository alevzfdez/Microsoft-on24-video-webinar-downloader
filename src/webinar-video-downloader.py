#!/bin/python3


######################################################################################
# 0. Set-up environment
######################################################################################
import os, sys
import argparse, requests, youtube_dl, json, unicodedata, re
from dateutil.parser import parse
from urllib.parse import urlparse, parse_qs


######################################################################################
# 1. Functions definition
######################################################################################
def load_argparse():
  # Set arguments to be parsed
  parser = argparse.ArgumentParser(description='Microsoft Webinar video downloader from mpd - v1.0')
  group = parser.add_mutually_exclusive_group(required=True)
  group.add_argument('--url', '-u', dest='url',  
                      help='Webinar URL from where to scrap info and download video')
  group.add_argument('--file', '-f', dest='file', 
                      help='List file with Webinar URLs from where to scrap info and download video. File must have one URL for each line.')
  parser.add_argument('--sub', '-s', dest='sub', default=0, choices=['0', '1'],
                      help='Set to "1" if you only want to download subtitles and no video.')

  # Check & set args
  return parser.parse_args()

# Remove not allowed values for filename
def slugify(value, allow_unicode=False):
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '_', value).strip('-_')

# Parse input URL to get needed URLs data
def parse_url(url):
  parsed_url=urlparse(re.escape(url))
  url_data={
    'eventid':parse_qs(parsed_url.query)['eventid'][0].rstrip('\\'),
    'sessionid':parse_qs(parsed_url.query)['sessionid'][0].rstrip('\\'),
    'key':parse_qs(parsed_url.query)['key'][0].rstrip('\\'),
    'eventuserid':parse_qs(parsed_url.query)['eventuserid'][0].rstrip('\\')
  }
  
  return url_data

# Scrapping some data from input url
def webinar_scrapping(url_data):
  # Gather main body JSON data
  url_main_body = 'https://event.on24.com/apic/utilApp/EventConsoleCachedServlet?eventId='+url_data['eventid']+'&eventSessionId='+url_data['sessionid']+'&eventuserid='+url_data['eventuserid']+'&displayProfile=player&key='+url_data['key']+'&contentType=A&useCache=true'
  
  req = requests.get(url_main_body)
  #date_filter = parse(json.loads(req.content)['localizedeventdate'].replace(',',''))
  #eventdate = str(date_filter.year)+'-'+str(date_filter.month)+'-'+str(date_filter.day)
  #video_filename=str(eventdate+' - '+slugify(json.loads(req.content)['description'])+'.mp4')
  video_filename=str(slugify(json.loads(req.content)['description'])+'.mp4')
  json_out_filename=str(slugify(json.loads(req.content)['description'])+'.json')
  ## Export JSON
  outpath='outjson/'
  if (os.path.exists(outpath) == False):
    os.makedirs(outpath)
  with open(outpath+json_out_filename, 'w') as oufile:
    oufile.write(json.dumps(json.loads(req.content), indent=2))
  ## Exported
  vtt_url=json.loads(req.content)['vttInfo'][0]['uploadurl']

  for mediaUrlInfoContent in json.loads(req.content)['mediaUrlInfo']:
    if 'mp4' in mediaUrlInfoContent['url']:
      video_url_1='https://dashod.akamaized.net/media/cv/events/'+mediaUrlInfoContent['sourcefilename'].rstrip('.mp4')+'_mpd/stream.mpd'
      video_url_2='https://dashod.akamaized.net/media/cv/events/'+mediaUrlInfoContent['sourcefilename'].rstrip('.mp4')+'_segments/stream.mpd'

  # Save all required data to return
  gathered_info= {
    'video_title': video_filename,
    'url_mpd_1': video_url_1,
    'url_mpd_2': video_url_2,
    'url_vtt': vtt_url
  }

  return gathered_info

# Download Video
def dnld_video(url_data, args):
  # Gather title and URLs for video manifest and subtitles
  gathered_info=webinar_scrapping(url_data)
  print(json.dumps(gathered_info, indent=2))
  
  # Download video only if don't want to download only subtitles
  if args.sub == 0:
    ydl_opts = {
        'verbose': True,
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': gathered_info['video_title']
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
      try:
        ydl.download([gathered_info['url_mpd_1']])
      except:
        ydl.download([gathered_info['url_mpd_2']])
  

  req = requests.get(gathered_info['url_vtt'])
  open(gathered_info['video_title'].rstrip('.mp4')+'.vtt', 'wb').write(req.content)
  
  return

######################################################################################
# Run MAIN program
######################################################################################
if __name__ == '__main__':
  args = load_argparse()
  
  # Check where one or more URLs will be parsed
  if args.url != None:
    url_in=args.url
    url_data=parse_url(url_in)
    try:
      dnld_video(url_data, args)
    except:
      pass
  else:
    with open(args.file, 'rb') as url_list:
      for url in url_list.readlines():
        url_data=parse_url(str(url))
        try:
          dnld_video(url_data, args)
        except:
          pass
