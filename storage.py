from google.cloud import storage
client = storage.Client()
# https://console.cloud.google.com/storage/browser/[bucket-id]/
bucket = client.get_bucket('gs://test-764cc.appspot.com')
# Then do other things...
#blob = bucket.get_blob('images/canada.jpg')
print(blob.download_as_string())
#blob.upload_from_string('New contents!')
#blob2 = bucket.blob('remote/path/storage.txt')
#blob2.upload_from_filename(filename='/local/path.txt')
