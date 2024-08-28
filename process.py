import os
import json
import time

from YOLOTracker import YOLOTracker

def get_fileName(file, outputFolder):

    return os.path.join(outputFolder, os.path.splitext(file)[0] + '.json') 

def main():

    inputFolder = 'data'
    listFiles = os.listdir(inputFolder)
    idx=0
    for file in listFiles:
        if '.mp4' in file:
            print(f'Processing {file}, {idx+1} of {len(listFiles)}')

            st = time.time()
            outputDic = YOLOTracker(os.path.join(inputFolder,file), "model/yolov8n.pt")
            JSONFilename = get_fileName(file, 'output')
            with open(JSONFilename, 'w') as fp:
                json.dump(outputDic, fp)

            print(f'Completed in {((time.time()-st)):.3f} seconds')
            idx+=1


if __name__ == "__main__":
    main()