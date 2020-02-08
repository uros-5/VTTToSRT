import re,os,shutil

pattern = re.compile("(\d{1,2}:)?(\d{2}):(\d{2})\.(\d{1,4}) --> (\d{1,2}:)?(\d{2}):(\d{2})\.(\d{1,4})")
#59:54.440 --> 59:56.540

def mkSTR(file):
    file1 = open(file,"r",encoding="utf-8")
    file2 = open(str(file).split(".vtt")[0]+".srt","w",encoding="utf-8")
    number=0
    while(True):
        line = file1.readline()
        if("WEBVTT" in line):
            file1.readline()
            continue
        if(line!=""):
            br = pattern.findall(line)

            if(len(br)>0):
                number+=1
                newstr=""
                hour1 = br[0][0]
                minute1 = br[0][1]
                second1 = br[0][2]
                millisecond1 = br[0][3]

                hour2 = br[0][4]
                minute2 = br[0][5]
                second2 = br[0][6]
                millisecond2 = br[0][7]

                if(hour1==""):
                    newstr+="00:"+minute1+":"+second1+","+millisecond1+" --> "
                    if(hour2==""):
                        newstr += "00:" + minute2 + ":" + second2 + "," + millisecond2
                    elif(hour2!=""):
                        newstr += "0"+hour2+ minute2 + ":" + second2 + "," + millisecond2
                elif(hour1!=""):
                    if(len(hour1)==3):
                        newstr += hour1 + minute1 + ":" + second1 + "," + millisecond1 + " --> "
                        newstr+= hour2 + minute2 + ":" + second2 + "," + millisecond2
                    else:
                        newstr += "0" + hour1 + minute1 + ":" + second1 + "," + millisecond1+" --> "
                        newstr+= "0" +hour2 + minute2 + ":" + second2 + "," + millisecond2
                
                file2.write(str(number)+"\n"+newstr+"\n")
            else:
                #this is just new line
                if(line.startswith("WEBVTT")):
                    file1.readline()
                    continue
                file2.write(line)

        else:
            break

for i in os.listdir("."):
    if(i.endswith(".vtt")):
        mkSTR(i)
        os.unlink(i)

# C:\Users\user\PycharmProjects\
