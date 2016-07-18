# Description
Playground (exercise, practice) for OpenCV 3.1.0, Python 2.7, Python 3.5, Numpy, and Scipy

### Setup Runtime container

* Pull this project to some folder
    ```
    $ cd ~/Code/Machine_Learning/OpenCV
    ```

* Pull Docker image 
    ```
    $ docker pull quay.io/rainbean/opencv
    ```

* Run interactive octave shell
    ```
    $ docker run -v $PWD:/source -it --rm quay.io/rainbean/opencv
    ```

* [Optional] Pull Python 2 only images
    ```
    $ docker pull quay.io/rainbean/opencv:python2
    ```

### Invoke Python scripts
* Python 2 scripts
    ```
    # python script/test/test1.py
    ```

* Python 3 scripts
    ```
    # python3 script/test/test2.py
    ```