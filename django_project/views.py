from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, FileResponse, JsonResponse
from CHART.models import NewResult, Contacts, NewTag, Feedback
from CHART.forms import NewResultForm, NewTagForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.admin.models import LogEntry


def Modifier(list):
    if len(list) == 0:
        for i in range(8):
            list.append('--')
    elif len(list) == 1:
        for i in range(7):
            list.append('--')
    elif len(list) == 2:
        for i in range(6):
            list.append('--')
    elif len(list) == 3:
        for i in range(5):
            list.append('--')
    elif len(list) == 4:
        for i in range(4):
            list.append('--')
    elif len(list) == 5:
        for i in range(3):
            list.append('--')
    elif len(list) == 6:
        for i in range(2):
            list.append('--')
    elif len(list) == 7:
        for i in range(1):
            list.append('--')
    else:
        pass
    return list

def chartMaker(list):
    new_list = ['RECORD CHART', 'OCTOBER 2024', '\n', "________________________", 'DB SG FB FZ GB LB GL DS']
    tempList = []
    for item in list:
        if len(tempList) <= 7:
            tempList.append(item)
        else:
            string = '-'.join(tempList)
            new_list.append(string)
            tempList = []
            tempList.append(item)

    string = '-'.join(tempList)
    new_list.append(string)
    new_list.append("________________________")
    new_list.append("https://vip-satta-result.in/")
    new_list.append("https://vip-satta-result.in/")
    return new_list
    
def chartMakerOmega(list1, list2, list3, list4, list5, list6):
    dates = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    
    new_list = ['RECORD CHART', 'OCTOBER 2024', '\n', "________________________", 'Date-DB SG FB GB GL DS']
    tempList = []
    for i in range(len(list1)):
        tempList.append(f'{dates[i]}OCT')
        tempList.append(list1[i])
        if i >= len(list2):
            tempList.append('xx')
        else:
            tempList.append(list2[i])
        if i >= len(list3):
            tempList.append('xx')
        else:
            tempList.append(list3[i])
        if i >= len(list4):
            tempList.append('xx')
        else:
            tempList.append(list4[i])
        if i >= len(list5):
            tempList.append('xx')
        else:
            tempList.append(list5[i])
        if i >= len(list6):
            tempList.append('xx')
        else:
            tempList.append(list6[i])
        string = '-'.join(tempList)
        new_list.append(string)
        tempList = []
    new_list.append("________________________")
    new_list.append("https://vip-satta-result.in/")
    new_list.append("https://vip-satta-result.in/")
    return new_list
        

