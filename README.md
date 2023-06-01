# google_translate_api
py script to translate .csv file by google translate free api


# How it works
By calling Google Cloud Translate REST API
`https://translation.googleapis.com/language/translate/v2`

See details here: https://cloud.google.com/translate/docs/reference/rest/v2/translate


# Authentication / security
In order to call Google Cloud Translate API, a token / API key is needed based on OAuth 2.0 authentication.  In order not to commit the keys, and since the token expires every hour, see "First time and every hour" setup

# How to use
* The first thing to do is to get a token:
    * you should take your yoken from here:
    * https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcloud-platform+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcloud-translation&access_type=offline
    * login with your g acccount
    * go to Step 2Exchange authorization code for tokens and tap Exchange authorization code for tokens
    * go back to step 2 and copy Access token
    * put access token to token varaible

* You need to pass the path to your csv file to be translated (don't forget to specify which column to translate/remove this line if the whole file is to be translated)
* Also write the path to your output file which you want the translation to be written to.
* The rest will be done by the script, enjoy
