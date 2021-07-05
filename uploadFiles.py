import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AzkcpbVHMbrNwJcDGr4zRvO2BFMbD_XEaY03rJHrdVL43mTMdt4PJK0WJBDd8d033zI3mJ-lug31tg3tZwg4igtS1RXkjUA9k_hJBkwjU5zvstTGKwUD6J3eJIJoKe_EWnjHIg4'
    transferData = TransferData(access_token)

    file_from = input('enter the file path to transfer: ')
    file_to = input("enter the path to upload to dropbox: ")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("the file has been moved")

main()