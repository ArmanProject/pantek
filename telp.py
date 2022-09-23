#!/bin/python2/telp.py

read -p "target : "
curl -s (f"https://darkteam.my.id/minispam/spamsms.php?nomor=$target")
if [ $? -eq 0 ]; "then
echo"Done"
else
echo "Error"
fi
