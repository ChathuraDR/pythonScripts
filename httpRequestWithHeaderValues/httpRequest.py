import _thread
import time
import urllib.request;
import urllib.parse;

def makeRqst():
    while True:
        try:
            time.sleep(4)
            url = 'http://localhost/index.php'

            headers = {}
            headers['Connection'] = 'keep-alive'
            headers['Cache-Control'] = 'max-age=0'
            headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
            headers['Upgrade-Insecure-Requests'] = '1'
            headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
            headers['Accept-Encoding'] = 'gzip, deflate, br'
            headers['Accept-Language'] = 'en-US,en;q=0.8,und;q=0.6'
            headers['Cookie'] = 'cookieValue'
            req = urllib.request.Request(url, headers=headers)
            urllib.request.urlopen(req)
            '''
            resp = urllib.request.urlopen(req)
            respData = resp.read()
            saveFile = open('withHeaders.txt', 'w')
            saveFile.write(str(respData))
            saveFile.close()
            '''

            print('sent')

        except Exception as e:
            print(str(e))

try:
   _thread.start_new_thread(makeRqst, ())
except:
   print("Error: unable to start thread")

while 1:
   pass