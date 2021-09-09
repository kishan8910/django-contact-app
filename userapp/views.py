from django.shortcuts import render
from django.http import HttpResponse
from userapp.models import Customer
from django.views.decorators.csrf import csrf_exempt
import openpyxl
import json


def index(request):
    if request.method == "GET":
        try:
            customer = Customer.objects.all()
            # response = customer
            response = "hi"
        except:
            response = json.dumps(
                [{"Error occurred! Please try again after adding customers"}]
            )
    return HttpResponse(response, content_type="text/json")


@csrf_exempt
def import_data(request):
    if request.method == "POST":
        excel_file = request.FILES["excel_file"]
        try:
            if (
                excel_file.content_type
                == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            ):
                wb = openpyxl.load_workbook(excel_file)

                # getting default sheet
                worksheet = wb.active

                # excel_data = list()
                # iterating over the rows and
                # getting value from each cell in row
                worksheet_data = worksheet.iter_rows()
                # skip the first row
                next(worksheet_data)
                for row in worksheet_data:
                    row_data = list()
                    customer_obj = Customer(
                        customer_name=row[0].value,
                        father_name=row[1].value,
                        customer_profile=row[2].value,
                        loan_account_number=row[3].value,
                    )
                    customer.save()
                    branch = Branch(
                        customer=customer_obj.id,
                        zone_name=row[4].value,
                        region_name=row[5].value,
                        area_name=row[6].value,
                        branch_name=row[7].value,
                        branch_code=row[8].value,
                    )
                    branch.save()
                    address = CustomerHomeAddress(
                        customer=customer_obj.id,
                        pincode=row[9].value,
                        landmark=row[10].value,
                        address1=row[11].value,
                        address2=row[12].value,
                        address3=row[13].value,
                    )
                    address.save()

                    # for cell in row:
                    #     row_data.append(str(cell.value))
                    # excel_data.append(row_data)

                return HttpResponse(excel_data, content_type="text/json")
            else:
                return HttpResponse(
                    "File type error! Please upload file in .xlsx format",
                    content_type="text/json",
                )
        except Exception as e:
            raise e
