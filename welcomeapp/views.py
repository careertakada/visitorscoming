from os import times
from django.shortcuts import render, redirect
from sklearn.metrics import precision_score
from .models import Visitors

from django.views.generic import TemplateView # テンプレートタグ
from .forms import AccountForm, AddAccountForm # ユーザーアカウントフォーム
# ログイン・ログアウト処理に利用
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def input(request):
    return render(request, 'input.html')

def output(request):
    if request.method == 'POST':
        name = request.POST.get('input_name')
        name1 = request.POST.get('company')
        name2 = request.POST.get('person')
        name3 = request.POST.get('tantousya')
        name4 = request.POST.get('douhan')
        name5 = request.POST.get('text1')
        name6 = request.POST.get('dates')
        name7 = request.POST.get('time')
        name8 = request.POST.get('affair1')
        name9 = request.POST.get('affair2')
        name10 = request.POST.get('douhan1')
        name11 = request.POST.get('douhan2')
        Visitors.objects.create(person_name=name,company=name1,douhan=name4,text1=name5,person=name2,dates=name6,\
            times=name7,tantousya=name3,affair1=name8,affair2=name9,douhan1=name10,douhan2=name11)
        context = {
            'output_name': name,
            'company_name': name1,
            'person': name2,
            'tantousya': name3,
            'douhan': name4,
            'text1': name5,
            'dates': name6,
            'time': name7,
            'affair1':name8,
            'affair2':name9,
            'douhan1': name10,
            'douhan2': name11

            }
        print(name)
        print(context)


    return render(request, 'output.html', context)

    
     
def kanri(request):
   visitors_list=Visitors.objects.all()
   context={'visitors':visitors_list}
   return render(request, 'kanri.html', context) 

def edit(request, pk):
    visitor_object=Visitors.objects.get(id=pk)
    if request.method == 'POST':
        name=request.POST.get('edit1')
        company_name=request.POST.get('edit2')
        ninzu=request.POST.get('edit3')
        entry_time=request.POST.get('edit4')
        texts=request.POST.get('edit25')
        accompany=request.POST.get('edit5')
        texts1=request.POST.get('edit26')

        print(name)
        print(company_name)

        visitor_object.person_name=name
        visitor_object.company=company_name
        visitor_object.person=ninzu
        visitor_object.visit_time=entry_time
        visitor_object.affair1=texts
        visitor_object.accompany=accompany
        visitor_object.affair2=texts1
        visitor_object.save()
        return redirect('kanri')

    else:
        # 下にcontextを後で追加
        context={'visitor':visitor_object}

        return render(request, 'edit_del.html', context)

def delete(request, pk):
    visitor_object=Visitors.objects.get(id=pk)
    print(visitor_object)
    visitor_object.delete()
    print(visitor_object)
    return redirect('kanri')

class  AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        "add_account_form":AddAccountForm(),
        }

    # Get処理
    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        return render(request,"register.html",context=self.params)

    # Post処理
    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)

        # フォーム入力の有効検証
        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            # アカウント情報をDB保存
            account = self.params["account_form"].save()
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()

            # 下記追加情報
            # 下記操作のため、コミットなし
            add_account = self.params["add_account_form"].save(commit=False)
            # AccountForm & AddAccountForm 1vs1 紐付け
            add_account.user = account

            # 画像アップロード有無検証
            if 'account_image' in request.FILES:
                add_account.account_image = request.FILES['account_image']

            # モデル保存
            add_account.save()

            # アカウント作成情報更新
            self.params["AccountCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,"register.html",context=self.params)

    #ログイン
def Login(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('home'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'login.html')
@login_required
def testview(request):
    user = request.user



#ログアウト
@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('Login'))


#ホーム
@login_required
def home(request):
    params = {"userid":request.user}
    print(params)
    return render(request, "loginhome.html",context=params)


#新規登録
class  AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        "add_account_form":AddAccountForm(),
        }

    #Get処理
    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        return render(request,"register.html",context=self.params)

    #Post処理
    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)

        #フォーム入力の有効検証
        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            # アカウント情報をDB保存
            account = self.params["account_form"].save()
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()

            # 下記追加情報
            # 下記操作のため、コミットなし
            add_account = self.params["add_account_form"].save(commit=False)
            # AccountForm & AddAccountForm 1vs1 紐付け
            add_account.user = account

            # 画像アップロード有無検証
            if 'account_image' in request.FILES:
                add_account.account_image = request.FILES['account_image']

            # モデル保存
            add_account.save()

            # アカウント作成情報更新
            self.params["AccountCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,"register.html",context=self.params)