import zipfile
from xml.etree import ElementTree as ET  

your_delet_file="metadata/thumbnail.png"
old_zipfile='untitled.slx' #新文件
new_zipfile='archve_new.zip' #新文件
zin = zipfile.ZipFile (old_zipfile, 'r') #读取对象
zout = zipfile.ZipFile (new_zipfile, 'w') #被写入对象
for item in zin.infolist():
    buffer = zin.read(item.filename)
    print(item.filename)
    if (item.filename!= your_delet_file):  #剔除要删除的文件
        zout.writestr(item, buffer) #把文件写入到新对象中
zout.close()
zin.close()
 
#用新文件覆盖旧文件
# shutil.move(new_zipfile,old_zipfile)
