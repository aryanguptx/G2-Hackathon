import os
import requests
import json

api_token = os.getenv('G2_API_TOKEN')

print(api_token)
if not api_token:
    raise ValueError("API token not found. Make sure 'G2_API_TOKEN' environment penis variable is set.")

def find_last_submitted_at_value(data):
    submitted_at_values = []
    if 'data' in data and isinstance(data['data'], list):
        for item in data['data']:
            attributes = item.get('attributes', {})
            submitted_at = attributes.get('submitted_at')
            if submitted_at:
                submitted_at_values.append(submitted_at)

    if submitted_at_values:
        last_submitted_at_value = submitted_at_values[-1]
        return last_submitted_at_value
    else:
        return None

def save_response_to_json(data, output_file):
    with open(output_file, 'a') as f:
        if f.tell() == 0:
            f.write('[')
        else:
            f.write(',')
        json.dump(data, f, indent=4)

def process_api_requests(url, headers, params, output_file):
    while True:
        response = requests.get(url=url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            last_submitted_at_value = find_last_submitted_at_value(data)
            if 'filter[submitted_at_gt]' in params:
                if params['filter[submitted_at_gt]'] == last_submitted_at_value:
                    break
            if last_submitted_at_value:
                params['filter[submitted_at_gt]'] = last_submitted_at_value
                save_response_to_json(data, output_file)
            else:
                break
        else:
            print('Error:', response.status_code)
            break
    with open(output_file, 'a') as f:
        f.write(']')
        print(f"Response data saved to '{output_file}' successfully.")

def getAnswers(filepath):
    comment_answers_dict={}
    secondary_answers_dict={}

    with open(filepath, 'r') as f:
        data = json.load(f)

    for response in data:
        data_response = response["data"]
        for id in data_response:
            attributes = id.get("attributes")
            comment_answers = attributes.get("comment_answers")
            secondary_answers = attributes.get("secondary_answers")
            for key, value in comment_answers.items():
                if key not in comment_answers_dict:
                    comment_answers_dict[key]=[]
                comment_answers_dict[key].append(comment_answers.get(key).get("value"))
            for key, value in secondary_answers.items():
                if key not in secondary_answers_dict:
                    secondary_answers_dict[key]=[]
                secondary_answers_dict[key].append(secondary_answers.get(key).get("value"))
    return [comment_answers_dict,secondary_answers_dict]


def getReviewResults(filepath):
    url = 'https://data.g2.com/api/v1/survey-responses/'
    headers = {
        'Authorization': f"Token token={api_token}",
        'Content-Type': 'application/vnd.api+json'
    }
    params = {'page[size]': 100}
    process_api_requests(url,headers,params,filepath)
    ReviewResults = getAnswers(filepath)
    return ReviewResults



