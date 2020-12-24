from django.http import HttpResponse
from  django.shortcuts import render

def index (request):

  
   return render(request,'index.html')

    #return HttpResponse("home")

def analyze(request):
    dtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    capitalizefirst=request.POST.get('capitalizefirst','off')
    newlinerremover=request.POST.get('newlinerremover','off')
    spaceremove=request.POST.get('spaceremove','off')
    charcount=request.POST.get('charcount','off')
    print(removepunc)
    print(dtext)
    if removepunc == "on":
      punctuation="""!()-[];:'",<>./?@#$%^&*_-"""
      analyzed=""
      for char in dtext:
        if char not in punctuation:
             analyzed=analyzed+char
   
      param={'purpose':'Removed punctuation','analzed_text':analyzed}
      dtext=analyzed
      #return render(request,'analyze.html',param)
    

    if capitalizefirst =="on":
      analyzed=""
      for char in dtext:
          analyzed=analyzed+char.upper()
      param={'purpose':'capitalizefirst','analzed_text':analyzed}
      dtext=analyzed
      #return render(request,'analyze.html',param)
    

    
    if newlinerremover == "on":
        analyzed=""
        for char in dtext:
           if char!="\n":
               analyzed=analyzed+char
        param={'purpose':'newlinerremover','analzed_text':analyzed}
        dtext=analyzed
        #return render(request,'analyze.html',param)
    
    if spaceremove == 'on':
        analyzed=""
        for char in dtext:
           analyzed=analyzed+char.strip()
        param={'purpose':'spaceremove','analzed_text':analyzed}
        dtext=analyzed
        #return render(request,'analyze.html',param)
        
    if charcount == "on":
       analyzed=''
       for char in dtext:
           analyzed=analyzed+char.count("keval")
       param={'purpose':'charcount','analzed_text':analyzed}
       dtext=analyzed
       #return render(request,'analyze.html',param)  

    return render(request,'analyze.html',param)
       
    
     

      