# MAIN_FUNCTION_HOMEVIEW
def home(request):
    # NEW RESULTS
    new_results = NewResult.objects.all().order_by('-timestamp')[0:3]
    if len(new_results) == 0:
        new_results = [
            {
                'game_name': 'DELHI BAZAR',
                'result': '--',
            },
            {
                'game_name': 'SHRI GANESH',
                'result': '--',
            },
            {
                'game_name': 'FARIDABAD',
                'result': '--',
            }
        ]
    elif len(new_results) == 1:
        new_results = [
            new_results[0],
            {
                'game_name': 'SHRI GANESH',
                'result': '--',
            },
            {
                'game_name': 'FARIDABAD',
                'result': '--',
            }
        ]
    elif len(new_results) == 2:
        new_results = [
            new_results[0],
            new_results[1],
            {
                'game_name': 'FARIDABAD',
                'result': '--',
            }
        ]

    # TODAY DB RESULTS
    db_results_pack = NewResult.objects.filter(game_name='DELHI BAZAR').order_by('-timestamp')[0:2]
    db_results = []
    for result in db_results_pack:
        db_results.append(result.result)
    db_results = reversed(db_results)
    if db_results_pack.count() == 0:
        db_results = ['--', '--']
    elif db_results_pack.count() == 1:
        db_results = list(db_results) + ['--']
    # TODAY SG RESULTS
    sg_results_pack = NewResult.objects.filter(game_name='SHRI GANESH').order_by('-timestamp')[0:2]
    sg_results = []
    for result in sg_results_pack:
        sg_results.append(result.result)
    sg_results = reversed(sg_results)
    if sg_results_pack.count() == 0:
        sg_results = ['--', '--']
    elif sg_results_pack.count() == 1:
        sg_results = list(sg_results) + ['--']

    # TODAY FB RESULTS
    fb_results_pack = NewResult.objects.filter(game_name='FARIDABAD').order_by('-timestamp')[0:2]
    fb_results = []
    for result in fb_results_pack:
        fb_results.append(result.result)
    fb_results = reversed(fb_results)
    if fb_results_pack.count() == 0:
        fb_results = ['--', '--']
    elif fb_results_pack.count() == 1:
        fb_results = list(fb_results) + ['--']

    # TODAY FZ RESULTS
    fz_results_pack = NewResult.objects.filter(game_name='FIROZABAD').order_by('-timestamp')[0:2]
    fz_results = []
    for result in fz_results_pack:
        fz_results.append(result.result)
    fz_results = reversed(fz_results)
    if fz_results_pack.count() == 0:
        fz_results = ['--', '--']
    elif fz_results_pack.count() == 1:
        fz_results = list(fz_results) + ['--']

    # TODAY GB RESULTS
    gb_results_pack = NewResult.objects.filter(game_name='GAZIABAD').order_by('-timestamp')[0:2]
    gb_results = []
    for result in gb_results_pack:
        gb_results.append(result.result)
    gb_results = reversed(gb_results)
    if gb_results_pack.count() == 0:
        gb_results = ['--', '--']
    elif gb_results_pack.count() == 1:
        gb_results = list(gb_results) + ['--']

    # TODAY LB RESULTS
    lb_results_pack = NewResult.objects.filter(game_name='LAXMI BAZAR').order_by('-timestamp')[0:2]
    lb_results = []
    for result in lb_results_pack:
        lb_results.append(result.result)
    lb_results = reversed(lb_results)
    if lb_results_pack.count() == 0:
        lb_results = ['--', '--']
    elif lb_results_pack.count() == 1:
        lb_results = list(lb_results) + ['--']

    # TODAY GL RESULTS
    gl_results_pack = NewResult.objects.filter(game_name='GALI').order_by('-timestamp')[0:2]
    gl_results = []
    for result in gl_results_pack:
        gl_results.append(result.result)
    gl_results = reversed(gl_results)
    if gl_results_pack.count() == 0:
        gl_results = ['--', '--']
    elif gl_results_pack.count() == 1:
        gl_results = list(gl_results) + ['--']

    # TODAY DS RESULTS
    ds_results_pack = NewResult.objects.filter(game_name='DESAWAR').order_by('-timestamp')[0:2]
    ds_results = []
    for result in ds_results_pack:
        ds_results.append(result.result)
    ds_results = reversed(ds_results)
    if ds_results_pack.count() == 0:
        ds_results = ['--', '--']
    elif ds_results_pack.count() == 1:
        ds_results = list(ds_results) + ['--']

    # ALL_RESULTS_MONTHLY

    # DAY 1
    monthly_1 = NewResult.objects.all().order_by('timestamp')[0:8]
    month_1 = []
    for m_1 in monthly_1:
        month_1.append(m_1.result)
    month_1 = Modifier(month_1)
    # DAY 2
    monthly_2 = NewResult.objects.all().order_by('timestamp')[8:16]
    month_2 = []
    for m_2 in monthly_2:
        month_2.append(m_2.result)
    month_2 = Modifier(month_2)
    # DAY 3
    monthly_3 = NewResult.objects.all().order_by('timestamp')[16:24]
    month_3 = []
    for m_3 in monthly_3:
        month_3.append(m_3.result)
    month_3 = Modifier(month_3)
    # DAY 4
    monthly_4 = NewResult.objects.all().order_by('timestamp')[24:32]
    month_4 = []
    for m_4 in monthly_4:
        month_4.append(m_4.result)
    month_4 = Modifier(month_4)
    # DAY 5
    monthly_5 = NewResult.objects.all().order_by('timestamp')[32:40]
    month_5 = []
    for m_5 in monthly_5:
        month_5.append(m_5.result)
    month_5 = Modifier(month_5)
    # DAY 6
    monthly_6 = NewResult.objects.all().order_by('timestamp')[40:48]
    month_6 = []
    for m_6 in monthly_6:
        month_6.append(m_6.result)
    month_6 = Modifier(month_6)
    # DAY 7
    monthly_7 = NewResult.objects.all().order_by('timestamp')[48:56]
    month_7 = []
    for m_7 in monthly_7:
        month_7.append(m_7.result)
    month_7 = Modifier(month_7)
    # DAY 8
    monthly_8 = NewResult.objects.all().order_by('timestamp')[56:64]
    month_8 = []
    for m_8 in monthly_8:
        month_8.append(m_8.result)
    month_8 = Modifier(month_8)
    # DAY 9
    monthly_9 = NewResult.objects.all().order_by('timestamp')[64:72]
    month_9 = []
    for m_9 in monthly_9:
        month_9.append(m_9.result)
    month_9 = Modifier(month_9)
    # DAY 10
    monthly_10 = NewResult.objects.all().order_by('timestamp')[72:80]
    month_10 = []
    for m_10 in monthly_10:
        month_10.append(m_10.result)
    month_10 = Modifier(month_10)
    # DAY 11
    monthly_11 = NewResult.objects.all().order_by('timestamp')[80:88]
    month_11 = []
    for m_11 in monthly_11:
        month_11.append(m_11.result)
    month_11 = Modifier(month_11)
    # DAY 12
    monthly_12 = NewResult.objects.all().order_by('timestamp')[88:96]
    month_12 = []
    for m_12 in monthly_12:
        month_12.append(m_12.result)
    month_12 = Modifier(month_12)
    # DAY 13
    monthly_13 = NewResult.objects.all().order_by('timestamp')[96:104]
    month_13 = []
    for m_13 in monthly_13:
        month_13.append(m_13.result)
    month_13 = Modifier(month_13)
    # DAY 14
    monthly_14 = NewResult.objects.all().order_by('timestamp')[104:112]
    month_14 = []
    for m_14 in monthly_14:
        month_14.append(m_14.result)
    month_14 = Modifier(month_14)
    # DAY 15
    monthly_15 = NewResult.objects.all().order_by('timestamp')[112:120]
    month_15 = []
    for m_15 in monthly_15:
        month_15.append(m_15.result)
    month_15 = Modifier(month_15)
    # DAY 16
    monthly_16 = NewResult.objects.all().order_by('timestamp')[120:128]
    month_16 = []
    for m_16 in monthly_16:
        month_16.append(m_16.result)
    month_16 = Modifier(month_16)
    # DAY 17
    monthly_17 = NewResult.objects.all().order_by('timestamp')[128:136]
    month_17 = []
    for m_17 in monthly_17:
        month_17.append(m_17.result)
    month_17 = Modifier(month_17)
    # DAY 18
    monthly_18 = NewResult.objects.all().order_by('timestamp')[136:144]
    month_18 = []
    for m_18 in monthly_18:
        month_18.append(m_18.result)
    month_18 = Modifier(month_18)
    # DAY 19
    monthly_19 = NewResult.objects.all().order_by('timestamp')[144:152]
    month_19 = []
    for m_19 in monthly_19:
        month_19.append(m_19.result)
    month_19 = Modifier(month_19)
    # DAY 20
    monthly_20 = NewResult.objects.all().order_by('timestamp')[152:160]
    month_20 = []
    for m_20 in monthly_20:
        month_20.append(m_20.result)
    month_20 = Modifier(month_20)
    # DAY 21
    monthly_21 = NewResult.objects.all().order_by('timestamp')[160:168]
    month_21 = []
    for m_21 in monthly_21:
        month_21.append(m_21.result)
    month_21 = Modifier(month_21)
    # DAY 22
    monthly_22 = NewResult.objects.all().order_by('timestamp')[168:176]
    month_22 = []
    for m_22 in monthly_22:
        month_22.append(m_22.result)
    month_22 = Modifier(month_22)
    # DAY 23
    monthly_23 = NewResult.objects.all().order_by('timestamp')[176:184]
    month_23 = []
    for m_23 in monthly_23:
        month_23.append(m_23.result)
    month_23 = Modifier(month_23)
    # DAY 24
    monthly_24 = NewResult.objects.all().order_by('timestamp')[184:192]
    month_24 = []
    for m_24 in monthly_24:
        month_24.append(m_24.result)
    month_24 = Modifier(month_24)
    # DAY 25
    monthly_25 = NewResult.objects.all().order_by('timestamp')[192:200]
    month_25 = []
    for m_25 in monthly_25:
        month_25.append(m_25.result)
    month_25 = Modifier(month_25)
    # DAY 26
    monthly_26 = NewResult.objects.all().order_by('timestamp')[200:208]
    month_26 = []
    for m_26 in monthly_26:
        month_26.append(m_26.result)
    month_26 = Modifier(month_26)
    # DAY 27
    monthly_27 = NewResult.objects.all().order_by('timestamp')[208:216]
    month_27 = []
    for m_27 in monthly_27:
        month_27.append(m_27.result)
    month_27 = Modifier(month_27)
    # DAY 28
    monthly_28 = NewResult.objects.all().order_by('timestamp')[216:224]
    month_28 = []
    for m_28 in monthly_28:
        month_28.append(m_28.result)
    month_28 = Modifier(month_28)
    # DAY 29
    monthly_29 = NewResult.objects.all().order_by('timestamp')[224:232]
    month_29 = []
    for m_29 in monthly_29:
        month_29.append(m_29.result)
    month_29 = Modifier(month_29)
    # DAY 30
    monthly_30 = NewResult.objects.all().order_by('timestamp')[232:240]
    month_30 = []
    for m_30 in monthly_30:
        month_30.append(m_30.result)
    month_30 = Modifier(month_30)
    # DAY 31
    monthly_31 = NewResult.objects.all().order_by('timestamp')[240:248]
    month_31 = []
    for m_31 in monthly_31:
        month_31.append(m_31.result)
    month_31 = Modifier(month_31)
    # NEW TAGS FOR GAMES
    db_tag = NewTag.objects.filter(game_name='DELHI BAZAR')
    sg_tag = NewTag.objects.filter(game_name='SHRI GANESH')
    fb_tag = NewTag.objects.filter(game_name='FARIDABAD')
    fz_tag = NewTag.objects.filter(game_name='FIROZABAD')
    gb_tag = NewTag.objects.filter(game_name='GAZIABAD')
    lb_tag = NewTag.objects.filter(game_name='LAXMI BAZAR')
    gl_tag = NewTag.objects.filter(game_name='GALI')
    ds_tag = NewTag.objects.filter(game_name='DESAWAR')
    
    # DATA_SENDS_TO_FRONTEND
    context = {
        'new_results': new_results,
        'db_results': db_results,
        'sg_results': sg_results,
        'fb_results': fb_results,
        'fz_results': fz_results,
        'gb_results': gb_results,
        'lb_results': lb_results,
        'gl_results': gl_results,
        'ds_results': ds_results,
        'month_1': month_1,
        'month_2': month_2,
        'month_3': month_3,
        'month_4': month_4,
        'month_5': month_5,
        'month_6': month_6,
        'month_7': month_7,
        'month_8': month_8,
        'month_9': month_9,
        'month_10': month_10,
        'month_11': month_11,
        'month_12': month_12,
        'month_13': month_13,
        'month_14': month_14,
        'month_15': month_15,
        'month_16': month_16,
        'month_17': month_17,
        'month_18': month_18,
        'month_19': month_19,
        'month_20': month_20,
        'month_21': month_21,
        'month_22': month_22,
        'month_23': month_23,
        'month_24': month_24,
        'month_25': month_25,
        'month_26': month_26,
        'month_27': month_27,
        'month_28': month_28,
        'month_29': month_29,
        'month_30': month_30,
        'month_31': month_31,
        'db_tag': db_tag,
        'sg_tag': sg_tag,
        'fb_tag': fb_tag,
        'fz_tag': fz_tag,
        'gb_tag': gb_tag,
        'lb_tag': lb_tag,
        'gl_tag': gl_tag,
        'ds_tag': ds_tag,
    }
    
    return render(request, 'home.html', context)

