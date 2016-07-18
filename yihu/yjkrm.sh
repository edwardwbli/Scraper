#! /bin/ksh



#Remove all empty-hospital city file
for i in `ls -l ./hos_rawdata/hos399/dp* | awk '{ if ($5 == 457) print $9}`;do
    echo 'remove '$i
    rm -f $i
done;

#Obtain all hospital department list according to hospital list
#ls -l cty* | awk '{ if ($5 > 50) print $9}'  to list all file which filesize > 50 bytes
#sed 's/\"//g' to remove all "


