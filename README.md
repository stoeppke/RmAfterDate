# Auto delegating a folders content every day
Creating the folder  ```~/Desktop/DeleateByDate_YYYY-MM-DD/``` and delegating its content every day at 23:59. Files and folders in there named ```YYYY-MM-DD``` will be deleted only after tha date of their name.
All of this is packed to a .pkg file using [munki-pkg](https://github.com/munki/munki-pkg) and can be installed on any Mac.
## Disable this script
Installed is a python script and a launchd job. To disable the script just disable the launchd job:
```bash
launchctl disable gui/$(id -u $USER)/com.knowunity.dev.pkg.RmAfterDate
launchctl bootout gui/$(id -u $USER)/com.knowunity.dev.pkg.RmAfterDate
rm $HOME/Library/LaunchAgents/com.knowunity.dev.pkg.RmAfterDate.plist
rm -rf /Library/Knowunity/
```
## Locations touched
Files or folders are written to:
* ```/Library/Knowunity/```
* ```~/Library/LaunchAgents/```
* ```~/Desktop/DeleateByDate_YYYY-MM-DD/```

A launchd daemon called ```com.knowunity.dev.pkg.RmAfterDate``` is started under the targed gui/$UID. 

## Build
To build the .pkg file run:
```bash
git clone https://github.com/stoeppke/RmAfterDate
git clone https://github.com/munki/munki-pkg.git
python3 ./munki-pkg/munkipkg ./RmAfterDate
```
