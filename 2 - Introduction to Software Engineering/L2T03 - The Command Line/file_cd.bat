:: Create 3 new directories
mkdir new_dir_1
mkdir new_dir_2
mkdir new_dir_3

:: Change to one of the new directories and create 3 new folders inside
cd new_dir_1
mkdir dir_to_delete_1
mkdir dir_to_delete_2
mkdir dir_to_delete_3

:: Remove 2 of the newly made empty directories
:: /s is used to removes all dirs and files in the deleted dir
:: /q causes the operation to execute without additional prompts
:: I have extensive previous knowledge of bash/cmd that I used here
rmdir /s /q dir_to_delete_2
rmdir /s /q dir_to_delete_3