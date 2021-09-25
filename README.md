# Windows lockscreen image extractor

Windows spotlight often turns up some great pictures that you might want to save permanently to, say, use as a desktop background. This simple Python script for automatically extracts these images from the hellish depths of `AppData/Local` to your `Pictures` folder.

## How it works
The script performs the following steps:
1. Detect files in `C:/Users/{username}/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets`.
2. Filter out irrelevant (smaller than 250 KB) files.
3. Copy over these files to `C:/Users/{username}/Pictures/lockscreen_images` with the `.jpg` extension added.
