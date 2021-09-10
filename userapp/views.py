from django.shortcuts import render, redirect
from django.http import HttpResponse
from userapp.models import Customer, Branch, CustomerHomeAddress
from django.views.decorators.csrf import csrf_exempt
import openpyxl
import json


def index(request):
    if request.method == "GET":
        try:
            customer_data = []
            customers = Customer.objects.all()
            customers_list = list(customers.values())
            for customer in customers_list:
                customer_id = customer["id"]
                branch_customer = Branch.objects.filter(customer=customer_id)
                customer["branch"] = list(branch_customer.values())
                address_customer = CustomerHomeAddress.objects.filter(
                    customer=customer_id
                )
                customer["address"] = list(address_customer.values())
                customer_data.append(customer)

            response = {"customers": customer_data}
        except:
            response = json.dumps(
                [{"Error occurred! Please try again after adding customers"}]
            )
    return render(request, "customers/list_customers.html", response)


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
                    customer_obj.save()
                    branch = Branch(
                        customer=Customer.objects.get(id=customer_obj.id),
                        zone_name=row[4].value,
                        region_name=row[5].value,
                        area_name=row[6].value,
                        branch_name=row[7].value,
                        branch_code=row[8].value,
                    )
                    branch.save()
                    address = CustomerHomeAddress(
                        customer=Customer.objects.get(id=customer_obj.id),
                        pincode=row[9].value,
                        landmark=row[10].value,
                        address1=row[11].value,
                        address2=row[12].value,
                        address3=row[13].value,
                    )
                    address.save()

                response = redirect("/")
                return response
            else:
                return HttpResponse(
                    "File type error! Please upload file in .xlsx format!",
                    content_type="text/json",
                )
        except Exception as e:
            raise e