# MAIN_FUNCTION_ENDS

# ADMIN PANEL VIEW
def coadmin(request):
    user_list = User.objects.all()
    
    # Result And Posts
    wa_result = NewResult.objects.all().order_by('-timestamp')[0:1]
    contacts = Contacts.objects.all()
    # Today Results
    last_db_result = NewResult.objects.filter(game_name='DELHI BAZAR').order_by('-timestamp')[0:1]
    last_db_result_id = 0
    for result in last_db_result:
        last_db_result_id = result.id
    today_last = NewResult.objects.filter(id__gt=last_db_result_id)
    today_results = []
    for num in today_last:
        today_results.append(num.result)

    today_results = Modifier(today_results)
    
    db_last = ""
    sg_last = f"{today_results[0]}"
    fb_last = f"{today_results[1]}"
    fz_last = f"{today_results[2]}"
    gb_last = f"{today_results[3]}"
    lb_last = f"{today_results[4]}"
    gl_last = f"{today_results[5]}"
    ds_last = f"{today_results[6]}"
    
    for dbgame in last_db_result:
        db_last = dbgame.result

    wa_post_title = ""
    post_title = NewResult.objects.all().order_by('-timestamp')[7:8]
    for post in post_title:
        wa_post_title = post.game_name


    last_actions = LogEntry.objects.all().order_by('-action_time')[0:15]
    last_updated_results = NewResult.objects.all().order_by('-timestamp')[0:20]
    # CHART MAKER VIEW
    all_games_results = NewResult.objects.all()
    all_results = []
    for results in all_games_results:
        all_results.append(results.result)

    chart_data = chartMaker(all_results)

    # CHART DB TO DS 6 GAMES
    dbData = NewResult.objects.filter(game_name='DELHI BAZAR')
    dbDataList = []
    for dbData in dbData:
        dbDataList.append(dbData.result)
    sgData = NewResult.objects.filter(game_name='SHRI GANESH')
    sgDataList = []
    for sgData in sgData:
        sgDataList.append(sgData.result)
    fbData = NewResult.objects.filter(game_name='FARIDABAD')
    fbDataList = []
    for fbData in fbData:
        fbDataList.append(fbData.result)
    gbData = NewResult.objects.filter(game_name='GAZIABAD')
    gbDataList = []
    for gbData in gbData:
        gbDataList.append(gbData.result)
    glData = NewResult.objects.filter(game_name='GALI')
    glDataList = []
    for glData in glData:
        glDataList.append(glData.result)
    dsData = NewResult.objects.filter(game_name='DESAWAR')
    dsDataList = []
    for dsData in dsData:
        dsDataList.append(dsData.result)

    newData = chartMakerOmega(dbDataList, sgDataList, fbDataList, gbDataList, glDataList, dsDataList)

    # Feedbacks
    feedbacks = Feedback.objects.all()
    # TAG FORM VIEW
    if request.method == 'POST':
        tag_form = NewTagForm(request.POST)
        if tag_form.is_valid():
            tag_form.save()
            return redirect('coadmin')
    else:
        tag_form = NewTagForm()

    #RESULT FORM VIEW
    if request.method == 'POST':
        form = NewResultForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('coadmin')
    else:
        form = NewResultForm()
    
    return render(request, 'coadmin.html', {'form': form, 'contacts': contacts, 'tag_form': tag_form, 'wa_result': wa_result, 'user_list': user_list, 'db_last': db_last, 'sg_last': sg_last, 'fb_last': fb_last, 'fz_last': fz_last, 'gb_last': gb_last, 'lb_last': lb_last, 'gl_last': gl_last, 'ds_last': ds_last, 'wa_post_title': wa_post_title, 'last_actions': last_actions, 'last_updated_results': last_updated_results, 'chart_data': chart_data, 'newData': newData, 'feedbacks': feedbacks})


