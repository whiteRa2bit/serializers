

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#data">Data</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
Comparison of data serialization formats in Python


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.


### Installation

- **Local**
  1. Clone the repo
     ```sh
     git clone https://github.com/whiteRa2bit/serializers.git
     ```
  2. Create venv
     ```
     python3 -m venv venv
     . venv/bin/activate
     ```
  3. Install requirements
     ```
     pip3 install -r requirements.txt
     ```

- **Docker**

    You can either build an image yourself or pull a ready one from [Dockerhub](https://hub.docker.com/repository/docker/whitera2bit/soa_serializers)

    - Build
        ```
        docker build -t whitera2bit/soa_serializers . -f dockerfiles/Dockerfile
        ```

    - Pull from Dockerhub
        ```
        docker pull whitera2bit/soa_serializers
        ```

<!-- USAGE EXAMPLES -->
## Usage
To get timing results and serialized data run:

- If you used local setup:
    ```
    python benchmark.py
    ```

- If you used docker:
    ```
    docker run --name soa_serializers -t whitera2bit/soa_serializers
    ```


## Data
Serialized data is stored at: `data/serialized`

Deserialized data is stored at `data/desirialized`

Report at `docs/report.xlsx`

## License

Distributed under the MIT License. See `LICENSE` for more information.


## Contact

Pavel Fakanov - pavel.fakanov@gmail.com

Project Link: [https://github.com/whiteRa2bit/serializers](https://github.com/whiteRa2bit/serializers)
