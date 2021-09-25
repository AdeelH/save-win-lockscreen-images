import os
import shutil
from pathlib import Path

# There are usually a bunch of smaller images in the same place
# that are not lockscreen images. We use this size threshold to detect them.
FILE_SIZE_THRESHOLD_BYTES = 250 * 1024

username = os.getlogin()
src_path = Path(f'C:/Users/{username}/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets') # yapf: disable
dst_path = Path(f'C:/Users/{username}/Pictures/lockscreen_images')

if not os.path.exists(src_path):
    raise FileNotFoundError(f'Source path {src_path} not found. '
                            'You will need to manually edit it in the script.')

os.makedirs(dst_path, exist_ok=True)

all_files = [f for f in src_path.iterdir() if f.is_file()]
large_files = [
    f for f in all_files if f.stat().st_size > FILE_SIZE_THRESHOLD_BYTES
]
dst_paths = [dst_path / f.with_suffix('.jpg').name for f in large_files]

for src, dst in zip(large_files, dst_paths):
    shutil.copyfile(src, dst)
    print(f'Extracted: {dst.name}')
