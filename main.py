count=1
p_1=4
p_2=4
stock=12
stock_price=5
backlog_price=25
leadtime=2
backlog=0
last_demand=4
incoming=p_2
last_backlog=0
last_order=0
while count<=20:
    print("=======================================")
    print(f"第{count}天")
    print(f"本期進貨量:{incoming}")
    print(f"上期存貨量:{stock}")
    forcast=int(input("請輸入預測量："))
    Outgoing=int(input("請輸入本出貨量："))
    backlog=int(input("請輸入缺貨量："))
    Demand=Outgoing+backlog
    print(f"需求量:{Demand}")
    a=0.8
    if backlog>0:
        targer_stock=forcast*leadtime+backlog
    else:
        target_stock=forcast*leadtime
    Order= target_stock-(stock+p_2+incoming-Demand+backlog-last_backlog)
               
    real_order=int(a*Order+(1-a)*last_order)
    if real_order<0:
        real_order=0
    
    last_demand=Demand
    
    stock=stock+incoming-Outgoing
    if stock<0:
        stock=0
    print(f"本期存貨量:{stock}")
    incoming=p_2
    p_2=p_1
    p_1=real_order
    last_order=Order
    print(f"請下訂:{real_order}")
    print(f"p_1:{p_1}")
    print(f"p_2:{p_2}")
    last_backlog=backlog
    
    count+=1
    
