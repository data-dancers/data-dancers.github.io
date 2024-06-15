import numpy as np
import os
from PIL import Image
import time

urls = [
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241662246_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241662251_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241662256_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241662301_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241662306_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241662311_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241662316_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241662321_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241662326_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241662331_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241662336_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241662341_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241662346_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241662351_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241662356_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670001_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670006_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670011_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670016_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670021_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670026_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670031_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670036_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670041_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670046_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670051_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670056_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670101_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670106_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670111_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670116_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670121_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670126_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670131_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670136_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670141_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670146_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670151_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670156_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670201_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670206_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670211_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670216_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670221_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670226_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670231_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670236_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670241_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670246_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670251_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670256_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670301_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670306_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670311_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670316_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670321_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670326_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670331_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670336_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670341_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670346_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670351_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670356_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670401_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670406_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670411_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670416_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670421_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670426_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670431_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670436_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670441_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670446_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670451_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670456_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670501_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670506_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670511_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670516_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670521_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670526_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670531_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670536_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670541_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670546_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670551_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670556_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670601_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670606_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670611_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670616_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670621_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670626_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670631_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670636_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670641_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670646_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670651_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670656_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670701_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670706_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670711_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670716_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670721_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670726_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670731_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670736_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670741_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670746_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670751_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670756_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670801_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670806_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670811_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670816_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670821_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670826_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670831_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670836_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670841_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670846_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670851_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670856_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670901_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670906_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670911_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670916_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670921_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670926_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670931_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670936_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670941_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670946_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670951_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241670956_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671001_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671006_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671011_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671016_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671021_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671026_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671031_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671036_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671041_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671046_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671051_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671056_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671101_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671106_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671111_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671116_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671121_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671126_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671131_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671136_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671141_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671146_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671151_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671156_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671201_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671206_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671211_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671216_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671221_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671226_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671231_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671236_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671241_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671246_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671251_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671256_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671301_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671306_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671311_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671316_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671321_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671326_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671331_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671336_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671341_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671346_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671351_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671356_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671401_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671406_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671411_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671416_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671421_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671426_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671431_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671436_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671441_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671446_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671451_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671456_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671501_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671506_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671511_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671516_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671521_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671526_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671531_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671536_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671541_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671546_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671551_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671556_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671601_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671606_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671611_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671616_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671621_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671626_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671631_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671636_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671641_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671646_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671651_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671656_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671701_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671706_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671711_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671716_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671721_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671726_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671731_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671736_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671741_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671746_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671751_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671756_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671801_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671806_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671811_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671816_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671821_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671826_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671831_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671836_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg",
  "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20241671841_GOES16-ABI-CONUS-GEOCOLOR-625x375.jpg"
][::3]

filenames = ["loop/" + url.split('/')[-1] for url in urls]

os.makedirs("loop", exist_ok=True)
for filename, url in zip(filenames, urls):
    if not os.path.exists(filename):
        os.chdir("loop")
        os.system(f"wget {url}")
        os.chdir("..")
        time.sleep(1)

images = [Image.open(filename) for filename in filenames]
# print(len(images))

N = len(images) // 2
combined = []
for i in range(len(images)):
    a = images[i]
    b = images[(i + N) % len(images)]
    a_weight = (i if i < N else N*2 - i) / N
    b_weight = (N - i if i < N else i - N) / N
    combined.append(Image.fromarray((np.asarray(a) * a_weight + np.asarray(b) * b_weight)[:-16, 56:].astype(np.uint8)))
    # print(i, a_weight, "vs", (i + N) % len(images), b_weight)


combined[0].save("content/background.webp", save_all=True, append_images=combined[1:], loop=0, quality=20, duration=100) # , method=6)
