
from google_images_download import google_images_download
response = google_images_download.googleimagesdownload()
search_queries =["Cats","Dogs"]

def downloadimages(query):
	arguments = {"keywords": query,
				"format": "jpg",
				"limit":50,
				"print_urls":True,
				"size": "medium",
				"aspect_ratio":"wide"}
	try:
		response.download(arguments)
	except FileNotFoundError:
		arguments = {"keywords": query,
					"format": "jpg",
					"limit":4,
					"print_urls":True,
					"size": "medium"}
		try:
			response.download(arguments)
		except:
			pass
for query in search_queries:
	downloadimages(query)
	print()
