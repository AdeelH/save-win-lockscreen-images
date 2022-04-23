import os
import shutil
from pathlib import Path
from datetime import datetime

# There are usually a bunch of smaller images in the same place
# that are not lockscreen images. We use this size threshold to detect them.
FILE_SIZE_THRESHOLD_BYTES = 250 * 1024

username = os.getlogin()
src_dir = Path(f'C:/Users/{username}/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets') # yapf: disable
curr_date = datetime.today()
dst_dir = Path(
    f'C:/Users/{username}/Pictures/lockscreen_images/{curr_date:%Y_%m_%d}')

if not os.path.exists(src_dir):
    raise FileNotFoundError(f'Source path {src_dir} not found. '
                            'You will need to manually edit it in the script.')

os.makedirs(dst_dir, exist_ok=True)

all_files = [f for f in src_dir.iterdir() if f.is_file()]
large_files = [
    f for f in all_files if f.stat().st_size > FILE_SIZE_THRESHOLD_BYTES
]
dst_dirs = [dst_dir / f.with_suffix('.jpg').name for f in large_files]

print(f'Extracting {len(dst_dirs)} files to {dst_dir}...')
for src, dst in zip(large_files, dst_dirs):
    shutil.copyfile(src, dst)
    print(f'Extracted: {dst.name}')
os.startfile(dst_dir)
