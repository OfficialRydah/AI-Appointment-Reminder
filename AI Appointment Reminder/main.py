from voice import make_call

for _, row in due.iterrows():

    make_call(
        row["Client_Name"],
        row["Phone_Number"]
    )
