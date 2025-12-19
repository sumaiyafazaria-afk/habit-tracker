@echo off
setlocal

set "DEFAULT_ROOT=C:\Program Files\MySQL"
set "FOUND_PATH="

if exist "%DEFAULT_ROOT%" (
    echo Searching in %DEFAULT_ROOT%...
    :: Loop through folders looking for bin\mysql.exe
    for /d %%D in ("%DEFAULT_ROOT%\MySQL Server*") do (
        if exist "%%D\bin\mysql.exe" (
            set "FOUND_PATH=%%D\bin"
            goto :Success
        )
    )
)

echo MySQL not found in standard locations.
goto :End

:Success
echo Found MySQL at: %FOUND_PATH%

:End
pause