# ADMIN PANEL LOGIN VIEW

def co_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('coadmin')
        else:
            messages.info(request, 'Username or password is incorrect')
    return render(request, 'login.html')

# ADMIN PANEL LOGOUT VIEW
def co_logout(request):
    logout(request)
    return redirect('home')




# DELETE TAGS VIEW
def delete_alltags(request):
    all_tags = NewTag.objects.all()
    all_tags.delete()
    return redirect('home')
    


# ABOUT US PAGE

def about(request):
    return render(request, 'about.html')

# CONTACT US PAGE

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        whatsapp = request.POST.get('whatsapp')
        message = request.POST.get('message')
        contact = Contacts(name=name, whatsapp=whatsapp, message=message)
        contact.save()
        return redirect('home')
    else:
        return render(request, 'contact.html')
    

# TOOLS PAGE

def tools(request):
    return render(request, 'tools.html')



# YEARLY CHARTS VIEW
# YEAR WISE DELHI BAZAR

def db20(request):
    return render(request, 'chartsyearly/db20.html')

def db21(request):
    return render(request, 'chartsyearly/db21.html')

def db22(request):
    return render(request, 'chartsyearly/db22.html')

def db23(request):
    return render(request, 'chartsyearly/db23.html')

# YEAR WISE SHRI GANESH

