:: Check if new_folder exists
if exist new_folder (
    echo Creating if_folder because new_folder has been created
    mkdir if_folder
) else (
    echo new_folder does not exist
)

:: Check if there is an if_folder. If True then create hyperionDev
:: If False then create new-projects
if exist if_folder (
    echo Creating hyperionDev because if_folder has been created
    mkdir hyperionDev
) else (
    echo Creating new-projects because if_folder does not exist
    mkdir new-projects
)
