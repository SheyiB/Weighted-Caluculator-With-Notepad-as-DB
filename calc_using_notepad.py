f = open("pgc.txt","r")

####To Print Line by line####
#for x in f:
#    print x


###To Read all...(3)-number of characters###
#print f.read()

f1=f.readlines()

#first_line = f1[0]
#second_line = f1[1]
#third_line = f1[2]
#fourth_line = f1[3]

zcomp=0
zunit=0
ave =0

for x in f1:
    x = x.rstrip('\n')
    thisline = x.split(',')
    var = len(thisline)
    var2 = var-2
   
    course =[]
    score =[]
    unit =[]
    for q in range(2, var-1):
        thisline2 = thisline[q].split(" ")
        course.append(thisline2[0])
        score.append(thisline2[1])
        unit.append(thisline2[2])
    ws =0
    totalunit =0
    output = ""
    for p in range(len(score)):
        ws = ws + int(score[p])* int(unit[p])
        totalunit = totalunit+ int(unit[p])
        output = output +str(course[p]) +" "+ str(score[p]) + " " + str(unit[p])+ " "
    ws = ws/totalunit
    output = output+ "weighted average = "+ str(ws)
    output = str(thisline[0]) + " " + str(thisline[1]) + " " +output
    print (output)
        
        #c = [str(e) for e in thisline2]
        
        #print c
        #x,y,z = c
        #ny = int(y)
        #nz = int(z)
        #total = ny * nz
        #print ny
        #print nz
        #continue
        #zcomp+= total
        #zunit+= int(z)
        #ave+=zcomp/zunit
        #print "Score in",x,"is",ny,"(",nz,"units)","and total point is",total
        #print zcomp 
        #print ave
        
        #ave = zcomp/zunit
        
        
        
        
        #print thisline2[0]
        #print thisline2[1]
        #print thisline2[2]
        #print thisline2[3]
        #print thisline2[4]
        #print thisline2[5]
        #print thisline2[6]
        
      
