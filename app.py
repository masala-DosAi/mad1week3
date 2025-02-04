import sys
from jinja2 import Template
import matplotlib.pyplot as plt




if sys.argv[1]=='-s' and sys.argv[2][0]=='1':
     total=0
     ls=[]
     f= open("data.csv",'r')
     hd=list(f.readline().split(','))


     for x in f:
          if list(x.split(', '))[0]==sys.argv[2]:
                         ls.append(list(x.split(', ')))
     print(ls)
     f.close()
     for t in ls:
             total+=int(t[2])
     template_file=open("output.html.jinja2")
     TEMPLATE=template_file.read()
     template_file.close()
            

     template=Template(TEMPLATE)
     
     content=template.render(data=ls,header ="Student details",headd=hd,total_marks=total)


     output=open('output.html',"w")
     output.write(content)
     output.close()
elif sys.argv[1]=='-c' and sys.argv[2][0]=='2':
     ls=[]
     f= open("data.csv",'r')
     hd=list(f.readline().split(', '))
     for x in f:
          if list(x.split(', '))[1]==sys.argv[2]:
                         ls.append(int(list(x.split(', '))[2]))
     print(ls)
     f.close()
     avg=sum(ls)/len(ls)
     max_val=max(ls)


     # Create and save the histogram
     plt.hist(ls, bins=5, edgecolor='black')
     plt.xlabel('Values')
     plt.ylabel('Frequency')
     plt.title('Histogram')

     # Save the image
     image_path = "histogram.png"
     plt.savefig(image_path)
     plt.close()


     
     
     template_file=open("outputc.jinja2")
     TEMPLATE=template_file.read()
     template_file.close()
            

     template=Template(TEMPLATE)
     
     content=template.render(average=avg,maximum=max_val,header="Course Details",image_path="histogram.png")


     output=open('output.html',"w")
     output.write(content)
     output.close()
       
     
else:
     template_file=open("outputelse.jinja2")
     TEMPLATE=template_file.read()
     template_file.close()
            

     template=Template(TEMPLATE)
     
     content=template.render()


     output=open('output.html',"w")
     output.write(content)
     output.close()