import os
os.environ['CLASSPATH'] = "/Users/amckenzie/Tools/tika-app-1.4.jar"

from jnius import autoclass

## Import the Java classes we are going to need
Tika = autoclass('org.apache.tika.Tika')
Metadata = autoclass('org.apache.tika.metadata.Metadata')
FileInputStream = autoclass('java.io.FileInputStream')

tika = Tika()
meta = Metadata()
text = tika.parseToString(FileInputStream("/Users/amckenzie/Documents/PDFs/sample.pdf"), meta)
print(text)