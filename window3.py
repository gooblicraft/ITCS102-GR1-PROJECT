import os
from openpyxl import load_workbook

def load_account_data(account_id):
    try:
        wb = load_workbook("AccountDatabase.xlsx")
        ws = wb.active

        headers = [cell.value for cell in ws[1]]

        for row in ws.iter_rows(min_row=2, values_only=True):
            current_id = str(row[0]).strip()
            if current_id == account_id:
                print(f"Details for Account ID: {account_id}")
                for header, value in zip(headers, row):
                    
                    # if header == "ID Number":
                    #     accountID = value
                    #     print(f"Account ID: {accountID}")
                    # elif header == "Account Type":
                    #     accountType = value
                    #     print(f"Account Type: {accountType}")
                     print(f"{header}: {value}")
                return

        print(f"Account ID {account_id} not found.")

    except FileNotFoundError:
        print("ERROR: AccountDatabase.xlsx not found.")

if __name__ == "__main__":
    account_id = os.environ.get("ACCOUNT_ID")
    
    if not account_id:
        print("ERROR: ACCOUNT_ID environment variable not set.")
    else:
        load_account_data(account_id)
