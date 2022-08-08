import os
import requests
import logging
import json
import urllib.request
from dotenv import dotenv_values
from progress.bar import Bar

logging.basicConfig(level=logging.INFO)
dist_dir_path = './dist'

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}
request_headers = { 'Authorization': f'Client-ID {config["ACCESS_KEY"]}'}

def fetch_photos():
    query_params = { 'query': 'baklava', 'per_page': 500 }
    response = requests.get(config["IMAGE_API"], params=query_params, headers=request_headers)
    return response.json()


def pick_result_data(result):
    relevant_keys = ['id', 'width', 'height']
    filtered_result = { relevant_key: result[relevant_key] for relevant_key in relevant_keys }
    filtered_result["image_url"] = result["urls"]["regular"]
    filtered_result["labels"] = ['baklava']
    filtered_result["download_link"] = result["links"]["download"]
    return filtered_result


def format_response(raw_data_json):
    raw_results = raw_data_json["results"]
    formatted_results = [pick_result_data(result) for result in raw_results]
    return formatted_results


def save_photo_to_disk(id, url):
    urllib.request.urlretrieve(url, f'./dist/{id}.jpg')


def save_data_to_disk(photo_data):
    # Save JSON
    os.makedirs(dist_dir_path, exist_ok=True)
    with open('./dist/data.json', 'w') as f:
        json.dump(photo_data, f)
        
    # Save Photos
    total_photos = len(photo_data)
    logging.info(f'Total Photos: {total_photos}')
    bar = Bar('Processing', max=total_photos)
    for photo in photo_data:
        save_photo_to_disk(photo['id'], photo['download_link'])
        bar.next()
    bar.finish()


def clean_dist():
    logging.info(f'Cleaning {dist_dir_path}')
    isDirectoryExisting = os.path.exists(dist_dir_path)
    if isDirectoryExisting:
        for file_name in os.listdir(dist_dir_path):
            file = os.path.join(dist_dir_path, file_name)
            os.remove(file)


def init():
    clean_dist()
    raw_photos_data_json = fetch_photos()
    formatted_photo_data = format_response(raw_photos_data_json)
    save_data_to_disk(formatted_photo_data)

if __name__=="__main__":
    init()