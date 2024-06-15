---
title: "Editing Video with `ffmpeg`"
author: "Cortland Mahoney"
---

Do you have some amazing footage, but it's *just too long*? 

Cut it down! Make it just right with handy dandy `ffmpeg`.

FFmpeg is a powerhouse of utility when it comes to editing video. You can use it to resize videos, transcode from one format (like .mov) to another (like .mp4), add audio tracks, add caption tracks, and more! 

In this example, we'll use `ffmpeg` to take a 15 second clip from a long video. We'll perform two tasks:

## Transcoding to MP4 (aka video conversion)

Most browsers don't support an .mov encoding, but many do allow .mp4. Right now my video is in .mov format and I'd like it to be .mp4. 

Most of the time this is called "converting" a video. The slightly more accurate technical term is "transcoding" because we _decode_ from one format and _encode_ it into a new format.

## Trimming

Sometimes you just have too much awesome video to share. Maybe your set was an hour long but need 15 seconds for a reel. Again, we can use ffmpeg for that!

**IMPORTANT**

Make sure that your trim length is _shorter_ than the whole video. If you try to trim longer than the video's duration, it might produce an output file but the file will not be a valid video. 

So if you want to do this action in bulk, use something like 

`ffprobe -i $INPUT -show_entries format=duration -v quiet -of csv="p=0"` 

to get the duration of a video).


## Using ffmpeg

This bash script defines four variables: Two for the file (input and output), and two for the trim action (where to start the trim from, and how much video to keep).

The INPUT and OUTPUT variables should be absolute (or relative paths) to the original _input_ file and the new transcoded & trimmed _output_ file. 

```
# For this example let's start the video from the beginning
# and take the first ten seconds of media

START_POSITION=0
VIDEO_LENGTH=10
INPUT=/home/naltroc/Documents/algorave-september-2023/Algorave-Video-20230914/IMG_3151.MOV
OUTPUT=/home/naltroc/Documents/algorave-september-2023/Algorave-Video-20230914/IMG_3151-shorter.mp4
ffmpeg -ss $START_POSITION -i $INPUT -t $VIDEO_LENGTH -c:v libx264 -c:a aac -b:a 192k $OUTPUT
```

