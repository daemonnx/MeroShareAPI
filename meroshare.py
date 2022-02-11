from MeroShareAPI import MeroShare 

def search_bank(code):
	for i in MeroShare.getBankInfo():
		if i['code'] == str(code):
			return i['id']


def check_iporesult(boid):
	liz = MeroShare.getCompany()['body'] #getCompany() returns a dict whose key "body" gives the list in ipo check website
	lenliz = len(liz)
	shareId = liz[lenliz-1]['id'] #to get the last ipo result
	shareName = liz[lenliz-1]['name']
	result = MeroShare.checkIPOResult(shareId, boid) 
	# print(result)
	# print(MeroShare.getCompany())
	if(result['success']):#if the result dict's "success" key has got True then voila share was alloted
		print(result['message'], "for", shareName)
	else:
		print(result['message'], "for", shareName)
# print('hello')
share = MeroShare('boid','your password', bank)
print('hello')
boid = share.getOwnDetails()['demat']
check_iporesult(boid) #calls the function