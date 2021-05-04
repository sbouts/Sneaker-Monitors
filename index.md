# Sneaker Monitors Documentation

Here, you will find basic documentation on setting up the monitors.

## Contents


## Installation
Ensure you have [Python 3+](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/) installed. 

To install the dependencies, use the command:
```
pip install -r requirements.txt
```

## Set Up

1. First perform the installation described in [#Installation](#installation).

2. Clone or Download the repository
    - Clone:
    ```
    git clone https://github.com/yasserqureshi1/Sneaker-Monitors.git
    ```
    - Download: Click on the green `Code` button and click on `Download ZIP`. Then unzip this folder
    
3. Start editting the `.env` file to your specifications. You will only be interacting with the ```.env``` file.
    - **Add Webhook**: Paste your Discord Webhook URL under the `WEBHOOK` variable. It should look like this:
    ```
    WEBHOOK = "https://discord.com/api/webhooks/..."
    ```
    - (Optional) **Add Proxy**: Paste your proxy under the `PROXY` variable. There are two structures:

        1. ```PROXY = "<proxy>:<port>"``` 
        2. ```PROXY = "<proxy_username>:<proxy_password>@<proxy_domain>:<port>"```
    - You can also edit other details within the `.env` file as you see fit

4. Run the Python file. You can use the following command:
  ```
  python [file name].py
  ```

**NOTE:** The script needs to be running continuously for it to keep monitoring websites. As such, you should host it on a server. I have a YouTube tutorial on this [here](https://youtu.be/nmUSSlt4JKk). However, I suggest testing this out on your PC before using a server.
    

## FAQs

1. Can I monitor multiple Shopify sites in the same Python file?

No. You will need to duplicate the Shopify folder and have seperate links in each .env file. 
This is a better monitoring solution than iterating through a list of URLs because iterating through a list introduces new delays that will reduce the speed of the monitor dramatically.

2. I get a red error saying "ERROR: Could not build wheels for multidict which use PEP 517 and cannot be installed directly". What do I do?

You need to install the visual c++ build tools. You can do this through the following link: https://visualstudio.microsoft.com/visual-cpp-build-tools/

3. I get a message saying PIP is not a known command.

This means you do not have pip installed on your system. This website details how to install pip: https://pip.pypa.io/en/stable/installing/

Essentially first you need to download pip using the command in Terminal or Command Prompt:
```curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py```

Then navigate to the directory in which it is downloaded (should be downloaded in the directory already open) and depending on your system, run the specific command:

Windows: ```py get-pip.py```
Unix/Mac: ```python get-pip.py```
There is a lot of documentation and many YouTube tutorials that cover this.

4. I get an error saying "ModuleNotFound: No module named ..."

This means you have not installed the dependencies. Please install these using the command:
```pip install -r requirements.txt```

5. I'm having issues with pip.

If you've installed it and are still having issues, ensure that it is in your PATH. This link should help: https://datatofish.com/add-python-to-windows-path/

6. How do I open the .env file?

You can use notepad or any text editor.

7. I can't see the .env files.

This is possibly because you are not able to view hidden files and folders.

For Windows users:
https://support.microsoft.com/en-us/windows/view-hidden-files-and-folders-in-windows-10-97fbc472-c603-9d90-91d0-1166d1d9f4b5

For Mac Users:
https://www.macworld.co.uk/how-to/show-hidden-files-mac-3520878/

8. Where are the free proxies from?

They are provided by [SSL Proxies](https://www.sslproxies.org/). 

9. If I use my own proxies, can they get banned?

Possibly. There may be a chance that they get banned, so bare that in mind when using the scripts.

