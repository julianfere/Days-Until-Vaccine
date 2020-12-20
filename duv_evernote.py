from evernote.api.client import EvernoteClient

dev_token='S=s1:U=963af:E=17dd6895e3e:C=1767ed83010:P=1cd:A=en-devtoken:V=2:H=de06e37cdbe6afa4a5295c0691f47a5a'

client = EvernoteClient(token=dev_token)
userStore = client.get_user_store()
user = userStore.getUser()
print (user.username)

