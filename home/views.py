from django import template
from django.contrib.auth.decorators import login_required
from core.decorators import teacher_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import redirect, render
from home.forms import FileUploadForm
from home.review_test.review import review_file
from home.review_test.rubric import create_rubric
import zipfile, os, io
import pandas as pd
from openpyxl import Workbook
import json
from django.http import JsonResponse
from django.core.mail import send_mail

@login_required(login_url="auth/login/")
def homepage(request):
    return redirect('core:courses_view')
        

@login_required(login_url="auth/login/")
def index(request):
    context = {'segment': 'index'}
    if (request.user.is_superuser):
        return redirect('core:tests_view')
        # html_template = loader.get_template('home/index.html')
        # return HttpResponse(html_template.render(context, request))
    else:
        return redirect('core:tests_student')


@login_required(login_url="auth/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split('/')[-1]
        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        elif load_template == 'success':
            return HttpResponseRedirect(reverse('home:sucess'))
        elif load_template == 'upload_files.html':
            form = FileUploadForm()
            if request.method == 'POST':
                form = FileUploadForm(request.POST, request.FILES)
                rubric_raw = request.FILES['rubric']
                rubric = create_rubric(rubric_raw)
                zip_tests = request.FILES['zip_file']
                with zipfile.ZipFile(zip_tests, 'r') as zip_ref:
                    temp_dir = 'temp_dir/'
                    zip_ref.extractall(temp_dir)
                    pre_results = []
                    for root, dirs, files in os.walk(temp_dir):
                        print('Root', root)
                        #print(files)
                        for filename in files:
                            if not root.startswith('temp_dir/__'):
                                test_path = os.path.join(root, filename)
                                #test_file = pd.read_excel(file_path)
                                if test_path.endswith('.xlsx') or filename.endswith('.xls'):
                                    temp=review_file(test_path,rubric)
                                    pre_results.append(temp)
                preg = ['P' + str(i) for i in range(1,len(pre_results[0]))]
                cols = ['Correo'] + preg
                results = pd.DataFrame(data = pre_results,columns = cols)
                results_json = results.to_json(orient='records')
                context['results'] = 'results'
                print(results_json)
                request.session['excel_data'] = results_json
                if form.is_valid():
                    form.save()
                    print('FORM SAVEDDDDD')
                    context['correct'] = 'correct'
                    #return HttpResponseRedirect(reverse('home:sucess'))
                    '''
                    output = io.BytesIO()
                    with pd.ExcelWriter(output, engine='openpyxl') as writer:
                        results.to_excel(writer, index=False)
                    output.seek(0)

                    # Return the Excel file as an HTTP response
                    response = HttpResponse(output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                    response['Content-Disposition'] = 'attachment; filename="downloaded_data.xlsx"'
                    return response
                    '''
                else:
                    context['form'] = form
            else:
                context['form'] = form

        context['segment'] = load_template
        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="auth/login/")
def success_view(request):
    context={}
    html_template = loader.get_template('home/success.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="auth/login/")
def download_excel(request):
    # Retrieve the data from the session
    json_data = request.session.get('excel_data')

    # Check if there is data to create the Excel file
    if not json_data:
        # Handle the case where there is no data (e.g., return an error or a different response)
        return HttpResponse("No data available for download.", status=404)


    df = pd.read_json(json_data, orient='records')

    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)

    # Rewind the buffer
    output.seek(0)

    # Set up HTTP response with the Excel file
    response = HttpResponse(output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="downloaded_data.xlsx"'

    return response


