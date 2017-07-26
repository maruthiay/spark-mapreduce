i#!/bin/bash
for filename in `hdfs dfs -ls /user/ma1306/new/ | awk '{print $NF}' | tr '\n' ' '`
do
        hadoop jar /home/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -file /home/ma1306/mapper.py    -mapper /home/ma1306/mapper.py -file /home/ma1306/reducer.py   -reducer /home/ma1306/reducer.py -input $filename -output $filename.final      ;
done

