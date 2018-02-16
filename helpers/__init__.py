from helpers import Forms, Error_helper, Request_handling


# WTForms
def Reg_form():
    return Forms.Register_Form()
def Login_form():
    return Forms.Login_Form()

# Request data
def Load_data(r):
    return Request_handling._Request_data(r)

# Error_helper
def Error(content="Error occured", error='REQUEST', status=400):
    return Error_helper._Get_error(content, error, status)