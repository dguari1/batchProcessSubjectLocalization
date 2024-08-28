This repository is used to batch process the subject localization step of VisionMD.  

The MP4 video files to process should be uploaded to the `data` folder. This repository can be used to process multiple video files.

After all video files are available, execute 

```
python process.py
```

This will generate `.JSON` files in the folder `output` containing the position of the subjects in the video. You can use the generated JSON files within VisionMD 
