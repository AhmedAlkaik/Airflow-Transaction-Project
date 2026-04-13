def trans_report_gen():
    transactions = [120, 300, 450, 200]
    total = sum(transactions)
    count = len(transactions)
    report = f'Daily transaction report\nNumber of transactions:{count}\nTotal amount : {total}'

    with open('/data/transactions_report.txt', 'w') as file:
        file.write(report)
        
    print("Report successfully saved!")