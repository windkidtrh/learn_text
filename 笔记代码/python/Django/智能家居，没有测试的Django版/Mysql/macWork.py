#-*-coding:utf-8-*- 
from TestModel.models import ProductCurrentState,ManageRequest,SwitchJoinDevice,ProductBelongTo,Product#,ProductDescription

def Product_isExist_inNum2(First_type,Second_type,Product_num): 
    try:
        if len(ProductCurrentState.objects.filter(first_type=First_type,second_type=Second_type,product_num=Product_num)) == 0:
            return None
        else:
            return ProductCurrentState.objects.get(first_type=First_type,second_type=Second_type,product_num=Product_num)

    except:
        print "Product_isExist_inNum2 Error"

def Product_isExist_inNum12(First_type,Second_type,Product_num):
    try:
        if len(ManageRequest.objects.filter(first_type=First_type,second_type=Second_type,product_num=Product_num)) == 0:
            return None
        else:
            return ManageRequest.objects.get(first_type=First_type,second_type=Second_type,product_num=Product_num)

    except:
        print "Product_isExist_inNum12 Error"

def Product_isExist_inNum11(First_type,Second_type,Product_num):
    try:
        if len(SwitchJoinDevice.objects.filter(first_type=First_type,second_type=Second_type,product_num=Product_num)) == 0:
            return None
        else:
            return SwitchJoinDevice.objects.filter(first_type=First_type,second_type=Second_type,product_num=Product_num)

    except:
        print "Product_isExist_inNum11 Error"
# def Product_inNum8(First_type,Second_type):
#     try:
#         conn=mysql.connect_mysql()
#         cur = conn.cursor()
#         sql1="select * from product_description where (first_type,second_type) in (('%s','%s'))"%(First_type,Second_type)
#         cur.execute(sql1)
#         result = cur.fetchone()
#         conn.commit()
#         cur.close()
#         return result

#     except MySQLdb.Error,e:
#         print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Product_isExist_inNum4(First_type,Second_type,Product_num,User_id):
    try:
        if len(ProductBelongTo.objects.filter(first_type=First_type,second_type=Second_type,product_num=Product_num,user_id=User_id)) == 0:
            return None
        else:
            return ProductBelongTo.objects.get(first_type=First_type,second_type=Second_type,product_num=Product_num,user_id=User_id)

    except:
        print "Product_isExist_inNum4 Error"

def Product_isExist_inNum1(First_type,Second_type,Product_num):
    try:
        if len(Product.objects.filter(first_type=First_type,second_type=Second_type,product_num=Product_num)) == 0:
            return None
        else:
            return Product.objects.get(first_type=First_type,second_type=Second_type,product_num=Product_num)
        # conn=mysql.connect_mysql()
        # cur = conn.cursor()
        # sql1="select * from product where (first_type,second_type,product_num) in (('%s','%s','%s'))"%(First_type,Second_type,Product_num)
        # cur.execute(sql1)
        # result = cur.fetchone()
        # conn.commit()
        # cur.close()
        # return result

    except:
        print "Product_isExist_inNum1 Error"

def Register_mac(First_type,Second_type,Product_num,Current_state,Ip_address,Net_port):
   # return "hah1"
    try:
        ProductCurrentState.objects.create(first_type=First_type,second_type=Second_type,product_num=Product_num,current_state=Current_state,ip_address=Ip_address,net_port=Net_port,online_value=2)
        # conn=mysql.connect_mysql()
        # cur = conn.cursor()
        # sql1="insert into product_current_state(first_type,second_type,product_num,current_state,ip_address,net_port,online_value) values ('%s','%s','%s','%s','%s','%s','%s')"%(First_type,Second_type,Product_num,Current_state,Ip_address,Net_port,2)
        # cur.execute(sql1)
        # conn.commit()
        # cur.close()

    except:
        print "Register_mac Error"

def Update_mac(First_type,Second_type,Product_num,Current_state,Ip_address,Net_port):
   # return "hah1"
    try:
        ProductCurrentState.objects.filter(first_type=First_type,second_type=Second_type,product_num=Product_num).update(current_state=Current_state,ip_address=Ip_address,net_port=Net_port,online_value=2)
        # conn=mysql.connect_mysql()
        # cur = conn.cursor()
        # sql1="update product_current_state set current_state='%s',ip_address='%s',net_port='%s',online_value='%s' where (first_type,second_type,product_num) in (('%s','%s','%s'))"%(Current_state,Ip_address,Net_port,2,First_type,Second_type,Product_num)
        # cur.execute(sql1)
        # conn.commit()
        # cur.close()

        # cur = conn.cursor()
        # sql2="select belong_id from product_current_state where (first_type,second_type,product_num) in (('%s','%s','%s'))"%(First_type,Second_type,Product_num)
        # cur.execute(sql2)
        # result = cur.fetchone()
        # conn.commit()
        # cur.close()

        # cur = conn.cursor()
        # sql3="select * from product_belong_to where (first_type,second_type,product_num) in (('%s','%s','%s'))"%(First_type,Second_type,Product_num)
        # cur.execute(sql3)
        # result1 = cur.fetchone()
        # conn.commit()
        # cur.close()

        # if result1 != None:
        #     cur = conn.cursor()
        #     sql4="update product_belong_to set user_id='%s' where (first_type,second_type,product_num) in (('%s','%s','%s'))"%(result[0],First_type,Second_type,Product_num)
        #     cur.execute(sql4)
        #     conn.commit()
        #     cur.close()
        # else:
        #     pass
    except:
        print "Update_mac Error"

def Update_Return_value(First_type,Second_type,Product_num,Request):
   # return "hah1"
    try:
        ManageRequest.objects.filter(first_type=First_type,second_type=Second_type,product_num=Product_num).update(return_value=Request)
        # conn=mysql.connect_mysql()
        # cur = conn.cursor()
        # sql1="update manage_request set return_value='%s' where (first_type,second_type,product_num) in (('%s','%s','%s'))"%(Request,First_type,Second_type,Product_num)
        # cur.execute(sql1)
        # conn.commit()
        # cur.close()

    except:
        print "Update_Return_value Error"

def Mac_is_not_in():
    try:
        result = ProductCurrentState.objects.all()
        if len(result) == 0:
            pass
        else:
            for i in result:
                ProductCurrentState.objects.filter(belong_id = i.belong_id).update(online_value= i.online_value-1)
            ProductCurrentState.objects.filter(online_value=0).delete()

    except:
        print "Mac_is_not_in Error"