def sg20(request):
    return render(request, 'chartsyearly/sg20.html')

def sg21(request):
    return render(request, 'chartsyearly/sg21.html')

def sg22(request):
    return render(request, 'chartsyearly/sg22.html')

def sg23(request):
    return render(request, 'chartsyearly/sg23.html')

# YEAR WISE FARIDABAD

def fb20(request):
    return render(request, 'chartsyearly/fb20.html')

def fb21(request):
    return render(request, 'chartsyearly/fb21.html')

def fb22(request):
    return render(request, 'chartsyearly/fb22.html')

def fb23(request):
    return render(request, 'chartsyearly/fb23.html')


# YEAR WISE FIROZABAD

def fz20(request):
    return render(request, 'chartsyearly/fz20.html')

def fz21(request):
    return render(request, 'chartsyearly/fz21.html')

def fz22(request):
    return render(request, 'chartsyearly/fz22.html')

def fz23(request):
    return render(request, 'chartsyearly/fz23.html')


# YEAR WISE GAZIABAD
def gb20(request):
    return render(request, 'chartsyearly/gb20.html')

def gb21(request):
    return render(request, 'chartsyearly/gb21.html')

def gb22(request):
    return render(request, 'chartsyearly/gb22.html')

def gb23(request):
    return render(request, 'chartsyearly/gb23.html')

