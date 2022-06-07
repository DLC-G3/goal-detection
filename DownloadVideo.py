
import time
import requests


def download(link):
    file_name = link.split('/')[-1].split('?')[0]
 
    print ("Downloading file: %s"%file_name)
 
    #create response object
    r = requests.get(link, stream = True)
 
    #download started
    with open(file_name, 'wb') as f:
      for chunk in r.iter_content(chunk_size = 1024*1024):
        if chunk:
          f.write(chunk)
        else: break


start_time = time.time()
download('https://storage.googleapis.com/360si-dlc/recordings/733515/video/ch1.mp4?GoogleAccessId=862250713673-kg5eq0ac1b7k2cl5433b8rs0r87dbit3%40developer.gserviceaccount.com&Expires=1654717471&Signature=E9Ay%2BlZjneL7QwU6Kpqk1yUFqsWaVBPUSHuLr%2F0rmXae7Y5DBHM4W04drsMRoi9ye4dwDg7AYHF4qeVtApTRr1zKGGxd%2F%2B0RLm9R%2FXlbc1piQ8GGfP24crKZEmpKkABEdgBAVcPIRL64HzL4CTlMXJ5J%2B6ceVhjcdW6tqbBQRic%3D') 
print(f"time: {time.time() - start_time} seconds")