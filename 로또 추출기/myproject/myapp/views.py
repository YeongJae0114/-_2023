from django.shortcuts import render


def home(request):
    return render(request,'index.html')

def lotto(request):
    import random
    lotto_num=[]
    game = request.GET.get('game')
    pull_num=[index for index in range(1,46)]

    for _ in range(int(game)):
        lotto_num.append(random.sample(pull_num,6))

    return render(request,'lotto.html',{'lotto_num' : lotto_num, 'game' : game})