# YEAR WISE LAXMI BAZAR

def lb20(request):
    return render(request, 'chartsyearly/lb20.html')

def lb21(request):
    return render(request, 'chartsyearly/lb21.html')

def lb22(request):
    return render(request, 'chartsyearly/lb22.html')

def lb23(request):
    return render(request, 'chartsyearly/lb23.html')


# YEAR WISE GALI

def gl20(request):
    return render(request, 'chartsyearly/gl20.html')

def gl21(request):
    return render(request, 'chartsyearly/gl21.html')

def gl22(request):
    return render(request, 'chartsyearly/gl22.html')

def gl23(request):
    return render(request, 'chartsyearly/gl23.html')


# YEAR WISE DESAWAR

def ds20(request):
    return render(request, 'chartsyearly/ds20.html')

def ds21(request):
    return render(request, 'chartsyearly/ds21.html')

def ds22(request):
    return render(request, 'chartsyearly/ds22.html')

def ds23(request):
    return render(request, 'chartsyearly/ds23.html')


# MONTHLY CHARTS VIEW

def january(request):
    return render(request, 'chart2024monthly/jan24.html')

def february(request):
    return render(request, 'chart2024monthly/feb24.html')

def march(request):
    return render(request, 'chart2024monthly/mar24.html')

def april(request):
    return render(request, 'chart2024monthly/apr24.html')

