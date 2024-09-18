from plistlib import Data

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from .models import Support
# Create your views here.
def index(request):
   return render(request, 'pages/index.html')
def support(request):
   if 'search' in request.GET:
      search = request.GET['search']
      #Data = {'Posts': Post.objects.filter(question__icontains=q)}
      multiple_search = Q(Q(question__icontains=search) | Q(reply__icontains=search))
      Data = Support.objects.filter(multiple_search)
   else:
      Data = Support.objects.all()
   paginator = Paginator(Data, 1)  # Show n contacts mỗi page
   page = request.GET.get('page', 1)
   try:
      Datas = paginator.page(page)
   except PageNotAnInteger:
      # Nếu page_number không thuộc kiểu integer, trả về page đầu tiên
      Datas = paginator.page(1)
   except EmptyPage:
      # Nếu page không có item nào, trả về page cuối cùng
      Datas = paginator.page(paginator.num_pages)
   return render(request, 'pages/support.html', {'Datas':Datas})
