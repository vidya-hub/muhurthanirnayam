from django.shortcuts import render

def home(request):
    return render(request, "home.html")
def H(request):
    return render(request, "home.html")

def options(request):
    value = request.POST["options"]
    if value=="tarabalam":
        return render(request, "tarabalam.html")
    elif value=="panchaka":
        return render(request,"panchakarahitham.html")
    else:
        return render(request, "home.html", {"option": value})

def arthamatic(request):
    global t_day, res,nak
    t_day=0
    val_1=0
    val_2=0
    val1 = request.POST["today"]
    val2 = request.POST["yourday"]

    # print(val1)
    nak = ["అశ్విని", "భరణి", "కృత్తిక", "రోహిణి", "మృగశిర", "ఆరుద్ర", "పునర్వసు", "పుష్యమి", "ఆశ్లేష", "మఖ", "పుబ్బ",
           "ఉత్తర", "హస్త", "చిత్త", "స్వాతి", "విశాఖ", "అనూరాధ", "జ్యేష్ట", "మూల", "పూర్వాషాఢ", "ఉత్తరాషాఢ", "శ్రవణ",
           "ధనిష్ఠ", "శతభిష", "పూర్వాభాద్ర", "ఉత్తరాభాద్ర", "రేవతి"]

    taralu = ["జన్మ తార", "సంపత్తార", "విపత్తార", "క్షేమతార", "ప్రత్యక్ తార", "సాధన తార", "నైధన తార", "మిత్ర తార",
              "పరమ మిత్ర తార"]
    # print(taralu[0])

    p_day = nak.index(val1)
    p_day += 1

    f_day = nak.index(val2)
    f_day += 1

    if f_day - p_day < 9 and f_day > p_day:
        t_day = (f_day - p_day) + 1  # front to back
    elif f_day - p_day >= 9 and f_day > p_day:
        diff = f_day - p_day
        if diff % 9 == 0:
            t_day = 1
        elif (diff + 1) % 9 == 0:
            t_day = 9
        else:
            t_day = (diff + 1) % 9
    elif f_day < p_day:  # back to front
        t_day = (((27 - (p_day - 1)) + f_day) % 9)
        if t_day == 0:
            t_day = 9
        else:
            t_day = t_day

    res = taralu[t_day - 1]
    if val1==val2:
        res=taralu[0]

    return render(request, "tarabalam.html", {"res": res,"today":val1,"yourday":val2})
def panchaka(request):
    tidhi = request.POST["tidhi"]
    varam = request.POST["varam"]
    nakshatram=request.POST["nakshatram"]
    lagnam=request.POST["lagnam"]
    tid =["పాడ్యమి","విదియ","తృతీయ","చతుర్థి","పంచమి","షష్ఠి","సప్తమి","అష్టమి","నవమి","దశమి","ఏకాదశి","ద్వాదశి","త్రయోదశి","చతుర్దశి","పౌర్ణమి","అమావాస్య"]
    varas=["ఆదివారం","సోమవారం","మంగళవారం","బుధవారం","గురువారం","శుక్రవారం","శనివారం"]
    naks=["అశ్విని", "భరణి", "కృత్తిక", "రోహిణి", "మృగశిర", "ఆరుద్ర", "పునర్వసు", "పుష్యమి", "ఆశ్లేష", "మఖ", "పుబ్బ",
           "ఉత్తర", "హస్త", "చిత్త", "స్వాతి", "విశాఖ", "అనూరాధ", "జ్యేష్ట", "మూల", "పూర్వాషాఢ", "ఉత్తరాషాఢ", "శ్రవణ",
           "ధనిష్ఠ", "శతభిష", "పూర్వాభాద్ర", "ఉత్తరాభాద్ర", "రేవతి"]
    lags=["మేషం","వృషభం","మిథునం","కర్కాటకం","సింహం","కన్య","తుల","వృశ్చికం","ధనసు","మకరం","కుంభం","మీనం"]

    # pan=[]
    t = tid.index(tidhi)
    v = varas.index(varam)
    n = naks.index(nakshatram)
    l = lags.index(lagnam)

    t+=1
    v+=1
    n += 1
    l += 1

    a=t+v+n+l
    r=(a)%9
    print(f"{t}   {v}  {n}  {l}  {a}  res {r}")

    if r==1:
        out="మృత్యు పంచకం"
    elif r==2:
        out="అగ్ని పంచకం"
    elif r==4:
        out="రాజ పంచకం"
    elif r==6:
        out="చోర పంచకం"
    elif r==8:
        out="రోగ పంచకం"
    else:
        out="శుభప్రదం"

    return render(request, "panchakarahitham.html", {"tidhi": tidhi, "varam": varam,"nakshatram": nakshatram, "lagnam": lagnam, "out": out,})