def may(request):
    return render(request, 'chart2024monthly/may24.html')

def june(request):
    return render(request, 'chart2024monthly/jun24.html')

def july(request):
    return render(request, 'chart2024monthly/jul24.html')

def august(request):
    return render(request, 'chart2024monthly/aug24.html')


def september(request):
    return render(request, 'chart2024monthly/sep24.html')



# User updation view
def user_edit(request, list_user_id):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        staff = 'staff' in request.POST
        up_user = User.objects.get(id=list_user_id)
        up_user.username = username
        up_user.email = email
        up_user.is_staff = staff
        up_user.save()
        return redirect('coadmin')
    else:
        checked_user = User.objects.get(id=list_user_id)
        uid = checked_user
        permission = uid.user_permissions.all()
        return render(request, 'usersettings.html', {'checked_user': checked_user, 'permission': permission})


def user_delete(request, list_user_id):
    if request.method == 'POST':
        user = User.objects.get(id=list_user_id)
        user.delete()
        return redirect('coadmin')
    else:
        checked_user = User.objects.get(id=list_user_id)
        uid = checked_user
        permission = uid.user_permissions.all()
        return render(request, 'deleteuser.html', {'checked_user': checked_user, 'permission': permission})



def adduser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        staff = 'staff' in request.POST
        user = User.objects.create_user(username=username, email=email, password=password, is_staff=staff)
        user.save()
        return redirect('coadmin')
    else:
        return render(request, 'adduser.html')


def edit_results(request, game_result_id):
    if request.method == 'POST':
        result = request.POST.get('result')
        up_result = NewResult.objects.get(id=game_result_id)
        up_result.result = result
        up_result.save()
        return redirect('coadmin')
    else:
        checked_result = NewResult.objects.filter(id=game_result_id)
        return render(request, 'edit_results.html', {'checked_result': checked_result})


def delete_results(request, game_result_id):
    if request.method == 'POST':
        result = NewResult.objects.get(id=game_result_id)
        result.delete()
        return redirect('coadmin')
    else:
        checked_result = NewResult.objects.filter(id=game_result_id)
        return render(request, 'delete_results.html', {'checked_result': checked_result})


def jantri(request):
    if request.method == 'POST':
        username = request.user.username
        name = request.POST.get('name')
        whatsapp = request.POST.get('whatsapp')
        message = request.POST.get('message')
        feedback = request.POST.get('feedback')
        if not feedback:
            contact = Contacts(name=name, whatsapp=whatsapp, message=message)
            contact.save()
            return redirect('jantri')
        else:
            feedback = Feedback(username=username, feedback=feedback)
            feedback.save()
            return redirect('jantri')
    else:
        return render(request, 'vipjantri.html')

def userguide(request):
    return render(request, 'userguide.html')
