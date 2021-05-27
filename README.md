## Installation

* Clone the repo. All further steps should be performed while in the `AutoSub/` directory
    ```bash
    $ git clone https://github.com/akashmeshram/potential-funicular.git
    $ cd potential-funicular
    ```
* Create a pip virtual environment to install the required packages
    ```bash
    $ python3 -m venv sub
    $ source sub/bin/activate
    $ pip3 install -r requirements.txt
    ```
* Download the model and scorer files from DeepSpeech repo. The scorer file is optional, but it greatly improves inference results.
    ```bash
    # Model file (~190 MB)
    $ wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
    # Scorer file (~950 MB)
    $ wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer
    ```
* Create two folders `audio/` and `output/` to store audio segments and final SRT file
    ```bash
    $ mkdir audio output
    ```
* Install FFMPEG. If you're running Ubuntu, this should work fine.
    ```bash
    $ sudo apt-get install ffmpeg
    ```
    
* [OPTIONAL] If you would like the subtitles to be generated faster, you can use the GPU package instead. Make sure to install the appropriate [CUDA](https://deepspeech.readthedocs.io/en/v0.9.3/USING.html#cuda-dependency-inference) version. 
    ```bash
    $ source sub/bin/activate
    $ pip3 install deepspeech-gpu
    ```

## Docker

* Installation using Docker is pretty straight-forward. The `model` build-arg configures which model and scorer versions to use. You can manually edit them to point to other model files easily. 
    ```bash
    $ docker build --build-arg model=0.9.3 -t ds-stt .
    $ docker run ds-stt --file video.mp4
    $ docker cp <container-name>:/output/ /<your-local-dir>/
    ```
* Make sure to use container name while copying to local.


## How-to example

* Make sure the model and scorer files are in the root directory. They are automatically loaded
* After following the installation instructions, you can run `autosub/main.py` as given below. The `--file` argument is the video file for which SRT file is to be generated
    ```bash
    $ python3 autosub/main.py --file ~/movie.mp4
    ```
* After the script finishes, the SRT file is saved in `output/`

## References
1. https://github.com/mozilla/DeepSpeech/
3. https://deepspeech.readthedocs.io/
