# PubTables-coco-formatData Preparation

   Download the pubtables dataset. Use the following commands to convert PubTables data from xml to coco format
   YOUR_DATA should be in the following shape 
    For eg.:
    YOUR_DATA_FOLDER/
       test.txt
       train.txt
       test.txt
       train/
       val/
       test/
       annotations/
    python clean-up.py                  #for train, test and val files
    python voc2coco.py --ann_dir val --ann_ids train.txt --labels labels.txt --output annotations/train.json --ext xml
    python voc2coco.py --ann_dir val --ann_ids val.txt --labels labels.txt --output annotations/val.json --ext xml
    python voc2coco.py --ann_dir val --ann_ids test.txt --labels labels.txt --output annotations/test.json --ext xml
