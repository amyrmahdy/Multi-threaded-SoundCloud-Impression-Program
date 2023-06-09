# Multi-threaded SoundCloud Impression Program

This Python program is a multi-threaded version of the SoundCloud impression program, which automates the process of playing a SoundCloud track repeatedly. The program uses concurrent.futures to create multiple threads, each of which plays a different SoundCloud track simultaneously.

<br >


## **Prerequisites**

- Python 3.6 or later

- `selenium` Python package

- Chrome

<br >


## **Installation**

1. Clone or download the repository.

2. Install the `selenium` package using `pip`:
```
pip install selenium
```
3. Download the appropriate driver for your browser and operating system from the following links:

- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

4. Update the `input.txt` file with the URLs of the SoundCloud tracks you want to play. Each URL should be on a separate line.

<br >


## **Usage**

To run the program, open a terminal and navigate to the directory containing the `soundcloud_multithreading.py` file. Then run the following command:

```
python soundcloud_multithreading.py <workers> <views> <seconds>
```

Replace `<workers>` with the number of threads you want to create, `<views>` with the number of times you want to play each track, and `<seconds>` with the number of seconds you want to wait between each play.

For example, to create 5 threads, play each track 100 times, and wait 30 seconds between each play, run the following command:

```
python soundcloud_multithreading.py 5 100 30
```

The program will create a thread for each URL in the `input.txt` file and play each track the specified number of times.

<br >


## **Contribution**

Contributions are always welcome! Here are some ways you can contribute to the project:

- Report any bugs or issues you encounter by opening an issue on GitHub.
- Suggest new features or improvements by opening an issue on GitHub.
- Fork the repository and create a pull request with your own changes.
- Improve the documentation by opening a pull request with your changes.

<br >


## **Note**

- If you encounter any errors or issues while running the program, try increasing the value of the `max_workers` parameter in the `ThreadPoolExecutor` function in the `soundcloud_multithreading.py` file.

- Be aware that automating the process of playing a SoundCloud track repeatedly is against SoundCloud's terms of use and may result in your account being suspended or terminated. Use this program at your own risk.

<br >
<br >

Author: **amyrmahdy**

Date: **19 April 2022**






