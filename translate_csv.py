import csv
import requests
import traceback


class GoogleTranslate:
    translate_url = "https://translation.googleapis.com/language/translate/v2"
    token = "<token>"
    
    # you should take your yoken from here:
    # https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcloud-platform+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcloud-translation&access_type=offline
    # login with your g acccount
    # go to Step 2 "Exchange authorization code for tokens" and tap "Exchange authorization code for tokens"
    # go back to step 2 and copy "Access" token
    # put access token to token varaible

    def _send_request(self, text_to_translate, target, source=None, format_type=None):
        """ Sends a request to Google Translate API with the given parameters """
        querystring = {"q": text_to_translate, "target": target}

        if source:
            querystring["source"] = source

        if format_type:
            querystring["format"] = format_type

        headers = {'Authorization': f'Bearer {self.token}', 'Host': "translation.googleapis.com"}

        return requests.request("GET", self.translate_url, headers=headers, params=querystring)

    @staticmethod
    def _parse_translate_response(resp_json):
        """ Parses the translated text from the response received from Google API """
        if resp_json.get('data'):
            return resp_json['data']['translations'][0]['translatedText']
        elif resp_json.get('error'):
            raise ValueError("ERROR: " + str(resp_json['error']))
        else:
            raise ValueError('ERROR: unknown parsing error of the response: ' + resp_json)

    def translate(self, text_to_translate, target, source=None, format_type=None):
        assert text_to_translate is not None
        assert target
        response = self._send_request(text_to_translate, target, source, format_type)
        if not response.ok:
            response.raise_for_status()
        return self._parse_translate_response(response.json())
    
    def __init__(self, token=token, url=translate_url):
        self.translate_url = url
        self.token = token


def read_csv(file_path):
    """Читает CSV-файл и возвращает его содержимое в виде списка словарей."""
    with open(file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)
    return rows


def translate_csv(input_file_path, output_file_path, target_language):
    try:
        translator = GoogleTranslate(token="<your_token>")
        rows = read_csv(input_file_path)
        with open(output_file_path, "w", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=rows[0].keys())
            writer.writeheader()
            for row in rows:
                text_to_translate = list(row.values())[1]
                translation = translator.translate(text_to_translate, target_language, source=None, format_type="text")
                row["Translation"] = translation
                writer.writerow(row)

    except Exception:
        print(traceback.print_exc())


def main():
    input_file_path = "../resources/table_search_results.csv"
    output_file_path = "../resources/table_search_results(en).csv"
    target_language = "en"  # language dectination code
    translate_csv(input_file_path, output_file_path, target_language)


if __name__ == "__main__":
    main()
