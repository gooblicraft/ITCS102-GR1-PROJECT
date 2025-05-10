def delete_account_data(account_id):
    confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this account?")
    if not confirm:
        return

    try:
        wb = load_workbook("AccountDatabase.xlsx")
        ws = wb.active

        for row_idx, row in enumerate(ws.iter_rows(min_row=2), start=2):
            if str(row[0].value).strip() == account_id:
                ws.delete_rows(row_idx)
                wb.save("AccountDatabase.xlsx")
                messagebox.showinfo("Deleted", "Account has been deleted.")
                logOut()  # Return to login or main screen
                return
        messagebox.showerror("Error", "Account ID not found.")

    except FileNotFoundError:
        messagebox.showerror("Error", "AccountDatabase.xlsx not found.")


delete_button_image = PhotoImage(file="assets\\window3\\account_tab\\image_btn_delete.png")
delete_button = Button(tab1, image=delete_button_image, borderwidth=0, highlightthickness=0,
                       relief="flat", command=lambda: delete_account_data(account_id))
delete_button.place(x=32, y=420)