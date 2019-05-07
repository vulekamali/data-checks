Data owners adding new datasets to be checked
---------------------------------------------
1. Log in or [sign up](https://github.com/join?source=header-home) for [github.com](https://github.com/)
2. Make sure you data is available on a publicly accessible url in "raw" format, such as s3 or a github gist.
3. Go to https://github.com/vulekamali/data-checks
4. Click on "Create new file"

   ![Create new file button](https://github.com/vulekamali/data-checks/raw/delena-how-to-upload/src/docs/images/create-new-file-button.png "Create new file button")

5. Type the file name as `datapackages/<financial year>/<dataset type>/datapackage.json`, for example `datapackages/2019-20/epre/datapackage.json`

   ![File name format](https://github.com/vulekamali/data-checks/raw/delena-how-to-upload/src/docs/images/file-name.png "File name format")

6. Copy the following text to the new file:

   ```
   {
    "name": "<INSERT NAME OF YOUR DATASET>",
    "schema": "tabular-data-package",
    "profile": "tabular-data-package",
    "resources": [
        {
            "path": "<INSERT URL TO YOUR DATASET>",
            "profile": "tabular-data-resource",
            "name": "<INSERT NAME OF YOUR DATASET>",
            "format": "csv",
            "mediatype": "text/csv",
            "encoding": "utf-8",
            "schema": "https://raw.githubusercontent.com/vulekamali/data-checks/master/schema/<INSERT TYPE OF YOUR DATASET>.json"
        }
    ]
   }
   ```

7. Update the `name` value and the `path`, `name` and `schema` values inside the `resources` values in your file.

   ![Filled file values](https://github.com/vulekamali/data-checks/raw/delena-how-to-upload/src/docs/images/file-values.png "Filled file values")

8. Under the "Commit new file" heading, select the "Create a new branch for this commit and start a pull request." option and click on "Propose new file".

   ![Select "Create a new branch..."](https://github.com/vulekamali/data-checks/raw/delena-how-to-upload/src/docs/images/commit-new-file.png "Select 'Create a new branch...'")

9. On the next screen, give your pull request a descriptive title such as "Add 2019-20 EPRE data" and click on "Create pull request"

   ![Click 'Create pull request'](https://github.com/vulekamali/data-checks/raw/delena-how-to-upload/src/docs/images/pull-request.png "Click 'Create pull request'")

10. You should now see a section that says "Some checks haven’t completed yet". Wait until the text turns red or green.