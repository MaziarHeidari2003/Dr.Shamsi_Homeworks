siteName = input("Enter the site URL, please: ")
x = siteName[:11]
y = siteName[-4:]
z = siteName[11:-4]
if x == 'http://www.' and y == '.com':
    print(z)
else:
    print('there is something wrong with your url')    

