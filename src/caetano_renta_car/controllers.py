from flask import request, jsonify
from .. import  dbt 
from   .ad_controlers import * 
from .advertiser_controller import *
from  .models import Announcement , Advertiser , Location
 

def  list_all_tables_Announcemet ():
  dataformAnnot = Announcement.query.all()
  form = []
  for x in dataformAnnot :
     form.append(x.to_dict())
  
   
def list_all_tables_advertiser():
  dataformAdveriser= Advertiser.query.all()
  formAdvert=[]
  
  for x in dataformAdveriser:
     formAdvert.append(x.to_dict())
  
  return jsonify(formAdvert)


def list_all_tables_location():
   data_location = Location.query.all()
   form_location=[]  
   for x in data_location :
      form_location.append(x.to_dict())

   return jsonify( form_location)   


def create_tables ():
   tables_ad=[]
   tables_loc=[]
   tables_annc=[]
   request_form = request.form.to_dict()
  
   for x in range ( 1,12,3):
       table_advertiser= Advertiser( contact=adress[x] ,company_name= name )
       tables_ad.append(table_advertiser)
   for  tables in tables_ad:
      dbt.session.add(tables)
   
   for  y in range(0 , 12 ,3):
      table_loct = Location( county= adress[y+1],t_advertiser_id_advertiser=table_advertiser.id_advertiser)
      print(table_loct)

      tables_loc.append(table_loct)
   for  tablesx in tables_loc:
      dbt.session.add(tablesx)
   

 
   for  z in range( 0, TOTAL_ANUNCIOS):
      table_ad = Announcement(
                               brand=marca_carro[z][0].text,  
                               passenger_number=numero_lugares[z][0].text,
                               price=preco[z][0].text,
                               extra_fees=taxas_extras[z][0].text ,
                               fuel_type=numero_lugares[z][1].text,
                               t_advertiser_id_advertiser=table_advertiser.id_advertiser
                              )
      tables_annc.append(table_ad)
   for  tablesy in tables_annc:
      dbt.session.add(tablesy)
   
   dbt.session.commit()


def delete_account_controller(account_id):
    Advertiser.query.filter_by(id=account_id).delete()
    dbt.session.commit()