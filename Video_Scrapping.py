#Program to Download/Scrape the Video from the Internet

import requests
#To Download the Video In Cunks of 256bytes/sec
chunk_size = 256

#Getting Video URL
video_url = requests.get('''http://files3.lynda.com/secure/courses/2819142/VBR_MP4h264_main_SD/2819142_00_01_WX30_Welcome.mp4?uBHitez
                            M6lQRPzMOn8sL6B2XUqcpk2jI1CqtiZuj8g9RTWZwFFOcYmubOmS3JbbHIkWVW6BhMB7FjsM49tFHpCpE4eYI-kSyhog1IGYnwrgMS_
                            6K1ursxuWgEfMQ8lv9i_2So41xvopMf64-0qAyPP8qTXRL1SAJxanbeCNkYKNRYlUEuj7jm-vpfTlO&c3.ri=3773695278716498042''',
                         stream = True)

#Save the file in Folder
with open('video.mp4', 'wb') as d:
    for chunk in video_url.iter_content(chunk_size = chunk_size):
        d.write(chunk)

