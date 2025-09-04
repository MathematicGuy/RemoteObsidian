## [[HCM AI Challenge Week 1]]

## [[HCM AI Challenge Week 2]]

## [[Multimodel RAG]]


```txt

1) get_predict_video()
----------------------
Input: None
Process:
  - Check if directory 'transnetv2pt' exists.
  - If not, clone the GitHub repo: https://github.com/SlimRG/transnetv2pt.git
  - Add the cloned repo to Python path.
  - Import the 'predict_video' function from 'transnetv2pt' package.
Output: returns the 'predict_video' function.

2) process_video(video_path, output_shot_path, predict_video)
------------------------------------------------------------
Input:
  - video_path: path to an mp4 video file
  - output_shot_path: directory to store shot boundary JSON file
  - predict_video: function returned by get_predict_video()

Process:
  - Determine device ('cuda' if available else 'cpu').
  - Call predict_video(video_path, device=device) to detect shot boundaries.
  - For each scene (start_frame, end_frame), store results in a list.
  - Write results to a JSON file named '<video_name>_shots.json' inside output_shot_path.

Output:
  - JSON file with structure:
    {
      "total": <number_of_shots>,
      "items": [
         {"start_frame": X, "end_frame": Y},
         ...
      ]
    }

3) detect_shot_boundary(input_video_dir, output_shot_dir, mode, lesson_name=None)
---------------------------------------------------------------------------------
Input:
  - input_video_dir: directory containing lessons or lesson/video subfolders
  - output_shot_dir: directory to store all shot boundary JSONs
  - mode: either 'lesson' or 'all'
  - lesson_name: used only if mode='lesson'

Process:
  - Ensure output_shot_dir exists.
  - Obtain predict_video function using get_predict_video().
  - If mode='lesson':
      * Look into input_video_dir/lesson_name/video/
      * For each .mp4 file: call process_video() to generate JSON
  - If mode='all':
      * For each lesson folder inside input_video_dir:
          * Look into <lesson_folder>/video/
          * For each .mp4 file: call process_video() to generate JSON
  - Handle and log any exceptions.

Output:
  - JSON shot boundary files stored in corresponding lesson folders inside output_shot_dir.
"""
```