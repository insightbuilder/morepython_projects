#!/bin/bash

# Base URL for the downloads
base_url="https://ptgmedia.pearsoncmg.com/imprint_downloads/informit/bookreg/9780134123486"

# Loop to download Ex0.mp4 to Ex49.mp4
for i in {2..49}; do
  # Format the filename with the loop index, must have updated a /media/uberdev/fdrv/tempVids01/LMorePy3 path here
  file="LMorePy3THW_Ex${i}.mp4"
  echo "Downloading ${file}" 
  # Download each file
  wget "${base_url}/${file}" -O "${file}"
  
  # Check if the download was successful
  if [[ $? -ne 0 ]]; then
    echo "Failed to download ${file}"
  else
    echo "Downloaded ${file} successfully"
  fi
done
