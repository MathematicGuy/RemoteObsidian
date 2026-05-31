Bugs in Jypyter Notebook
```sh
File "D:\CODE\IDE\Anaconda\envs\vision\lib\site-packages\ultralytics\utils\patches.py", line 86, in torch_load return _torch_load(*args, **kwargs) File "D:\CODE\IDE\Anaconda\envs\vision\lib\site-packages\torch\serialization.py", line 1097, in load return _load( File "D:\CODE\IDE\Anaconda\envs\vision\lib\site-packages\torch\serialization.py", line 1525, in _load result = unpickler.load() File "D:\CODE\IDE\Anaconda\envs\vision\lib\pathlib.py", line 962, in __new__ raise NotImplementedError("cannot instantiate %r on your system" NotImplementedError: cannot instantiate 'PosixPath' on your system
```
> Wrong file routh/path. Or Wrong path transition when you use `\` instead of `/`.
+ ? Sometime run a singl command work and in a for loop won't

+ ! This won't work
```python
directory_path = Path(os.path.join(runs_directory, run_name)) # join 2 path variables
!python detect.py --source {directory_path}/test1.jpg --weights ../dataset-pcb-runs/best3.pt --conf 0.4  
```


+ $ This work
```python
# Get the total number of .jpg files in the test_images directory  
directory_path = '../test_images'  
!python detect.py --source {directory_path}/test1.jpg --weights ../dataset-pcb-runs/best3.pt --conf 0.4  
```