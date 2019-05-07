Data owners adding new datasets to be checked
---------------------------------------------
1. Log in or [sign up](https://github.com/join?source=header-home) for [github.com](https://github.com/)
2. Make sure your data is available on a publicly accessible url in "raw" format, such as s3 or a github [gist](https://gist.github.com/).
3. Go to https://github.com/vulekamali/data-checks
4. Click on "Create new file"

   ![Create new file button](https://github.com/vulekamali/data-checks/raw/delena-how-to-upload/docs/images/create-new-file-button.png "Create new file button")

5. Type the file name as `datapackages/<financial year>/<dataset type>/datapackage.json`, for example `datapackages/2019-20/epre/datapackage.json`

   ![File name format](https://github.com/vulekamali/data-checks/raw/delena-how-to-upload/docs/images/file-name.png "File name format")

6. Copy the following text to the new file:

   ```
   {
    "name": "<INSERT NAME OF YOUR DATA SET>",
    "schema": "tabular-data-package",
    "profile": "tabular-data-package",
    "resources": [
        {
            "path": "<INSERT URL TO YOUR DATA SET>",
            "profile": "tabular-data-resource",
            "name": "<INSERT NAME OF YOUR DATA SET>",
            "format": "csv",
            "mediatype": "text/csv",
            "encoding": "utf-8",
            "schema": "https://raw.githubusercontent.com/vulekamali/data-checks/master/schema/<INSERT TYPE OF YOUR DATA SET>.json"
        }
    ]
   }
   ```

7. Update the `name` value and the `path`, `name` and `schema` values inside the `resources` value in your new file.

   ![Filled file values](https://github.com/vulekamali/data-checks/raw/delena-how-to-upload/docs/images/file-values.png "Filled file values")

8. Scroll down to the "Commit new file" heading. Select the "Create a new branch for this commit and start a pull request." option and click on "Propose new file".

   ![Select "Create a new branch..."](https://github.com/vulekamali/data-checks/raw/delena-how-to-upload/docs/images/commit-new-file.png "Select 'Create a new branch...'")

9. On the next screen, give your pull request a descriptive title such as "Add 2019-20 EPRE data" and click on "Create pull request"

   ![Click 'Create pull request'](https://github.com/vulekamali/data-checks/raw/delena-how-to-upload/docs/images/pull-request.png "Click 'Create pull request'")

10. You should now see a section with yellow text that reads: "Some checks haven’t completed yet". Wait until the text turns either red or green.

   ![Some checks haven't completed yet](https://github.com/vulekamali/data-checks/raw/delena-how-to-upload/docs/images/checks-havent-completed.png "Some checks haven't completed yet")

  - If you see a section with green text reading "All checks have passed", your data set has passed all of the checks **successfully**:

     ![All checks have passed](https://github.com/vulekamali/data-checks/raw/delena-how-to-upload/docs/images/success.png "All checks have passed")

  - If you see a section with red text reading "All checks have failed", your data set did not pass all of the checks:

     ![All checks have failed](https://github.com/vulekamali/data-checks/raw/delena-how-to-upload/docs/images/failure.png "All checks have failed")

11. If your data set did not pass all of the checks, you can click on "details" on the first item under "All checks have failed". On the next screen, scroll down to the bottom of the screen. You should see a list of error messages generated for your data set.

     ![Error messages](https://github.com/vulekamali/data-checks/raw/delena-how-to-upload/docs/images/errors.png "Error messages")
