import urllib.request
import urllib.parse
import urllib.error


# url = 'http://www.maodan.com/'
url = 'https://stackoverflow.com/quesions/3448112/django-python-error-importerror-import-by-filename-is-not-suppo'

try:

    response = urllib.request.urlopen(url)

    print(response)

except urllib.error.HTTPError as e:
    print(e)
    print(e.code)

except urllib.error.URLError as e:
    print(e)

